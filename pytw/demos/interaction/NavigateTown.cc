/* Puts up a fence around a scene with several small buildings.
   Demonstrates navigation callbacks.

Written by Caroline Geiersbach and Scott D. Anderson
scott.anderson@acm.org
Summer 2003
*/

#include <stdio.h>
#include <math.h>
#include <tw.h>

// Window dimensions
const int WinWidth = 600;
const int WinHeight = 600;

// Frustum dimensions.  We'll have some distortion if the frustum
// (image rectangle) is square and the window is not
const float FrustumWidth = 2;
const float FrustumHeight = 2;
const float Near = 1;
const float Far = 200;

// Bounding box dimensions

const int BBXmin = -45;         // bounding box X min
const int BBXmax = 65;          // X max
const int BBYmin = 0;           // Y min
const int BBYmax = 65;          // Y max
const int BBZmin = -130;        // Z min
const int BBZmax = 5;           // Z min

twTriple rail [] =
{
  {0,0,0},
  {5,0,0},
  {5,2,0},
  {0,2,0}
};

void drawRail () {
    glBegin(GL_POLYGON);
    {
        glVertex3fv(rail[0]);
        glVertex3fv(rail[1]);
        glVertex3fv(rail[2]);
        glVertex3fv(rail[3]);
    }
    glEnd();
}

// Arbitrary numeric identifier for this display list.
const int PICKET = 100;

/* Initializes a display list to draw one picket.  The picket is 5
   wide, 10 high, and 2 deep, with the reference point at the lower
   left front of the picket. Rails stick out 0.5 to the left and are
   flat planes through the middle of the picket, with a width of 5 and
   a height of 2, with the bottom edge at heights 1 and 4. */

void drawInit() {
  twTriple maroon = {0.5,0,0};
  twTriple black  = {0,0,0};
  twTriple orange = {1,0.5,0};
  
  /* Create a call list for one picket of the fence */
  glNewList(PICKET, GL_COMPILE);
  glPushMatrix();
  glScalef(4,10,2); // must scale to create 4*10*2 barn
  twSolidBarn(maroon, black, orange);
  glPopMatrix();
  glPushMatrix();
  twColorName(TW_OLIVE);
  glTranslatef(-0.5,1,-1);
  drawRail();
  glTranslatef(0,3,0);
  drawRail();
  glPopMatrix();
  glEndList();
}

void fences() {
    int i;
    // draw front fence
    glPushMatrix();
    glTranslatef(-40,0,0);
    for(i=0;i<20;i++) {
        glCallList(PICKET);
        glTranslatef(5,0,0);
    }
    glPopMatrix();
  
    // draw right side fence
    glPushMatrix();
    glTranslatef(60,0,0);
    glRotatef(90,0,1,0); 
    for(i=0;i<25;i++) {
        glCallList(PICKET);
        glTranslatef(5,0,0);
    }
    glPopMatrix();
  
    // draw left side fence
    glPushMatrix();
    glTranslatef(-40,0,0);
    glRotatef(90,0,1,0);
    for(i=0;i<17;i++) {
        glCallList(PICKET);
        glTranslatef(5,0,0);
    }
    glPopMatrix();
}

void barn1() {
    glPushMatrix();
    glTranslatef(-40,0,-125);
    glRotatef(-90,0,1,0);
    glScalef(40,35,50);
    twTriple teal = {0,0.5,0.5};
    twTriple dark_blue = {0,0,0.5};
    twTriple cyan = {0,1,1};
    twSolidBarn(teal,dark_blue,cyan);
    glPopMatrix();
}

void crosshairs() {
    // this will only work properly in the default camera frame
    GLfloat near,far;
    twNearFarSet(near,far);     // this really should be called Get...
    glDisable(GL_LIGHTING);
    twColorName(TW_BLACK);
    int size = 10;
    GLfloat depth = -(near+1);
    glBegin(GL_LINES);
    glVertex3f(-size,0,depth);
    glVertex3f(+size,0,depth);
    glVertex3f(0,-size,depth);
    glVertex3f(0,+size,depth);
    glEnd();
}

twTriple VRP = {(BBXmax+BBXmin)/2,
                (BBYmax+BBYmin)/2,
                BBZmax };
twTriple VPN = {0,0,-1};
twTriple VRIGHT = {1,0,0};

void display(void) {
    twDisplayInit();
    
    //twCameraShape();
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

    // now, set the camera where we really want it
    // twCameraPosition();
    gluLookAt(VRP[0],VRP[1],VRP[2],
              VRP[0]+VPN[0],VRP[1]+VPN[1],VRP[2]+VPN[2],
              0,1,0);

    // draw ground
    twColorName(TW_GREEN);
    twGround();

    // draw sky
    twTriple lightSkyBlue = { 135.0/255.0, 206.0/255.0, 250.0/255.0 };
    twColor(lightSkyBlue,0,0);
    twSky();

    // Lighting
    glEnable(GL_LIGHTING);
    twAmbient(0.1);
    GLfloat lightDir[] = {2,3,5,0};
    twGrayLight(GL_LIGHT0,lightDir,0.1,0.5,0.5); // bright light in the sky

    fences();
    barn1();                    // the one in the back corner

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


void mySpecialFunction( int key, int x, int y ) {
    switch(key) {
    case GLUT_KEY_UP:   VRP[1]++; break;
    case GLUT_KEY_DOWN: VRP[1]--; break;
    case GLUT_KEY_RIGHT:
        VRP[0]+=VRIGHT[0];
        VRP[1]+=VRIGHT[1];
        VRP[2]+=VRIGHT[2];
        break;
    case GLUT_KEY_LEFT:
        VRP[0]-=VRIGHT[0];
        VRP[1]-=VRIGHT[1];
        VRP[2]-=VRIGHT[2];
        break;
    case GLUT_KEY_PAGE_UP:
        // goes forward
        VRP[0]+=VPN[0];
        VRP[1]+=VPN[1];
        VRP[2]+=VPN[2];
        break;
    case GLUT_KEY_PAGE_DOWN:
        // goes backward
        VRP[0]-=VPN[0];
        VRP[1]-=VPN[1];
        VRP[2]-=VPN[2];
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
    if( button != GLUT_LEFT_BUTTON ) return;
    if( state != GLUT_DOWN ) return;
    mx = mx - WinWidth/2;
    my = WinHeight/2 - my;

    float ix = (FrustumWidth*mx)/WinWidth;
    float theta = -atan(ix/Near);
    printf("mx=%d theta=%f degrees\n",mx,theta*180/M_PI);
    turnCamera(theta);
    glutPostRedisplay();
}    

int main(int argc, char** argv) {
  glutInit(&argc, argv);
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
  twInitWindowSize(WinWidth,WinHeight);
  glutCreateWindow(argv[0]);
  drawInit();
  glutDisplayFunc(display);
  twBoundingBox(BBXmin,BBXmax,BBYmin,BBYmax,BBZmin,BBZmax);
  twMainInit(); 
  // the following two are after twMainInit to override its callback settings
  glutMouseFunc(myMouseFunction);
  glutMotionFunc(NULL);
  glutSpecialFunc(mySpecialFunction);
  glutMainLoop();
  return 0;
}
