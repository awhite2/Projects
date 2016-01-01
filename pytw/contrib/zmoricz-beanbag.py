#***********************************************************/
# Beanbag created by Zsuzsa Moricz, Fall 2005.
# CS307 - Computer Graphics, Professor Scott Anderson

# Beanbag is a striped juggling ball. 
# To make the ball striped two spheres are placed into each other:
# one is stretched along the x-axis while the other one along the z-axis. 
# This is how the illusion of the stripes is created.
# Origin is at the bottom of the ball, radius of ball is 1.
# Beanbag has two colors one is always black.
# The other one is determined by the user with the twColor() function 
# before the beanbag function is called.
# Suggested values: 1 for specularity and 40 for shininess.

import sys;
import math;

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''

def zmoriczBeanbag():
  stretch = 1.1;
  compress = 0.9;
  black = (0,0,0);

  glPushMatrix();
  glTranslatef(0,1,0);

  glPushMatrix();
  glScalef(compress,1,stretch);
  glShadeModel(GL_SMOOTH);  
  glutSolidSphere(1,20,20);
  glPopMatrix();

  glPushMatrix();
  glScalef(stretch,1,compress);
  twColor(black,1,40);
  glShadeModel(GL_SMOOTH);  
  glutSolidSphere(1,20,20);
  glPopMatrix();
  glPopMatrix();  

# drawing the origin helps to place the objects on different surfaces
def drawOrigin():
  glPointSize(3); 
  glBegin(GL_POINTS);
  twColorName (TW_MAGENTA);
  glVertex3f(0,0,0);
  glEnd();

def setLight():
  # directional light
  glEnable(GL_LIGHTING); 
  light0=(1,0,0,0); 	
  twGrayLight(GL_LIGHT0,light0,0,0.75,0.5);

def display():
  twDisplayInit();
  twCamera();
  glPushAttrib(GL_ALL_ATTRIB_BITS);
  
  glEnable(GL_LIGHTING);
  glShadeModel(GL_SMOOTH);
  
  setLight();

  drawOrigin();

  beanbagColor= (255/255.0,0.0,0.0);
  twColor(beanbagColor,0.5,100);
  zmoriczBeanbag();
  
  glPopAttrib();
  glFlush();
  glutSwapBuffers();

def main():
  glutInit(sys.argv);
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
  glutInitWindowSize(500, 500);
  glutCreateWindow(sys.argv[0]);
  glutDisplayFunc(display);
  twBoundingBox(-1,1,-1,3,-1,1);
  twMainInit();
  glutMainLoop();

if __name__ == '__main__':
  main()
