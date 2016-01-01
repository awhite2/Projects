''' Demonstrates the difference between diffuse and specular lighting.  The
   left ball only gets specular light, the right ball only gets diffuse
   light.  Neither has any ambient light.  
   
Written by Scott D. Anderson
scott.anderson@acm.org
Fall 2004

Fall 2009 ported to Python
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

    light0Pos = (0, 0, 1, 1)
    twGrayLight(GL_LIGHT0,light0Pos,1,0,1)

    light1Pos = (0, 0, 1, 1)
    twGrayLight(GL_LIGHT1,light1Pos,1,1,0);

    glEnable(GL_LIGHTING);
    glShadeModel(GL_SMOOTH);
    twAmbient(0.2);

    objColor = (0.2, 0.3, 0.4)
    twColor(objColor,0.9,20);        

    glEnable(GL_LIGHT0);
    glDisable(GL_LIGHT1);
    glPushMatrix();
    glTranslatef(-1,0,0);
    glutSolidSphere(1,30,30);   # left ball gets specular light (light0)
    glPopMatrix();

    glEnable(GL_LIGHT1);
    glDisable(GL_LIGHT0);
    glPushMatrix();
    glTranslatef(1,0,0);
    glutSolidSphere(1,30,30);   # right ball gets diffuse light (light1)
    glPopMatrix();

    glFlush();
    glutSwapBuffers();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-1,1,-0.7,0.7,-0.7,0.7); # a lie, to get us closer in
    twInitWindowSize(650,650)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()
