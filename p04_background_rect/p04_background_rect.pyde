#File-Save 存成 p04_background_rect
def setup():
    size(500,500)
    background(33,255,242)
def draw():
    if mousePressed:
     line(mouseX, mouseY, pmouseX, pmouseY)
