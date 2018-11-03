import curses
import threading
lock = threading.RLock()
print("Yo Alyssa you're gonna learn some coding basics and soon you will be even more baddass.")

# get the curses screen window
screen = curses.initscr()
 
# turn off input echoing
curses.noecho()
 
# respond to keys immediately (don't wait for enter)
curses.cbreak()
 
# map arrow keys to special values
screen.keypad(True)

min_id = 2
max_id = 25

sel_id = min_id

ids = range(min_id, max_id + 1)

id_idx = 0
cur_id = 0

x = 5
y = 5

def clear():
    screen.clear()

def draw_border():
    for i in xrange(12):
        for j in xrange(1,13):
            if (i == 0 or i == 11 or j == 1 or j == 12):
                screen.addstr(j, i, '0')

def draw(x, y, char):
    screen.addstr(y+2, x+1, char)

def draw_screen():
    screen.addstr(0, 0, 'x:' + str(x) +' y:' + str(y))
    draw_border()

    # Uncomment the following lines are just an illustration of how to use the 'draw(...)' function
    # for i in range(10):
    #     draw(i, 6, '.')

    # Alyssa, add your code here.
    for i in range(10):
        draw(i, y, '.')
        draw(x, i, '.')

    draw(x, y, '+')

    # end user code
    



try:
    draw_screen()
    while True:
        char = screen.getch()
        lock.acquire()
        if char == ord('q'):
            break
        elif char == curses.KEY_RIGHT:
            x += 1
            if (x > 9):
                x = 9
        elif char == curses.KEY_LEFT:
            x -= 1
            if (x < 0):
                x = 0
        elif char == curses.KEY_DOWN:
            y += 1
            if (y > 9):
                y = 9
        elif char == curses.KEY_UP:
            y -= 1
            if (y < 0):
                y = 0
        clear()
        draw_screen()
        lock.release()

finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()  