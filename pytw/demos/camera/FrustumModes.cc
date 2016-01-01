/* Demonstrates the projection concepts of distortion, letterboxing, and
   clipping.  Displays two TeddyBears in a 10x10x10 bounding cube, and
   defines keyboard callbacks to switch among distortion, letterboxing and
   clipping.
   
Directions for best effect:

(a) turn on the bounding box, and remember that nothing we do changes the
fact that it is, really, a cube.

(b) Try the l, c,and d callbacks with the initial window, which is square.
You'll notice that there's not much difference.  That's because mapping a
cubic view volume onto a square isn't too difficult.

(c) Reshape the window to be really wide and short, like 600x200.  Try the
l,c, and d callbacks now.  Notice that if we letterbox, there is a lot of
wasted space to the left and right, but the scene is not distorted.  If we
distort, the bears look squashed.  If we clip, the top and bottom get
clipped off.

(d) Reshape the window to be really narrow and tall, like 200x600.  Try
the l,c, and d callbacks now.  Notice that if we letterbox, there is a lot
of wasted space on the top and bottom, but the scene is not distorted.  If
we distort, the bears look squished tall and thin, like the window.  If we
clip, the left and right get clipped off.

This clipping of the right and left is exactly what happens when a movie
with a theatrical aspect ratio of, say, 2.35 to 1 is shown on a regular TV
with an aspect ratio of 4:3 (1.33 to 1).

Written by Caroline Geiersbach and Scott D. Anderson
scott.anderson@acm.org
Summer 2003
*/

#include <stdio.h>
#include <math.h>
#include <tw.h>

char* mode = "LETTERBOX";

const float BBSize = 5.0;
const float BearSize = 8.0;

void display(void) {
    twDisplayInit();
    twCamera();
    twError();
    
    glPushMatrix();
    glTranslatef(+3,0,0);

    glPushMatrix();
    glScalef(BearSize,BearSize,BearSize);
    twTeddyBear();
    glPopMatrix();

    glTranslatef(-6,0,0);

    glPushMatrix();
    glScalef(BearSize,BearSize,BearSize);
    twTeddyBear();
    glPopMatrix();

    glPopMatrix();
    twDrawString(-BBSize,-BBSize,BBSize,mode); // front left corner of bounding box
    twError();
    glFlush();
    glutSwapBuffers();       // necessary for animation
}


// Specify functions for the keys l,c,d 
void reshapeCommand(unsigned char k, int x, int y) {
    switch(k) {
    case 'c': twFrustumMode(CLIP); mode="CLIP"; break;
    case 'l': twFrustumMode(LETTERBOX); mode="LETTERBOX"; break;
    case 'd': twFrustumMode(DISTORT); mode="DISTORT"; break;
    }
glutPostRedisplay(); 
}

// Initialize new key settings 
void keyInit () {  
    twKeyCallback('c', reshapeCommand, "Reshape in clipping mode");
    twKeyCallback('l', reshapeCommand, "Reshape in letterbox mode");
    twKeyCallback('d', reshapeCommand, "Reshape in distort mode");
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    twInitWindowSize(500,500);
    glutCreateWindow(argv[0]);
    glutDisplayFunc(display);
    twBoundingBox(-BBSize,BBSize,-BBSize,+BBSize,-BBSize,BBSize);
    twMainInit();
    keyInit();
    glutMainLoop();
    return 0;
}
