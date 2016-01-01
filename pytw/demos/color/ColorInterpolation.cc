/* Demo of the color interpolation

Implemented Fall 2005
Modified to remove the Quad, Fall 2006

Scott D. Anderson
*/

#include <stdio.h>
#include <tw.h>

twTriple Tri[] = 
    {
        {0,0,0},
        {3,-2,-1},
        {1,4,0}
    };

twTriple Colors[] =
    {
        {1,0,0},                // red
        {1,0,1},                // magenta
        {1,1,0}                 // yellow
    };
        
// A simple convenience to shorten the code and guarantee that the same
// color is always associated with each vertex.  Notice that the color is
// given *before* the vertex.

void drawVertex(int index) {
    glColor3fv(Colors[index]);
    glVertex3fv(Tri[index]);
}

void drawTri() {
    glBegin(GL_TRIANGLES);
    drawVertex(0);
    drawVertex(1);
    drawVertex(2);
    glEnd();
}

void display(void) {
    twDisplayInit();
    twCamera();

    // glShadeModel(GL_SMOOTH);
    drawTri();

    glFlush();
    glutSwapBuffers();
}

int main(int argc, char** argv) {
  glutInit(&argc, argv);
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
  twInitWindowSize(500,300);
  glutCreateWindow(argv[0]);
  glutDisplayFunc(display);
  twBoundingBox(0,3,-2,4,-1,0);
  twMainInit();            
  glutMainLoop();
  return 0;
}
