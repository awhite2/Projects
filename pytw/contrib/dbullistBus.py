'''
dbullistBus.py

Draws a bus made of texture mapped quads and glutSolidCylinders. Size is
10x12x35,origin is at the front of the bus, in the center, on the ground,
with the bus facing the camera.

Written by Dana Bullister

May 10, 2012

Copyright (C) 2012 by Dana Bullister. This program is released under the GPL
License.
'''

import sys
from TW import *

def drawBus():
    '''
    Creates a scaled 10x12x35 school bus object consisting of texture-mapped
    quads and cylinders. Relative origin is on the ground at the center
    front of the bus. Bus faces toward camera. 
    '''

    #size variables
    width = 10
    height = 12
    length = 35
    wheeldiam = 3.9    
    xTaper = 3.2 # how much width of roof differs from width of bus
    yTaper = 1.8 # how much height of side of bus differs from height of body of bus
    s = 40 # slices and stacks
    
    def drawWheel(wheeldiam = 3.9):
        '''
        Creates the bus wheel of specified diameter. Just a black
        glutSolidCylinder. 
        '''
        thickness = 0.6*wheeldiam
        glDisable(GL_TEXTURE_2D)
        glColor3f(0,0,0)    
        glutSolidCylinder(0.5*wheeldiam, thickness, s, s)
        glEnable(GL_TEXTURE_2D)

    glPushMatrix()
    glTranslate(0,-2,0)    
    twPPM_Tex2D(twPathname("busLeftSide.ppm",False)) 
    glBegin(GL_QUADS);
   
    # left side
    shiftx3 = -0.13
    glNormal(0,0,1)
    glTexCoord2f(.5 + shiftx3 + .01,0); glVertex3f(0.5*width,height-yTaper,0);
    glTexCoord2f(1.5 + shiftx3,0); glVertex3f(0.5*width,height-yTaper,-length); 
    glTexCoord2f(1.5 + shiftx3,1); glVertex3f(0.5*width,wheeldiam,-length); 
    glTexCoord2f(0.5 + shiftx3,1); glVertex3f(0.5*width,wheeldiam,0);
    glEnd()

    # right side
    glBegin(GL_QUADS);     
    glNormal(-1,0,0)
    glTexCoord2f(1.5 + shiftx3 + 0.01,0); glVertex3f(-0.5*width,height-yTaper,-length);
    glTexCoord2f(0.5 + shiftx3,0); glVertex3f(-0.5*width,height-yTaper,0); 
    glTexCoord2f(0.5 + shiftx3,1); glVertex3f(-0.5*width,wheeldiam,0); 
    glTexCoord2f(1.5 + shiftx3,1); glVertex3f(-0.5*width,wheeldiam,-length);
    glEnd()
    twPPM_Tex2D(twPathname("busFront.ppm",False))

    # front
    glBegin(GL_QUADS);    
    shiftx = -.12
    shifty = .25
    glNormal(0,0,1)
    glTexCoord2f(0 + shiftx,0 + shifty); glVertex3f(-0.5*width,height-yTaper,0);
    glTexCoord2f(1 + shiftx,0 + shifty); glVertex3f(0.5*width,height-yTaper,0); 
    glTexCoord2f(1 + shiftx,.95); glVertex3f(0.5*width,wheeldiam,0); 
    glTexCoord2f(0 + shiftx,.95); glVertex3f(-0.5*width,wheeldiam,0);    

    # front top
    glTexCoord2f(0 + shiftx + xTaper/width,.03); glVertex3f(-0.5*width+xTaper,height,0);
    glTexCoord2f(1 + shiftx - xTaper/width, .03); glVertex3f(0.5*width-xTaper,height,0); 
    glTexCoord2f(1 + shiftx,.23); glVertex3f(0.5*width,height-yTaper,0); 
    glTexCoord2f(0 + shiftx,.23); glVertex3f(-0.5*width,height-yTaper,0);
    glEnd()

    # back
    twPPM_Tex2D(twPathname("busBack.ppm",False)) 
    glBegin(GL_QUADS);
    shiftx2 = -.16    
    glNormal(0,0,-1)
    glTexCoord2f(0 + shiftx2,0.15); glVertex3f(0.5*width,height-yTaper,-length);
    glTexCoord2f(1 + shiftx2,0.15); glVertex3f(-0.5*width,height-yTaper,-length); 
    glTexCoord2f(1 + shiftx2,1); glVertex3f(-0.5*width,wheeldiam,-length); 
    glTexCoord2f(0 + shiftx2,1); glVertex3f(0.5*width,wheeldiam,-length);

    # back top
    glTexCoord2f(0 + shiftx2 + xTaper/width,0); glVertex3f(0.5*width-xTaper,height,-length);
    glTexCoord2f(1 + shiftx2 - xTaper/width,0); glVertex3f(-0.5*width+xTaper,height,-length); 
    glTexCoord2f(1 + shiftx2,.15); glVertex3f(-0.5*width,height-yTaper,-length); 
    glTexCoord2f(0 + shiftx2,.15); glVertex3f(0.5*width,height-yTaper,-length);
    glEnd()

    # top
    twPPM_Tex2D(twPathname("busRoof.ppm",False)) 
    glBegin(GL_QUADS);    
    glNormal(0,1,0)
    glTexCoord2f(0,0); glVertex3f(0.5*width-xTaper,height,0);
    glTexCoord2f(1,0); glVertex3f(-0.5*width+xTaper,height,0); 
    glTexCoord2f(1,1); glVertex3f(-0.5*width+xTaper,height,-length); 
    glTexCoord2f(0,1); glVertex3f(0.5*width-xTaper,height,-length);

    # top left
    glTexCoord2f(0,0); glVertex3f(0.5*width-xTaper,height,0);
    glTexCoord2f(1,0); glVertex3f(0.5*width-xTaper,height,-length); 
    glTexCoord2f(1,1); glVertex3f(0.5*width,height-yTaper,-length); 
    glTexCoord2f(0,1); glVertex3f(0.5*width,height-yTaper,0);
    
    # top right
    glTexCoord2f(0,0); glVertex3f(-0.5*width+xTaper,height,-length);
    glTexCoord2f(1,0); glVertex3f(-0.5*width+xTaper,height,0); 
    glTexCoord2f(1,1); glVertex3f(-0.5*width,height-yTaper,0); 
    glTexCoord2f(0,1); glVertex3f(-0.5*width,height-yTaper,-length);
    glEnd()

    # wheels
    glPushMatrix()
    glColor3f(0,0,0)
    glTranslate(0.8*wheeldiam,wheeldiam,-.19*length)
    glRotate(90,0,1,0)
    drawWheel()
    glPopMatrix()

    glPushMatrix()
    glColor3f(0,0,0)
    glTranslate(-1.5*wheeldiam,wheeldiam,-.19*length)
    glRotate(90,0,1,0)
    drawWheel()
    glPopMatrix()

    glPushMatrix()
    glColor3f(0,0,0)
    glTranslate(0.8*wheeldiam,wheeldiam,-.66*length)
    glRotate(90,0,1,0)
    drawWheel()
    glPopMatrix()

    glPushMatrix()
    glColor3f(0,0,0)
    glTranslate(-1.5*wheeldiam,wheeldiam,-.66*length)
    glRotate(90,0,1,0)
    drawWheel()
    glPopMatrix()

    glPopMatrix()

def display():
    ' a callback function to draw scene as necessary '   
    twDisplayInit() 
    twCamera()     
    glEnable(GL_TEXTURE_2D);    
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL);
    drawBus()    
    glFlush() 
    glutSwapBuffers() 

def main():
    ' a main function that creates and displays scene, sets up the bounding box'
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(500,500)
    twBoundingBox(-0.5*10,0.5*10,0,12-2,-35,0)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display) 
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()
