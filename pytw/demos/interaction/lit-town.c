/* Builds several barns, with different materials.  Added an overhead
   light source, to produce shadows.  Allows the user to walk around in
   the scene by clicking the mouse.

Scott D. Anderson
Fall 2000
*/

#include <stdio.h>
#include <stdlib.h>             /* for exit() */
#include <math.h>               /* for sqrt() */
#include <GL/glut.h>
#include "barn.h"


/* ================================================================
   code for frustum etc.  In this program, we size the viewport to
   the whole window, compute the gluPerspective parameters from the
   viewport, and finally compute the width and height of the image
   rectangle from the gluPerspective parameters.  The last
   parameters are important because they're used in the navigation.
*/

/* everything has the same aspect ratio (width/height): window,
   viewport, and image_rectangle, so we just need the aspect_ratio
   parameter and the heights.  To get widths, just multiply the
   height by the aspect ratio. */

GLfloat aspect_ratio;

/* This is the height of the window, in pixels */

GLsizei window_height=400;
GLsizei window_width=400;

/* Initialize the fovy to always be 90 degrees. In fact, we never
   change it, but we could. */

GLfloat fovy=90;
GLfloat near=10;
GLfloat far=1000;

GLfloat image_rectangle_height;
GLfloat image_rectangle_width;

void myReshape(GLsizei w, GLsizei h)
{
    aspect_ratio = ((GLfloat) w)/((GLfloat) h);
    window_width=w;
    window_height=h;

    glViewport(0,0,w,h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(fovy,aspect_ratio,near,far);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    /* The math here is a simple mapping from window coordinates
       (pixels) to world coordinates.  The height of the image
       rectangle is proportional to the height of the window, and
       the ratio of half the image height to near equals the
       tangent of the field of view angle.

       tan(fovy/2) = (irh/2)/near

       Solve that for irh.  Remember that we have to deal with
       degrees and radians as well.
    */
    image_rectangle_height = 2*near*tan(fovy*((M_PI/180)/2));
    image_rectangle_width = image_rectangle_height*aspect_ratio;
    // printf("irh = %f, irw = %f\n",image_rectangle_height,image_rectangle_width);
}

/* The first is the view reference point (VRP), which is the same as the
eye location for the gluLookAt function.  The second is the view plane
normal (VPN).  The VRP is modified by moving forward and backward in the
scene.  The VPN is modified by turning left and right. */

GLfloat VRP[3] = {300,20,0};
GLfloat VPN[3] = {-1,0,-1};

void place_camera()
{
    gluLookAt(VRP[0],VRP[1],VRP[2],
              VRP[0]+VPN[0],VRP[1]+VPN[1],VRP[2]+VPN[2],
              0,1,0);
}
    
void sun()
{
    GLfloat global_ambient[]= {0.4,0.4,0.4,1};
    GLfloat sun_direction[] = {-500,500,500,0};
    GLfloat sun_ambient[]   = {1,1,0.9,1};
    GLfloat sun_diffuse[]   = {1,1,0.9,1};
    GLfloat sun_specular[]  = {1,1,0.9,1};

    glEnable(GL_LIGHTING);
    // Doesn't matter right now, but if we add another light...
    glShadeModel(GL_SMOOTH);
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, global_ambient);

    glEnable(GL_LIGHT0);        /* light0 is the sun */
    glLightfv(GL_LIGHT0, GL_POSITION, sun_direction);
    glLightfv(GL_LIGHT0, GL_AMBIENT,  sun_ambient);
    glLightfv(GL_LIGHT0, GL_DIFFUSE,  sun_diffuse);
    glLightfv(GL_LIGHT0, GL_SPECULAR, sun_specular);
}

// Brick house, so these are slightly reddish

GLfloat ambient[]  = { 0.3, 0.2, 0.2, 1.0 };
GLfloat diffuse[]  = { 1.0, 0.8, 0.8, 1.0 };
GLfloat specular[] = { 1.0, 0.8, 0.8, 1.0 };

void display(void)
{
    glPushAttrib(GL_ALL_ATTRIB_BITS);
    glClearColor(1,1,1,1);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    /* The following code will put in our viewport and the cross-hairs.
       We're still in a coordinate system where the camera is at the
       origin and the image rectangle is centered about the negative z
       axis at a distance of near. */
    glColor3f(0,0,0);
    // This "if" statement allows me to easily excise this code, by just
    // changing the 1 to 0
    if(1) {
        glBegin(GL_LINE_LOOP);
        {
            GLfloat irw=image_rectangle_width/2;
            GLfloat irh=image_rectangle_height/2;
            glVertex3f(-irw,-irh,-near-1);
            glVertex3f(+irw,-irh,-near-1);
            glVertex3f(+irw,+irh,-near-1);
            glVertex3f(-irw,+irh,-near-1);
        }
        glEnd();
    }
    glBegin(GL_LINES);
    {
        GLfloat cx=image_rectangle_width/2;
        GLfloat cy=image_rectangle_height/2;
        glVertex3f(-cx,0,-near-1);
        glVertex3f(+cx,0,-near-1);
        glVertex3f(0,-cy,-near-1);
        glVertex3f(0,+cy,-near-1);
    }
    glEnd();

    glPushMatrix();
    // At this point, the camera moves to a new location
    place_camera();

    // Mark the ground in a dark green.  The 
    glColor3f(0,0.5,0);
    glBegin(GL_POLYGON);
    {
        glVertex3i(0,0,0);
        glVertex3i(400,0,0);
        glVertex3i(400,0,-400);
        glVertex3i(0,0,-400);
    }
    glEnd();

    solid_barn(60,70,100);

    glPushMatrix();
    glTranslatef(100,0,-200);
    solid_barn(50,60,50);
    glPopMatrix();

    // from now on, material has to have normals and so forth
    sun();

    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient);
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse);
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular);
    glMaterialf(GL_FRONT, GL_SHININESS, 100.0);

    glPushMatrix();
    glTranslatef(200,0,-200);
    glRotatef(-30,0,1,0);
    solid_barn(80,80,100);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(180,0,-100);
    glRotatef(180,0,1,0);
    solid_barn(60,70,70);
    glPopMatrix();
    
    glPopMatrix();
    /* done */
    glFlush();
    glutSwapBuffers();
    glPopAttrib();
}

void key(unsigned char k, int xx, int yy)
{
    if( k == 'q' ) {
        exit(0);
    }
    glutPostRedisplay();
}

void mouse(int btn, int state, int mx, int my)
{
    /* mx,my are in pixels, while ix is in world coordinates. */
    GLfloat ix;
    /* only left button down matters */
    if( ! (btn==GLUT_LEFT_BUTTON && state==GLUT_DOWN) ) return; 
    /* convert to first quadrant */
    my=window_height-my;
    // printf("mx = %d, my = %d\n",mx,my);
    /* measure from center */
    mx=mx-(window_width/2);
    my=my-(window_height/2);
    // printf("mx = %d, my = %d\n",mx,my);
    /* Figure out what angle to rotate.  This computation is based
       on the fact that the tangent of the angle of rotation equals
       x/near, after x has been scaled to image_rectangle
       units. That scaling is easy, because:

       x : window_width :: ix : image_rectangle_width

       Solve that for ix. */
    ix = (image_rectangle_width*mx)/window_width;
    // printf("ix=%f\n",ix);
    /* Now, do the rotation of the view plane normal (VPN) */
    {
        GLfloat theta=-atan(ix/near); /* flip the sign */
        // printf("theta = %f (%f)\n",theta, theta*180/M_PI);

        // temporary values 
        float x = VPN[0];
        float z = VPN[2];
        // for efficiency and brevity, compute these once
        float c = cos(theta);
        float s = sin(theta);

        VPN[0] =  x*c+z*s;
        VPN[2] = -x*s+z*c;
    }
    /* Now, move forward, if necessary. The math here is simpler;
       we just move forward by an amount proportional to the
       distance above the midline.  */
    {
        GLfloat factor=(20.0*my)/window_height;
        // printf("factor = %f\n",factor);
        // printf("VRP = %f %f\n",VRP[0],VRP[2]);
        VRP[0] += factor*VPN[0];
        VRP[2] += factor*VPN[2];
        // printf("VRP = %f %f\n",VRP[0],VRP[2]);
    }
    glutPostRedisplay();
}

int main(int argc, char** argv)
{
    glutInit(&argc,argv);
    // have to add GLUT_DEPTH here, so that near things win over far
    glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH );
    glutInitWindowSize(window_width, window_height);
    glutCreateWindow(argv[0]);
    glutDisplayFunc(display);
    glutReshapeFunc(myReshape);
    glutKeyboardFunc(key);
    glutMouseFunc(mouse);
    glEnable(GL_DEPTH_TEST); /* Enable hidden-surface removal */
    glutMainLoop();
    return 0;
}
