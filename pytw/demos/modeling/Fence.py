''' Puts up a fence around the barn.  Demonstrates display lists and affine
   transforms.

   This program uses twGround and twSky to draw those objects.  The sky
   has the fun property of being opaque only on the inside, so you can
   look through it into the scene, but you see it behind your objects.
   This is accomplished by using one-sided polygons (which is not the TW
   default).

   The coordinate system for this scene has y=0 as the ground, and the
   origin approximately in the center of the front edge, but see the
   bounding box for details.

Written by Caroline Geiersbach and Scott D. Anderson
scott.anderson@acm.org
Summer 2003

Modified in Fall 2006 to put a picket on the ground.  This clarifies the
difference between the display list (which makes drawing a picket easier)
and the use of multiple affine transformations without push/pop of the
modelview matrix.

Adapted to use Python in Fall 2009
'''

import sys

from TW import *

## A picket is, essentially, a barn with two horizontal rails.  The rails
## are 2D quads, and this vertex array gives the vertices for the lower rail. 

def drawRail():
    '''Draws one of the rails through a picket.  This is just a flat quad of
length 5 (parallel to x) and height 2 (parallel to y).'''
    rail = (
      (0,0,0),
      (5,0,0),
      (5,2,0),
      (0,2,0)
      )
    glBegin(GL_QUADS);
    if True:
        glVertex3fv(rail[0]);
        glVertex3fv(rail[1]);
        glVertex3fv(rail[2]);
        glVertex3fv(rail[3]);
    glEnd();

def drawPicket():
    '''Draws one picket.  The picket is 5 wide, 10 high, and 2 deep,
with the reference point at the lower left front of the picket. Rails
stick out 0.5 to the left and are flat planes through the middle of
the picket, with a width of 5 and a height of 2, with the bottom edge
at heights 1 and 4.'''
    maroon = (0.5,0,0)
    black  = (0,0,0)
    orange = (1,0.5,0)

    glPushMatrix();
    glScalef(4,10,2);           # must scale to create 4*10*2 barn
    twSolidBarn(maroon, black, orange);
    glPopMatrix();
    glPushMatrix();
    twColorName(TW_OLIVE);
    glTranslatef(-0.5,1,-1);
    drawRail();
    glTranslatef(0,3,0);
    drawRail();
    glPopMatrix();

# The following is an arbitrary numeric identifier for this display list.
# Here, we use 100 just because it is clearly not a coordinate of a
# vertex, a scale factor, or any other number in the program. */

PICKET = 100

def drawInit():
    '''Create a call list for one picket of the fence.  The first
argument is our numeric constant.  The second requests that the
graphics pipeline just record this display list, but don't draw
anything.'''
    glNewList(PICKET, GL_COMPILE);
    drawPicket();
    glEndList();

def display():
    twDisplayInit();
    twCamera();

    # draw ground and sky, using default colors
    twSky();
    twGround();

    # draw a picket lying on the ground in the middle of the field.  With
    # the exception of using CallList instead of something like
    # drawPicket(), this is the same as any drawing code.
    glPushMatrix();
    glTranslatef(0,0,-40);
    glRotatef(30,0,1,0);
    glRotatef(-90,1,0,0);
    glTranslatef(0,0,2);
    glCallList(PICKET);
    glPopMatrix();

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

    # draw barn
    glPushMatrix();
    glTranslatef(-40,0,-125);
    glRotatef(-90,0,1,0);
    glScalef(40,35,50);
    teal      = (0,0.5,0.5)
    dark_blue = (0,0,0.5)
    cyan      = (0,1,1)
    twSolidBarn(teal,dark_blue,cyan);
    glPopMatrix();

    glFlush();
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    # the real limits are is -40,60 and -125,5
    twBoundingBox(-45,65,0,65,-130,5);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    drawInit();
    glLineWidth(2);
    glutDisplayFunc(display)
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()
