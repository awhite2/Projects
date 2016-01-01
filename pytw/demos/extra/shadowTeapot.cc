/* Test of Angel's shadow example */

/* See pgs. 177-178 for his explanations of glVertexPointer, glColorPointer,
 glDrawElements */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <tw.h>

//variables for the position and angle of "sun"
GLfloat angle=0; 
GLfloat xVal =1.0; 
GLfloat yVal =0.0;
GLfloat zVal =0.0;

void sun() {
    GLfloat lightPosition [] = {xVal,yVal,zVal,1.0};
    GLfloat ambient [] = {1,1,1,1};
    GLfloat diffuse [] = {1,1,1,1};
    GLfloat specular [] = {0.8,0.8,0.8,1};
    glLightfv(GL_LIGHT1, GL_POSITION, lightPosition);
    glLightfv(GL_LIGHT1, GL_AMBIENT, ambient);
    glLightfv(GL_LIGHT1, GL_DIFFUSE, diffuse);
    glLightfv(GL_LIGHT1, GL_SPECULAR, specular);
    glShadeModel(GL_SMOOTH);
    glEnable(GL_LIGHT1);
    glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE);
    glEnable(GL_LIGHTING);
}

void drawShape() {
    glPushMatrix();
    glRotatef(45,0,1,0);
    glutSolidTeapot(4);
    glPopMatrix();
}

// Fill in a projection matrix, m, where the projection plane is at y=yp.
void projectionMatrix(GLfloat m[], GLfloat yp) {
    int i;
    for(i=0;i<16;i++) m[i]=0;
    m[0]=m[5]=m[10]=1; 
    m[7]=1/yp;
    for(i=0;i<16;i++) printf("%f ",m[i]);
}
    

void display(void) {
    xVal = 20.0*cos(angle);
    yVal = 20.0*sin(angle);
    GLfloat light[3]={xVal,yVal,zVal}; /*light position*/
    GLfloat m[16];

    glClearColor(1,1,1,1);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    twCamera();
    sun();                        // lighting

    glPushMatrix();
    glTranslatef(light[0], light[1], light[2]);
    twTriple sunColor = {0.5, 0.5, 0};
    twColor(sunColor,0,0);        // sun isn't shiny at all
    glutSolidSphere(0.5,10,10); // draw the sun
    glPopMatrix();

    glPushMatrix();
    glTranslatef(0.0, 3.0, 0.0);
    twTriple teapotColor = {0,0.6,0};
    twColor(teapotColor,0,64);        //color of object
    drawShape();
    glPopMatrix();
    
    glDisable(GL_LIGHTING);        // we don't want lighting effects on this surface!
    glColor3f(0.5,0.5,0.5);     // color of shadow

    glPushMatrix();
    glTranslatef(light[0], light[1], light[2]);        // STEP 1: move origin to light pos

    projectionMatrix(m, -light[1]);        // project onto -light[1]
    glMultMatrixf(m);           // STEP 2: flattens out the teapot

    glTranslatef(-light[0],-light[1],-light[2]); // STEP 3: translate back
    
    drawShape();                // STEP 4: draw the object in shadow color

    glPopMatrix();

    glFlush();
    glutSwapBuffers(); 
}

void timeLapse() {
    angle+=0.01;
    if(angle>M_PI) angle-=M_PI;
    glutPostRedisplay();
}

void start (unsigned char key, int x, int y) {
    angle = 0;
    xVal = 1;
    yVal = 0;
    zVal = 0;
    glutIdleFunc(timeLapse); //necessary after one pauses
    glutPostRedisplay();
}

void keyInit() {
    twKeyCallback('s', start, "starts animation from beginning");
}

int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    twInitWindowSize(500, 500);
    twBoundingBox(-10,10,0,20,-5,5);
    glutCreateWindow(argv[0]);
    glutDisplayFunc(display);
    twMainInit();
    keyInit();
    glutIdleFunc(timeLapse);
    glutMainLoop();
    return 0;
}
