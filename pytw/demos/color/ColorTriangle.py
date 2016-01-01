### RGB Colored triangle with color interpolation

### Implemented by Scott D. Anderson
### scott.anderson@acm.org

import sys

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''

def display():
    twDisplayInit();
    twCamera();

    glShadeModel(GL_SMOOTH)

    glBegin(GL_TRIANGLES)
    glColor3f(1,0,0)
    glVertex3f(1,0,0)
    glColor3f(0,1,0)
    glVertex3f(0,1,0)
    glColor3f(0,0,1)
    glVertex3f(0,0,1)
    glEnd()

    glFlush();
    glutSwapBuffers();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(0,1,0,1,0,1)
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
  main()
