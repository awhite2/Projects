/* Demo of two partly coincident quads, to show color speckling.

The red one is drawn first, then the green one.

Implemented Fall 2005
Scott D. Anderson
*/

#include <stdio.h>
#include <math.h>               // for atan
#include <tw.h>

GLint depthBits[1];             // depends on the graphics card
float EyeZ = 10;                // adjusted in a callback
float Near = 1;                 // adjusted in a callback
float fovy = 22;                // adjusted in a callback

float Angle = 0;                // angle for spinning around y

bool BgBlack = true;
bool DepthTest = true;

float TextLeft = -0.2;          // X coordinate for left end of text
float TextTop  = -0.2;          // Y coordinate for first line of text

void RedThenGreenQuads() {
    glBegin(GL_QUADS);

    glColor4f(1,0,0,1);                // solid red
    glVertex3f(0,0,0);        // lower left, then CCW
    glVertex3f(2,0,0);
    glVertex3f(2,2,0);
    glVertex3f(0,2,0);
    glColor4f(0,1,0,1);                // solid green
    glVertex3f(1,0,-1);        // lower left, then CCW
    glVertex3f(3,0,-1);
    glVertex3f(3,2,-1);
    glVertex3f(1,2,-1);

    glEnd();
}

void depthTest() {
    twColorName(BgBlack?TW_WHITE:TW_BLACK);
    if(DepthTest) {
        glEnable(GL_DEPTH_TEST);
        twDrawString(TextLeft,TextTop,0, "Depth Test ON - 'd' toggles");
    } else {
        glDisable(GL_DEPTH_TEST);
        twDrawString(TextLeft,TextTop,0, "Depth Test OFF - 'd' toggles");
    }
}

void display(void) {
    if(BgBlack) 
        glClearColor(0,0,0,0);        // transparent black
    else
        glClearColor(1,1,1,1);        // opaque white
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(fovy,1,Near,EyeZ+10);
    // gluPerspective(22,1,Near,EyeZ+10);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(1.5,1,EyeZ,
              1.5,1,0,
              0,1,0);
    glRotatef(Angle,0,1,0);
    
    depthTest();

    RedThenGreenQuads();

    glFlush();
    glutSwapBuffers();
}

void idle() {
    Angle+= 0.1;
    if(Angle>360) Angle -= 360;
    glutPostRedisplay();
}

void keys(unsigned char k, int, int) {
    float r;
    switch(k) {
    case 'b': BgBlack = !BgBlack; break;
    case 'd': DepthTest = !DepthTest; break;
    case '+':
        EyeZ *= 2;
        fovy = 2*atan(2/EyeZ)*180/M_PI;
        r = log((EyeZ+10)/Near)/log(2);
        printf("fovy = %f lost %f depth bits\n",fovy,r);
        break;
    case '-':
        EyeZ /= 2;
        fovy = 2*atan(2/EyeZ)*180/M_PI;
        r = log((EyeZ+10)/Near)/log(2);
        printf("fovy = %f lost %f depth bits\n",fovy,r);
        break;
    case 'y':
        glutIdleFunc( idle );
    }
   glutPostRedisplay();
}

int main(int argc, char** argv) {
  glutInit(&argc, argv);
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
  twInitWindowSize(700,300);
  glutCreateWindow(argv[0]);
  glutDisplayFunc(display);
  twBoundingBox(0,3,0,2,0,0);
  twMainInit();            
  twKeyCallback('b',keys,"toggle black/white background");
  twKeyCallback('d',keys,"toggle depth test");
  twKeyCallback('+',keys,"double eye distance");
  twKeyCallback('-',keys,"halve eye distance");
  twKeyCallback('y',keys,"toggle spinning");
  glGetIntegerv(GL_DEPTH_BITS,depthBits);
  printf("Depth bits = %d\n",depthBits[0]);
  glutMainLoop();
  return 0;
} 
