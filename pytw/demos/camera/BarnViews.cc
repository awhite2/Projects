/* Different views of the barn.  Demonstrates gluPerspective and gluLookAt.

Implemented Fall 2003
Scott D. Anderson

The "G" code was added in Fall 2005.
*/

#include <stdio.h>
#include <stdlib.h>                // for random
#include <math.h>
#include <tw.h>

/* We're using twWireBarn, which draws a unit-size barn: a barn in a unit
   cube.  The BARN_SIZE is the scaling factor we're using. */

const float BARN_SIZE = 5.0;

/* The constant B is useful for placing the camera and related operations.
   For example, since the center of the barn is at (B,B,-B), if we want to
   place the camera directly above the center of the barn, we'd place it a
   (B,Y,-B), where we determine B in some way. */

const float B = BARN_SIZE/2;

/* parameters for gluPerspective */
const GLfloat FOVY = 90;
const GLfloat ASPECT_RATIO = 1;

/* The cube that contains the barn fits inside a sphere whose diameter is
   sqrt(3*BARN_SIZE^2). Thus, the radius of that bounding sphere is the
   following. */

const GLfloat BS_RADIUS  = BARN_SIZE*sqrt(3)/2;

/* The eye needs to be a little farther from the center of the bounding
   sphere than the radius of the bounding sphere.  In fact, to maintain
   the 90 degree FOVY and have the eye be as close as possible, we can do
   a little geometry to determine that the eye radius must be the
   following. */

const GLfloat EYE_RADIUS = BS_RADIUS*sqrt(2);

/* Near can be anywhere between the eye and the bounding sphere, but for
   the sake of computing a legal location, we will make the image plane be
   tangent to the bounding sphere, and so NEAR is the
   EYE_RADIUS-BS_RADIUS.  Similarly, we'll make the FAR side of the
   frustum be tangent to the bounding sphere, so FAR is
   EYE_RADIUS+BS_RADIUS. */
  
const GLfloat NEAR = EYE_RADIUS-BS_RADIUS;
const GLfloat FAR  = EYE_RADIUS+BS_RADIUS;

/* The following global variable determines which view of the barn we
   have.  It is set in the key callbacks and selects a case that sets up
   the the camera location. */

char ViewMode = 'Z';

// returns a random floating point number between 0 and 1.
float random01() {
    float n = (float) random();
    float d = (float) RAND_MAX;
    return n/d;
}

void setCamera() {
    switch(ViewMode) {
    case 'Z':
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        gluPerspective(FOVY,ASPECT_RATIO,NEAR,FAR);
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
        gluLookAt(B,B,-B+EYE_RADIUS,
                  B,B,-B,
                  0,1,0);
        break;
    case 'X':
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        gluPerspective(FOVY,ASPECT_RATIO,NEAR,FAR);
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
        gluLookAt(B+EYE_RADIUS,B,-B,
                  B,B,-B,
                  0,1,0);
        break;
    case 'Y':
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        gluPerspective(FOVY,ASPECT_RATIO,NEAR,FAR);
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
        gluLookAt(B,B+EYE_RADIUS,-B,
                  B,B,-B,
                  0,0,-1);
        break;
    case 'G':
        /* This is an exotic case where whenever we enter it, it chooses a
           random fovy (1-90 degrees) and computes the eye radius, near
           and far. We also compute the delta in each dimension so that we
           can look at the barn from the upper left front. */
        // This yields fovy in the range [1-90].
        float fovy = 89*random01()+1;
        float eyeRadius = BS_RADIUS/sin(fovy/2*M_PI/180);
        float delta = eyeRadius/sqrt(3);
        float near = eyeRadius-BS_RADIUS;
        float far  = eyeRadius+BS_RADIUS;
        printf("fovy=%f eye radius=%f delta=%f near=%f far=%f\n",fovy,eyeRadius,delta,near,far);
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        gluPerspective(fovy,ASPECT_RATIO,near,far);
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
        gluLookAt(B+delta,B+delta,-B+delta,
                  B,B,-B,
                  0,1,0);
    }
}

void display(void) {
    twDisplayInit();
    setCamera();
 
    glPushMatrix();
    glScalef(BARN_SIZE,BARN_SIZE,BARN_SIZE);
    twTriple sideColor={0.8,0.2,0.1};
    twTriple roofColor={0.2,0.2,0.2};
    twTriple endColor={0.5,0.8,0.3};
    twSolidBarn(sideColor,roofColor,endColor);
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
    twBoundingBox(0,5,0,5,-5,0);
    twMainInit();                // calculate near and far 
    twKeyCallback('X', myCamSettings, "View from X axis");
    twKeyCallback('Y', myCamSettings, "View from Y axis");
    twKeyCallback('Z', myCamSettings, "View from Z axis");
    twKeyCallback('G', myCamSettings, "View from XYZ axis with random FOVY and adjusted eye radius");
    glutMainLoop();
    return 0;
}
