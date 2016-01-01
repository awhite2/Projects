'''Different views of the barn.  Demonstrates gluPerspective and
gluLookAt.  Also sets up the camera the same way TW does, so it acts as an
introduction to that code.

Implemented Fall 2003
Scott D. Anderson

The "G" code was added in Fall 2005.

Ported to Python in Fall 2009
'''

import sys
from math import sqrt,sin
from random import random

from TW import *

### ================================================================

## We're using twWireBarn, which draws a unit-size barn: a barn in a unit
## cube.  The BARN_SIZE is the scaling factor we're using.

BARN_SIZE = 5.0

## The constant B is useful for placing the camera and related operations.
## For example, since the center of the barn is at (B,B,-B), if we want to
## place the camera directly above the center of the barn, we'd place it at
## (B,Y,-B), where we determine Y in some way.

B = BARN_SIZE/2

## parameters for gluPerspective
FOVY = 90
ASPECT_RATIO = 1

## The cube that contains the barn fits inside a sphere whose diameter is
## sqrt(3*BARN_SIZE^2). Thus, the radius of that bounding sphere is the
## following.

BS_RADIUS  = BARN_SIZE*sqrt(3)/2

## The eye needs to be a little farther from the center of the bounding
## sphere than the radius of the bounding sphere.  In fact, to maintain
## the 90 degree FOVY and have the eye be as close as possible, we can do
## a little geometry to determine that the eye radius must be the
## following. 

EYE_RADIUS = BS_RADIUS*sqrt(2)

## Near can be anywhere between the eye and the bounding sphere, but for
## the sake of computing a legal location, we will make the image plane be
## tangent to the bounding sphere, and so NEAR is the
## EYE_RADIUS-BS_RADIUS.  Similarly, we'll make the FAR side of the
## frustum be tangent to the bounding sphere, so FAR is
## EYE_RADIUS+BS_RADIUS.
  
NEAR = EYE_RADIUS-BS_RADIUS
FAR  = EYE_RADIUS+BS_RADIUS

## The following global variable determines which view of the barn we
## have.  It is set in the key callbacks and selects a case that sets up
## the the camera location.

ViewMode = 'Z'

def setCamera():
    '''Configures the camera for one of several fixed setups, depending on a global variable named 'ViewMode.' '''
    # Note that Python doesn't have switch statements, so we have this:
    if ViewMode == 'Z':
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        gluPerspective(FOVY,ASPECT_RATIO,NEAR,FAR);
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
        gluLookAt(B,B,-B+EYE_RADIUS,
                  B,B,-B,
                  0,1,0);
    elif ViewMode == 'X':
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        gluPerspective(FOVY,ASPECT_RATIO,NEAR,FAR);
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
        gluLookAt(B+EYE_RADIUS,B,-B,
                  B,B,-B,
                  0,1,0);
    elif ViewMode == 'Y':
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        gluPerspective(FOVY,ASPECT_RATIO,NEAR,FAR);
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
        gluLookAt(B,B+EYE_RADIUS,-B,
                  B,B,-B,
                  0,0,-1);
    elif ViewMode == 'G':
        ## This is an exotic case where whenever we enter it, it chooses a
        ## random fovy (1-90 degrees) and computes the eye radius, near
        ## and far. We also compute the delta in each dimension so that we
        ## can look at the barn from the upper right front. */
        ## This yields fovy in the range [1-90].
        fovy = 89*random()+1;
        eyeRadius = BS_RADIUS/sin(fovy/2*M_PI/180);
        delta = eyeRadius/sqrt(3);
        near = eyeRadius-BS_RADIUS;
        far  = eyeRadius+BS_RADIUS;
        print "fovy=%f eye radius=%f delta=%f near=%f far=%f" % (
          fovy,eyeRadius,delta,near,far)
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        gluPerspective(fovy,ASPECT_RATIO,near,far);
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
        gluLookAt(B+delta,B+delta,-B+delta,
                  B,B,-B,
                  0,1,0);

def display():
    twDisplayInit();
    setCamera();
    twSetOriginPointSize(10)
    twCoordinateFrameCues()     # to show axes and such
 
    glPushMatrix();
    glScalef(BARN_SIZE,BARN_SIZE,BARN_SIZE);
    sideColor=(0.8,0.2,0.1)
    roofColor=(0.2,0.2,0.2)
    endColor =(0.5,0.8,0.3)
    twSolidBarn(sideColor,roofColor,endColor);
    glPopMatrix();
    
    glFlush();
    glutSwapBuffers();

def myCamSettings (key, x, y):
    global ViewMode
    ViewMode = key;
    glutPostRedisplay();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(0,5,0,5,-5,0);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    # nice fat lines.  In this program, we only need to say this once
    glLineWidth(3)               
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    twKeyCallback('X', myCamSettings, "View from X axis");
    twKeyCallback('Y', myCamSettings, "View from Y axis");
    twKeyCallback('Z', myCamSettings, "View from Z axis");
    twKeyCallback('G', myCamSettings, "View from XYZ axis with random FOVY and adjusted eye radius");
    glutMainLoop()

if __name__ == '__main__':
    main()
