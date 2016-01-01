''' The teddy bear again, but now with two lights, that can be turned
   on/off independently.

Written by Caroline Geiersbach and Scott D. Anderson
scott.anderson@acm.org
Summer 2003

Fall 2005, added a second light and the key callbacks.
Fall 2009, ported to Python
'''

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''

## ================================================================

Light0 = True
Light1 = True

def display():
    twDisplayInit();
    twCamera();
    twAmbient(0.1); # turn down global ambient to make the lights more obvious
    light0 = ( 0.35, 0.4, 0.25, 1 )
    twGrayLight(GL_LIGHT0, light0, 0.1, 0.7, 0.7);
    if Light0:
        glEnable(GL_LIGHT0);
    else:
        glDisable(GL_LIGHT0);
    light1 = ( 0, 1, 0, 0 )     # coming from X axis
    twGrayLight(GL_LIGHT1, light1, 0.1, 0.8, 0.8);
    if Light1:
        glEnable(GL_LIGHT1);
    else:
        glDisable(GL_LIGHT1);

    twTeddyBear()

    glFlush()
    glutSwapBuffers()

def lightToggle(key, x, y):
    global Light0, Light1
    if key == '1':
        Light0 = not Light0
    elif key == '2':
        Light1 = not Light1
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-0.35,0.35, -0.55,0.4, -0.25,0.25)
    twInitWindowSize(650,650)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    twKeyCallback('1', lightToggle, "Toggle first light");
    twKeyCallback('2', lightToggle, "Toggle second light");
    glutMainLoop()

if __name__ == '__main__':
    main()
