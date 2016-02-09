import stepAnimation
from math import *

def rgbString(red, green, blue):   
    return "#%02x%02x%02x" % (red, green, blue)

lightgrey=rgbString(224,224, 224)
colorstep=255/7.0


def loadingAnimation(canvas,width,height,step):
    cx=150         # center of the big circle
    cy=150
    r=100          #radius of big circle
    r2=17          #radius of small circles
    move=((2*pi)/2)/7.0
    canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill=lightgrey,outline=lightgrey)
    for a in xrange(0,8):
        canvas.create_oval(cx-r*sin(a*move-step*move)-r2,
            cy-r*cos(a*move-step*move)-r2,
            cx-r*sin(a*move-step*move)+r2,
            cy-r*cos(a*move-step*move)+r2,fill=rgbString(a*colorstep,
                                                a*colorstep,a*colorstep))       

    canvas.create_text(cx,cy,text="Loading...", fill="black",
        font="Helvetica 20 bold")
stepAnimation.run(loadingAnimation)
