''' Demo of two cones.  One is done using glutSolidCone, and the other with
   gluCylinder (via twCylinder).  glutSolidCone has the base drawn, but
   gluCylinder does not, so if you want an "open" cone (like a desk lamp
   or a megaphone), you have to use cylinders.

   The result looks a little like a witch's hat.

Implemented Fall 2007
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

def display():
    twDisplayInit()
    twCamera()

    # Lighting is not enabled in the program, but if you enable it
    # interactively via the menu, you can see lighting effects on both
    # cones, which means both have normals defined.
    lightpos = ( 1, 1, 0, 0 )
    twGrayLight(GL_LIGHT0, lightpos, 0.1, 1, 1 );

    # The following draws the z=0 plane, which confirms that the base of
    # each cone lies on that plane.
    if False:
        twColorName(TW_CYAN);
        glBegin(GL_QUADS);
        glVertex3f(-10,-10,0);
        glVertex3f(+10,-10,0);
        glVertex3f(+10,+10,0);
        glVertex3f(-10,+10,0);
        glEnd();

    # Mark the origin
    glPointSize(5);
    twColorName(TW_MAGENTA);
    glBegin(GL_POINTS);
    glVertex3f(0,0,0);
    glEnd();

    # this is the brim of the witch's hat
    twColorName(TW_MAROON);
    cylHeight = 2;              # from z=0 to z=2
    cylCutoff = 65;             # half-angle at top of the cone, in degrees
    # compute radius of cone at z=0, given angle and height of cone
    cylBase = cylHeight*math.tan(cylCutoff*M_PI/180);
    twCylinder(cylBase,0,cylHeight,8,1);

    # this is the long peak of the witch's hat
    twColorName(TW_BROWN);
    coneHeight = 10;            # from z=0 to z=10
    coneCutoff = 15;            # half-angle at top of hat, in degrees
    # compute radius of cone at z=0.  This'll be "inside" the brim.
    coneBase = coneHeight*math.tan(coneCutoff*M_PI/180);
    glutSolidCone(coneBase,coneHeight,8,1);

    glFlush();
    glutSwapBuffers();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-10,10,-10,10,-10,10);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
  main()
