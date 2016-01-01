#***********************************************************/
# Club created by Zsuzsa Moricz, Fall 2005.
# CS307 - Computer Graphics, Professor Scott Anderson

import sys;
import math;

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''
#------------ CLUB - (SELF-CONTAINED FUNCTION) ------------*/
# The club has a total height 7.5.
# Origin is at handle and the club points downwards.
# Color needs to be set by user beforehand with twColor(). 
# Suggested values: 1 for specularity and 30 for shininess.

def zmoriczClub():
  maxRadius = 0.7;
  minRadius = 0.1;
  topRadius = 0.3;
  barLength = 2.5;
  lowerCylinder = 3; # length
  topCylinder = 2;  # length
  
  glPushMatrix();
  glShadeModel(GL_SMOOTH);  
  #handle
  glPushMatrix();
  glScalef(1,0.5,1);
  glutSolidSphere(topRadius,20,20);
  glPopMatrix();

  #bar
  glPushMatrix();
  glRotatef(-90,1,0,0);
  twTube(minRadius,minRadius,barLength,20,20);
  glPopMatrix();

  #lower cylinder
  glRotatef(-90,1,0,0);
  glTranslatef(0,0,barLength);
  twCylinder(minRadius,maxRadius,lowerCylinder,20,20);
  
  #top cylinder
  glTranslatef(0,0,lowerCylinder);
  twCylinder(maxRadius,topRadius,topCylinder,20,20);
  
  #cover for top
  glTranslatef(0,0,topCylinder);
  twDisk(topRadius,20);
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

  clubColor= (255/255.0,144/255.0,0.0);
  twColor(clubColor,0.5,100);
  zmoriczClub();
  
  glPopAttrib();
  glFlush();
  glutSwapBuffers();

def main():
  glutInit(sys.argv);
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
  glutInitWindowSize(500, 500);
  glutCreateWindow(sys.argv[0]);
  glutDisplayFunc(display);
  twBoundingBox(-1,1,-2,10,-1,1);
  twMainInit();
  glutMainLoop();                   

if __name__ == '__main__':
  main()
