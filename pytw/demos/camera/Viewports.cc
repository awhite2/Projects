/* Demonstrates multiple viewports and the concepts of distortion,
   letterboxing, and clipping.  Displays one TeddyBear in three different
   sizes of viewport:

   2/3 S x 2/3 S
   1/3 S x 2/3 S
   S x 1/3 S
   
Written by Scott D. Anderson
scott.anderson@acm.org
Fall 2003
*/

#include <stdio.h>
#include <math.h>
#include <tw.h>

const int S = 600;                // window size

void cameraSetup() {
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(90,1,1,3);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(0,0,2, 0,0,0, 0,1,0);
}

void display(void) {
    twDisplayInit();
    glLineWidth(2);

    // lower viewport is landscape and spans the whole window
    cameraSetup();
    glViewport(0,0,S,S/3);
    twColorName(TW_RED);
    glutWireCube(1);
    twTeddyBear();

    // upper left viewport is square
    cameraSetup();
    glViewport(0,S/3,S/3*2,S/3*2);
    twColorName(TW_GREEN);
    glutWireCube(1);
    twTeddyBear();

    // upper right viewport is portrait
    cameraSetup();
    glViewport(S/3*2,S/3,S/3,S/3*2);
    twColorName(TW_BLUE);
    glutWireCube(1);
    twTeddyBear();

    glFlush();
    glutSwapBuffers();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(S,S);
    glutCreateWindow(argv[0]);
    glutDisplayFunc(display);
    twBoundingBox(-1,+1,-1,+1,-1,+1);
    twMainInit();
    glutMainLoop();
    return 0;
}
