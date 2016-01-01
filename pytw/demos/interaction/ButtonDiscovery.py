""" A bunch of keyboard callbacks that just report the code for the key
   that was struck.

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

keytext = ""                    # string describing key

def display():
    twDisplayInit();
    twCamera();
    
    sides = (1,0,0)   # red
    ends  = (0,0,1)   # blue
    roof  = (0,1,0)   # green

    twAmbient(0.3)
    twGrayLight(GL_LIGHT0, (-5,5,5,0), 0.2, 0.9, 0.4)
    glEnable(GL_LIGHTING);
    walls = (1,0.8,0.8)   # reddish
    roof  = walls
    sides = walls
    ends = walls

    twSolidBarn(ends,sides,roof);

    twColorName(TW_BLACK);
    twDrawString(-0.05,-0.05,0.05,keytext);

    glFlush();
    glutSwapBuffers();

def normalKeys(k, x, y):
    global keytext
    keytext = "normal key = %c (%d) x = %d y = %d" % (k,ord(k),x,y)
    if k=='q':
        exit(0)
    glutPostRedisplay();

specialKeyNames = range(255)

def initSpecialKeyNames():
    specialKeyNames[ GLUT_KEY_F1 ] = "GLUT_KEY_F1";
    specialKeyNames[ GLUT_KEY_F2 ] = "GLUT_KEY_F2";
    specialKeyNames[ GLUT_KEY_F3 ] = "GLUT_KEY_F3";
    specialKeyNames[ GLUT_KEY_F4 ] = "GLUT_KEY_F4";
    specialKeyNames[ GLUT_KEY_F5 ] = "GLUT_KEY_F5";
    specialKeyNames[ GLUT_KEY_F6 ] = "GLUT_KEY_F6";
    specialKeyNames[ GLUT_KEY_F7 ] = "GLUT_KEY_F7";
    specialKeyNames[ GLUT_KEY_F8 ] = "GLUT_KEY_F8";
    specialKeyNames[ GLUT_KEY_F9 ] = "GLUT_KEY_F9";
    specialKeyNames[ GLUT_KEY_F10 ] = "GLUT_KEY_F10";
    specialKeyNames[ GLUT_KEY_F11 ] = "GLUT_KEY_F11";
    specialKeyNames[ GLUT_KEY_F12 ] = "GLUT_KEY_F12";
    specialKeyNames[ GLUT_KEY_LEFT ] = "GLUT_KEY_LEFT";
    specialKeyNames[ GLUT_KEY_UP ] = "GLUT_KEY_UP";
    specialKeyNames[ GLUT_KEY_RIGHT ] = "GLUT_KEY_RIGHT";
    specialKeyNames[ GLUT_KEY_DOWN ] = "GLUT_KEY_DOWN";
    specialKeyNames[ GLUT_KEY_PAGE_UP ] = "GLUT_KEY_PAGE_UP";
    specialKeyNames[ GLUT_KEY_PAGE_DOWN ] = "GLUT_KEY_PAGE_DOWN";
    specialKeyNames[ GLUT_KEY_HOME ] = "GLUT_KEY_HOME";
    specialKeyNames[ GLUT_KEY_END ] = "GLUT_KEY_END";
    specialKeyNames[ GLUT_KEY_INSERT ] = "GLUT_KEY_INSERT";

def specialKeys(key, x, y):
    global keytext
    keytext = "special key %s at %d %d" % (specialKeyNames[key], x, y)
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
    initSpecialKeyNames();
    glutKeyboardFunc(normalKeys);
    glutSpecialFunc(specialKeys);
    glutMainLoop();

if __name__ == '__main__':
    main()
