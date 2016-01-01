/* RGB Color Cube with color interpolation

Implemented Summer 2003
Scott D. Anderson and Caroline Geiersbach
*/

#include <stdlib.h>
#include <tw.h>

twTriple vertices[8] = {{-1,-1,-1}, {1,-1,-1},
                        {1,1,-1}, {-1,1,-1},
                        {-1,-1,1}, {1,-1,1},
                        {1,1,1}, {-1,1,1}};

twTriple colors[8]   = {{0,0,0}, {1,0,0},
                        {1,1,0}, {0,1,0},
                        {0,0,1}, {1,0,1},
                        {1,1,1}, {0,1,1}};

/* draw a face given four vertices */

void face(int a, int b, int c , int d) {
    glBegin(GL_POLYGON);
    glColor3fv(colors[a]);
    glVertex3fv(vertices[a]);
    glColor3fv(colors[b]);
    glVertex3fv(vertices[b]);
    glColor3fv(colors[c]);
    glVertex3fv(vertices[c]);
    glColor3fv(colors[d]);
    glVertex3fv(vertices[d]);
    glEnd();
}                                                                                                                                                       
void colorcube(void) {
    /* map vertices to faces */
    face(0,3,2,1);
    face(2,3,7,6);
    face(0,4,7,3);
    face(1,2,6,5);
    face(4,5,6,7);
    face(0,1,5,4);
}

// Sends two vertices down the pipeline.  Presumably they form an edge
void edge(int A, int B) {
    glVertex3fv(vertices[A]);
    glVertex3fv(vertices[B]);
}

void wireCube() {
    glBegin(GL_LINES);
    // back
    edge(0,1);
    edge(1,2);
    edge(2,3);
    edge(3,0);
    // front
    edge(4,5);
    edge(5,6);
    edge(6,7);
    edge(7,4);
    // sides
    edge(0,4);
    edge(1,5);
    edge(2,6);
    edge(3,7);
    glEnd();
}

void display(void) {
    twDisplayInit();
    twCamera();

    // The frame around the cube is thick gray.
    twColorName(TW_GRAY);
    glLineWidth(2);
    wireCube();                        // glutWireCube would also work

    glShadeModel(GL_SMOOTH);        // bilinear color interpolation
    colorcube();                //draw cube

    glFlush();
    glutSwapBuffers();
}

int main(int argc, char **argv) {
  glutInit(&argc, argv);
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
  twInitWindowSize(500, 500);  
  glutCreateWindow(argv[0]);
  glutDisplayFunc(display);
  twVertexArray(vertices,8);
  twMainInit();
  glutMainLoop();
  return 0;
}
