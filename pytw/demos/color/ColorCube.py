### RGB Color Cube with color interpolation

### First written by Scott D. Anderson and Caroline Geiersbach, Summer 2003
### Updated to use Python, Fall 2009

import sys

from TW import *

Vertices = ((-1,-1,-1), (1,-1,-1),
            (1,1,-1), (-1,1,-1),
            (-1,-1,1), (1,-1,1),
            (1,1,1), (-1,1,1))

Colors   = ((0,0,0), (1,0,0),
            (1,1,0), (0,1,0),
            (0,0,1), (1,0,1),
            (1,1,1), (0,1,1));

def face(a,b,c,d):
    '''draw a face defined by four vertex indices'''
    glBegin(GL_QUADS)
    glColor3fv(Colors[a]);    glVertex3fv(Vertices[a]);
    glColor3fv(Colors[b]);    glVertex3fv(Vertices[b]);
    glColor3fv(Colors[c]);    glVertex3fv(Vertices[c]);
    glColor3fv(Colors[d]);    glVertex3fv(Vertices[d]);
    glEnd()

def colorcube():
    '''Draws the entire cube, six faces'''
    face(0,3,2,1)
    face(2,3,7,6)
    face(0,4,7,3)
    face(1,2,6,5)
    face(4,5,6,7)
    face(0,1,5,4)

def edge(A, B):
    '''Sends two vertices down the pipeline.  Presumably they form an edge'''
    glVertex3fv(Vertices[A]);
    glVertex3fv(Vertices[B]);

def wireCube():
    glBegin(GL_LINES)
    ## back
    edge(0,1)
    edge(1,2)
    edge(2,3)
    edge(3,0)
    ## front
    edge(4,5)
    edge(5,6)
    edge(6,7)
    edge(7,4)
    ## sides
    edge(0,4)
    edge(1,5)
    edge(2,6)
    edge(3,7)
    glEnd()

def display():
    twDisplayInit();
    twCamera();

    ## The frame around the cube is thick gray.
    twColorName(TW_GRAY);
    glLineWidth(2);
    wireCube();                 # glutWireCube would also work

    ## Or, just turn on smooth shading with the right button menu
    ## glShadeModel(GL_SMOOTH);    # bilinear color interpolation
    colorcube();                # draw cube

    glFlush();
    glutSwapBuffers();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    # bigger than the color cube, to minimize perspective
    size = 2
    twBoundingBox(-size,size,-size,size,-size,size)
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()
