'''
Ported by Gabe Goodwin 2/27/2012
Copyright (C) 2007 by Natasha Kellaway under the GNU GPL

// An OpenGL model of a drumstick. Copyright (C) 2007 by Natasha Kellaway
// This program is released under the GNU General Public License

// *********** My Object for the object library ************
// Function: Draws a drumstick
  The length of the drumstick can be chosen by the user.

  The color of the drumstick is automatically light brown.

  The user can decide whether or not the cymbal has a stand.

  The only argument for nkellawaDrumstick is:

  1. the length

  The initial view is looking at the cymbal from the bottom. Of the 
  drumstick. The shaft and tip of the drumstick point back along the
  z-axis. 

  The origin lies in the center of the drumstick shaft.

*/'''

def nkellawaDrumstick(GLfloat length):

    glPushMatrix();
    
    twTriple stickColor = {1,204/255.0,102/255.0};
    
    twColor(stickColor,0,0);
    
    glPushMatrix();
    
    # // draw shaft of stick
    twCylinder(0.05,0.05,length,50,50);
    
    # //draw bottom of stick
    twDisk(0.05,50);
    
    glPopMatrix();
    
    # // draw tip of stick
    
    glPushMatrix();
    
    glScalef(0.5,0.5,1);
    glTranslatef(0,0,-length*0.05);
    glutSolidSphere(0.12,50,50);
    
    glPopMatrix();
    
    glPopMatrix();




"""// *********** My Object for the object library ************
// Function: Draws a drumstick

/*

  The length of the drumstick can be chosen by the user.

  The color of the drumstick is automatically light brown.

  The user can decide whether or not the cymbal has a stand.

  The only argument for nkellawaDrumstick is:

  1. the length

  The initial view is looking at the cymbal from the bottom. Of the 
  drumstick. The shaft and tip of the drumstick point back along the
  z-axis. 

  The origin lies in the center of the drumstick shaft.

*/

#include <stdio.h>
#include <math.h>
#include <tw.h>
//#include "nkellawaDS.cpp"
#include <f07/objects.h>"""

if__name__=='__main__':
    def display():
        
        twDisplayInit();
        twCamera();         # // sets up bounding box
        
        # //draws a drumstick of length 1
        
        nkellawaDrumstick(1);
        
        glFlush();
        glutSwapBuffers();



    def main(int argc, char** argv):

        glutInit(&argc,argv);
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
        twInitWindowSize(650,650);
        glutCreateWindow(argv[0]);
        twBoundingBox(-0.1,0.1,-0.1,0.1,-0.2,1.1);
        twMainInit();
        glutDisplayFunc(display);
        glutMainLoop();
        return 0;

