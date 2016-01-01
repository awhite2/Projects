/* Loads a maze and allows us to navigate it.

Written by Scott D. Anderson, with Maze code from Dan Cliburn
scott.anderson@acm.org
Fall 2005
*/

#include <stdio.h>
#include <stdlib.h>             // for malloc
#include <string.h>             // for strlen
#include <math.h>
#include <tw.h>

// Some of the following variables are referred to in the maze code, so
// they need to be declared before we include that file.

twTriple VRP;
twTriple VPN = {0,0,-1};
twTriple VRIGHT = {1,0,0};

#include "Maze.h"

// Window dimensions
const int WinWidth = 600;
const int WinHeight = 600;

// Frustum dimensions.  We'll have some distortion if the frustum
// (image rectangle) is square and the window is not
const float FrustumWidth = 0.2;
const float FrustumHeight = 0.2;
const float Near = 0.1;
const float Far = 20;

bool godMode = false;

float Speed = 0.1;       // scale factor for movement

bool Collision = false;         // true if last movement was a collision

// ================================================================

void crosshairs() {
    // this will only work properly in the default camera frame
    glDisable(GL_LIGHTING);
    twColorName(TW_BLACK);
    float size = 0.5;
    GLfloat depth = -(Near+0.1);
    glBegin(GL_LINES);
    glVertex3f(-size,0,depth);
    glVertex3f(+size,0,depth);
    glVertex3f(0,-size,depth);
    glVertex3f(0,+size,depth);
    glEnd();
}

void display(void) {
    twDisplayInit(100/255.0,149/255.0,237/255.0);
    
    if(!godMode) {
        // This should be done only once.
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        glFrustum(-FrustumWidth/2,FrustumWidth/2,
                  -FrustumHeight/2,FrustumHeight/2,
                  Near,Far);

        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();

        crosshairs();
    
        // set up a light facing forward.  It travels with us!
        GLfloat origin[] = {0,0,0,1};
        GLfloat ahead[] = {0,0,-1};
        twGrayLight(GL_LIGHT1,origin,0,1,1);
        glLightfv(GL_LIGHT1,GL_SPOT_DIRECTION,ahead);
        glLightf(GL_LIGHT1,GL_SPOT_CUTOFF,20);

        if(Collision) {
            glDisable(GL_TEXTURE_2D);
            glDisable(GL_LIGHTING);
            twColorName(TW_WHITE);
            //twDrawString(-FrustumWidth/2,-FrustumHeight/2,0,"Collision");
            printf("Drawing Collision\n");
            twDrawString(-FrustumWidth/2,-FrustumHeight/2,-Near-0.01,"Collision");
        }
        // now, set the camera where we really want it
        // twCameraPosition();
        gluLookAt(VRP[0],VRP[1],VRP[2],
                  VRP[0]+VPN[0],VRP[1]+VPN[1],VRP[2]+VPN[2],
                  0,1,0);
    } else {
        twCamera();
        // Mark person's location.
        glDisable(GL_LIGHTING);
        twColorName(TW_MAGENTA);
        glPushMatrix();
        glTranslatef(VRP[0],VRP[1],VRP[2]);
        glutSolidSphere(0.1,10,10);
        glPopMatrix();
    }

    // Lighting
    glEnable(GL_LIGHTING);
    twAmbient(0.1);
    GLfloat lightDir[] = {2,3,5,0};
    twGrayLight(GL_LIGHT0,lightDir,1,1,1); // bright light in the sky

    glEnable(GL_TEXTURE_2D);
    glCallList(dlMaze);

    glFlush();
    glutSwapBuffers();       // necessary for animation
}

void turnCamera(float radians) {
        float c = cos(radians);
        float s = sin(radians);

        // update VPN
        float x = VPN[0];
        float z = VPN[2];
        VPN[0] = c*x+s*z;
        VPN[2] = -s*x+c*z;

        // update VRIGHT
        x = VRIGHT[0];
        z = VRIGHT[2];
        VRIGHT[0] = c*x+s*z;
        VRIGHT[2] = -s*x+c*z;
}    

bool collision(twTriple point) {
    // Collision if point x or z is within 0.1 (Near) of wall.  This code
    // only makes sense if Near < 1, but we don't check for that.  We need
    // to check if there's a wall in the direction we're going, and that
    // requires a determine if we're going left (x is small

    float x = point[0];
    float z = point[2];

    int floorx = (int) floor(x);
    int floorz = (int) floor(z);

    float fracx = x - floorx;
    float fracz = z - floorz;
    // if we're not near a cell boundary, there's no problem
    if (! ( fracx < Near ||
            fracx > 1-Near ||
            fracz < Near ||
            fracz > 1-Near ) ) return false;
    printf("%f %f cell boundary = %d %d = %c\n",
           x,z,floorx, floorz, Maze[floorz][floorx]);
    if(fracx<Near && Maze[floorz][floorx-1] == 'w') return true; // left wall
    if(fracx>1-Near && Maze[floorz][floorx+1] == 'w') return true; // right wall
    if(fracz<Near && Maze[floorz-1][floorx] == 'w') return true; // upper wall
    if(fracz>1-Near && Maze[floorz+1][floorx] == 'w') return true; // upper wall
    return false;
}

void mySpecialFunction( int key, int x, int y ) {
    switch(key) {
    case GLUT_KEY_UP:   VRP[1] += Speed; break;
    case GLUT_KEY_DOWN: VRP[1] -= Speed; break;
    case GLUT_KEY_RIGHT:
        // need to check for collisions here
        VRP[0]+=Speed*VRIGHT[0];
        VRP[1]+=Speed*VRIGHT[1]; // VRIGHT is always horizontal
        VRP[2]+=Speed*VRIGHT[2];
        break;
    case GLUT_KEY_LEFT:
        // need to check for collisions here
        VRP[0]-=Speed*VRIGHT[0];
        VRP[1]-=Speed*VRIGHT[1];
        VRP[2]-=Speed*VRIGHT[2];
        break;
    case GLUT_KEY_PAGE_UP:
    case GLUT_KEY_PAGE_DOWN:
        {
            float dir = (key==GLUT_KEY_PAGE_UP? 1 : -1);
            twTriple newVRP;
            newVRP[0] = VRP[0]+dir*Speed*VPN[0];
            newVRP[1] = VRP[1]+dir*Speed*VPN[1];
            newVRP[2] = VRP[2]+dir*Speed*VPN[2];
            if(!(Collision=collision(newVRP))) {
                VRP[0] = newVRP[0];
                VRP[1] = newVRP[1];
                VRP[2] = newVRP[2];
            }
            printf("Collision = %s\n",Collision?"true":"false");
        }
        break;
    case GLUT_KEY_HOME:
        // turn 10 degrees left
        turnCamera(10*M_PI/180);
        break;
    case GLUT_KEY_END:
        // turns 10 degrees right
        turnCamera(-10*M_PI/180);
        break;
    }
    glutPostRedisplay();
}

void myMouseFunction(int button, int state, int mx, int my ) {
    printf("myMouseFunction");
    if( button != GLUT_LEFT_BUTTON ) return;
    if( state != GLUT_DOWN ) return;
    mx = mx - WinWidth/2;
    my = WinHeight/2 - my;

    float ix = (FrustumWidth*mx)/WinWidth;
    float theta = -atan(ix/Near);
    // printf("mx=%d theta=%f degrees\n",mx,theta*180/M_PI);
    turnCamera(theta);
    glutPostRedisplay();
}    

void keys(unsigned char key, int x, int y) {
    switch(key) {
    case 'G':
        godMode = !godMode; 
        if(godMode) {
            glutMouseFunc(twMouseFunction);
            glutMotionFunc(twMotionFunction);
        } else {
            glutMouseFunc(myMouseFunction);
            glutMotionFunc(NULL);
        }
        twYview();
        break;
    }
    glutPostRedisplay();
}

int main(int argc, char** argv) {
  glutInit(&argc, argv);
  if(argc==1) {
      printf("Usage: %s mazefile\n",argv[0]);
      exit(0);
  }
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
  twInitWindowSize(WinWidth,WinHeight);
  glutCreateWindow(argv[0]);
  glutDisplayFunc(display);
  loadMaze(argv[1]);
  initMaze(0.3,0.8);
  twBoundingBox(0,MazeSizeX,0,1,0,MazeSizeZ);
  twMainInit(); 
  twKeyCallback('G',keys,"Toggle god's eye mode");
  if(!godMode) {
      // the following two are after twMainInit to override its callback settings
      glutMouseFunc(myMouseFunction);
      glutMotionFunc(NULL);
  } else {
      twYview();
  }
      
  glutSpecialFunc(mySpecialFunction);
  glutMainLoop();
  return 0;
}
