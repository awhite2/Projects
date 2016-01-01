/* An attempt a forced-perspective.  The two teddy bears are, in real
   life, the same size.  I'm trying to make it look like they're looking
   at each other.

This implementation has just begun.

Implemented Fall 2005
Scott D. Anderson

*/

#include <stdio.h>
#include <stdlib.h>                // for random
#include <math.h>
#include <tw.h>


bool front = true;

float CamY = 0.5;

void setCamera() {
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(60,1,1,10);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    // Camera is mid-height and aimed straight ahead.
    gluLookAt(4,CamY,0,
              4,CamY,-1,
              0,1,0);
}

twTriple red = {1,0,0};

void display(void) {
    twDisplayInit();
    if( front ) {
        setCamera();
    } else {
        twCamera();
    }
 
    // The bear on the left is the smaller one.  We have to lower it as
    // well, so that the feet appear to be at the same level.  
    glPushMatrix();
    glTranslatef(3,-CamY/3,-4);
    twTeddyBear();
    twWireBarn(red,red,red);
    glPopMatrix();
    
    glPushMatrix();
    glTranslatef(4,0,-3);
    twTeddyBear();
    twWireBarn(red,red,red);
    glPopMatrix();
    
    glFlush();
    glutSwapBuffers();
}

void myCamSettings (unsigned char key, int x, int y) {
    glutPostRedisplay();
}

int main(int argc, char** argv) {
    glutInit(&argc,argv);
    glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH );
    twInitWindowSize(500, 500);
    glutCreateWindow(argv[0]);
    glutDisplayFunc(display);   
    twBoundingBox(0,10,0,2,-10,0);
    twMainInit();
    twKeyCallback('g', myCamSettings, "Global view");
    glutMainLoop();
    return 0;
}
