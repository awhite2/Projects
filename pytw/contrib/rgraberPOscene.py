###File: rgraberPOscene.py
###Author: Rebecca Graber
###Assignment 4
###Last modified: 10/30/09
##Note: at the moment, the music box is slightly smaller than the user-specified height.Hopefully this will be corrected soon. Also, this was mostly written on a Mac.


''' An OpenGL model of the music box from Phantom of the Opera, as well as some additional
    features related objects (mask and rose).
  
    Copyright (C) 2009 Rebecca Grber

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.'''

import sys

try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print '''
ERROR: PyOpenGL not installed properly.  
        '''

try:
  from TW import *
except:
  print '''
ERROR: Could not import TW.

        '''

##Set-up color constants
darkBrown= (.5,.25,0)
redderBrown= (.75, .25, 0)
duskyBlue= (.25, .25, .5)
lighterBlue= (.5,.5,1)
cyan = (0,1,1)
darkBlue= (.12,.12,.25)
magenta= (.95, .19, .6)
yellow = (1,1,0)
darkPurple = (.6,0,.8)
lightBeige = (1,.9,.62)
grassGreen = (.4,.8,0)
black = (0,0,0)
gold = (245.0/255,184.0/255,0)
white = (1,1,1)
roseRed = (153/255.0,0,50/255.0)
darkGreen = (0,51/255.0,0)

monkeyColor = darkBrown
roseColor = roseRed
stemColor = darkGreen

mainObject = "scene"

def scene():
  '''draws a snapshot from Phantom of the Opera, with a mask, rose, and monkey music box'''
  drawFloor()
  glPushMatrix()
  glTranslatef(0,0,-7)
  rgraberMonkeyMusicBox(20, monkeyColor)  ##music box
  glPopMatrix()
  glPushMatrix()
  glTranslatef(2,0,0)
  glRotatef(75,1,0,0)
  glRotatef(30,0,0,1)
  drawRose(5)                             ##rose
  glPopMatrix()
  glPushMatrix()
  glTranslatef(3,.75,5)
  glScalef(.5,.5,.5)
  glRotatef(-55,1,0,0)  
  rgraberMask()                             ##mask
  glPopMatrix()
  
  
  

def drawFloor():
  '''draws the black floor'''
  glColor3fv(black)
  twGround();

def showOrigin():
    '''show the origin. From Teapot.py'''
    glPointSize(5)
    twColorName(TW_MAGENTA)
    glBegin(GL_POINTS)
    glVertex3f(0,0,0)
    glEnd()

##points that make up a basic petal ring
petalVArray = [(0,0,0),(1.5,3,3),(-1.5,3,3),(-2.5,3,0),(-1.5,3,-3),
               (1.5,3,-3),(2.5,3,0),(1.5,3,3)]
eyeVArray= [(1,-2,0),(2,-1,0),(2,1,0),(1,2,0),(-1,2,0),(-2,1,0),(-2,-1,0),(-1,-2,0)]

def drawPetalRing(scaleFactor):
  '''draws a single ring of petals with the scaled by scaleFactor'''
  ring = map(lambda v: twVectorScale(twVectorNormalize(v),scaleFactor), petalVArray)
  glBegin(GL_TRIANGLE_FAN)
  glColor3fv(roseColor)
  glVertex3fv(ring[0])
  glVertex3fv(ring[1])
  glVertex3fv(ring[2])
  glVertex3fv(ring[3])
  glVertex3fv(ring[4])
  glVertex3fv(ring[5])
  glVertex3fv(ring[6])
  glVertex(ring[7])
  glEnd()

def drawRoseTop():
  '''draws concenctric rings of petals'''
  drawPetalRing(2)
  glPushMatrix()
  glScalef(1,1.5,1)
  drawPetalRing(1.5)
  glScalef(1,1.5,1)
  drawPetalRing(1.1)
  glPopMatrix()

def drawStem(length):
  '''draws the rose stem'''
  glColor3fv(stemColor)
  glPushMatrix()
  glRotatef(90,1,0,0)
  twTube(.5,.5,length,20,20)
  glPopMatrix()

def drawRose(stemlength):
  '''draws a very basic rose with the given stemlength'''
  glTranslatef(0,stemlength,0)
  drawStem(stemlength)
  drawRoseTop()

def drawOneEye():
  '''draws a single eyehole of the mask'''
  glColor3fv((1,1,1))
  glPushMatrix()
  glScalef(1.25,1,.1)
  glutSolidTorus(.7,1.7,30,30)
  glPopMatrix()

def rgraberMask():
  '''draws a simple white Halloween-type mask. Origin is at the center of the mask, between
  the eyes'''
  glPushMatrix()
  glTranslatef(-2.15,0,0)
  drawOneEye()  #draw one eye
  glPopMatrix()
  glPushMatrix()
  glTranslatef(2.15,0,0)
  drawOneEye()  #draw the other
  glPopMatrix()
  glBegin(GL_TRIANGLES)    #connect the two eyes with a triangle
  glVertex3fv((2.15,2.4,0))
  glVertex3fv((-2.15,2.4,0))
  glVertex3fv((0,.2,0))
  glEnd()

def rgraberMonkeyMusicBox(height,monkeycolor):
  '''draws the Music Box from the Phantom of the Opera.
  Everything is scaled from the (user-specified) height of the entire object.
  The origin is at the bottom, in the center of the box.
  The bounding box should be set ((-1.5/5.5)*height,(1.5/5.5)*height,0,height,
                                    -height/5.5, height/5.5 +4)
  The monkey is based off a specific design very dependent on proportions, so it is only
  customizable up to the height and color of the monkey.
                                  '''
  benchHeight = height/5.5
  glPushMatrix()
  drawBench(benchHeight)
  glTranslatef(0,benchHeight,0)
  drawMonkey(height*3/5.5,monkeycolor)
  glPopMatrix()

def drawBench(height):
  '''draws the bench on which the monkey sits with a user-specified height.
  The origin is at the bottom, in the center.
  The dimensions of the bench are 3height x 1height x 2height''' 
  glPushMatrix()
  glTranslatef(0,height/2.0,0) ##draws bench completely above the origin
  glPushMatrix()
  glScalef(3,1,2)
  glColor3fv((0,0,0))   ##bench is black
  glutSolidCube(height) ##draw the main body of the bench
  glPopMatrix()
  glColor3fv((1,0,0))   ##cushion is red
  glPushMatrix()
  glTranslatef(0,height/2.0,0)
  glScalef(1.5*height,height/4.0,height)  ##draw the cushion
  glutSolidSphere(1,20,20)
  glPopMatrix()
  glPopMatrix()

def drawMonkey(totalheight,monkeycolor):
  '''draws the monkey figurine, with cymbals. The origin is at the base of the monkey's main
  body, so the legs are below y=0. The body is entirely in proportion, so only the color
  and overall size of the monkey (based on the main body size) can be specified'''
  height = totalheight/2.0
  glColor3fv(monkeycolor)
  glPushMatrix()
  width = height/2.0
  depth = height/2.0
  glScalef(width,height,depth)  
  glTranslatef(0,1,0)
  glutSolidSphere(1,20,20)    ##main body, twice as tall as it is long and wide
  glPopMatrix()
  glPushMatrix()
  glTranslatef(-width/2.0 ,height/4.0,0)
  leg(height,depth,monkeycolor)                       ##draw the left leg
  glPopMatrix()
  glPushMatrix()
  glTranslatef(width/2.0 ,height/4.0,0)
  glScalef(-1,1,1)            ##draw the right leg, a mirror image of the left
  leg(height,depth,monkeycolor)
  glPopMatrix()
  arm(height,width,1,monkeycolor)         ##draw left and right arms, also mirror images
  arm(height,width, -1, monkeycolor)
  glPushMatrix()
  glTranslatef(0,9*height/5.0,0)
  head(height/3.0, monkeycolor)            ##draws the entire head
  glPopMatrix()
  
def head(radius,color):
  '''draws the head of the monkey with a specified radius. The head includes the 3 cones
  and the monkey's face (which protrudes). The origin is at the bottom of the main sphere. Color
  should be the same as the main monkey body.'''
  glPushMatrix()
  glTranslatef(0,radius,0)
  glutSolidSphere(radius,20,20)  ##draw main sphere
  glPushMatrix()
  glTranslatef(0,(7/8.0)*radius,0)
  glRotatef(-90,1,0,0)
  glutSolidCone((1/2.0)*radius,radius,20,20)  ##draw top cone
  glPopMatrix()
  faceCone(1,radius)             ##left side cone
  faceCone(-1,radius)            ##right side cone
  mouth(radius,color)                    ##protruding mouth
  eye(radius,1,color)                  ##left eye
  eye(radius,-1,color)                 ##right eye
  glPopMatrix()                  ##go home
  
  
def faceCone(neg,s):
  '''draws the type of horizontal cone that sticks out to the side of the monkey's face
  to the left or right (neg is 1 or -1, the scaling constant that allows us to reflect
  the cone across the yz plane. s is based on the size of the head.'''
  glPushMatrix()
  glTranslatef(0,-s/4.0,0)
  glScalef(neg,1,1)
  glRotatef(90,0,1,0)    ##cone is originally drawn up the z-axis, change to x
  glutSolidCone((3/4.0)*s,2*s,20,20)
  glPopMatrix()

def mouth(size,color):
  '''draws the mouth that protrudes from the monkey's head, based on the head size'''
  glColor3fv(lightBeige)
  glPushMatrix()
  glTranslatef(0,-size/2.0,size/2)
  glScalef(2*size/3.0,size/2.0,3*size/4.0)
  glutSolidSphere(1,20,20) ##draw the protruding part
  glColor3fv(black)
  glRotatef(90,1,0,0)
  glScalef(1.05,1.2,1)
  twDisk(1,20)              ##draw the actual mouth 
  glPopMatrix()
  glColor3fv(color)         ##reset the color
  
def eye(size,neg,color):
  '''draws a single white eye with a black pupil in the area specified by size and neg
  neg = -1 for the right eye, 1 for the left. "color" should be the same as the rest of
  the monkey. The origin is the center of the face.'''
  glPushMatrix()
  glTranslatef(neg*size/2.0,size/3.0,3*size/4.0)
  glColor3fv(white)
  glScalef(size/6.0,size/6.0,size/6.0)
  glutSolidSphere(1,20,20)   ##draw the main part of the eye
  glColor3fv(black)
  glTranslatef(0,0,size/5.0)
  glScalef(.8,.8,1)
  glutSolidSphere(1,20,20)   ##draw the pupil in the center
  glPopMatrix()
  glColor3fv(color)          ##reset the color
   
  


def arm(height,width,neg,color):
  '''draws an arm with a cymbal attached at the appropriate angle to the body, based on the
  size of the main body. neg = -1 for the right arm, 1 for the left.
  color is the same as the rest of the monkey. Origin is at the shoulder.'''
  glPushMatrix()
  glScalef(neg,1,1)
  glTranslatef(-(width),1.5*height,0)
  glRotatef(-5,0,0,1)
  drawLimb(height/8.0,height/2.0,height/2.0,True,color)
  glPopMatrix()

def leg(height,depth,color):
  '''draws a leg, origin at the hip joint. color should be the same as that of the monkey. Depth
  and height ensure proper proportion'''
  drawLimb(height/4.0,height,depth,False,color)
  

  

def drawLimb(r,length1,length2,arm,color):
  '''draws a limb (two tubes and a sphere) with a given radius, length of the two segments
  (below and above the joint), and a boolean stating whether or not the limb is the arm. If it
  is an arm, attaches a cymbal. color should be the same as that of the monkey. Origin at the
  top of the limb'''
  glPushMatrix()
  glPushMatrix()
  glRotatef(-15,0,1,0)       
  twTube(r,r,length1,20,20)                     ##draw the upper limb 
  glTranslatef(-.05,0,length1-(length1*3.0/20)) ##cylindars should overlap to form a joint
  glRotatef(90,1,.25,0)
  twTube(3*r/4.0,3*r/4.0,length2,20,20)         ##draw the lower limb 
  glTranslatef(-r/2.0,r,length2)
  glRotatef(-90,1,.25,0)
  glPushMatrix()
  glScalef(1,1,2)
  glutSolidSphere(r,20,20)                      ##draw the extremity (hand or foot)
  glPopMatrix()
  if arm: #add the cymbal
    glPushMatrix()
    glTranslatef(r,0,1.5*r)
    glRotatef(90,0,1,0)
    glColor3fv(gold)
    twTube(r,3*r,r/4.0,20,20)
    glPopMatrix()
  glPopMatrix()
  glPopMatrix()
  glColor3fv(color)                              ##reset color                  
  
  
def changeScene(key,x,y):
  '''changes the scene to the entire picture or just the music box, based on keyboard input'''
  global mainObject
  if key == 'S':
    mainObject = "scene"
  elif key == 'M':
    mainObject = "music box"
  glutPostRedisplay()



##TW Code

def display():
    twDisplayInit(0.7, 0.7, 0.7)

    twCamera()
    showOrigin()
    if mainObject == "scene":
      scene()
    elif mainObject == "music box":
      rgraberMonkeyMusicBox(20, monkeyColor)

    glFlush()
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(500,500)
    twBoundingBox((-1.5/5.5)*20,(1.5/5.5)*20,0,20,-20/5.5,20/5.5 + 5)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    twKeyCallback('S',changeScene, "entire scene")
    twKeyCallback('M',changeScene, "music box")
    glutMainLoop()

if __name__ == '__main__':
  main()

