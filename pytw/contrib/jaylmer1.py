'''Objects created by Justine Aylmer
Includes temple object and trident object
CS 307
'''

import sys

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''

def jaylmerTemple():
   '''Temple object is 17 units along the x-axis, 34 units along the
   z-axis, and 23 units along the y-axis.  Its origin lies at the
   front left corner.'''

   tempSpec = 0.9;
   tempShine = 20;

   glPushMatrix();
   # Translate so temple is at ground level with front left corner at
   # origin
   glTranslatef(8.5,1,-17);

   # draw bottom level
   glPushMatrix();
   glScalef(17,2,34);
   glutSolidCube(1);
   glPopMatrix();
 
   # draw upper level
   glPushMatrix();
   glTranslatef(0,2,0);
   glScalef(15,2,30);
   glutSolidCube(1);
   glPopMatrix();
 
   # draw left pillars
   glPushMatrix();
   glTranslatef(-6,17,13);
   for i in range(6):
     twSolidCylinder(1,1,15,12,3);
     glTranslatef(0,0,-5);
   glPopMatrix();
 
   # draw right pillars
   glPushMatrix();
   glTranslatef(6,17,13);
   for i in range(6):
     twSolidCylinder(1,1,15,12,3);
     glTranslatef(0,0,-5);
   glPopMatrix();
 
   # draw front pillars
   glPushMatrix();
   glTranslatef(-2,17,13);
   for i in range(2):
     twSolidCylinder(1,1,15,12,3);
     glTranslatef(4,0,0);
   glPopMatrix();
 
   # draw back pillars
   glPushMatrix();
   glTranslatef(-2,17,-13);
   for i in range(2):
     twSolidCylinder(1,1,15,12,3);
     glTranslatef(4,0,0);
   glPopMatrix();
 
   roof = (
     (-8.5,17,17),    #front left bottom
     (8.5,17,17),     #front right bottom
     (0,22,17),       #front top
     (-8.5,17,-17),   #back left bottom
     (8.5,17,-17),    #back right bottom
     (0,22,-17),      #back top
     );
 
   glBegin(GL_POLYGON);  #front
   if True:
     glVertex3fv(roof[0]);
     glVertex3fv(roof[1]);
     glVertex3fv(roof[2]);
   glEnd();
   glBegin(GL_POLYGON);  #back
   if True:
     glVertex3fv(roof[3]);
     glVertex3fv(roof[5]);
     glVertex3fv(roof[4]);
   glEnd();
   glBegin(GL_POLYGON);  #left side
   v = twVector(roof[0],roof[2]);
   w = twVector(roof[5],roof[2]);
   u = twCrossProduct(v,w);
   u = twVectorNormalize(u);
   glNormal3fv(u);
   if True:
     glVertex3fv(roof[3]);
     glVertex3fv(roof[0]);
     glVertex3fv(roof[2]);
     glVertex3fv(roof[5]);
   glEnd();
   glBegin(GL_POLYGON);  #right side
 
   # Surface Normal was found by hand by taking the cross product of
   # the vector from vertex 2 to vertex1 and vertex 2 to vertex 5
   normal = (170,289,8.5)
   glNormal3fv(normal);
   if True:
     glVertex3fv(roof[4]);
     glVertex3fv(roof[5]);
     glVertex3fv(roof[2]);
     glVertex3fv(roof[1]);
   glEnd();
 
   glPopMatrix();

def jaylmerBoat():
  ''' Boat object is 10 units long (along x-axis) with oars spanning
  16 units (along z-axis).  It is 2 units high, and is drawn from the
  center.'''

  glPushMatrix();
  glTranslatef(0,2,0);
  glPushMatrix();
  glScalef(10,2,2);
  twSolidCylinder(1,1,1,45,1);
  glPopMatrix();
  glTranslatef(5,0,0);
  glRotatef(80,1,0,0);
  for j in range(4):
    twSolidCylinder(.5,.5,8,20,1);
    glRotatef(200,1,0,0);
    twSolidCylinder(.5,.5,8,20,1);
    glRotatef(-200,1,0,0);
    glTranslatef(-4,0,0);
  glPopMatrix();

def jaylmerTrident():
  '''Trident is 35 units long (along y-axis), 14 units wide (along
  x-axis) and is drawn from the bottom of the handle, facing down.'''
  length = 25;
  glPushMatrix();
  #long handle
  glRotatef(180,0,1,0);
  twSolidCylinder(1,1,length,20,12);
  #short base
  glTranslatef(0,-length,0);
  glRotatef(90,0,0,1);
  glTranslatef(0,5,0);
  twSolidCylinder(1,1,10,20,12);
  #end prong
  glRotatef(-90,0,0,1);
  twSolidCylinder(1,1,6,20,12);
  #end prong tip
  glPushMatrix();
  glTranslatef(0,-6,0);
  glRotatef(90,1,0,0);
  glutSolidCone(2,2,12,12);
  glPopMatrix();
  #middle prong
  glTranslatef(5,0,0);
  twSolidCylinder(1,1,8,20,12);
  #middle prong tip
  glPushMatrix();
  glTranslatef(0,-8,0);
  glRotatef(90,1,0,0);
  glutSolidCone(2,2,12,12);
  glPopMatrix();
  #end prong
  glTranslatef(5,0,0);
  twSolidCylinder(1,1,6,20,12);
  #end prong tip
  glPushMatrix();
  glTranslatef(0,-6,0);
  glRotatef(90,1,0,0);
  glutSolidCone(2,2,12,12);
  glPopMatrix();

  glPopMatrix();

### ================================================================

### Testing code.  Note that all the rest of the file is indented, so that
### it is controlled by the "if" statement. This "if" statement runs if
### the file is run as a shell script, but is not run if the file is
### imported.  Thus, if you run it as a shell script, you automatically
### get a demo, but if you import it, you can just use the functions.

if __name__ == '__main__':

    # a global to hold the current function to demo
    # initialized for real in main
    demoObject = = lambda : None

    def display():
        twDisplayInit();
        twCamera();
        # Justine decided to use lighting in her demo:
        lightPos = (20,30,0,1)
        twGrayLight(GL_LIGHT0, lightPos, .5,.5,.1);
        glEnable(GL_LIGHTING);
        ad = (.5, .5, .6, 1)
        s  = (.1, .1, .1, 1)
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, ad);
        glMaterialfv(GL_FRONT, GL_SPECULAR, s);
        # draw whatever the current object is; this is a global variable that
        # is set by various functions below.
        demoObject();

        glFlush();
        glutSwapBuffers();

    def objectTemple(key,x,y):
        global demoObject
        twBoundingBox(0,17, 0,23, -34,0)
        twZview()
        # don't put the () after this, this just copies the
        # function definition to a new name
        demoObject = jaylmerTemple
        glutPostRedisplay()

    def objectBoat(key,x,y):
        global demoObject
        twBoundingBox(-10,10, 0,2, -8,8)
        twZview()
        # don't put the () after this, this just copies the
        # function definition to a new name
        demoObject = jaylmerBoat
        glutPostRedisplay()

    def objectTrident(key,x,y):
        global demoObject
        twBoundingBox(-7,7, -35,0, -3,3)
        twZview()
        # don't put the () after this, this just copies the
        # function definition to a new name
        demoObject = jaylmerTrident 
        glutPostRedisplay()

    def main():
        glutInit(sys.argv)
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        twInitWindowSize(500,500)
        glutCreateWindow(sys.argv[0])
        glutDisplayFunc(display)
        # default to showing the temple. Note that this call must be
        # put *here*, after glutCreateWindow and before twMainInit
        objectTemple(None,None,None)
        twMainInit()
        # keyboard callbacks to switch among objects
        # don't put () here, because we are passing in a function object,
        # not invoking the function
        twKeyCallback('1',objectTemple, "Show the Temple")
        twKeyCallback('2',objectBoat,   "Show the Boat")
        twKeyCallback('3',objectTrident,"Show the Trident")
        # twSetMessages(TW_CAMERA)
        glutMainLoop()

    main()

