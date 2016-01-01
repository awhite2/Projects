/* Builds several barns and shows an elevated view of them.

Scott D. Anderson
Fall 2000
*/

#include <stdio.h>
#include <stdlib.h>             /* for exit() */
#include <math.h>               /* for sqrt() */
#include <GL/glut.h>

/* This is the width and height of the window */
#define WIN_SIZE 400

/* ================================================================
   code for projection
*/

int camera_mode = 3;

#define SIZE 150

GLfloat left=-SIZE;
GLfloat right=SIZE;
GLfloat bottom=-SIZE;
GLfloat top=SIZE;
GLfloat near=244;
GLfloat far=1000;
int lookat=1;

void set_camera()
{
    GLfloat fovy;

    glViewport(10,10,WIN_SIZE-20,WIN_SIZE-20);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    switch(camera_mode) {
    case 3:
        fovy=(180.0/M_PI)*2.0*atan((top-bottom)/(2.0*near));
        fovy=45.0;
        printf("perspective angle: %f\n",fovy);
	
        gluPerspective(fovy,1,near,far);
        break;
    case 2:
        glFrustum(left,right,bottom,top,near,far);
        break;
    case 1:
    default: 
        glOrtho(left,right,bottom,top,near,far);
        break;
    }
    gluLookAt(-200,200,300,
              300,0,-300,
              0,1,0);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}


/* ================================================================
   code for the barn
*/

#define barn_width 3
#define barn_height 5
#define barn_length 7

GLfloat barn[10][3] = 
{
    {0,0,0},                    /* left, bottom, front */
    {barn_width,0,0},           /* right, bottom, front */
    {barn_width,barn_height,0}, /* right, top, front */
    {0,barn_height,0},          /* left, top, front */
    {barn_width/2.0,barn_height+barn_width/2.0,0}, /* ridge, front */
};

void init_barn()
{
    int i;
    for(i=0;i<5;++i) {
        barn[i][2] = 0;
        barn[5+i][0] = barn[i][0];
        barn[5+i][1] = barn[i][1];
        barn[5+i][2] = -barn_length;
    }
}

/* this draws an instance, so the caller should do translation, rotation
   and scaling */

void draw_barn()
{
    int i;

    glColor3f(1,0,0);           /* front is in red */
    glBegin(GL_LINE_LOOP);
    {
        glVertex3fv(barn[0]);
        glVertex3fv(barn[1]);
        glVertex3fv(barn[2]);
        glVertex3fv(barn[3]);
    }
    glEnd();
    glColor3f(1,0,0);           /* front top is also in red */
    glBegin(GL_LINE_LOOP);
    {
        glVertex3fv(barn[3]);
        glVertex3fv(barn[2]);
        glVertex3fv(barn[4]);
    }
    glEnd();
    glColor3f(0,1,0);           /* back is in green */
    glBegin(GL_LINE_LOOP);
    {
        glVertex3fv(barn[5]);
        glVertex3fv(barn[6]);
        glVertex3fv(barn[7]);
        glVertex3fv(barn[8]);
    }
    glEnd();
    glBegin(GL_LINE_LOOP);
    {
        glVertex3fv(barn[7]);
        glVertex3fv(barn[8]);
        glVertex3fv(barn[9]);
    }
    glEnd();
    glColor3f(0,0,1);           /* side rails in blue */
    glBegin(GL_LINES);
    {
        for(i=0;i<5;++i) {
            glVertex3fv(barn[i]);
            glVertex3fv(barn[i+5]);
        }
    }
    glEnd();
}

void display(void)
{
    set_camera();
    glPushAttrib(GL_ALL_ATTRIB_BITS);
    glClearColor(1,1,1,1);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    
    // Mark the origin; helps in debugging.
    //glColor3f(1,0,1);
    //glutSolidSphere(10,10,10);

    glPushMatrix();
    glScalef(20,20,20);
    draw_barn();
    glLoadIdentity();
    glTranslatef(100,0,-300);
    glScalef(15,15,15);
    draw_barn();                /* this barn is smaller */
    glLoadIdentity();
    glTranslatef(300,0,-300);
    glScalef(20,20,20);
    draw_barn();
    glLoadIdentity();
    glTranslatef(300,0,0);
    glScalef(30,30,30);         /* this one is really big */
    draw_barn();
    glPopMatrix();
      
    /* done */
    glFlush();
    glPopAttrib();
}

void key(unsigned char k, int xx, int yy)
{
    if( k == 'q' ) {
        exit(0);
    }
}

int main(int argc, char** argv)
{
    glutInit(&argc,argv);
    // have to add GLUT_DEPTH here, so that near things win over far
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH );
    glutInitWindowSize(WIN_SIZE, WIN_SIZE);
    glutCreateWindow(argv[0]);
    init_barn();
    glutDisplayFunc(display);
    glutKeyboardFunc(key);
    glEnable(GL_DEPTH_TEST); /* Enable hidden-surface-removal */
    glutMainLoop();
    return 0;
}
