''' Demonstrates the phases of the moon, by looking at it from different
   directions.  It uses distant lighting and a sphere.
   
Written by Scott D. Anderson
scott.anderson@acm.org
Fall 2004

Fall 2009, ported to Python and modified to use twGrayLight
'''

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''

## ================================================================

def display():
    twDisplayInit(0,0,0);       # clear to black, instead of the default
    twCamera();

    sunDir = (1, 0, 0, 0)       # sun straight from the right
    twGrayLight(GL_LIGHT0, sunDir, 0, 1, 1) # no ambient

    glEnable(GL_LIGHTING);
    glShadeModel(GL_SMOOTH);
    twAmbient(0);               # no ambient light in space ?

    glPushMatrix();
    moonColor = (0.99, 0.99, 0.99);
    twColor(moonColor,0.0,1);   # the moon is *not* shiny
    glutSolidSphere(1,30,30);
    glPopMatrix();

    glFlush();
    glutSwapBuffers();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-1,1,-1,1,-1,1);
    twInitWindowSize(500,500);
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()
