'''Demo exhibiting the use of a spotlight 

Written by Scott D. Anderson
scott.anderson@acm.org
Fall 2004
Ported to Python Fall 2009
'''

import sys
import math                            # for sin and cos

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''
## ================================================================

## variables for spotlight.  If you change the spotlight direction, you
## have to change the drawing of the cone.  Search for "depends on the
## light vector"

GLfloat lightPosition[] = {5,2,2,1};
GLfloat lightDirection [] = {0,-1,1};

## ================================================================
## Globals for callbacks

##allows user to change number of squares
int Resolution = 16;

bool outline = false ;           ## whether to draw the squares
bool smooth = true;             ## whether to use smooth shading
GLfloat lightCutoff = 35;

/* =====================================================================
 1*1 unit square drawn with triangle_strips. Adapted from lamppost.c This
 allows outlining the quads, if desired.  In practice, we would probably
 just use twDrawUnitSquare().
*/

void drawUnitSquare(int w, int h ) {
    int i,j;
    GLfloat dw = 1.0/w;
    GLfloat dh = 1.0/h;
    glNormal3f(0,1,0);
    for( i=0; i<w; ++i) {
        glBegin( GL_TRIANGLE_STRIP );
        for( j=0; j<=h; ++j ) {
                   glVertex3f(dw*i,0,dh*j);
            glVertex3f(dw*(i+1),0,dh*j);
        }
        glEnd();
    }
    if (outline) {  ##draw quads of unit square
        glDisable(GL_LIGHTING);
        glPushMatrix();
        glTranslatef(0,0.03,0);
        twColorName(TW_YELLOW);
        for( i=0; i<w; ++i) { 
            for( j=1; j<=h; ++j ) {
                glBegin( GL_LINE_LOOP );
                glVertex3f(dw*i,0,dh*(j-1));
                glVertex3f(dw*(i+1),0,dh*(j-1));
                glVertex3f(dw*(i+1),0,dh*(j));
                glVertex3f(dw*i,0, dh*(j));
                glEnd();
            }
        }
        glPopMatrix();
        glEnable(GL_LIGHTING);
    } 
}

##sets up lighting
void lamp() {
    GLfloat ambient [] = {1,1,1,1};
    GLfloat diffuse [] = {1,1,1,1};
    GLfloat specular [] = {0.5,0.5,0.5,1};
    GLfloat lightExponent = 5;

    glLightfv(GL_LIGHT0, GL_POSITION, lightPosition);
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse);
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular);
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, lightDirection);
    glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, lightCutoff);
    glLightf(GL_LIGHT0, GL_SPOT_EXPONENT, lightExponent);
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.3);
    glEnable(GL_LIGHT0); 
  
    if(smooth) glShadeModel(GL_SMOOTH);
    else glShadeModel(GL_FLAT);

    glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE);
    glEnable(GL_LIGHTING);
}

void display(void) {
    twDisplayInit();
    twCamera();

    ##draw cone at location of light, but without lighting
    glDisable(GL_LIGHTING);
    glPushMatrix();
    twTriple lampColor = { 0.9, 0.1, 0.1 };
    twColor(lampColor,1,64);
    GLfloat base = tan(lightCutoff*M_PI/180); ## radius of base of cone
    glTranslatef(lightPosition[0],lightPosition[1],lightPosition[2]);
    glRotatef(45,1,0,0);        ## depends on the light vector
    twCylinder(0.01,base,1,20,20);
    glPopMatrix();
    
    twAmbient(0);               ## no distracting ambient light
    lamp();                     ## turn on the light, and enable lighting

    ## Draw a surface for the light to illuminate
    glPushMatrix();
    glScalef(10,1,10);
    twTriple surfColor = {0.1, 0.9, 0.5};
    twColor(surfColor,1,10);     ## primarily interested in diffuse, but still
    drawUnitSquare(Resolution,Resolution);
    glPopMatrix();
    
    glFlush();
    glutSwapBuffers(); 
}

void modifySquare (unsigned char key, int x, int y) {
  switch(key) {
  case 'h': outline = false; break;
  case 'd': outline = true;  break;
  case '+': Resolution=Resolution<<1; Resolution=Resolution==0?1:Resolution; break;
  case '-': Resolution=Resolution>>1; Resolution=Resolution==0?1:Resolution; break;
  }
  glutPostRedisplay(); 
}

void modifyCutoff (unsigned char key, int x, int y) {
  switch(key) {
  case 'w': lightCutoff++; glutPostRedisplay(); break;
  case 'n': lightCutoff--; glutPostRedisplay(); break;
  }
}

void modifyShading (unsigned char key, int x, int y) {
 switch(key) {
 case 's': smooth = true;
           glutPostRedisplay(); break;
 case 'f': smooth = false;
           glutPostRedisplay(); break;
  }
}

void keyInit() {
  twKeyCallback('h', modifySquare, "hides the lines of the unit square");
  twKeyCallback('d', modifySquare, "draws the lines of the unit square");
  twKeyCallback('+', modifySquare, "double the number of squares");
  twKeyCallback('-', modifySquare, "halve the number of squares");
  twKeyCallback('w', modifyCutoff, "widens the cutoff angle");
  twKeyCallback('n', modifyCutoff, "narrows the cutoff angle");
  twKeyCallback('s', modifyShading, "smooth shading");
  twKeyCallback('f', modifyShading, "flat shading");
}


int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    twInitWindowSize(800,500);
    twBoundingBox(0,10,0,5,0,10);
    glutCreateWindow(argv[0]);
    glutDisplayFunc(display);
    twMainInit();
    keyInit();
    glutMainLoop();
    return 0;
}
