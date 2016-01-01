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

GlobeRadius = 5

Wire = False     ## wire-frame mode (vs filled)
Texture = True ## texture mapping (on or off)

Stacks = 30
Slices = 30

# red, green, yellow and blue
# s is constant color
# t goes over four colors

def BeachBall(colors=((255,0,0,255),
                      (0,255,0,255),
                      (255,255,0,255),
                      (0,0,255,255),
                      (255,0,0,255),
                      (0,255,0,255),
                      (255,255,0,255),
                      (0,0,255,255)),
              radius=1,
              slices=30,
              stacks=30,
              texture,
              textureid,
              wire)
    '''Draw a texture-mapped sphere'''
    glBindTexture(GL_TEXTURE_2D,textureid)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
    if wire:
      twWireGlobe(radius,stacks,slices)
    else:
      if texture:
        glEnable(GL_TEXTURE_2D)
      else:
        glDisable(GL_TEXTURE_2D)
        twSolidGlobe(radius,stacks,slices)

TextureNumber = None            # set in main

def display():
    twDisplayInit();
    twCamera();
    glPushAttrib(GL_ALL_ATTRIB_BITS);

    
    glBindTexture(GL_TEXTURE_2D,TextureNumber)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
    if Wire:
        twWireGlobe(GlobeRadius,Stacks,Slices);
    else:
        if Texture:
            glEnable(GL_TEXTURE_2D);
        else:
            glDisable(GL_TEXTURE_2D);
        twSolidGlobe(GlobeRadius,Stacks,Slices);

    glFlush();
    glutSwapBuffers();
    glPopAttrib();

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
        Stacks -=1 
        Slices -= 1
    glutPostRedisplay();

def main():
    global TextureNumber
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

    TextureNumber = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D,TextureNumber)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
    glTexImage2D(GL_TEXTURE_2D, 0, 3,
                 len(BeachBallColors), len(BeachBallTexture),
                 0,
                 GL_RGBA, GL_UNSIGNED_BYTE, BeachBallTexture);

    glutMainLoop()

if __name__ == '__main__':
    main()
