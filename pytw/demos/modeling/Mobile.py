'''Using stacks and affine transformations to construct a mobile. 

Written by Caroline Geiersbach and Scott D. Anderson
scott.anderson@acm.org
Summer 2003

Adapted to use Python in Fall 2009
'''

import sys

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''

#bounding box dimensions
BBwidth = 80;
BBheight = 60;
BBdepth2 = 5;                   # half the depth

#bar lengths
bLength1=35;                    # length of first bar from top
bLength2=20;                    # length of second bar
bLength3=15;                    # length of third bar 
bLength4=8;                     # length of fourth bar 
 
#string lengths
sLength1=10;                    # length of first string from top
sLength2=7;                     # length of second string
sLength3=15;                    # length of third string
sLength4=15;                    # length of fourth string

def drawBar(length):
    '''draws a "bar" of unit height and width; takes length as a parameter'''
    glPushMatrix();
    twColorName(TW_GRAY);
    glScalef(length,1,1);
    glutSolidCube(1);
    glPopMatrix();

def drawString(len):
    '''draws a red string of length len down the negative y axis and moves
coordinate system to the end of the string'''
    twColorName(TW_RED);
    glBegin(GL_LINES);
    glVertex3f(0,0,0);
    glVertex3f(0,-len,0);
    glEnd();
    glTranslatef(0,-len,0);

def drawBarn():
    '''resizes twDrawBarn, translated so that barn is drawn from the center
(x and z directions) and from the top (y direction).'''
    glPushMatrix();
    glRotatef(75,0,1,0); #turn so sides of barn can be seen
    glTranslatef(-2,-6,3); #center barn at end of string
    glScalef(4,6,6);
    # colors of faces
    side = (0.2,0.2,0.9);       #color of sides
    roof = (0.3,0.3,0.3);       #color of roof
    ends = (0.3,0.3,0.9);       #color of ends
    twSolidBarn(ends,side,roof);
    glPopMatrix();

# ================================================================

def mobileLR():
    glPushMatrix();
    drawString(sLength2);
    drawBarn();
    glPopMatrix();

def mobileLLR():
    glPushMatrix();
    drawString(sLength3);
    darkCyan = (0, 0.5, 0.5)
    twColor(darkCyan,0,0);
    glTranslatef(0,-2,0); #translate down the size of the radius of the sphere
    glutSolidSphere(3,20,20);   # sphere
    glPopMatrix();

def mobileLLLR():
    glPushMatrix();
    drawString(sLength4);
    darkPink = (0.5, 0, 0.5)
    twColor(darkPink, 0, 0);        #set color for tetrahedron
    glScalef(2,2,2);
    glutSolidTetrahedron();        # tetrahedron
    glPopMatrix();

def mobileLLLL():
    glPushMatrix();
    drawString(sLength4);
    greenish = (0.2, 0.8, 0.2)
    twColor(greenish,0,0);      #set color for icosahedron
    glScalef(2,2,2);
    glutSolidIcosahedron();
    glPopMatrix();

def mobileLLL():
    glPushMatrix();
    drawString(sLength3);
    drawBar(bLength4);
    glTranslatef(bLength4/2,0,0);
    mobileLLLR();
    glTranslatef(-bLength4,0,0);
    mobileLLLL();
    glPopMatrix();

def mobileLL():
    glPushMatrix();
    drawString(sLength2);
    drawBar(bLength3);
    glTranslatef(bLength3/2,0,0);
    mobileLLR();
    glTranslatef(-bLength3,0,0);
    mobileLLL();
    glPopMatrix();

def mobileL():
    glPushMatrix();
    drawString(sLength1);
    drawBar(bLength2);
    glTranslatef(bLength2/2,0,0);
    mobileLR();
    glTranslatef(-bLength2,0,0);
    mobileLL();
    glPopMatrix();

def mobileRRRR():
    glPushMatrix();
    drawString(sLength4);
    lightRed = (0.2,0.2,1)
    twColor(lightRed,0,0);        #set color for teapot
    glutSolidTeapot(1.5);
    glPopMatrix();

def mobileRL():
    glPushMatrix();
    drawString(sLength2);
    darkYellow = (0.8, 0.8, 0.0)
    twColor(darkYellow,0,0);
    glTranslatef(0,-3,0); #translate down the size of the torus's outer radius
    glutSolidTorus(1,3,10,10);  # TORUS
    glPopMatrix();

def mobileRRL():
    glPushMatrix();
    drawString(sLength3);
    darkGreen = (0.5,0.1,0.1)
    twColor(darkGreen,0,0);
    glScalef(10,10,10);
    twTeddyBear();                # bear
    glPopMatrix();

def mobileRRRL():
    glPushMatrix();
    drawString(sLength4);
    twColorName(TW_CYAN);
    glScalef(2,2,2);
    glutSolidOctahedron();        # octahedron
    glPopMatrix();

def mobileRRR():
    glPushMatrix();
    drawString(sLength3);
    drawBar(bLength4);
    glTranslatef(bLength4/2,0,0);
    mobileRRRR();
    glTranslatef(-bLength4,0,0);
    mobileRRRL();
    glPopMatrix();

def mobileRR():
    glPushMatrix();
    drawString(sLength2);
    drawBar(bLength3);
    glTranslatef(bLength3/2,0,0);
    mobileRRR();
    glTranslatef(-bLength3,0,0);
    mobileRRL();
    glPopMatrix();

def mobileR():
    glPushMatrix();
    drawString(sLength1);
    drawBar(bLength2);
    glTranslatef(bLength2/2,0,0);
    mobileRR();
    glTranslatef(-bLength2,0,0);
    mobileRL();
    glPopMatrix();

def mobile():
    glPushMatrix();
    drawString(10);             #top middle string
    drawBar(bLength1);          #draw top bar
    glTranslatef(bLength1/2,0,0);
    mobileR();
    glTranslatef(-bLength1,0,0);
    mobileL();
    glPopMatrix();

def display():
    twDisplayInit();
    twCamera();

    glPushMatrix();
    glTranslatef(BBwidth/2,BBheight,0);
    mobile();
    glPopMatrix();

    glFlush();
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(0,BBwidth,0,BBheight,-BBdepth2,+BBdepth2);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glLineWidth(2);
    glutDisplayFunc(display)
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()
