'''
    Object: Swingset
    Created by: Irene Juang
    April 2012
    CS 307

    An OpenGL model of a swingset. Copyright (C) 2012 by Irene Juang
    This program is released under the GNU GPL.

'''
import sys

from TW import *

### ================================================================


def lumber(scale,c1):
    '''This method creates a peice of "lumber" by taking in the input scale
       and creating a piece of scale[0]x[scale[1]xscale[2] rectangular/box shape.
       The piece of lumber will be of the color, c'''
    glPushMatrix()
    glColor3fv(c1) #color of the lumber
    glScale(scale[0],scale[1],scale[2]) #scaling the unit cube by scale
    glutSolidCube(1)
    glPopMatrix()

def floorBoard(x,floorC):
    '''This method was used as a helper method to create the
        floorboards of the treehouse. The floorboard dimensions are
        1.8x0.5x19 and the input x is the amount of space between boards''' 
    glTranslate(x+1.8,0,0)
    lumber((1.8,0.5,19),floorC)

def ladder(c):
    '''This method crates a ladder for the treehouse that has an agle of 60
       between the ground and the ladder. The ladder itself is of length 30.
       It takes in one argument, c, for the color'''
    glPushMatrix()
    glTranslate(0,-5,0)
    glRotate(30,-1,0,0) # 60 degree angle between ladder and ground
    glPushMatrix()
    lumber((1.1,30,1.1),c) #left side of the ladder
    glTranslate(7,0,0)
    lumber((1.1,30,1.1),c) #right side of the ladder
    glTranslate(-7,10,0)
    glRotatef(90,0,1,0)
    gluCylinder(gluNewQuadric(),0.3,0.3,7,20,20) # first ladder step
    for i in range(4): # creates 4 more steps with spacing of 5
        glTranslate(0,-5,0)
        gluCylinder(gluNewQuadric(),0.3,0.3,7,20,20)
    glPopMatrix()
    glPopMatrix()
    
def swings(wood,metal,seat,chain):
    '''Draws the swings part of the swingset, takes in 4 colors
       has a length of 35. This method helps create ijuangSwingSet()
       function.'''
    glPushMatrix()
    glTranslate(0,16,0)
    lumber((35,1.2,1.2),wood) # long horizontal, top beam
    glPushMatrix()
    glTranslate(-16,0,0)
    glPushMatrix()
    glTranslate(0,-16,8.5)
    glRotate(25,-1,0,0)     #rotate beam 25 degrees
    lumber((1,37,1),wood)   #(front)supporting beam
    glPopMatrix()
    glPushMatrix()
    glTranslate(0,-16,-8.5)
    glRotate(25,1,0,0)      #rotate beam 25 degrees
    lumber((1,37,1),wood)   #draws back supporting beam
    glPopMatrix()
    glTranslate(0,-18,0)
    lumber((1,1,19),wood)   #connects the 2 side supporting beams
    glPopMatrix()
    glTranslate(-10,-0.6,0)
    glColor3fv(metal)       #color of the metal rings holding the swingsup
    glutSolidTorus(0.5,0.6,10,10)   #draws 4 metal rings
    for i in range(3):
        glTranslate(7,0,0)
        glutSolidTorus(0.4,0.6,10,10)
    glPushMatrix()
    glRotatef(90,1,0,0)
    for i in range(4):      #draw the dangling chain/rope of swings 
        glColor3fv(chain)
        gluCylinder(gluNewQuadric(),0.1,0.1,25,20,20)
        glTranslate(-7,0,0)
    glPopMatrix()
    glTranslate(-17.5,-25,0)
    lumber((8,0.3,2),seat)  # draw left swing seat
    glTranslate(14,0,0)
    lumber((8,0.3,2),seat)  # draw right swing seat
    glPopMatrix()


def ijuangSwingSet(woodC,floorC,awningC,seatC,chainC,metalC):
    '''Draws a swingset and treehouse combo set, with 6 given colors.
       The swingset is 60x45x45, and the origin is in the middle of the
       first pole of the treehouse. The swing set is facing the viewer
       (The +z axis). '''
    ##set up the tall rods of the treehouse 
    glPushMatrix()
    lumber((1,35,1),woodC)   #these stilts are 35 in length
    glTranslate(20,0,0)         #the tree house is 20x20 width/length
    lumber((1,35,1),woodC)
    glTranslate(0,0,-20)
    lumber((1,35,1),woodC)
    glTranslate(-20,0,0)
    lumber((1,35,1),woodC)
    glTranslate(0,17.5,10)
    lumber((1,0.5,20),woodC) 
    glTranslate(20,0,0)
    lumber((1,0.5,20),woodC)
    glPopMatrix()

    ##draw the middle poles of the treehouse that holds up the awning
    glPushMatrix()
    glTranslate(10,15,0)
    lumber((1,20,1),woodC) # vertical pole, length 20 
    glTranslate(0,0,-20)
    lumber((1,20,1),woodC) # vertical pole, length 20
    glTranslate(0,10,10)
    lumber((1,.8,21),woodC) #beam connecting the two poles, length 21 
    glPopMatrix()

    ## pieces of wood supporting the floorboards, each length of 20 
    glPushMatrix()
    glTranslate(10,5,-1)
    lumber((20,1,1),woodC)
    glTranslate(0,0,-18)
    lumber((20,1,1),woodC)
    glTranslate(0,11,-2)
    lumber((20,1,1),woodC)
    glTranslate(0,0,22)
    lumber((20,1,1),woodC)
    glPopMatrix()    

    ## draw the floorboards using the floorBoard method
    ## total of 9 floorboards with space of 0.475 between each one
    glPushMatrix()
    glTranslate(1,5.5,-10)
    lumber((1.8,0.5,19),floorC)
    for i in range(8):
        floorBoard(0.475,floorC)
    glPopMatrix()

    ## draw the boards holding the sidings of the treehouse  
    glPushMatrix()
    glTranslate(-0.75,6,-10) 
    lumber((0.5,2.5,21),woodC)
    glTranslate(0,8,0)
    lumber((0.5,2.5,21),woodC)
    glTranslate(21.75,0,0)
    lumber((0.5,2.2,21),woodC)
    glTranslate(0,-8,0)
    lumber((0.5,2.2,21),woodC)
    glPopMatrix()
    glPushMatrix()
    glTranslate(5,6,0.75)
    lumber((10,2.5,0.5),woodC)
    glTranslate(0,8,0)
    lumber((10,2.5,0.5),woodC)
    glTranslate(0,0,-21.75)
    lumber((10,2.5,0.5),woodC)
    glTranslate(10,0,0)
    lumber((10,2.5,0.5),woodC)
    glTranslate(0,-8,0)
    lumber((10,2.5,0.5),woodC)
    glTranslate(-10,0,0)
    lumber((10,2.5,0.5),woodC)
    glPopMatrix()
    
    #vertical siding/panesl of the treehouse  
    glPushMatrix()
    glTranslate(2,10,0)
    lumber((2,8,0.5),floorC)
    for i in range(2):          # front 3 panels
        glTranslate(3,0,0)
        lumber((2,8,0.5),floorC)
    glTranslate(-6,0,-20)
    lumber((2,8,0.5),floorC)    # back 6 panels 
    for i in range(5):
        glTranslate(3,0,0)
        lumber((2,8,0.5),floorC)
    glPopMatrix()
    glPushMatrix()
    glTranslate(0,10,-2)
    lumber((0.5,8,2),floorC)    # left 6 panels 
    for i in range(5):
        glTranslate(0,0,-3)
        lumber((0.5,8,2),floorC)
    glTranslate(20,0,0)         # right 6 panels
    lumber((0.5,8,2),floorC)
    for i in range(5):
        glTranslate(0,0,3)
        lumber((0.5,8,2),floorC)
    glPopMatrix()

    ##awning part of the treehouse
    glPushMatrix()
    glColor3fv(awningC)     #awning/tent color
    glTranslate(5,22,-10)   
    glRotatef(40,0,0,1)     #40 degree rotation
    glScale(13,0.1,20)
    glutSolidCube(1)        #left side 
    glPopMatrix()
    glPushMatrix()
    glTranslate(15,22,-10)
    glRotatef(-40,0,0,1)
    glScale(13,0.1,20)
    glutSolidCube(1)        #right side 
    glPopMatrix()

    ##place the ladder in the right spot 
    glPushMatrix()
    glTranslate(12,1,6)
    ladder(floorC)
    glPopMatrix()

    ## addding the swings to the set
    glPushMatrix()
    glTranslate(-18,0,-10)
    swings(woodC,metalC,seatC,chainC)
    glPopMatrix()
    

### ================================================================

def display():
    twDisplayInit();
    twCamera();
    #twSky()
    #twGround()

    # colors for the swingset
    gray = (127.0/255.0,127.0/255.0,127.0/255.0)
    blue = (77.0/255.0,77.0/255.0,255.0/255.0)
    green = (0.0/255.0,140.0/255.0,70.0/255.0)
    brown1 = (107.0/255.0,66.0/255.0,38.0/255.0)
    brown2 = (100.0/255.0,75.0//255.0,30.0/255.0)
    pink = (255.0/255.0,20.0/255.0,147.0/255.0)

    #draw Swing Set
    glPushMatrix()
    # colors of the swing set:
        # woodC = brown1, floorC = brown2
        # awningC = green, seatC = pink
        # chainC = blue, metal = gray
    ijuangSwingSet(brown1,brown2,green,pink,blue,gray)
    glPopMatrix()
        
    glFlush();
    glutSwapBuffers();

### ================================================================

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-37,+23,-18,+27,-28,+17) 
    twInitWindowSize(500,500);
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()
