""" Demo of two partly coincident quads, to show color speckling.

The red one is drawn first, then the green one.

Implemented Fall 2005
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

BgBlack = True
DepthTest = True

TextLeft = -0.2          # X coordinate for left end of text
TextTop  = -0.2          # Y coordinate for first line of text

def RedThenGreenQuads():
    glBegin(GL_QUADS);

    glColor4f(1,0,0,1);         # solid red
    glVertex2f(0,0);            # lower left, then CCW
    glVertex2f(2,0);
    glVertex2f(2,2);
    glVertex2f(0,2);

    glColor4f(0,1,0,1);         # solid green
    glVertex2f(1,0);            # lower left, then CCW
    glVertex2f(3,0);
    glVertex2f(3,2);
    glVertex2f(1,2);

    glEnd();

def depthTest():
    twColorName(TW_WHITE if BgBlack else TW_BLACK);
    if(DepthTest):
        glEnable(GL_DEPTH_TEST);
        twDrawString(TextLeft,TextTop,0, "Depth Test ON - 'd' toggles");
    else:
        glDisable(GL_DEPTH_TEST);
        twDrawString(TextLeft,TextTop,0, "Depth Test OFF - 'd' toggles");

def display():
    if(BgBlack):
        glClearColor(0,0,0,0);        # transparent black
    else:
        glClearColor(1,1,1,1);        # opaque white
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    twCamera();
    depthTest();

    RedThenGreenQuads();

    glFlush();
    glutSwapBuffers();

def keys(key, x, y):
    global BgBlack, DepthTest
    if key == 'b': 
        BgBlack = not BgBlack
    elif key == 'd': 
        DepthTest = not DepthTest
    glutPostRedisplay();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    twBoundingBox(0,3,0,2,0,0);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    twKeyCallback('b',keys,"toggle black/white background");
    twKeyCallback('d',keys,"toggle depth test");
    glutMainLoop();
    return 0;

if __name__ == '__main__':
    main()
