import curses 
import random
import time

def move(direction):
    new_head=[snake[0][0],snake[0][1]]
    if direction==curses.KEY_DOWN:
                new_head[0]+=1
    elif direction==curses.KEY_UP:
                new_head[0]-=1
    elif direction==curses.KEY_RIGHT:
                new_head[1]+=1
    elif direction==curses.KEY_LEFT:
                new_head[1]-=1
    snake.insert(0,new_head)
    return snake
    
def draw(x,symbol):
    win.addch(x[0],x[1],symbol)

def rest(currentScore):
    delay = (0.4 - (0.1)*(currentScore/6) )
    if (delay < 0.1):
        delay = 0.1
    time.sleep(delay)


curses.initscr()
win=curses.newwin(40,40,0,0)
win.keypad(1)
win.border(0)
win.nodelay(True)

snake=[[1,4],[1,3],[1,2]]
for i in snake:
    draw(i,"*")
blocks=[[19,20],[20,20],[21,20]]
for j in blocks:
    draw(j,"#")
food=[20,30]
draw(food,"$")

key=curses.KEY_RIGHT
score=0

while key!=27:
    new_key=win.getch()
    key = key if new_key == -1 else new_key
    if snake[0]==food:
        food=None
        move(key)
        while food is None:
            x=random.randint(1,39)
            y=random.randint(1,39)
            if [y,x] in blocks:
                x=random.randint(1,39)
                y=random.randint(1,39)
            food=[y,x]
            draw(food,"$") 
        score=score+3
    if snake[0][0]==0 or snake[0][0]==39 or snake[0][1]==39 or snake[0][1]==0:
        print("score =",score)
        break
    if snake[0]==snake[1:]:
        print("score =",score)
        break
    if snake[0] in blocks:
        print("score =",score)
        break
    else:
        tail=snake.pop()
        draw(tail," ")
        move(key)
    a=snake[0]
    draw(a,"*")
    rest(score)


curses.endwin()
print("GAME_OVER")
print("Score : ",score)