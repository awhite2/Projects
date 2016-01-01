''' Demonstrates the difference between directional and positional lights.
   It uses a sphere, so that we're guaranteed to get specular highlights. 
   
Written by Scott D. Anderson
scott.anderson@acm.org
Fall 2004

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
    twDisplayInit();
    twCamera();

    light0Pos = (0, 0, 1, 0)    # w=0, so a directional light
    twGrayLight(GL_LIGHT0,light0Pos,0,2,0,True); 

    light1Pos = (0, 0, 1, 1)    # same x,y,z, but w=1, which makes this a point
    twGrayLight(GL_LIGHT1,light1Pos,0,2,0,True);

    glEnable(GL_LIGHTING);
    glShadeModel(GL_SMOOTH);
    twAmbient(0.2);

    objColor = (0.4, 0.6, 0.9)
    twColor(objColor,0.9,20);        

    glEnable(GL_LIGHT0);
    glDisable(GL_LIGHT1);
    glPushMatrix();
    glTranslatef(-1,0,0);
    glutSolidSphere(1,30,30);   # left ball gets light0, a directional light
    glPopMatrix();

    glEnable(GL_LIGHT1);
    glDisable(GL_LIGHT0);
    glPushMatrix();
    glTranslatef(1,0,0);
    glutSolidSphere(1,30,30);   # right ball gets light1, a point source
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
