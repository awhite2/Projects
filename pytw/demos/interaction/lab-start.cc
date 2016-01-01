/* A starting point for the lab on interactively rotating the teddy bear.

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

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    twInitWindowSize(500,500);
    glutCreateWindow(argv[0]);
    glutDisplayFunc(display);
    twBoundingBox(-0.5,0.5,-0.5,0.5,-0.5,0.5);
    twMainInit();            
    glutMainLoop();
    return 0;
}
