""" Demo of several quads, to show transparency.

Implemented Fall 2003
Scott D. Anderson
Ported to Python Fall 2009
"""

import sys
import math

try:
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
        '''

### ================================================================

BgBlack = False
MidTrans = False
DepthMask = True
DepthTest = True
FarthestFirst = True

TextLeft = -0.2          # X coordinate for left end of text
TextZ = 0                # Z coordinate for text

# These quads are all 3x1, parallel to z=0

def Quad(color4,lowerleft,angle):
    glPushMatrix()
    glTranslate(*lowerleft)
    glRotate(angle,0,0,1)
    glBegin(GL_QUADS);
    glColor4fv(color4)
    glVertex3f(0,0,0)       # lower left
    glVertex3f(1,0,0)       # left right
    glVertex3f(1,3,0)       # upper right
    glVertex3f(0,3,0)       # upper left
    glEnd()
    glPopMatrix()

def depthMask():
    twColorName(TW_WHITE if BgBlack else TW_BLACK);
    glDepthMask(GL_TRUE if DepthMask else GL_FALSE);
    text = "Depth Mask %s - 'm' to toggle" % ("TRUE" if DepthMask else "FALSE");
    twDrawString(TextLeft, -0.1, TextZ, text)

def depthTest():
    twColorName(TW_WHITE if BgBlack else TW_BLACK);
    if(DepthTest):
        glEnable(GL_DEPTH_TEST)
    else:
        glDisable(GL_DEPTH_TEST);
    text = "Depth Test %s - 'd' toggles" % ("ON" if DepthTest else "OFF")
    twDrawString(TextLeft, -0.3, TextZ, text)
    

def display():
    if(BgBlack):
        glClearColor(0,0,0,1)   # solid black
    else:
        glClearColor(1,1,1,1)   # solid white
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    twCamera()
    depthTest()
    depthMask()

    # Settings for transparent objects
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glEnable(GL_BLEND);

    glColor(1,1,1)
    twDrawString(TextLeft,-0.5, TextZ, "farthest to nearest")
    Quad((0,0,1,0.6),(1,0,-2),0)   # blue 60% farthest
    Quad((1,0,0,0.3),(1,1,0),0)  # red 30% nearest

    glColor(1,1,1)
    twDrawString(TextLeft+3,-0.4,0, "nearest to farthest")
    Quad((1,0,0,0.3),(3,1,0),0)  # red 30% nearest
    Quad((0,0,1,0.6),(3,0,-2),0)   # blue 60% farthest
    
    glFlush()
    glutSwapBuffers()

def keys(key, x, y):
    global BgBlack, DepthTest, DepthMask, MidTrans, FarthestFirst
    if key == 'B': 
        BgBlack = not BgBlack
    elif key == 'd': 
        DepthTest = not DepthTest
    elif key == 'm': 
        DepthMask = not DepthMask
    elif key == 'f': 
        FarthestFirst = not FarthestFirst
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    twBoundingBox(1,4,-1,4,-4,1)
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    glutDisplayFunc(display)
    twKeyCallback('B',keys,"toggle black/white background")
    twKeyCallback('d',keys,"toggle depth test")
    twKeyCallback('m',keys,"toggle depth mask")
    twKeyCallback('f',keys,"toggle distance sort")
    glutMainLoop()
    return 0

if __name__ == '__main__':
    main()
