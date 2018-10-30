x=0
slide = 0
def setup():
    global gallo_img
    size(640+x,480)
    gallo_img = loadImage("two ball.jpg")
def draw():
    global x
    background(255)
    fill(0)
    image(gallo_img,50,50,x,x)
    x=x+50
    if x==600:
        x=0
