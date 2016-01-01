/* Contrast of perspective as a function of FOVY. Both scenes are viewing
   a wire cube of the same size.  The camera moved farther from the scene
   and the NEAR is changed so that the image plane is the same distance
   from the cube in each scene.  The aspect ratio of the cameras is the
   same.  The only difference in the camera shapes is the FOVY.

Implemented Fall 2003
Scott D. Anderson
*/

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

void leftDisplay(void) {
    twDisplayInit(0.8,1.0,1.0);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(90,aspectRatio(leftWinWidth,leftWinHeight),1,3);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(0,0,2, 0,0,0, 0,1,0);

    twColorName(TW_RED);
    glutWireCube(1);
  
    glFlush();
    glutSwapBuffers();
}

void rightDisplay(void) {
    twDisplayInit(0.8,1.0,0.8);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    const GLfloat M = 3;        // multiplication factor
    // The following code calculates a fovy such that the focal point is M 
    // times farther from the image plane than in the leftDisplay.  The
    // calculation is based on right triangle with legs of length 1 and M,
    // the fovy is double that angle, converted to degrees.
    GLfloat fovy = 2*atan(1/M)*180/M_PI;
    printf("fovy = %f degrees\n",fovy);
    gluPerspective(fovy,aspectRatio(rightWinWidth,rightWinHeight),M,2+M);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(0,0,1+M, 0,0,0, 0,1,0);

    twColorName(TW_MAGENTA);
    glutWireCube(1);
  
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

    rightWin = glutCreateSubWindow(parentWin,GAP*2+leftWinWidth,GAP,rightWinWidth,rightWinHeight);
    glutDisplayFunc(rightDisplay);
    twMainInit();
    glLineWidth(2);
  
    redisplayAll(); 
    glutMainLoop();
    return 0;
}
