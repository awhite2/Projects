''' Demo of a teapot.  Have to guess the bounding box and reference point.

Implemented Fall 2009
Scott D. Anderson
scott.anderson@acm.org

ported to Python, Fall 2009
'''

import sys

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''

BBsize = 1    # Bounding box is a cube around the origin of this half-size

Wire = False                   # by default, show a solid teapot

def display():
    twDisplayInit()
    twCamera()

    # Lighting is not enabled in the program, but if you enable it
    # interactively via the menu, you can see lighting effects on both
    # cones, which means both have normals defined.
    lightpos = ( 1, 1, 0, 0 )
    twGrayLight(GL_LIGHT0, lightpos, 0.1, 1, 1 );

    # Mark the origin
    glPointSize(5);
    twColorName(TW_MAGENTA);
    glBegin(GL_POINTS);
    glVertex3f(0,0,0);
    glEnd();

    blue = (0, 0, 1)
    twColor( blue, 0.8, 10 )
    if Wire:
        glutWireTeapot(1)
    else:
        glutSolidTeapot(1)

    glFlush()
    glutSwapBuffers()

def toggleWire(key,x,y):
    '''Turns wire on/off, modifying the kind of figure'''
    global Wire
    Wire = not Wire
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-BBsize,BBsize,-BBsize,BBsize,-BBsize,BBsize);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    twKeyCallback('w',toggleWire,"turn wire on/off")
    glutMainLoop()

if __name__ == '__main__':
  main()
