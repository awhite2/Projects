""" Demo of the classic barn object.  This has a special callback to rotate
   it negatively around the y axis at 24 frames per second.

Implemented Fall 2006
Scott D. Anderson
Ported to Python, Fall 2009
"""

import sys
import math

from TW import *

### ================================================================

BarnAngle = 0.0;        # for rotating the barn 

def display():
    twDisplayInit();
    twCamera();

    lightpos = (3, 2, 1, 0 ); # directional light from low right side
    twGrayLight(GL_LIGHT0,lightpos,0.1,0,7,0.3);
    glEnable(GL_LIGHT0);
    glEnable(GL_LIGHTING);

    glPushMatrix();
    d = 255.0;
    roof = ( 188/d, 143/d, 143/d ); # rosy brown 
    wall = ( 178/d,  34/d,  34/d ); # firebrick
    glRotatef(BarnAngle,0,1,0);
    glScalef(10,10,10);
    twSolidBarn(wall,wall,roof);
    glPopMatrix();

    glFlush();
    glutSwapBuffers();

# True when timer animation on.  Also necessary so that the animation
# can turn itself off.
TimerAnimationOn = False;

# milliseconds per frame to yield 24 frames per second.  Alas, the
# integer value is 42 and it should be 41.67, so it's off by a little
MsecsPerFrame = 42;

# This function rotate the barn, redraw the screen, and sets up
# another timer interrupt, so that it's an infinite loop until the
# animation is stopped by a keyboard callback.

def rotateBarnAnimation(cookie):
    global BarnAngle
    # printf("rotating barn to %f\n",BarnAngle);
    BarnAngle += 5;
    glutPostRedisplay();
    if(TimerAnimationOn):
        glutTimerFunc(MsecsPerFrame, rotateBarnAnimation, 0);

def setTimer(key, x, y):
    global TimerAnimationOn
    TimerAnimationOn = not TimerAnimationOn;
    if( TimerAnimationOn ):
        print "starting timer animation";
        # Registers rotateBarnAnimation to be called in at least this
        # many milliseconds.  Last arg is a kind of cookie or identifer,
        # passed to the callback. In this case, we don't care, so we'll
        # just pass zero.  
        glutTimerFunc(MsecsPerFrame,
                      rotateBarnAnimation,
                      0);
    else:
        print "stopping timer animation";

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-10,10,0,10,-10,10);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    twKeyCallback('t',setTimer,"starts/stops timer interrupt animation");
    glutMainLoop();
    return 0;


if __name__ == '__main__':
    main()

