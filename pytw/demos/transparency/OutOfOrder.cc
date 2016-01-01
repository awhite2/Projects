/* Demo of three quads whose projections overlap

Implemented Fall 2005
Scott D. Anderson
*/

#include <stdio.h>
#include <tw.h>

bool BgBlack = true;

float TextLeft = -0.2;          // X coordinate for left end of text

void Quad() {
    glBegin(GL_QUADS);

    glVertex2f(0,0);       // lower left, then CCW
    glVertex2f(1,0);
    glVertex2f(1,1);
    glVertex2f(0,1);

    glEnd();
}

void display(void) {
    if(BgBlack) 
        glClearColor(0,0,0,0);        // transparent black
    else
        glClearColor(1,1,1,1);        // opaque white
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    twCamera();
    glEnable(GL_DEPTH_TEST);

    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

    glPushMatrix();
    glColor4f(1,0,0,1);         // opaque red first
    Quad();
    glColor4f(0,1,0,0.5);       // 50% green second
    glDepthMask(GL_FALSE);
    glTranslatef(0.2,0,1);      // forward and right
    Quad();
    glDepthMask(GL_TRUE);
    glColor4f(0,0,1,1);         // opaque blue third
    glTranslatef(0.2,0,-0.5);      // more right, but middle
    Quad();
    glPopMatrix();

    glFlush();
    glutSwapBuffers();
}

void keys(unsigned char k, int, int) {
    switch(k) {
    case 'b': BgBlack = !BgBlack; break;
    }
    glutPostRedisplay();
}

int main(int argc, char** argv) {
  glutInit(&argc, argv);
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
  twInitWindowSize(500,500);
  glutCreateWindow(argv[0]);
  glutDisplayFunc(display);
  twBoundingBox(0,1,0,1,0,1);
  twMainInit();            
  twKeyCallback('b',keys,"toggle black/white background");
  glutMainLoop();
  return 0;
} 
