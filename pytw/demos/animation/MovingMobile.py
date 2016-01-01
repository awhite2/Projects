#!/usr/bin/python

""" Extension of demos/modeling/Mobile, added animation.  You can control
   the speed of the animation with a command-line argument.

Scott D. Anderson
scott.anderson@acm.org
Fall 2009, ported to Python
"""

import sys

from TW import *

### ================================================================

DeltaT = 1.0             # helps determine the speed/smoothness of the animation

WinHeight = 500
WinWidth  = 500

Spinning = False               # whether we are spinning
SaveFrames = False             # whether to save animation frames.

#spin variables.  These are the angle for the various joints, etc.  We
# use Python dictionaries for these so that our code uses symbolic
# names (dictionary keys) instead of constants.

InitialPartAngles = {'octahedron': 0,
                     'teapot': 0,
                     'rightJoint3': 0,
                     'bear': 0,
                     'rightJoint2': 0,
                     'torus': 0,
                     'rightJoint1': 0,
                     'middleJoint': 0,
                     'icosahedron': 0,
                     'tetrahedron': 0,
                     'leftJoint3': 0,
                     'sphere': 0,
                     'leftJoint2': 0,
                     'barn': 0,
                     'leftJoint1': 0}

PartAngles = InitialPartAngles.copy()

PartSpeeds = {'octahedron': 3,
              'teapot': 4,
              'rightJoint3': -5,
              'bear': 3,
              'rightJoint2': 2,
              'torus': 5, 
              'rightJoint1': -2,
              'middleJoint': 1,
              'icosahedron': 5,
              'tetrahedron': 4,
              'leftJoint3': -3,
              'sphere': 2,
              'leftJoint2': 1,
              'barn': -2,
              'leftJoint1': 1}

#bounding box dimensions
width = 80
height = 60
depth2 = 5                     # half the depth

#bar lengths
bLength1=35                    # length of first bar from top
bLength2=20                    # length of second bar
bLength3=15                    # length of third bar 
bLength4=8                     # length of fourth bar 
 
#string lengths
sLength1=10                    # length of first string from top
sLength2=7                     # length of second string
sLength3=15                    # length of third string
sLength4=15                    # length of fourth string

#draws a "bar" of uniform height and width; takes length as a parameter
def drawBar(length):
  glPushMatrix()
  glTranslatef(-length/2,0,0)
  glRotatef(90,0,0,1)
  gray50 = (0.5, 0.5, 0.5)
  twColor(gray50,0.7,100) #set color of bar
  twSolidCylinder(1,1,length,10,10) 
  glPopMatrix()

#draws a red string; takes length as parameter
def drawString(length):
  glPushMatrix()
  red = (1,0,0)
  twColor(red,0,0)
  glBegin(GL_LINES)
  glVertex3f(0,0,0)
  glVertex3f(0,-length,0)
  glEnd()
  glPopMatrix()

#resizes twDrawBarn to appropriate dimension
def drawBarn():
  glPushMatrix()
  glRotatef(75,0,1,0)
  glTranslatef(-2,-5.5,3) #translate so barn is centered at end of string
  
  glScalef(4,6,6)
  pink = (1, 0.7, 0.7)
  red  = (1, 0, 0)
  twSolidBarn(pink, pink, red)
  glPopMatrix()

def drawRightSide():
  glPushMatrix()
  glTranslatef((bLength1)/2,0,0) #translate to right end of first bar
  drawString(sLength1)           #draw top right string
  glTranslatef(0,-sLength1,0)    #translate to bottom of first string
  glRotatef(PartAngles['rightJoint1'],0,1,0)  #rotation for rightJoint1 spin
  drawBar(bLength2)

  glPushMatrix()           #stores location after second bar is drawn
  glTranslatef((bLength2)/2,0,0) #translate to right end of second bar
  drawString(sLength2)           # 
  glTranslatef(0,-sLength2,0)  #translate to bottom of second string
  glRotatef(PartAngles['rightJoint2'],0,1,0)  #rotation- for rightJoint2 spin
  drawBar(bLength3)

  glPushMatrix()            #stores location after third bar is drawn
  glTranslatef((bLength3)/2,0,0) #translate to right end of third bar
  drawString(sLength3)           # 
  glTranslatef(0,-sLength3,0)    #translate to bottom of third string
  glRotatef(PartAngles['rightJoint3'],0,1,0)
  drawBar(bLength4)
  
  glPushMatrix()  #stores location after fourth bar is drawn
  glTranslatef((bLength4)/2,0,0) #translate to right end of fourth bar
  drawString(sLength4)
  glTranslatef(0,-sLength4,0)  #translate to bottom of fourth string
  glRotatef(PartAngles['teapot'],0,1,0)  #rotation for teapot spin
  lightRed = (0.2,0.2,1)
  twColor(lightRed,0.7,128)        #set color for teapot
  glutSolidTeapot(1.5) 
  glPopMatrix() #return to middle of fourth bar

  glTranslatef((-bLength4)/2,0,0)
  drawString(sLength4)
  glTranslatef(0,-sLength4,0)
  orange = (1, 0.5, 0)
  twColor(orange,0.6,70) #set color for octahedron
  glRotatef(PartAngles['octahedron'],0, 1, 0)  #rotation for octahedron spin
  glScalef(2,2,2)
  glutSolidOctahedron()
  glPopMatrix()  #return to middle of third bar
  
  glTranslatef((-bLength3)/2,0,0)
  drawString(sLength3)
  glTranslatef(0,-sLength3,0)
  glRotatef(PartAngles['bear'],0,1,0)  #rotation for bear spin
  glScalef(10,10,10)
  twTeddyBear()
  glPopMatrix()  # return to middle of second bar
  
  glTranslatef((-bLength2)/2,0,0)
  drawString(sLength2)
  glTranslatef(0,-sLength2,0)
  darkYellow = (0.8, 0.8, 0)
  twColor( darkYellow, 0.5, 100) 
  glTranslatef(0,-3,0) #translate down the size of the torus's outer radius
  glRotatef(PartAngles['torus'],0,1,0)  #rotation for torus spin
  glutSolidTorus(1,3,10,10)
  glPopMatrix()


def drawLeftSide():
  glPushMatrix()
  glTranslatef((-bLength1)/2,0,0) #translate to left end of first bar
  drawString(sLength1) #draw top left string
  glTranslatef(0,-sLength1,0) #translate to bottom of first string
  glRotatef(PartAngles['barn'],0,1,0)  #rotation for leftJoint1 spin
  drawBar(bLength2)

  glPushMatrix() #stores location after second bar is drawn
  glTranslatef((-bLength2)/2,0,0) #translate to left end of second bar
  drawString(sLength2)
  glTranslatef(0,-sLength2,0) #translate to bottom of second string
  glRotatef(PartAngles['leftJoint2'],0,1,0)  #rotation for leftJoint2 spin
  drawBar(bLength3)

  glPushMatrix()            #stores location after third bar is drawn
  glTranslatef((-bLength3)/2,0,0) #translate to left end of third bar
  drawString(sLength3)
  glTranslatef(0,-sLength3,0)  #translate to bottom of third string
  glRotatef(PartAngles['leftJoint3'],0,1,0)    #rotation for leftJoint3 spin
  drawBar(bLength4) 
  
  glPushMatrix()           #stores location after fourth bar is drawn
  glTranslatef((-bLength4)/2,0,0) #translate to left end of fourth bar
  drawString(sLength4)
  glTranslatef(0,-sLength4,0)  #translate to bottom of fourth string
  glRotatef(PartAngles['icosahedron'],0,1,0)     #rotation for icosahedron spin
  greenish = (0.2, 0.8, 0.2)
  twColor(greenish,0.5,100)    #set color for icosahedron
  glScalef(2,2,2)
  glutSolidIcosahedron() # ICOSAHEDRON 
  glPopMatrix() #return to middle of fourth bar

  glTranslatef((bLength4)/2,0,0) #translate to right end of fourth bar
  drawString(sLength4)
  glTranslatef(0,-sLength4,0)
  glRotatef(PartAngles['tetrahedron'],0,1,0)  #rotation for tetrahedron spin
  darkPink = (0.5, 0, 0.5)
  twColor(darkPink,0.5,100)  #set color for tetrahedron
  glScalef(2,2,2)
  glutSolidTetrahedron()
  glPopMatrix()  #return to middle of third bar
  
  glTranslatef((bLength3)/2,0,0) #translate to right end of third bar
  drawString(sLength3)
  glTranslatef(0,-sLength3,0)
  darkBlueGreen = (0, 0.5, 0.5)
  twColor( darkBlueGreen, 0.8, 128)
  glTranslatef(0,-2,0) #translate down the size of the radius of the sphere
  glRotatef(PartAngles['barn'],0,1,0)  #rotation for sphere spin
  glutSolidSphere(3,20,20) 
  glPopMatrix() 
  
  glTranslatef((bLength2)/2,0,0) #translate to right end of second bar
  drawString(sLength2)
  glTranslatef(0,-sLength2,0)
  glRotatef(PartAngles['sphere'],0,1,0) # rotation for barn spin
  drawBarn() 
  glPopMatrix()

FrameNumber = 1

FrameFileTemplate = "/tmp/MovingMobile%03d.ppm"

def saveFrame():
    global FrameNumber
    file = FrameFileTemplate % (FrameNumber)
    FrameNumber += 1
    if FrameNumber > 999:
        print "Sorry, this program assumes 3 digit numbers.  Please update it"
        sys.exit(1)
    twSaveFrame(file, False)

def display():
    twDisplayInit()
    twCamera() #sets up camera based on bounding box coords.

    glEnable(GL_LIGHTING)
    twGrayLight(GL_LIGHT0, (1,3,1,0), 0.2, 0.8, 0.7)
    twAmbient(0.2)
    glShadeModel(GL_SMOOTH)

    glPushMatrix()

    glTranslatef(width/2,height,0)
    drawString(10) #top middle string
    glTranslatef(0,-10,0)
    glRotatef(PartAngles['middleJoint'],0,1,0)  #rotation for middleJoint spin
    drawBar(bLength1)  #draw top bar
    drawRightSide()
    drawLeftSide()
    glPopMatrix()

    glFlush()
    glutSwapBuffers()   #necessary for animation

    if SaveFrames:
        saveFrame()


#idle callback for animation
def spin():
    for i in PartAngles:
        PartAngles[i] += PartSpeeds[i] * DeltaT
        if (PartAngles[i]>360):
            PartAngles[i]-=360
    glutPostRedisplay() 

def keys(key, x, y):
    global SaveFrames, Spinning
    if key == '1':
        SaveFrames = not SaveFrames
        print "the program %s save frames in %s" % (
            "will" if SaveFrames else "won't",
            FrameFileTemplate )
    elif key == '2':
        Spinning = not Spinning
        if Spinning:
            glutIdleFunc(spin)
        else:
            glutIdleFunc(None)
    elif key == '3':
        spin()
    elif key == '4':
        global PartAngles
        PartAngles = InitialPartAngles.copy()
        glutPostRedisplay()

### ================================================================

def main():
    global DeltaT
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(0,width,0,height,-depth2,depth2)
    twInitWindowSize(WinWidth, WinHeight)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    if len(sys.argv) > 1:
        DeltaT = float(sys.argv[1])
    else:
        DeltaT = 1.0            # default value
    twMainInit()
    twKeyCallback('1',keys,"toggle saving frames")
    twKeyCallback('2',keys,"toggle spinning")
    twKeyCallback('3',keys,"just one step")
    twKeyCallback('4',keys,"reset to first step")
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == '__main__':
    main()
