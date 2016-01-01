/* Demo of unprojection and the mouse callback.

Implemented Fall 2003
Scott D. Anderson
*/

#include <stdio.h>
#include <tw.h>

GLfloat winx=0,winy=0;

// These points come from unprojecting the mouse click.
twTriple A,B;

void display(void) {
    twDisplayInit();
    twCamera();

    // The following just draws a barn.
    glPushMatrix();
    twTriple endsColor = {0.2,0.8,0.3};
    twTriple sideColor = {0.8,0.2,0.3};
    twTriple roofColor = {0.4,0.4,0.2};
    twSolidBarn(endsColor,sideColor,roofColor);
    glPopMatrix();

    // This draws the two endpoints of our line segment from the near face
    // to the far face of the frustum.
    glPointSize(3);
    glBegin(GL_POINTS);
    glColor3f(1,1,0);
    glVertex3fv(A);
    glColor3f(1,0,1);
    glVertex3fv(B);
    glEnd();    

    // This draws the line segment from A to B.
    glLineWidth(2);
    glBegin(GL_LINES);
    glColor3f(1,1,0);
    glVertex3fv(A);
    glColor3f(1,0,1);
    glVertex3fv(B);
    glEnd();    

    glFlush();
    glutSwapBuffers();
}

void myMouseClick(int button, int state, int x, int y) {
    if(button!=GLUT_MIDDLE_BUTTON) {
        twMouseFunction(button,state,x,y);
        return;
    }
    y=500-y;                    // 500 is the fixed window height

    // This is the location of the mouse click, in window coordinates
    // instead of mouse coordinates.
    winx=x;
    winy=y;

    // This is a point data structure holding the location of the mouse click
    twTriple win = {winx,winy};
    // The Z value of the point is 0 for the near face
    win[2] = .01;                // near face
    // This does the unprojection, computing A from "win"
    twUnProject(A,win);
    twTriplePrint("A=",A);
    // The Z value of the point is 1 for the far face
    win[2] = .99;                // far face
    // This does the unprojection, computing B from "win"
    twUnProject(B,win);
    twTriplePrint("B=",B);

    glutPostRedisplay();
}    

int main(int argc, char** argv) {
  glutInit(&argc, argv);
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
  twInitWindowSize(500,500);
  glutCreateWindow(argv[0]);
  glutDisplayFunc(display);
  twBoundingBox(0,1,0,1,-1,0);
  twMainInit();            
  glutMouseFunc(myMouseClick);
  glutMainLoop();
  return 0;
}
