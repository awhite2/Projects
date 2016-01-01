''' Displays a frustum.

Written by Caroline Geiersbach and Scott D. Anderson
scott.anderson@acm.org
Summer 2003

Ported to Python, Fall 2009, Scott
'''

import sys

from TW import *

## This frustum has an aspect ratio of 2.

Frustum = ((-2,-1,-1), (2,-1,-1), (2,1,-1),(-2,1,-1), # top of frustum at z=-1
           (-20,-10,-10), (20,-10,-10),(20,10,-10), (-20,10,-10))

def drawFrustum():
    glLineWidth(2.5);
    twColorName(TW_ORANGE);     # top (near)
    glBegin(GL_LINE_LOOP);
    glVertex3fv(Frustum[0]);
    glVertex3fv(Frustum[1]);
    glVertex3fv(Frustum[2]);
    glVertex3fv(Frustum[3]);
    glEnd();

    twColorName(TW_BROWN);      # bottom (far)
    glBegin(GL_LINE_LOOP);
    glVertex3fv(Frustum[4]);
    glVertex3fv(Frustum[5]);
    glVertex3fv(Frustum[6]);
    glVertex3fv(Frustum[7]);
    glEnd();

    twColorName(TW_YELLOW);     # sides in
    glBegin(GL_LINES);
    glVertex3fv(Frustum[0]);
    glVertex3fv(Frustum[4]);

    glVertex3fv(Frustum[1]);
    glVertex3fv(Frustum[5]);

    glVertex3fv(Frustum[2]);
    glVertex3fv(Frustum[6]);

    glVertex3fv(Frustum[3]);
    glVertex3fv(Frustum[7]);
    glEnd();

def display():
    twDisplayInit();
    twCamera();
  
    drawFrustum();
    twColorName(TW_PURPLE);     # origin (VRP) in purple
    glutSolidSphere(0.2,20,20);

    glFlush();
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-20,20,-20,20,-20,0)
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    # nice fat lines.  In this program, we only need to say this once
    glLineWidth(3)               
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()
