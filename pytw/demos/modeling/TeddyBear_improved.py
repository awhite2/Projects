''' Creates a ``TeddyBear'' object.  Demonstrates affine transforms,
including nested transformations, and the new twColor convenience.

The body is 4 x 6 x 3, the head is a sphere of unit radius, sitting on
top.  The arms are 2.5 units long and are 1 unit from the midline, so the
span is 7 total.  The legs are 3 units long and are rotated twice, so
calculating the endpoint is in principal complex.  However, because the
arms are long enough, we only have to worry about Y, not X.

60 degrees around x, so endpoint drops to z=-1.5-3*sqrt(3)/2

Thus, the whole bear is 7 units wide, 6.5+3*sqrt(3)/2 = 9.1 units high,
and 3 units deep.  Plus, it sticks out of the bounding box a little.

Written by Caroline Geiersbach and Scott D. Anderson
scott.anderson@acm.org
Summer 2003

Adapted to use Python Fall 2009

Fall 2013, Rewritten in a better, more modular style, with better
documentation of arguments and frames for each component.

'''

import sys
import math                     # for sqrt

try:
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
        '''

Wirep = True               # true if you want wire-frame body and head

# Since the scene consists of just the teddy bear, we use its dimensions
# for the bounding box and such

SceneWidth=7
SceneHeight=13.1
SceneDepth=3

def drawBear(wireframe=False,
             bodyColor=(0.8,0.5,0.3),
             headColor=(0.7,0.4,0.2),
             eyeColor=(0,0,0)):
    '''Draw a teddybear around origin in the current frame.

Colors of the body, head and eyes can be set, defaulting to light brown,
dark brown, and black, Respectively

Drawn either solid or wireframe, depending on the 'wireframe' boolean
argument.

The teddybear is drawn with the y axis parallel to the spine, facing down
the positive z axis and the bear's left arm parallel to the positive x
axis.

The teddy bear is 7 units wide, about 9.1 units high and 3 units deep. The
origin is in the center of the belly.

'''

    glPushMatrix();
  
    # by "body" I mean the big fluffy belly
    bodyWidth = 2
    bodyHeight = 3
    headRadius=1
    # draw body
    twColor(bodyColor,0,0);
    glPushMatrix();
    glScalef(bodyWidth,bodyHeight,1.5);
    drawSphere(wireframe)
    glPopMatrix();
  
    # limbs are in the head color
    twColor(headColor,0,0)
    drawBearArm(True,bodyWidth,bodyHeight)
    drawBearArm(False,bodyWidth,bodyHeight)

    drawBearLeg(True,bodyWidth,bodyHeight)
    drawBearLeg(False,bodyWidth,bodyHeight)

    # draw head
    glPushMatrix();             # head coordinate system
    glTranslatef(0,bodyHeight+headRadius,0);
    glScalef(headRadius,headRadius,headRadius)
    drawBearHead(wireframe,bodyColor,headColor,eyeColor)
    glPopMatrix()               # end of head coordinate system

    glPopMatrix();              # end of bear coordinate system

def drawBearArm(right,bodyWidth,bodyHeight):
    '''Draws a tapering tube at the shoulder in the current color

The tube starts at the "shoulder" (depending on "right") and is either
aligned with the positive y-axis (right=true) or the negative y-axis
(right=false). The shoulder position is calculated based on the bodyWidth
and bodyHeight and assumes that the origin is at the center of the
body. The length of the arm is 85% of the bodyHeight.'''
    # draw right arm (the arm on our right = the bear's left)
    direction = +1 if right else -1
    glPushMatrix();
    glTranslatef(direction*bodyWidth*0.5,bodyHeight*0.67,0)
    glRotatef(direction*90,0,1,0);
    # arm girth is fixed, not dependent on body size, but
    # length depends on body height
    twTube(0.5,0.4,0.85*bodyHeight,20,1); 
    glPopMatrix();

def drawBearLeg(right,bodyWidth,bodyHeight):
    '''Draws a tapering tube at the hip in the current color

The tube starts at the "hip" either right or left, depending on "right"
the hip position is calculated based on bodyWidth and bodyHeight, and
assumes that the origin is at the center of the body. The length of the leg
is the same as the bodyHeight.
'''
    # draw right leg (the leg on our right = the bear's left)
    direction = +1 if right else -1
    glPushMatrix();
    glTranslatef(direction*bodyWidth*0.5, -0.5*bodyHeight, 0);
    glRotatef(direction*30,0,1,0); # rotate around y
    glRotatef(60,1,0,0);           # and around x
    # leg girth is fixed, not dependent on body size, but
    # length depends on body height
    twTube(0.7,0.6,bodyHeight,20,1);
    glPopMatrix();


def drawBearHead(wireframe,bodyColor,headColor,eyeColor):
    '''Draws a unit-sized bear head around the origin

The nose below the equator, at (0,-0.4,0.9) and the eyes above the equator
at (+/-0.4,0,0.9), and the ears near the top of the head at (+/-0.7,0.7,0.2)
'''
    twColor(headColor,0,0)
    drawSphere(wireframe)
    twColor(bodyColor,0,0)
    drawBearEar(True)
    drawBearEar(False)
    
    # didn't do eyes as separate functions, since they're so simple
    twColor(eyeColor,0,0)
    glPushMatrix()
    glTranslatef(-0.4,0,0.9);
    glutSolidSphere(0.12,10,10);  # eye on our left
    glTranslatef(0.8,0,0);
    glutSolidSphere(0.12,10,10);  # eye on our right
    glPopMatrix();

    glPushMatrix();
    glTranslatef(0,-0.4,0.9);
    glutSolidSphere(0.2,10,10);   # nose is slightly bigger
    glPopMatrix();


def drawBearEar(right):
    '''Draw a Bear's ear.  Position is hard-coded at (+/-0.7,0.7,0.2)'''
    direction = +1 if right else -1
    glPushMatrix();
    glTranslatef(direction*0.7,0.7,0.2);
    glScalef(1,1,0.5);
    glutSolidSphere(0.4,20,20);  # right ear
    glPopMatrix();


def drawSphere(wireframe):
    '''draws a unit sphere around the origin, either wireframe or solid.'''
    if wireframe:
        glutWireSphere(1,20,20);
    else:
        glutSolidSphere(1,20,20);


def display():
    twDisplayInit();
    twCamera();

    glPushMatrix()
    glTranslate(SceneWidth*0.5,SceneHeight*0.5,SceneDepth*0.5)
    drawBear(Wirep)
    glPopMatrix()

    glFlush();
    glutSwapBuffers();

def wireToggle(key, x, y):
    global Wirep
    Wirep = not Wirep;
    glutPostRedisplay();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(0,SceneWidth,
                  0,SceneHeight,
                  0,SceneDepth)
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    twKeyCallback('w',wireToggle,"toggle wire-frame bear body and head");
    glutMainLoop()

if __name__ == '__main__':
    main()
