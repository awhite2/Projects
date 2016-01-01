# Objects created by Zsuzsa Moricz, Fall 2005.
# CS307 - Computer Graphics, Professor Scott Anderson

#------------ HAT - (SELF-CONTAINED FUNCTION) ------------*/
# Hat is created from a torus, a cylinder and a disk. 
# Origin is at the bottom of the hat 
# to be able to place it on a head or a surface.
# Radius of hat 1.4, height 2.
# Color needs to be set by the user beforehand with twColor(). 
# Suggested values: 0.5 for specularity and 100 for shininess. */

import sys;
import math;

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''

wire = False;                # whether to use wireframe or fill

def zmoriczHat():
  hatHeight = 2;
  outerRadius = 1.4; 
  innerRadius = 0.8;
  flare = 0.2;

  glPushMatrix();
  glRotatef(-90,1,0,0);

  glShadeModel(GL_SMOOTH);  
  glPushMatrix();
  glScalef(1,1,0.2);
  glutSolidTorus(outerRadius-innerRadius,outerRadius,30,30);
  glPopMatrix();
  
  twCylinder(innerRadius+0.1,innerRadius+flare,hatHeight,20,20);
  
  glPushMatrix();
  glTranslatef(0,0,hatHeight);
  twDisk(1,20);
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
  #directional light
  glEnable(GL_LIGHTING); 
  light0=(0,1,0,0); 	
  twGrayLight(GL_LIGHT0,light0,0,0.75,0.5);

def display():
  twDisplayInit();
  twCamera();
  glPushAttrib(GL_ALL_ATTRIB_BITS);
  
  glEnable(GL_LIGHTING);
  glShadeModel(GL_SMOOTH);
  
  setLight();

  drawOrigin();

  hatColor= (0,0,0);
  twColor(hatColor,0.5,100);
  zmoriczHat();
  
  glPopAttrib();
  glFlush();
  glutSwapBuffers();

def wireToggle(key, x, y):
    global wire
    wirep = not wire;
    glutPostRedisplay();

def main():
  glutInit(sys.argv);
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
  glutInitWindowSize(500, 500);
  glutCreateWindow(sys.argv[0]);
  glutDisplayFunc(display);
  twBoundingBox(-1,1,-2,4,-1,1);
  twMainInit();
  twKeyCallback('w',wireToggle,"toggle wire frame");
  glutMainLoop();                   

if __name__ == '__main__':
  main()
