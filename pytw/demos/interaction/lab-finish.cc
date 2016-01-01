/* The finished lab on interactively rotating the teddy bear.

Implemented Fall 2006
Scott D. Anderson
*/

#include <stdio.h>
#include <stdlib.h>             // for exit
#include <tw.h>

GLfloat DeltaAngle;
GLfloat BearAngle;

void display(void) {
    twDisplayInit();
    twCamera();
    
    glPushMatrix();
    glRotatef(BearAngle,0,1,0);
    twTeddyBear();
    glPopMatrix();

    glFlush();
    glutSwapBuffers();
}

void rotate(void) {
    BearAngle += DeltaAngle;
    glutPostRedisplay();
}

/* This function is called when a special key goes down, and so it sets up
   the glutIdleFunc so that the bear starts rotating, in a direction that
   is determined by which special key is it. */

void startRotating(int key, int x, int y) {
    if(key != GLUT_KEY_RIGHT && key != GLUT_KEY_LEFT ) return;
    if(key == GLUT_KEY_RIGHT) {
	DeltaAngle=+2;
    } else {
	DeltaAngle=-2;
    }
    glutIdleFunc(rotate);
}

/* This function is the reverse of the startRotating function; it turns
   the idle function off.  It is called when a special key is released.
   For this lab, we don't even need to check which key has been released,
   but it's better to do so, so that when we add behavior for other keys,
   we won't inadvertently interfere with them.
*/

void stopRotating(int key, int x, int y) {
    if(key != GLUT_KEY_RIGHT && key != GLUT_KEY_LEFT ) return;
    glutIdleFunc(NULL);
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    twInitWindowSize(500,500);
    glutCreateWindow(argv[0]);
    glutDisplayFunc(display);
    twBoundingBox(-0.5,0.5,-0.5,0.5,-0.5,0.5);
    twMainInit();            
    glutSpecialFunc(startRotating); // set up the down-transition callback
    glutSpecialUpFunc(stopRotating); // set up the up-transition callback
    glutMainLoop();
    return 0;
}
