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

def drawBear():
    '''Draw a teddybear, either solid or wireframe, depending on the
    global variable 'Wirep' See twTeddyBear for an alternative.'''
    bodyColor = (0.8,0.5,0.3)
    headColor = (0.7,0.4,0.2)

    glPushMatrix();
  
    # draw body
    twColor(bodyColor,0,0);
    glPushMatrix();
    glScalef(2,3,1.5);
    # body
    if Wirep:
        glutWireSphere(1,20,20);
    else:
        glutSolidSphere(1,20,20);
    glPopMatrix();
  
    # limbs are in the head color
    twColor(headColor,0,0); # dark brown

    # draw right arm (the arm on our right = the bear's left)
    glPushMatrix();
    glTranslatef(1,2,0);
    glRotatef(90,0,1,0);
    twTube(0.5,0.4,2.5,20,1); 
    glPopMatrix();

    # draw left arm (the arm on our left = the bear's right)
    glPushMatrix();
    glTranslatef(-1,2,0);
    glRotatef(-90,0,1,0);
    twTube(0.5,0.4,2.5,20,1); 
    glPopMatrix();

    # draw right leg (the leg on our right = the bear's left)
    glPushMatrix();
    glTranslatef(1,-1.5,0);        # hip joint here
    glRotatef(30,0,1,0);        # rotate around y
    glRotatef(60,1,0,0);        # and around x
    twTube(0.7,0.6,3,20,1);
    glPopMatrix();
  
    # draw left leg (the leg on our left = the bear's right)
    glPushMatrix();
    glTranslatef(-1,-1.5,0);        # hip joint here
    glRotatef(-30,0,1,0);        # rotate around y
    glRotatef(60,1,0,0);        # and around x
    twTube(0.7,0.6,3,20,1);
    glPopMatrix();

    # draw head
    twColor(headColor,0,0);

    glPushMatrix();                # head coordinate system
    glTranslatef(0,4,0);
    # head
    if Wirep:
        glutWireSphere(1,20,20);
    else:
        glutSolidSphere(1,20,20);

    twColorName(TW_BLACK);        # eyes and nose in black

    glPushMatrix();
    glTranslatef(-0.4,0,0.9);
    glutSolidSphere(0.12,10,10);  # left eye
    glTranslatef(0.8,0,0);
    glutSolidSphere(0.12,10,10);  # right eye
    glPopMatrix();

    glPushMatrix();
    glTranslatef(0,-0.4,0.9);
    glutSolidSphere(0.2,10,10);   # nose
    glPopMatrix();

    twColor(bodyColor,0,0);        # ears are in body color

    glPushMatrix();
    glTranslatef(-0.6,0.7,0.2);
    glScalef(1,1,0.5);
    glutSolidSphere(0.4,20,20);  # left ear
    glPopMatrix();

    glPushMatrix();
    glTranslatef(0.6,0.7,0.2);
    glScalef(1,1,0.5);
    glutSolidSphere(0.4,20,20);  # right ear
    glPopMatrix();

    glPopMatrix();                # end of head coordinate system
    glPopMatrix();                # final pop

def display():
    twDisplayInit();
    twCamera();

    drawBear();

    glFlush();
    glutSwapBuffers();

def wireToggle(key, x, y):
    global Wirep
    Wirep = not Wirep;
    glutPostRedisplay();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-3.5,3.5,-1.5-3*math.sqrt(3)/2,3+2,-1.5,1.5);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    twKeyCallback('w',wireToggle,"toggle wire-frame bear body and head");
    glutMainLoop()

if __name__ == '__main__':
    main()
