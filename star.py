from turtle import *

def turtle(x,y,r,linec,fillc):
    setpos(x,y)
    color(linec,fillc)
    begin_fill()
    while True:
        forward(r)
        left(110)
        if abs(pos()-(x,y)) < 1:
            break
    end_fill()


from turtle import *

shape('turtle')
turtle(100,100,300,'green','lightgreen')
#turtle(-100,-100,350)
done()