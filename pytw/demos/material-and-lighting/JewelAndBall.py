''' Two figures, one with smooth shading and one with flat.

Written by Scott D. Anderson
scott.anderson@acm.org
Fall 2003

Fall 2009, ported to Python
'''

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''

## ================================================================

def display():
    S = 8                       # slices and stacks
    twDisplayInit();
    twCamera();
    lightPos = ( 2, 2, 2, 1 )
    twGrayLight(GL_LIGHT0,lightPos,0.2,0.8,0.8);
    glEnable(GL_LIGHTING);

    cornflower = (100.0/255, 149.0/255, 237.0/255)
    twColor(cornflower, 0.7, 10);

    glShadeModel(GL_FLAT);
    glPushMatrix();
    glTranslatef(-1,0,0);
    glutSolidSphere(0.9,S,S);
    glPopMatrix();
    
    glShadeModel(GL_SMOOTH);
    glPushMatrix();
    glTranslatef(+1,0,0);
    glutSolidSphere(0.9,S,S);
    glPopMatrix();

    glFlush();
    glutSwapBuffers();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    SIZE = 0.7
    twBoundingBox(-2*SIZE,+2*SIZE,-SIZE,+SIZE,-SIZE,+SIZE) # a lie, to get us closer
    twInitWindowSize(500,300);
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()
