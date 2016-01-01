""" Demo of the classic mass-spring oscillator.  This is undamped
   (frictionless), so it will oscillate forever like this.

Recall that the frequency of oscillation is equal to sqrt(k/m).  The
higher the spring constant, the fasster the oscillation.  The larger the
mass, the slower the oscillation.  The greater the initial displacement,
the greater the amplitude of the oscillation.  The smaller the "DeltaT,"
the smoother the motion will be.

Implemented Fall 2004
Scott D. Anderson
Ported to Python, Fall 2009
"""

import sys
import math

from TW import *

### ================================================================

Width =100;                     # width of scene
WallWidth=10;                   # thickness of left wall
WallSize=50;                    # the height and depth of left wall

def leftWall():
    glPushAttrib(GL_ALL_ATTRIB_BITS);
    glPushMatrix();
    glTranslatef(-Width/2-WallWidth/2,0,0);
    glScalef(WallWidth,WallSize,WallSize);
    twColorName(TW_YELLOW);
    glutSolidCube(1);
    glPopMatrix();
    glPopAttrib();

def platform():
    PlatformHeight=10;
    glPushAttrib(GL_ALL_ATTRIB_BITS);
    glPushMatrix();
    glTranslatef(0,-PlatformHeight/2,0);
    glScalef(Width,PlatformHeight,WallSize);
    twColorName(TW_BROWN);
    glutSolidCube(1);
    glPopMatrix();
    glPopAttrib();

def origin():
    glPushAttrib(GL_ALL_ATTRIB_BITS);
    twColorName(TW_CYAN);
    glutSolidSphere(1,32,32);
    glPopAttrib();

MASS_INIT_X = 40;             # initial horizonal position of the mass

mass = 1200;                    # the mass (in kilograms?)
springK = 3;                    # the spring constant (in what units?)

massV = 0                       # velocity of the mass
massA = 0                       # acceleration of the mass
massX = MASS_INIT_X;

DeltaT = 0.1;                       # time step

MASS_SIZE=20;

def massSpring():
    glPushAttrib(GL_ALL_ATTRIB_BITS);
    twColorName(TW_RED);
    glBegin(GL_LINES);
    glVertex3f(-Width/2,MASS_SIZE/2,0);
    glVertex3f(massX,MASS_SIZE/2,0);
    glEnd();
    twColorName(TW_BLUE);
    glPushMatrix();
    glTranslatef(massX,MASS_SIZE/2,0);
    glutSolidCube(MASS_SIZE);
    glPopMatrix();
    glPopAttrib();
    
def display():
    twDisplayInit();
    twCamera();

    leftWall();
    platform();
    origin();
    massSpring();
    
    glFlush();
    glutSwapBuffers();

Time = 0;

def idle():
    global massA, massV, massX, Time
    # by diff eq
    massA = - springK / mass * massX;
    massV += massA * DeltaT;
    massX += massV * DeltaT;
    # by solved diff eq.  These values are ignored by the simulation, but
    # are computed for comparison during debugging.
    Time += DeltaT;
    omega = math.sqrt(springK/mass);
    massX2 = MASS_INIT_X * math.cos(omega*Time);
    # printf("%f %f %f\n",massX, massX2, massX/massX2);
    glutPostRedisplay();

def main():
    if(len(sys.argv) != 5):
        print "Usage: %s mass spring_constant initx dt\ntry 1 16 30 0.01\n" % (sys.argv[0])
        exit(0);
    else:
        global mass, springK, massX, DeltaT
        mass = float(sys.argv[1])
        springK = float(sys.argv[2])
        massX = MASS_INIT_X = float(sys.argv[3]);
        DeltaT = float(sys.argv[4]);
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-Width/2,Width/2,0,WallSize,-WallSize/2,WallSize/2);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    glutIdleFunc(idle);
    glutMainLoop();
    return 0;


if __name__ == '__main__':
    main()

