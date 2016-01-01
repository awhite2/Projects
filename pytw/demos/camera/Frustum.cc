/* Displays a frustum.

Written by Caroline Geiersbach and Scott D. Anderson
scott.anderson@acm.org
Summer 2003
*/

#include <stdio.h>
#include <tw.h>

// This frustum has an aspect ratio of 2.

twTriple frustum[8] = {{-2,-1,-1}, {2,-1,-1}, {2,1,-1},
                       {-2,1,-1},{-20,-10,-10}, {20,-10,-10},
                       {20,10,-10}, {-20,10,-10}};

void drawFrustum() {
    glLineWidth(2.5);
    twColorName(TW_RED);
    glBegin(GL_LINE_LOOP);
    glVertex3fv(frustum[0]);
    glVertex3fv(frustum[1]);
    glVertex3fv(frustum[2]);
    glVertex3fv(frustum[3]);
    glEnd();

    twColorName(TW_GREEN);
    glBegin(GL_LINE_LOOP);
    glVertex3fv(frustum[4]);
    glVertex3fv(frustum[5]);
    glVertex3fv(frustum[6]);
    glVertex3fv(frustum[7]);
    glEnd();

    twColorName(TW_BLUE);
    glBegin(GL_LINES);
    glVertex3fv(frustum[0]);
    glVertex3fv(frustum[4]);

    glVertex3fv(frustum[1]);
    glVertex3fv(frustum[5]);

    glVertex3fv(frustum[2]);
    glVertex3fv(frustum[6]);

    glVertex3fv(frustum[3]);
    glVertex3fv(frustum[7]);
    glEnd();
}

void display(void) {
    twDisplayInit();
    twCamera(); // sets up camera based on bounding box coords.
  
    drawFrustum();
    twColorName(TW_PURPLE);
    glutSolidSphere(0.2,20,20);

    glFlush();
    glutSwapBuffers();   // necessary for animation
}

int main(int argc, char** argv) {
  glutInit(&argc, argv);
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
  twInitWindowSize(650,650);
  glutCreateWindow(argv[0]);
  twBoundingBox(-20,20,-20,20,-20,0);
  twMainInit(); 
  glutDisplayFunc(display);
  glutMainLoop();
  return 0;
}

