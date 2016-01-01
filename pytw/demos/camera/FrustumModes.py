''' Demonstrates the projection concepts of distortion, letterboxing, and
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

ported to Python, Fall 2009
'''

import sys
import math                     # for atan and others

from TW import *

## ================================================================

Mode = "LETTERBOX"              # for the frustum

BBSize = 5.0;                   # bounding box size
BearSize = 8.0;

def display():
    twDisplayInit();
    twCamera();
    
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
    # put some text on front left corner of bounding box
    twDrawString(-BBSize,-BBSize,BBSize,Mode); 
    glFlush();
    glutSwapBuffers()

def reshapeCommand(key, x, y):
    '''Specify functions for the keys l,c,d '''
    global Mode
    if key == 'c': 
        twFrustumMode(CLIP); 
        Mode="CLIP"; 
    elif key == 'l': 
        twFrustumMode(LETTERBOX); 
        Mode="LETTERBOX";
    elif key == 'd': 
        twFrustumMode(DISTORT); 
        Mode="DISTORT"; 
    glutPostRedisplay(); 

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-BBSize,BBSize,-BBSize,+BBSize,-BBSize,BBSize);
    twInitWindowSize(500,500);
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    twKeyCallback('c', reshapeCommand, "Reshape in clipping mode");
    twKeyCallback('l', reshapeCommand, "Reshape in letterbox mode");
    twKeyCallback('d', reshapeCommand, "Reshape in distort mode");
    glutMainLoop()

if __name__ == '__main__':
    main()
