""" A bunch of mouse callbacks that just report the event in the window.

Implemented Fall 2005
Scott D. Anderson
Ported to Python 2009
"""

import sys

try:
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
        '''

### ================================================================

keytext = ""   # buffer for putting key/button information for display
motiontext = "" # buffer for putting mouse motion information for display

def display():
    twDisplayInit();
    twCamera();
    
    sides = (1,0,0)   # red
    ends  = (0,0,1)   # blue
    roof  = (0,1,0)   # green

    twSolidBarn(ends,sides,roof);

    twColorName(TW_BLACK);
    twDrawString(-0.05,-0.05,0.05,keytext);
    twDrawString(-0.05,-0.10,0.05,motiontext);

    glFlush();
    glutSwapBuffers();

def normalKeys(k, x, y):
    global keytext
    keytext = "normal key = %c (%d) x = %d y = %d" % (k,ord(k),x,y)
    if k=='q':
        exit(0)
    glutPostRedisplay();

buttonNames = range(3)
buttonStates = range(2)

def initButtonNames():
    buttonNames[GLUT_LEFT_BUTTON] = "GLUT_LEFT_BUTTON";
    buttonNames[GLUT_MIDDLE_BUTTON] = "GLUT_MIDDLE_BUTTON";
    buttonNames[GLUT_RIGHT_BUTTON] = "GLUT_RIGHT_BUTTON";
    buttonStates[GLUT_DOWN] = "GLUT_DOWN";
    buttonStates[GLUT_UP] = "GLUT_UP";

def mouseClick(button, state, x, y):
    global keytext
    keytext = "%s %s %d %d" % ( buttonNames[button],
                                buttonStates[state],
                                x,y)
    glutPostRedisplay();

old_mouse = None

def mouseDrags(x, y):
    global motiontext, old_mouse
    if old_mouse == None:
        motiontext = "mouse moves to %d %d; no prior location" % (x,y)
    else:
        motiontext = "mouse moves to %d %d from %s" % (x,y,old_mouse)
    old_mouse = (x,y)
    glutPostRedisplay();

# ================================================================

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(0,1,0,1,-1,0);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    glutDetachMenu(GLUT_RIGHT_BUTTON);

    initButtonNames();
    glutKeyboardFunc(normalKeys);
    # glutPassiveMotionFunc(mouseMoves);
    glutMouseFunc(mouseClick);
    glutMotionFunc(mouseDrags);
    glutMainLoop();

if __name__ == '__main__':
    main()
