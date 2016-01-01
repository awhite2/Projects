/* Rotating hexagon with HSV color wheel on front. 

   Each vertex is given a hue based on its angle.  The whole hexagon has
   the same intensity (V=1).  Thus, we convert from HSV to RGB to specify
   the color at each vertex.

First written by Scott D. Anderson, February, 1999
Updated to use TW Summer, 2003
*/

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <tw.h>

// ================================================================
// Cone has this radius and height

const float CONE_HEIGHT = 3;
const float CONE_RADIUS = 2;

/* ***********************************************************************
   Information about each vertex of the cone.  The avoids having to
   calculate the color and position information four times. */

typedef struct {
    twTriple position;
    twTriple rgbColor;
    twTriple hsvColor;
} Vinfo;

Vinfo Center;                        // special vertex for center
Vinfo Apex;                        // special vertex for apex
Vinfo* Vertices;                // dynamically allocated

int NumWedges = 6;

// Create a cone with a circular base on the z=0 plane with center at
// origin and tip at (0,0,-height).

void initVertexInfo() {
    twTripleInit(Center.position,0,0,0);
    twTripleInit(Center.rgbColor,1,1,1);
    twTripleInit(Center.hsvColor,0,0,1);
    twTripleInit(Apex.position,0,0,-CONE_HEIGHT);
    twTripleInit(Apex.rgbColor,0,0,0);
    twTripleInit(Apex.hsvColor,0,0,0);

    Vertices = (Vinfo*) malloc(NumWedges*sizeof(Vinfo));
    int i;
    GLfloat angle;
    for(i=0; i<NumWedges; i++) {
        angle = i*360.0/NumWedges; // in degrees
        twTripleInit(Vertices[i].hsvColor,angle,1,1);
        twHSV2RGB(Vertices[i].rgbColor,Vertices[i].hsvColor);
        angle = angle*M_PI/180.0; // in radians
        twTripleInit(Vertices[i].position,
                     CONE_RADIUS*cos(angle),
                     CONE_RADIUS*sin(angle),
                     0.0);
    }
}

void drawVertex(Vinfo* v) {
    glColor3fv(v->rgbColor);
    glVertex3fv(v->position);
}    

void drawColorHexCone(void) {
    int i;

    /* First, the circular base.  Do it as a triangle fan rather than one
       big polygon, otherwise OpenGL doesn't interpolate the colors
       correctly. */
    glBegin(GL_TRIANGLE_FAN); 
    drawVertex(&Center);
    for(i=0; i<NumWedges; i++) {
        drawVertex(&Vertices[i]);
        drawVertex(&Vertices[(i+1)%NumWedges]);
    }
    glEnd();
    /* Next, the side of the cone, again in a triangle fan. */
    glBegin(GL_TRIANGLE_FAN); 
    drawVertex(&Apex);
    for(i=0; i<NumWedges; i++) {
        drawVertex(&Vertices[i]);
        drawVertex(&Vertices[(i+1)%NumWedges]);
    }
    glEnd();
}

void display(void) {
    twDisplayInit();
    twCamera();

    drawColorHexCone();

    glFlush();
    glutSwapBuffers();
}

void increaseWedges(unsigned char k, int x, int y) {
    NumWedges++;
    initVertexInfo();
    glutPostRedisplay();
}

int main(int argc, char **argv) {
  glutInit(&argc, argv);
  initVertexInfo();
  twBoundingBox(-CONE_RADIUS,CONE_RADIUS,-CONE_RADIUS,CONE_RADIUS,-CONE_HEIGHT,0);
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
  twInitWindowSize(500, 500);
  glutCreateWindow(argv[0]);
  glutDisplayFunc(display);
  twMainInit();
  twKeyCallback('w',increaseWedges, "increase the number of wedges");
  glutMainLoop();
  return 0;
}
