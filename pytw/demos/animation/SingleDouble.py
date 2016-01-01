"""
/*
 *  This program demonstrates double buffering for flicker-free animation.
 *  Originally written by Edward Angel, and only slightly adapted by Scott
 *  D. Anderson.
 */

Fall 2009, Ported to Python.
"""

import sys

from TW import *

### ================================================================

WinSize = 400;
spinAngle = 0.0;
SingleBufferWindow = None
DoubleBufferWindow = None

def displayDoubleBuffering():
    glClear (GL_COLOR_BUFFER_BIT);
    glRectf (-25.0, -25.0, 25.0, 25.0);
    glFlush();
    glutSwapBuffers ();

def displaySingleBuffering():
    glClear(GL_COLOR_BUFFER_BIT);
    glRectf(-25.0, -25.0, 25.0, 25.0);
    glFlush();

## This is the idle callback
def spinDisplay ():
    global spinAngle
    spinAngle = spinAngle + 1.0;
    if (spinAngle > 360.0):
	spinAngle = spinAngle - 360.0;
    glutSetWindow(SingleBufferWindow);
    glLoadIdentity();
    glRotatef (spinAngle, 0, 0, 1);
    glutPostRedisplay(); 
    glutSetWindow(DoubleBufferWindow);
    glLoadIdentity();
    glRotatef (spinAngle, 0, 0, 1);
    glutPostRedisplay();

def myinit ():
    glClearColor(0, 0, 0, 1);
    glColor3f(1, 1, 1);
    glShadeModel(GL_FLAT);

Animate = False

def keys(key, x, y):
    global Animate
    if key == 'q':
        exit(0)
    elif key == ' ':
	Animate = not Animate;
        if(Animate):
            glutIdleFunc(spinDisplay);
        else:
            glutIdleFunc(None);
    else:
        print "hit space bar to toggle animation"
        print "q to quit"
        return

def myReshape(w, h):
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    if (w <= h):
	glOrtho (-50.0, 50.0, -50.0*float(h)/(float(w)),
                  50.0*float(h)/(float(w)), -1.0, 1.0)
    else:
	glOrtho (-50.0*(float(w)/(float(h))),
                  50.0*(float(w)/float(h)), -50.0, 50.0, -1.0, 1.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity ();

def main(): 
    global SingleBufferWindow, DoubleBufferWindow
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_SINGLE | GLUT_RGB)
    twInitWindowSize(WinSize,WinSize)
    glutInitWindowPosition(0,0);
    SingleBufferWindow=glutCreateWindow("single buffered");
    myinit ();
    glutDisplayFunc(displaySingleBuffering); 
    glutReshapeFunc (myReshape);
    glutIdleFunc (None);
    glutKeyboardFunc(keys);

    glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(WinSize,WinSize);
    glutInitWindowPosition(WinSize+50,0);
    DoubleBufferWindow=glutCreateWindow("double buffered");
    myinit ();
    glutDisplayFunc(displayDoubleBuffering);
    glutReshapeFunc (myReshape);
    glutIdleFunc (None);
    glutKeyboardFunc(keys);

    glutMainLoop();

if __name__ == '__main__':
    main()
