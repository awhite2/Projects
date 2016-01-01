""" This program displays a sphere with a picture texture-mapped onto it.

Scott D. Anderson
Scott.Anderson@acm.org

Fall 2000 original
Fall 2003 adapted for TW
Fall 2009 ported to Python
"""

import sys
import math                     # for sin and cos

from TW import *

### ================================================================

# red, green, yellow and blue
# s is constant color
# t goes over four colors

red = (255,0,0,255)
green = (0,255,0,255)
yellow = (255,255,0,255)
blue = (0,0,255,255)

BeachBallColors = (red,green,yellow,blue,red,green,yellow,blue)
BeachBallTexture = None

def BeachBallinit(colors=BeachBallColors):
    '''Initialize the texture for a beach ball.  Must be invoked before drawing'''
    global BeachBallTexture
    # make this a 2D texture, since that's what the 
    BeachBallTexture = [ colors[:]
                         for i in range(2) ]
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexImage2D(GL_TEXTURE_2D, 0, 3,
                 len(BeachBallColors), len(BeachBallTexture),
                 0,
                 GL_RGBA, GL_UNSIGNED_BYTE, BeachBallTexture)


def BeachBall(**args):
    '''Draw a striped beach ball.  Same args as twTextureSphere'''
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
    twTextureSphere(**args)

### ================================================================

if __name__ == '__main__':

    GlobeRadius = 5

    Wire = False     ## wire-frame mode (vs filled)
    Texture = True   ## texture mapping (on or off)

    Stacks = 30
    Slices = 30

    def display():
        twDisplayInit();
        twCamera();
        glPushAttrib(GL_ALL_ATTRIB_BITS);
        glPushMatrix()
        glRotate(60,1,0,0)
        glRotate(30,0,0,1)
        BeachBall(radius=GlobeRadius,
                  wireframe=Wire,
                  texture=Texture,
                  stacks=Stacks,
                  slices=Slices)
        glPopMatrix()
        glFlush()
        glutSwapBuffers()
        glPopAttrib()

    def keys(key, x, y):
        global Wire, Texture, Slices, Stacks
        if key == 'w': 
            Wire = not Wire
        elif key == 't': 
            Texture = not Texture
        elif key == '.': 
            Stacks += 1 
            Slices += 1
        elif key == ',': 
            Stacks -= 1 
            Slices -= 1
        print Stacks,Slices
        glutPostRedisplay();

    def main():
        glutInit(sys.argv)
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        twBoundingBox(-GlobeRadius,GlobeRadius,
                       -GlobeRadius,GlobeRadius,
                       -GlobeRadius,GlobeRadius);
        twInitWindowSize(500,500)
        glutCreateWindow(sys.argv[0])
        glutDisplayFunc(display)
        twMainInit()
        twKeyCallback('w',keys,"toggle wire frame");
        twKeyCallback('t',keys,"toggle texture mapping");
        twKeyCallback('.',keys,"increase slices and stacks");
        twKeyCallback(',',keys,"decrease slices and stacks");
        BeachBallinit()
        glutMainLoop()

    main()
