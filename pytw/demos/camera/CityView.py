'''Demo of perspective. Callbacks to modify fovy, near and far.  

Implemented Summer 2003
Scott D. Anderson and Caroline Geiersbach

Ported to Python Fall 2009
'''

import sys
from math import sqrt,sin
from random import random

from TW import *

## variables for gluPerspective
myFovy = 90
myAspectRatio = 1
myNear = 1
myFar  = 100

def setCamera():
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(myFovy,myAspectRatio,myNear,myFar);
    twCameraPosition(); 

def drawBuilding(color, 
                 xPos, yPos, zPos,
                 xScale, yScale, zScale):
    '''Draws a building (a cube) in a given color at the given
    position and scale

The color (arg 1) is just one of the TW color names.  The function
translates the building to the desired location x,y,and z locations
(args 2-4), and scales the object (args 5-7).  No rotation.'''
    glPushMatrix();
    twColorName(color);
    glTranslatef(xPos,yScale/2+yPos,zPos); # y transl.affected by scaling
    glScalef(xScale,yScale,zScale); # scales from center of glutWireCube
    glutSolidCube(1);
    glPopMatrix();
                
def display():
    twDisplayInit();
    setCamera();
    #twCamera();
 
    twColorName(TW_GREEN);
    twGround();

    ## draw buildings
    drawBuilding(TW_MAGENTA,-5,0,-20,10,20,10);
    drawBuilding(TW_OLIVE,-20,0,-20,15,45,15);
    drawBuilding(TW_PURPLE,-40,0,-20,10,20,10);
    drawBuilding(TW_RED,10,0,-20,15,60,10);
    drawBuilding(TW_ORANGE,50,0,-20,10,40,20);
    drawBuilding(TW_MAROON,30,0,-20,10,50,10);
    drawBuilding(TW_BLUE,-60,0,-20,8,40,8);

    ## done
    glFlush();
    glutSwapBuffers();

def myCamSettings (key, x, y):
    global myFovy, myNear, myFar
    if key == '+':
        myFovy += 1
    elif key == '-': 
        myFovy -= 1
    elif key == 'n': 
        myNear -= 1
    elif key == 'N': 
        myNear += 1
    elif key == 'f': 
        myFar -= 1
    elif key == 'F': 
        myFar += 1
    else:
        print "invalid key %c for myCamSettings()." % (key)
    glutPostRedisplay();

def printCamSettings(key, x, y):
    print "near=%f, far=%f, fovy=%f" % (myNear,myFar,myFovy)

def initVals ():
    global myNear, myFar, myFovy
    (myNear,myFar) = twNearFarSet()
    myFovy = twFovySet();

def myReset(key, x, y):
    initVals();
    twReset(key, x, y);

def keyInit ():
    '''Initialize new key settings'''
    twKeyCallback('+', myCamSettings, "Increase the field of view angle by 1");
    twKeyCallback('-', myCamSettings, "Decrease the field of view angle by 1");
    twKeyCallback('n', myCamSettings, "Decrease near value by 1");
    twKeyCallback('N', myCamSettings, "Increase near value by 1");
    twKeyCallback('f', myCamSettings, "Decrease far value by 1");
    twKeyCallback('F', myCamSettings, "Increase far value by 1");
    twKeyCallback('r', myReset, "Reset to original screen");
    twKeyCallback('=', printCamSettings, "print camera settings");

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-50,50,0,60,-50,50);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    initVals();
    keyInit();       
    glutMainLoop()

if __name__ == '__main__':
    main()
