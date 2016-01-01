''' Demo of unprojection and the mouse callback.

Implemented Fall 2003
Scott D. Anderson

ported to Python, Fall 2009
'''

import sys

from TW import *

## ================================================================

WinHeight = 500                 # the height of the whole window

# The location of the mouse click, in window coordinates
ClickLocation = (0,0)

## These points come from unprojecting the mouse click.  They're in
## world coordinates.
A = (0,0,0)
B = (0,0,0)

def display():
    twDisplayInit();
    twCamera();

    if True:
        # The following just draws a barn.
        endsColor = (0.2,0.8,0.3)
        sideColor = (0.8,0.2,0.3)
        roofColor = (0.4,0.4,0.2)
        twWireBarn(endsColor,sideColor,roofColor);

    # This draws the two endpoints of our line segment from the near
    # face to the far face of the frustum.
    glPointSize(3);
    glBegin(GL_POINTS);
    glColor3f(1,1,0);
    glVertex3fv(A);
    glColor3f(1,0,1);
    glVertex3fv(B);
    glEnd();    

    # This draws the line segment from A to B.
    glLineWidth(2);
    glBegin(GL_LINES);
    glColor3f(1,1,0);
    glVertex3fv(A);
    glColor3f(1,0,1);
    glVertex3fv(B);
    glEnd();    

    glFlush();
    glutSwapBuffers();

def myMouseClick(button, state, x, y):
    '''callback executed when a mouse button goes up or down'''
    global ClickLocation, A, B
    if button != GLUT_MIDDLE_BUTTON:
        twMouseFunction(button,state,x,y);
        return;
    y = WinHeight - y;

    # in window coordinates (origin at lower left) instead of mouse
    # coordinates (origin at upper left)
    ClickLocation = [x,y,None]

    ClickLocation[2] = .01;     # near face has z = 0
    # This does the unprojection, computing A from ClickLocation
    A = twUnProject(ClickLocation);
    twTriplePrint("A=",A);
    ClickLocation[2] = .99;     # far face has z = 1
    # This does the unprojection, computing B from ClickLocation
    B = twUnProject(ClickLocation);
    twTriplePrint("B=",B);

    glutPostRedisplay();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(0,1,0,1,-1,0);
    twInitWindowSize(500,WinHeight);
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    glutMouseFunc(myMouseClick); # NEW CODE HERE!
    glutMainLoop()

if __name__ == '__main__':
    main()
