/* Different views of the barn.  Demonstrates gluPerspective and gluLookAt.

Implemented Fall 2007
Scott D. Anderson
*/

#include <stdio.h>
#include <stdlib.h>             // for exit
#include <tw.h>
#include <math.h>

const float BARN_WIDTH = 10.0;
const float BARN_LENGTH = 30.0;
const float BARN_HEIGHT = 20.0;

/* parameters for gluPerspective */
const GLfloat FOVY = 90;
const GLfloat ASPECT_RATIO = 1;

char ViewMode = '1';

void setCamera() {
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    switch(ViewMode) {
    case '1':
    case '2':
        gluPerspective(30,ASPECT_RATIO,1,200);
        break;
    default:
        printf("No such case for camera shape\n");
        exit(1);
    }

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    switch(ViewMode) {
    case '1':
        // Looking straight down the ridgepole
        gluLookAt(BARN_WIDTH*0.5,BARN_HEIGHT,90,
                  BARN_WIDTH*0.5,BARN_HEIGHT,0,
                  0,1,0);
        break;
    case '2':
        // Looking straight down the ridgepole, but at an angle
        gluLookAt(BARN_WIDTH*0.5,BARN_HEIGHT,90,
                  BARN_WIDTH*0.5,BARN_HEIGHT,0,
                  // The following comes out of analyzing the vector from the "shoulder" of the barn to the ridge
                  -0.5*BARN_WIDTH,0.3*BARN_HEIGHT,0);
        break;
    default:
        printf("No such case for camera location\n");
        exit(1);
    }
}

void display(void) {
    twDisplayInit();
    setCamera();
 
    glPushMatrix();
    glScalef(BARN_WIDTH,BARN_HEIGHT,BARN_LENGTH);
    twTriple xColor={1.0,0.0,0.0};
    twTriple yColor={0.0,1.0,0.0};
    twTriple zColor= {0.0,0.0,1.0};
    twWireBarn(xColor,yColor,zColor);
    glPopMatrix();
    
    glFlush();
    glutSwapBuffers();
}

void myCamSettings (unsigned char key, int x, int y) {
    ViewMode = key;
    glutPostRedisplay();
}

int main(int argc, char** argv) {
    glutInit(&argc,argv);
    glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH );
    twInitWindowSize(500, 500);
    glutCreateWindow(argv[0]);
    glutDisplayFunc(display);   
    twBoundingBox(0,BARN_WIDTH,0,BARN_HEIGHT,-BARN_LENGTH,0); // unnecessary, but it quiets the error message if you use the mouse
    twMainInit();
    twKeyCallback('1', myCamSettings, "View from in front of ridgepole, upright");
    twKeyCallback('2', myCamSettings, "View from in front of ridgepole, at an angle");
    glutMainLoop();
    return 0;
}
