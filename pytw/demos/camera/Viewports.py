''' Demonstrates multiple viewports and the concepts of distortion,
   letterboxing, and clipping.  Displays one TeddyBear in three different
   sizes of viewport:

   2/3 S x 2/3 S
   1/3 S x 2/3 S
   S x 1/3 S
   
Written by Scott D. Anderson
scott.anderson@acm.org
Fall 2003

ported to Python, Fall 2009

'''

import sys
import math                     # for atan and others

from TW import *

## ================================================================

S = 600                         # window size

def cameraSetup():
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(90,1,1,3);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(0,0,2, 0,0,0, 0,1,0);

def display():
    twDisplayInit();
    glLineWidth(2);

    # lower viewport is landscape and spans the whole window, but the
    # lower third (vertically)  600px x 200px
    cameraSetup();
    glViewport(0,0,S,S/3);      # args are llx, lly, width, height
    twColorName(TW_RED);
    glutWireCube(1);
    twTeddyBear();

    # upper left viewport is square, 400px x 400px
    cameraSetup();
    glViewport(0,S/3,S/3*2,S/3*2); # args are llx, lly, width, height
    twColorName(TW_GREEN);
    glutWireCube(1);
    twTeddyBear();

    # upper right viewport is portrait, 200px x 400px
    cameraSetup();
    glViewport(S/3*2,S/3,S/3,S/3*2);
    twColorName(TW_BLUE);
    glutWireCube(1);
    twTeddyBear();

    glFlush();
    glutSwapBuffers();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-1,+1,-1,+1,-1,+1);
    glutInitWindowSize(S,S);    # NOT twInitWindowSize()
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()
