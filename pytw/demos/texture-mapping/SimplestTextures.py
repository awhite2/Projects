''' Simplest demo of texture mapping using static arrays instead files.
There are two arrays, one black and white and one color.  Toggle between
them with the 'u' callback.

Scott D. Anderson
Fall 2004
Ported to Python Fall 2009
'''

import sys
import math                            # for sin and cos

from TW import *

## ================================================================

BW = True                       # which flag to show

def toggleFlag(key, x, y):
    global BW
    BW =  not BW;
    glutPostRedisplay();

ShowTeapot = False

def toggleObject(key, x, y):
    global ShowTeapot
    ShowTeapot =  not ShowTeapot;
    glutPostRedisplay();

### ================================================================
###   Texture arrays

## The dimensions of the black and white texture array.  Note that they
## are both powers of 2.

BWwidth = 4
BWheight = 4

## The array elements are unsigned bytes:  grayscale values from 0 to 255.

bwTexture = ((  0,   0,   0, 255),
             (  0,   0, 255,   0),
             (255,   0, 255, 255),
             (  0, 255, 255, 255))

## The dimensions of the color texture array.  

ColorWidth = 2
ColorHeight = 2

## We add a extra value to handle the issue of rows being aligned on a
## four-byte boundary.  By using RGBA instead of RGB, the rows necessarily
## are aligned on a four-byte boundary, since each element is 4 bytes.

colorTexture = (
    ( (0,0,0,255), (255,0,0,255) ),
    ( (0,255,0,255), (0,0,255,255) )
    )
    
### ================================================================

def display():
    twDisplayInit();
    twCamera();

    glPushAttrib(GL_ALL_ATTRIB_BITS);

    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);

    if BW:
        glTexImage2D(GL_TEXTURE_2D, 0, 3, BWwidth, BWheight, 0,
                     GL_LUMINANCE, GL_UNSIGNED_BYTE, bwTexture);
    else:
        glTexImage2D(GL_TEXTURE_2D, 0, 3, ColorWidth, ColorHeight, 0,
                     GL_RGBA, GL_UNSIGNED_BYTE, colorTexture);

    glEnable(GL_TEXTURE_2D);

    if ShowTeapot:
        glPushMatrix()
        glTranslate(5,2,0)
        glScale(2,2,2)
        glutSolidTeapot(1)
        glPopMatrix()
    else:
        glBegin(GL_QUADS);
        glTexCoord2f(0,1); glVertex3f( 0,0,0); # green
        glTexCoord2f(1,1); glVertex3f(10,0,0); # blue
        glTexCoord2f(1,0); glVertex3f(10,5,0); # red 
        glTexCoord2f(0,0); glVertex3f( 0,5,0); # black
        glEnd();

    glPopAttrib();
    glFlush();
    glutSwapBuffers();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(0,10,0,5,-1,1);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    twKeyCallback('u',toggleFlag,"toggle which flag to show");
    twKeyCallback('t',toggleObject,"toggle whether to show Quad or Teapot");
    glutMainLoop()

if __name__ == '__main__':
    main()
