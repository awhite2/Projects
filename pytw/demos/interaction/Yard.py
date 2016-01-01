""" Just draws the scene.

Written by Caroline Geiersbach and Scott D. Anderson
scott.anderson@acm.org
Summer 2003
Ported to Python 2009
"""

import sys
import math # for tan, atan

try:
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
        '''

### ================================================================

BBXmin = -45;         # bounding box X min
BBXmax = 65;          # X max
BBYmin = 0;           # Y min
BBYmax = 65;          # Y max
BBZmin = -130;        # Z min
BBZmax = 5;           # Z min

def drawRail():
    rail = (
        (0,0,0),
        (5,0,0),
        (5,2,0),
        (0,2,0)
        )
    glBegin(GL_POLYGON);
    glVertex3fv(rail[0]);
    glVertex3fv(rail[1]);
    glVertex3fv(rail[2]);
    glVertex3fv(rail[3]);
    glEnd();

# Arbitrary numeric identifier for this display list.
PICKET = 100

""" Initializes a display list to draw one picket.  The picket is 5
   wide, 10 high, and 2 deep, with the reference point at the lower
   left front of the picket. Rails stick out 0.5 to the left and are
   flat planes through the middle of the picket, with a width of 5 and
   a height of 2, with the bottom edge at heights 1 and 4. """

def drawInit():
    maroon = (0.5,0,0)
    black  = (0,0,0)
    orange = (1,0.5,0)
  
    ## Create a call list for one picket of the fence 
    glNewList(PICKET, GL_COMPILE);
    glPushMatrix();
    glScalef(4,10,2); # must scale to create 4*10*2 barn
    twSolidBarn(maroon, black, orange);
    glPopMatrix();
    glPushMatrix();
    twColorName(TW_OLIVE);
    glTranslatef(-0.5,1,-1);
    drawRail();
    glTranslatef(0,3,0);
    drawRail();
    glPopMatrix();
    glEndList();

def fences():
    # draw front fence
    glPushMatrix();
    glTranslatef(-40,0,0);
    for i in range(20):
        glCallList(PICKET);
        glTranslatef(5,0,0);
    glPopMatrix();
  
    # draw right side fence
    glPushMatrix();
    glTranslatef(60,0,0);
    glRotatef(90,0,1,0); 
    for i in range(25):
        glCallList(PICKET);
        glTranslatef(5,0,0);
    glPopMatrix();
  
    # draw left side fence
    glPushMatrix();
    glTranslatef(-40,0,0);
    glRotatef(90,0,1,0);
    for i in range(17):
        glCallList(PICKET);
        glTranslatef(5,0,0);
    glPopMatrix();

def barn1():
    glPushMatrix();
    glTranslatef(-40,0,-125);
    glRotatef(-90,0,1,0);
    glScalef(40,35,50);
    teal = (0,0.5,0.5)
    dark_blue = (0,0,0.5)
    cyan = (0,1,1)
    twSolidBarn(teal,dark_blue,cyan);
    glPopMatrix();

def draw():

    glDisable(GL_LIGHTING)
    # draw ground
    twColorName(TW_GREEN);
    twGround();

    # draw sky
    lightSkyBlue = ( 135.0/255.0, 206.0/255.0, 250.0/255.0 )
    twColor(lightSkyBlue,0,0);
    twSky();

    # Lighting
    glEnable(GL_LIGHTING);
    twAmbient(0.1);
    twGrayLight(GL_LIGHT0,(2,3,5,0),0.1,0.5,0.5); # bright light in the sky

    fences();
    barn1();                    # the one in the back corner

### Should add a main() for testing purposes
