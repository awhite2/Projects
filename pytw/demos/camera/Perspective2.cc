/* Contrast of perspective as a function of FOVY. Both scenes are viewing
   a wire cube of the same size.  The camera moved farther from the scene
   and the NEAR is changed so that the image plane is the same distance
   from the cube in each scene.  The aspect ratio of the cameras is the
   same.  The only difference in the camera shapes is the FOVY.

Implemented Fall 2003
Scott D. Anderson
*/

#include <stdlib.h>             // for exit();
#include <stdio.h>
#include <math.h>
#include <tw.h>

#define GAP  25      /* gap between subwindows */
int leftWinWidth=300;
int leftWinHeight=300;
int rightWinWidth=300;
int rightWinHeight=300;

void parentDisplay(void) {
    twDisplayInit();
    glFlush();
    glutSwapBuffers();
}

GLfloat aspectRatio(int w, int h) {
    return ((GLfloat) w) / ((GLfloat) h);
}

/* In the left display, the image plane is 1 unit from the VRP, which is
   3 units from the origin, and the cube is centered around the origin and
   is 2 units big, so the front face of the cube is a Z=1 and the image
   plane is at Z=2, so the front of the cube is exactly 1 unit from the
   image plane and 2 units from the VRP.

   Using similar triangles, we can show that the width and height of the
   projection of the front of the cube will be 1 unit.  

   The back of the cube is at Z=-1 and so is is 4 units from the VRP and 3
   units from the image plane.  Again using similar triangles, we can show
   that the width and height of the projection of the back of the cube
   will be 1/2 unit.  Thus, the back will be one half the dimensions of
   the front.  This makes sense because it is twice as far from the
   VRP. */

void leftDisplay(void) {
    twDisplayInit(0.8,1.0,1.0);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(90,aspectRatio(leftWinWidth,leftWinHeight),1,4);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(0,0,3, 0,0,0, 0,1,0);

    twColorName(TW_RED);
    glutWireCube(2);
  
    glFlush();
    glutSwapBuffers();
}


/* In the right display, the front face of the cube is again at Z=1, and
   the image plane is at Z=2, but the VRP is at Z=M.  Let h be half the
   projected width (or height) of the cube.  Using similar triangles, we
   can show that for the front of the cube, h/(M-2) = 1/(M-1).  Because
   the back of the cube is two units farther, we can show that
   h/(M-2)=1/(M+1).  These same formulas work for the cube on the left,
   using M=3, resulting in h=1/2 and h=1/4.  We double h to get the
   projected dimensions.
*/

GLfloat M=3.0;

void rightDisplay(void) {
    twDisplayInit(0.8,1.0,0.8);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    // The following code calculates a fovy such that the focal point is M
    // times farther from the origin than in the leftDisplay.  The result
    // is that the frustum is always 4 units tall (y direction), so the
    // half-height is 2.  The calculation is based on right triangle with
    // legs of length 2 and M-1, the fovy is double that angle, converted
    // to degrees.
    GLfloat fovy = 2*atan(2/(M-1))*180/M_PI;
    printf("fovy = %f degrees\n",fovy);
    gluPerspective(fovy,aspectRatio(rightWinWidth,rightWinHeight),M-2,M+2);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(0,0,M, 0,0,0, 0,1,0);

    twColorName(TW_MAGENTA);
    glutWireCube(2);
  
    glFlush();
    glutSwapBuffers();
}

int parentWin, leftWin, rightWin;

void redisplayAll(void) {
    glutSetWindow(leftWin);
    glutPostRedisplay();
    glutSetWindow(rightWin);
    glutPostRedisplay();
}

void modifyM(unsigned char key, int x, int y) {
    switch (key) {
    case 'q': exit(0); break;
    case '+': M++; break;
    case '-': M--; if( M<3 ) M=3; break;
    case '?': printf("+ to increase M, - to decrease, q to quit\n"); break;
    }
    printf("M is now %f\n", M);
    printf("Front projects to size %f\n", 2*(M-2)/(M-1));
    printf(" Back projects to size %f\n", 2*(M-2)/(M+1));
    
    redisplayAll();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH | GLUT_DOUBLE);
    glutInitWindowSize(leftWinWidth+rightWinWidth+GAP*3, 
                       leftWinHeight+GAP*2); //parent window
    parentWin = glutCreateWindow(argv[0]);
    glutDisplayFunc(parentDisplay);
    twBoundingBox(-1,1,-1,1,-1,1); // keeps twMainInit quiet
    twMainInit();

    /*glutCreateSubWindow returns the ID of the sub-window and takes 
      arguments:(int parent,int x,int y,int width,int height).
      Origin at x,y; height equals distance from y _down_ */
    leftWin = glutCreateSubWindow(parentWin,GAP,GAP,leftWinWidth,leftWinHeight);

    /*Each time you create a new window you need to give it its own 
      callbacks and initialization. These can be the same as those
      from other windows but you must call them each time*/
    twBoundingBox(-10,10,-10,10,-10,10);
    glutDisplayFunc(leftDisplay);
    twMainInit(); 
    glutKeyboardFunc(modifyM);
    glLineWidth(2);

    rightWin = glutCreateSubWindow(parentWin,GAP*2+leftWinWidth,GAP,rightWinWidth,rightWinHeight);
    glutDisplayFunc(rightDisplay);
    twMainInit();
    glutKeyboardFunc(modifyM);
    glLineWidth(2);
  
    redisplayAll(); 
    glutMainLoop();
    return 0;
}
