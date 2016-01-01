'''
Monet Spells | mspells@wellesley.edu
CS 307 Problem Set #4
Fall 2009
'''

import sys
import math

try:
    from TW import *
except:
    print '''ERROR: Couldn't import TW.'''

### === VARIABLES === ###
Wired = False # true if you want wire-framed desk elements
desk = (92.0/255,51.0/255,23.0/255) # chocolate brown
deskDrawers = (139.0/255,115.0/255,85.0/255) # light brown
drawerHandle = (255.0/255,255.0/255,255.0/255) # white
computer = (255.0/255,255.0/255,255.0/255) # white
screen = (0.0/255,0.0/255,0.0/255) # black
keys = (120.0/255,120.0/255,120.0/255) # gray
stapler = (193.0/255,105.0/255,105.0/255) # reddish-brown
stapleMetal = (166.0/255,166.0/255,166.0/255) # light gray
glasses = (255.0/255,0.0/255,0.0/255) # red
pencil = (218.0/255,165.0/255,32.0/255) # mustard yellow
pencilTip = (0.0/255,0.0/255,0.0/255) # black
eraser = (255.0/255,130.0/255,171.0/255) # light pink
picFrame = (153.0/255,204.0/255,52.0/255) # yellow green
lamp = (0.0/255,127.0/255,255.0/255) # slate blue (bit darker than sky blue)
lampAccent1 = (0.0/255,0.0/255,128.0/255) # navy blue
lampAccent2 = (108.0/255,123.0/255,139.0/255) # bluish gray
floppy1 = (255.0/255,127.0/255,0.0/255) # coral orange
floppy2 = (0.0/255,0.0/255,0.0/255) # black
floppy3 = (0.0/255,238.0/255,0.0/255) # bright green

black = (0.0/255,0.0/255,0.0/255) # black for small, un-customizable things
white = (255.0/255,255.0/255,255.0/255) # white for small, un-customizable things
### ================= ###

def mspellsDrawPictureFrame(color):
    '''
    Draws a picture frame with a given color. The inner portion of the frame will always be white, just as the back support of the frame will always be black.
    Dimensions: 4x5x2
    '''
    back = (0.0/255,0.0/255,0.0/255) # black
    inner = (255.0/255,255.0/255,255.0/255) # white
    glPushMatrix()
    twColor (color,0,0)
    createCube(4,5,1,1) # frame
    twColor (inner,0,0)
    glTranslate(0,0,0.1)
    createCube(3,4,1,1) # inside frame
    twColor (back,0,0)
    glTranslate(0,-1,-1)
    glRotate(45,1,0,0)
    createCube(1,3.5,0.25,1) # backing
    glPopMatrix()

def mspellsDrawDesk(deskColor,drawerColor,handleColor):
    '''
    Draw a desk, with changable colors for the desk, drawers and drawer handles.
    Dimensions: 25x15x20   
    '''
    twColor(deskColor,0,0)
    glPushMatrix() # desk coordinate system
    createCube(0.75,3,4,5) # left side of desk
    glTranslate(11.5,7,0)
    createCube(5,0.25,4,5) # top of desk
    glTranslate(8.5,-7,0)
    createCube(2,3,4,5) # right side of desk
    glTranslate (0,0,9.75)
    glPushMatrix() # drawer coordinate system
    mspellsDrawDrawer(drawerColor,handleColor) # middle drawer
    glPopMatrix()
    glPushMatrix()
    glTranslate (0,4.5,0) # top drawer
    mspellsDrawDrawer(drawerColor,handleColor)
    glPopMatrix()
    glPushMatrix()
    glTranslate (0,-4.5,0) # bottom drawer
    mspellsDrawDrawer(drawerColor,handleColor)
    glPopMatrix() # end drawer coordinate system
    glPopMatrix() # </desk>

def mspellsDrawDrawer(drawerColor,handleColor):
    '''
    Helper function to drawDesk. Values manipulated from drawDesk.
    Dimensions: 8x2x1
    '''
    twColor(drawerColor,0,0)
    createCube(4,1.5,0.5,2)
    twColor(handleColor,0,0)
    createSphere (1,1,1,1)

def mspellsDrawComputer(compColor,screenColor,keyColor):
    '''
    Draw a laptop computer, with changable computer, screen and keyboard colors.
    Dimensions: 8x7x6
    '''
    twColor(compColor,0,0)
    glPushMatrix()
    glPushMatrix() # computer coordinate system
    createCube(4,3.5,0.25,2) # computer frame
    glPushMatrix() # screen
    twColor(screenColor,0,0)
    glTranslate(0,0,0.2)
    mspellsDrawScreen()
    glPopMatrix() # </screen>
    glPushMatrix() # keyboard
    glTranslate(0,-3.25,2.8)
    mspellsDrawKeyboard(keyColor)
    glPopMatrix() #</keyboard>
    glPopMatrix() # </computer>
    glPopMatrix()

def mspellsDrawPencil():
    '''
    Draws a pencil. Colors are not changable.
    Dimensions: 0.5x0.2,3
    '''
    pencil = (218.0/255,165.0/255,32.0/255) # mustard yellow
    pencilTip = (0.0/255,0.0/255,0.0/255) # black
    eraser = (255.0/255,130.0/255,171.0/255) # light pink
    glPushMatrix()
    twColor(pencil,0,0)
    createCube(0.2,0.2,3,1) # main pencil
    glPushMatrix()
    glTranslate(0,0,1.5)
    twColor(pencilTip,0,0)
    createCone(0.1,0.15) # tip of pencil
    glPopMatrix()
    glTranslate(0,0,-1.5)
    twColor(eraser,0,0)
    createCube(0.2,0.2,0.2,1) # eraser
    glPopMatrix()

def mspellsDrawKeyboard(keyColor):
    '''
    Draw a computer keyboard. Helper function for drawComputer
    Dimensions: 8x0.5x6(keyboard) 0.3x0.3x0.3 (keys) 1.9x0.2x1.25 (mouse pad)
    '''
    createCube(4,0.25,3,2)
    # draw keys
    twColor(keyColor,0,0)
    glPushMatrix()
    glTranslate(-3.25,0.2,-1.25)
    for x in range(6):
        glPushMatrix()
        for i in range(14):
            createCube(0.3,0.3,0.3,1)
            glTranslate(0.5,0,0)
        glPopMatrix()
        glTranslate(0,0,0.5)
    #mousePad
    glTranslate(3,0,0.6)
    createCube(1.9,0.2,1.25,1)
    glPopMatrix()

def mspellsDrawPaperStack():
    '''
    Draws a paper stack. Color not changable.
    Dimensions: 3.5x5x5
    '''
    paper = (255.0/255,255.0/255,255.0/255) # white
    twColor(paper,0,0)
    glPushMatrix()
    glPushMatrix()
    for i in range (50): # make a stack of 50 pieces of paper
        createCube(3.5,0.1,5,1)
        glTranslate(0,0.05,0) # translate up to create stack
        glRotate(0.25,0,1,0) # rotate each paper a little bit
    glPopMatrix()
    glTranslate(0,0,6)
    glRotate(10,0,1,0)
    createCube(2.5,0.1,4,1) # additional piece of paper
    glPopMatrix()

def mspellsDrawFloppyDisc(color):
    '''
    Draws 1 floppy disc with given color. Dimensions: 3x3x0.3
    Dimensions:  3x3x0.3
    '''
    sliderColor = (255.0/255,255.0/255,255.0/255)
    glPushMatrix()
    twColor(color,0,0)
    createCube(1.5,1.5,0.15,2) # main floppy square
    glTranslate(0,0.75,0.05)
    twColor(sliderColor,0,0)
    createCube(1,0.75,0.15,2) # white sliding frame
    glTranslate(0.5,0,0.1)
    twColor(color,0,0)
    createCube(0.5,0.75,0.15,1) # visible through slider
    glPopMatrix()
    
def mspellsDrawGlasses(frameColor):
    '''
    Draws a pair of glasses, with changable frame colors
    '''
    glPushMatrix() # glasses
    twColor(frameColor,0,0)
    glScale(2,2,1)
    createCube(0.1,0.1,1.4,2) # left ear piece
    glTranslate(0.6,0,1.1)
    createTorus(0.1,0.4,20,20) # left rim
    glTranslate (0.65,0,0)
    createCube(0.4,0.15,0.25,1) # bridge of glasses
    glTranslate (0.7,0,0)
    createTorus(0.1,0.4,20,20) # right rim
    glTranslate(0.6,0,-1.1)
    createCube(0.1,0.1,1.4,2) # right ear piece
    glPopMatrix() # </glasses>

def mspellsDrawLamp(shadeColor,supportColor):
    '''
    Draws a regular desk lamp with changable accent colors (for shade and support).
    Base and lightbulb colors not changable
    '''
    bulb = (255.0/255,255.0/255,255.0/255)
    lampAccent = (108.0/255,123.0/255,139.0/255)
    glPushMatrix()
    twColor(shadeColor,0,0)
    glRotate(-125,1,0,0) # tilt lamp shade
    createCone (3,4) # lamp shade
    twColor(bulb,0,0)
    createSphere(1,1,1,1) # light bulb
    glTranslate(0,0,4) # translate the length of the lamp shade (along z)
    twColor (lampAccent,0,0)
    createSphere(1,1,1,0.75) # bulb @ end of lamp shade
    glTranslate(0,3,-1.5)
    glRotate(-30,1,0,0)
    twColor(supportColor,0,0)
    createCube(1,2.75,0.25,2) # top-support of lamp
    glTranslate(0,2.75,-2.25)
    glRotate(90,1,0,0)
    createCube(1,2.75,0.25,2) # bottom-support
    glTranslate(0,-2.75,0)
    glRotate(60,1,0,0)
    twColor(lampAccent,0,0)
    createSphere(2,0.5,2,1) # base of lamp
    glPopMatrix()
    
def mspellsDrawScreen():
    twColor(screen,0,0)
    createCube(3.5,3,0.1,2) # computer screen
    twColor(computer,0,0) # set back to computer color

def mspellsDrawStapler(staplerColor):
    '''
    Draws a stapler with a changable color.
    '''
    stapleMetal = (166.0/255,166.0/255,166.0/255) # light gray
    stapleBase = (0.0/255,0.0/255,0.0/255) # black
    twColor(staplerColor,0,0)
    glPushMatrix() # stapler
    createCube(1.25,0.25,3.5,1) # base of stapler
    twColor(stapleBase,0,0)
    createCube(1.15,0.27,3.3,1)
    glRotate(-17,1,0,0) # rotate a little for the head of the stapler
    glTranslate(0,0.5,0)
    twColor(stapleMetal,0,0)
    createCube(1,0.5,3,1) # metal part of stapler
    twColor(stapler,0,0)
    glTranslate(0,0.25,0)
    createCube(1.25,0.5,3.5,1) # top of stapler
    glPopMatrix() # </stapler>
                
def mspellsDrawDeskScene():
    glPushMatrix()

    # = DESK = #
    glPushMatrix()
    glTranslate(-9,-12,-5)
    mspellsDrawDesk(desk,deskDrawers,drawerHandle)
    glPopMatrix()

    # = COMPUTER = #
    glPushMatrix()
    glTranslate(-3,-0.9,-8)
    glRotate(15,0,1,0)
    mspellsDrawComputer(computer,screen,keys)
    glPopMatrix()

    # = STAPLER = #
    glPushMatrix()
    glTranslate(8,-4.25,-4)
    glRotate(-10,0,1,0)
    mspellsDrawStapler(stapler)
    glPopMatrix()

    # = GLASSES = #
    glPushMatrix()
    glTranslate(-1,-2.5,-6)
    glRotate(-13,0,0,1)
    mspellsDrawGlasses(glasses)
    glPopMatrix()
    
    # = PAPER STACK = #
    glPushMatrix()
    glTranslate(11,-4.4,-8)
    mspellsDrawPaperStack()
    glPopMatrix()
    
    # = PENCILS = #
    glPushMatrix()
    glTranslate(3,-4,-10)
    mspellsDrawPencil()
    glTranslate(1,0,8)
    glRotate(-50,0,1,0)
    mspellsDrawPencil()
    glPopMatrix()
    
    # = PICTURE FRAME = #
    glPushMatrix()
    glTranslate(10.5,0.5,-7)
    mspellsDrawPictureFrame(picFrame)
    glPopMatrix()

    # = LAMP = #
    glPushMatrix()
    glTranslate(6,0.5,-9)
    glRotate(-30,0,1,0)
    mspellsDrawLamp(lamp,lampAccent1)
    glPopMatrix()

    # = FLOPPY DISC = #
    glPushMatrix()
    glTranslate(-6.5,-4.5,1)
    glRotate(-90,1,0,0)
    glRotate(10,0,0,1)
    mspellsDrawFloppyDisc(floppy1) # orange floppy
    glTranslate(3,0,0.05)
    glRotate(-25,0,0,1)
    mspellsDrawFloppyDisc(floppy2) # black floppy
    glTranslate(-1,-2,0.05)
    glRotate(15,0,0,1)
    mspellsDrawFloppyDisc(floppy3) # green floppy
    glPopMatrix()

    glPopMatrix() # end scene coordinate system


## === HELPER FUNCTIONS === ###
# I used helper functions to create cubes, spheres, cones and toruses to process
# the case that the viewer is using wire-frame or not. Values passed aren't too surprising,
# but I wanted to make sure that every component could be viewed as a wire frame if the
# user wanted.
###

def createCube(x, y, z, size):
    glPushMatrix();
    glScale (x, y, z);
    if Wired:
      glutWireCube(size);
    else:
      glutSolidCube(size);
    glPopMatrix();

def createTorus(inR, outR, slices, stacks):
    glPushMatrix();
    if Wired:
      glutWireTorus(inR, outR, slices, stacks);
    else:
      glutSolidTorus(inR, outR, slices, stacks);
    glPopMatrix()

def createSphere(x, y, z, size):
    glPushMatrix()
    glScale (x, y, z)
    if Wired:
      glutWireSphere(size, 20, 20)
    else:
      glutSolidSphere(size, 20, 20)
    glPopMatrix()

def createCone(b, h):
    glPushMatrix();
    if Wired:
      glutWireCone(b, h, 10, 10);
    else:
      glutSolidCone(b, h, 10, 10);
    glPopMatrix();
### ======================== ###



def wireToggle(key, x, y):
    global Wired
    Wired = not Wired;
    glutPostRedisplay();

def display():
    twDisplayInit()
    twCamera()
    
    mspellsDrawDeskScene()
    
    glFlush()
    glutSwapBuffers()

def main ():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twBoundingBox(-15,20,-20,10,-20,10)
    twMainInit()          
    twKeyCallback('w',wireToggle,"toggle wire-frame bear body and head");
    glutMainLoop()

if __name__ == '__main__':
    main()
