'''
dbullistCar.py

Creates a car made of texture mapped quads and black glutSolidCylinders for
wheels.

Written by Dana Bullister

May 10, 2012

Copyright (C) 2012 by Dana Bullister. This program is released under the GPL
License.
'''

import sys
from TW import *

def drawCar(myColor = "red"):
    '''
    Draws a car. Size is 10x12x25, origin is located at the front of the car,
    on the ground, in the center, with car facing towards the camera. Car is
    by default red, although can have the following other colors as input:

     -black
     -blue
     -brown
     -green
     -lightblue
     -magenta
     -silver
     -yelloworange    
    '''

    # size variables
    width = 10
    height = 12
    length = 25
    wheeldiam = 5
    s = 40 # slices and stacks

    def drawWheel(wheeldiam = wheeldiam):
        '''
        Method that draws a wheel (a black glutSolidCylinder)
        '''
        thickness = 0.6*wheeldiam
        glDisable(GL_TEXTURE_2D)
        glColor3f(0,0,0)    
        glutSolidCylinder(0.5*wheeldiam, thickness, s, s)
        glEnable(GL_TEXTURE_2D)

    # texture file
    color = myColor + ".ppm"
    twPPM_Tex2D(twPathname(color,False))
   
    # left side
    glBegin(GL_POLYGON);
    shiftx3 = 0.04
    glNormal(0,0,1)         #.55   
    glTexCoord2f(0 + shiftx3,.8 ); glVertex3f(0.5*width,.2*height,-length);
    glTexCoord2f(.05 + shiftx3,.4 ); glVertex3f(0.5*width,.6*height,-.95*length); 
    glTexCoord2f(.2 + shiftx3,.3 ); glVertex3f(0.5*width,.7*height,-0.8*length); 
    glTexCoord2f(.3 + shiftx3,.05 ); glVertex3f(0.5*width,height,-0.7*length);
    glTexCoord2f(.53 + shiftx3,.065 ); glVertex3f(0.5*width,height,-.45*length);
    glTexCoord2f(.6 + shiftx3,.3 ); glVertex3f(0.5*width,.7*height,-.4*length); 
    glTexCoord2f(.92 + shiftx3,.4 ); glVertex3f(0.5*width,.6*height,0); 
    glTexCoord2f(.92 + shiftx3,.85 ); glVertex3f(0.5*width,.2*height,0);                                
    glEnd()

    # right side
    glBegin(GL_POLYGON);    
    glNormal(0,0,1)
    glTexCoord2f(0 + shiftx3,.8 ); glVertex3f(-0.5*width,.2*height,-length);
    glTexCoord2f(.05 + shiftx3,.4 ); glVertex3f(-0.5*width,.6*height,-.95*length); 
    glTexCoord2f(.2 + shiftx3,.3 ); glVertex3f(-0.5*width,.7*height,-0.8*length); 
    glTexCoord2f(.3 + shiftx3,.05 ); glVertex3f(-0.5*width,height,-0.7*length);
    glTexCoord2f(.53 + shiftx3,.065 ); glVertex3f(-0.5*width,height,-.45*length);
    glTexCoord2f(.6 + shiftx3,.3 ); glVertex3f(-0.5*width,.7*height,-.4*length); 
    glTexCoord2f(.92 + shiftx3,.4 ); glVertex3f(-0.5*width,.6*height,0); 
    glTexCoord2f(.92 + shiftx3,.85 ); glVertex3f(-0.5*width,.2*height,0); 
    glEnd()

    # back
    glBegin(GL_QUADS);
    shiftx3 = -0.13
    glNormal(0,0,1)
    glTexCoord2f(.5,.5); glVertex3f(-0.5*width,.2*height,-length);
    glTexCoord2f(.5,.4); glVertex3f(-0.5*width,.6*height,-.95*length); 
    glTexCoord2f(.6,.4); glVertex3f(0.5*width,.6*height,-.95*length);
    glTexCoord2f(.6,.5);glVertex3f(0.5*width,.2*height,-length);
    glEnd()

    # back
    glBegin(GL_QUADS);
    shiftx3 = -0.13
    x = .5
    X = .6
    y = .55
    Y = .7
    glNormal(0,0,1)
    glTexCoord2f(x,Y); glVertex3f(-0.5*width,.6*height,-.95*length); 
    glTexCoord2f(x,y); glVertex3f(-0.5*width,.7*height,-0.8*length); 
    glTexCoord2f(X,y); glVertex3f(0.5*width,.7*height,-0.8*length); 
    glTexCoord2f(X,Y); glVertex3f(0.5*width,.6*height,-.95*length);
    glEnd()

    # back
    glBegin(GL_QUADS);
    shiftx3 = -0.13
    glNormal(0,0,1)
    glTexCoord2f(x,Y); glVertex3f(-0.5*width,.7*height,-0.8*length);  
    glTexCoord2f(x,y); glVertex3f(-0.5*width,height,-0.7*length);
    glTexCoord2f(X,y); glVertex3f(0.5*width,height,-0.7*length);
    glTexCoord2f(X,Y); glVertex3f(0.5*width,.7*height,-0.8*length);
    glEnd()

    # back
    glBegin(GL_QUADS);
    shiftx3 = -0.13
    glNormal(0,0,1)
    glTexCoord2f(x,Y); glVertex3f(-0.5*width,height,-0.7*length); 
    glTexCoord2f(x,y); glVertex3f(-0.5*width,height,-.45*length);
    glTexCoord2f(X,y); glVertex3f(0.5*width,height,-.45*length);
    glTexCoord2f(X,Y); glVertex3f(0.5*width,height,-0.7*length);
    glEnd()

    # back
    glBegin(GL_QUADS);
    shiftx3 = -0.13
    shifty = .6
    glNormal(0,0,1)
    glTexCoord2f(x+shiftx3,y+shifty); glVertex3f(-0.5*width,height,-.45*length);
    glTexCoord2f(x+shiftx3,Y+shifty); glVertex3f(-0.5*width,.7*height,-.4*length); 
    glTexCoord2f(X+shiftx3,Y+shifty); glVertex3f(0.5*width,.7*height,-.4*length); 
    glTexCoord2f(X+shiftx3,y+shifty); glVertex3f(0.5*width,height,-.45*length);
    glEnd()

    # back
    glBegin(GL_QUADS);
    shiftx3 = 0
    glNormal(0,0,1)
    glTexCoord2f(x,Y); glVertex3f(-0.5*width,.7*height,-.4*length); 
    glTexCoord2f(x,y); glVertex3f(-0.5*width,.6*height,0); 
    glTexCoord2f(X,y); glVertex3f(0.5*width,.6*height,0); 
    glTexCoord2f(X,Y); glVertex3f(0.5*width,.7*height,-.4*length); 
    glEnd()


    glBegin(GL_QUADS);   
    # back
    shiftx3 = -0.13
    glNormal(0,0,1)
    glTexCoord2f(x,Y); glVertex3f(-0.5*width,.6*height,0); 
    glTexCoord2f(x,y); glVertex3f(-0.5*width,.2*height,0);    
    glTexCoord2f(X,y); glVertex3f(0.5*width,.2*height,0);    
    glTexCoord2f(X,Y); glVertex3f(0.5*width,.6*height,0);
    glEnd()
  
    # wheels
    glPushMatrix()
    glColor3f(0,0,0)
    glTranslate(-0.3*wheeldiam+0.5*width,0.5*wheeldiam,-.19*length)
    glRotate(90,0,1,0)
    drawWheel()
    glPopMatrix()

    glPushMatrix()
    glColor3f(0,0,0)
    glTranslate(-0.3*wheeldiam-0.5*width,0.5*wheeldiam,-.19*length)
    glRotate(90,0,1,0)
    drawWheel()
    glPopMatrix()

    glPushMatrix()
    glColor3f(0,0,0)
    glTranslate(-0.3*wheeldiam+0.5*width,0.5*wheeldiam,-.83*length)
    glRotate(90,0,1,0)
    drawWheel()
    glPopMatrix()

    glPushMatrix()
    glColor3f(0,0,0)
    glTranslate(-0.3*wheeldiam-0.5*width,0.5*wheeldiam,-.83*length)
    glRotate(90,0,1,0)
    drawWheel()
    glPopMatrix()

def display():
    ' a callback function to draw scene as necessary '   
    twDisplayInit() 
    twCamera()  
    glEnable(GL_TEXTURE_2D);
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL);
    drawCar()    
    glFlush() 
    glutSwapBuffers() 

def main():
    ' a main function that creates and displays scene, sets up the bounding box'
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(500,500)
    twBoundingBox(-0.5*10-0.3*5,0.5*10+0.3*5,0,12,-25,0)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display) 
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()
