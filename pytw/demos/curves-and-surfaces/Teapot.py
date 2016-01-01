""" The teapot, but with two lights, which can be turned on/off
   independently.

Written by Caroline Geiersbach and Scott D. Anderson
scott.anderson@acm.org
Summer 2003

Fall 2005, added a second light and the key callbacks.

Fall 2009, ported to Python
"""


import sys

try:
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
        '''

### ================================================================

Light0 = True
Light1 = True

Textured = False

flat_tid = None

def display():
    twDisplayInit();
    twCamera();

    glEnable(GL_LIGHTING);
    glShadeModel(GL_SMOOTH);

    twAmbient(0);                # turn down ambient to make the lights more obvious
    twGrayLight(GL_LIGHT0, (1,1,1,1), 0.1, 0.7, 0.7);
    if Light0:
        glEnable(GL_LIGHT0)
    else:
        glDisable(GL_LIGHT0)
    twGrayLight(GL_LIGHT1, (0,1,0,0), 0.1, 0.8, 0.8);
    if Light1:
        glEnable(GL_LIGHT1)
    else:
        glDisable(GL_LIGHT1)

    twColor((0.8, 0.8, 0.8),0.9,64); # pewter?
    glBindTexture(GL_TEXTURE_2D,int(flag_tid))
    if Textured:
        glEnable(GL_TEXTURE_2D)
    else:
        glDisable(GL_TEXTURE_2D)
    glutSolidTeapot(1);

    glFlush();
    glutSwapBuffers()

def lightToggle(key, x, y):
    global Light0, Light1, Textured
    if key == '1':
        Light0 = not Light0
    elif key == '2':
        Light1 = not Light1
    elif key == 't':
        Textured = not Textured
    glutPostRedisplay(); 

# ================================================================

def main():
    global flag_tid
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-1,+1,-1,+1,-1,+1);
    twInitWindowSize(600,400)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    twKeyCallback('1',lightToggle,"toggle light 1");
    twKeyCallback('2',lightToggle,"toggle light 2");
    twKeyCallback('t',lightToggle,"toggle texturing");
    flag_tid = glGenTextures(1);
    glBindTexture(GL_TEXTURE_2D,int(flag_tid))
    twUSFlag()
    glutDisplayFunc(display);
    glutMainLoop();

if __name__ == '__main__':
    main()
