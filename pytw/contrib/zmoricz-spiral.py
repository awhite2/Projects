# PROBLEM: When I try to run the script, it tells me that at line 48, glMap2() is only supposed to 
# take 6 arguments, and it currently has 10. I don't know which arguments to remove.
# -Ariana


#***********************************************************/
# Spiral created by Zsuzsa Moricz, Fall 2005.
# CS307 - Computer Graphics, Professor Scott Anderson

import sys;
import math;

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''
        
def zmoriczSpiral(color, n, nsteps):
  spiral = [
    [-0.5, 0, -0.5],            #  1 left 
    [ 0, 1,-1],                 #  2
    [ 1, 2, 0],                 #  3 
    [ 0, 3, 1],                 #  4 
    [-0.5, 4, 0.5],             #  5
    
    [0.5, 0, 0.5],              #  6 right
    [ 0, 1, 1],                 #  7 
    [-1, 2, 0],                 #  8 
    [ 0, 3,-1],                 #  9 
    [0.5, 4, -0.5]];            # 10

  #int i;
  glMaterialfv(GL_FRONT_AND_BACK,GL_AMBIENT_AND_DIFFUSE,color);
  glMaterialfv(GL_FRONT_AND_BACK,GL_SPECULAR,color);
  glMaterialf(GL_FRONT_AND_BACK,GL_SHININESS,10);
  glPushMatrix();
  glTranslatef(0,-4,0);
  
  for count in range (1,n):
    glTranslatef(0,4,0);
    # to put two pieces of spiral together a rotation is needed
    glRotatef(90,0,1,0);

    # drawing the bezier curve
    glEnable(GL_AUTO_NORMAL);        # automatically compute normals 
    glMap2f(GL_MAP2_VERTEX_3, 0, 1, 3, 5, 0, 1, 15, 2, spiral[0]);
    glEnable(GL_MAP2_VERTEX_3);
    
    # set up grid and generate the desired surface
    glMapGrid2f(nsteps, 0, 1, nsteps, 0, 1);
    
    glEnable(GL_NORMALIZE);
    
    glEvalMesh2(GL_FILL, 0, nsteps, 0, nsteps);

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
  light0=(1,1,0,0); 	
  twGrayLight(GL_LIGHT0,light0,0,0.75,0.5);

def display():
  twDisplayInit();
  twCamera();
  glPushAttrib(GL_ALL_ATTRIB_BITS);
  
  glEnable(GL_LIGHTING);
  glShadeModel(GL_SMOOTH);
  
  setLight();

  drawOrigin();

  spiral= (1,0,0);
  zmoriczSpiral(spiral,5,16);
  
  glPopAttrib();
  glFlush();
  glutSwapBuffers();

def main():
  glutInit(sys.argv);
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
  glutInitWindowSize(500, 500);
  glutCreateWindow(sys.argv[0]);
  glutDisplayFunc(display);
  twBoundingBox(-1,1,-2,22,-1,1);
  twMainInit();
  glutMainLoop();
  
if __name__ == '__main__':
  main()
