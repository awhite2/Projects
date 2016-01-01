#Original author: Stephanie Judge 
#Ported by: Danika Suggs

'''
Copyright (C) 2012 by Stephanie Judge under the GNU GPL

Description: This creates a Penguin of a user-specified size.  The feet are made of polygons and disks with a low stack and slice count, to make them seem more toy-like, as this is a toy penguin.  The body is made up of two scaled spheres, one white, and one black.  The black one lies further back than the white, overlapping to give the appearance of a white belly.  The arms are made up of a scaled, flat cube and a disk for the bottom, curved end of the arms.  The head is a black sphere, with a cone for a beak, which is rotated upwards.  The eyes are also made up of two spheres, one white, with a black sphere slightly outside and forward.  Finally, there is a tail in the back made up of a cylinder with a wide base and narrow top. When specifying a size, the penguin will be about 4*size units tall.
'''

import sys
from TW import *

def sjudgePenguin(size):

    #colors
    black = (0,0,0)
    orange = (1,0.55,0)
    white = (1,1,1)
    tie = (0.22,0.48,0.9)

    #right foot coordinates
    RFootTranslateX = size
    RFootTranslateZ = -size*0.2
  
    #left foot coordinates
    LFootTranslateX = -size
    LFootTranslateZ = -size*0.2

    #foot coordinates
    FootSize = size*0.3

    #body
    penguinHeight = 2*size
    BodyTranslateZ = -0.2*size
    bodySize = size

    #back part of the body
    BBodyTranslateY = -0.2*size
    BBodyTranslateZ = -0.5*size

    #arms
    penguinArms = 2.7*size
    ArmTranslateZ = -0.5*size
    RArmTranslateX = size
    RArmTranslateY = 0.05*size
    LArmTranslateX = -size
    LArmTranslateY = 0.05*size
    armSize = 0.2*size
    armCylinderB =0.4*size
    armCylinderH = 0.1*size

    #tie constants
    tieHeight = 2.9*size
    TieTranslateZ = 0.4*size

    #head constants
    penguinHead = 3.7*size
    HeadTranslateZ = -0.5*size
    headSize = 0.6*size

    #beak
    BeakTranslateY = 0.1*size
    BeakTranslateZ = 0.3*size
    BeakBase = 0.4*size
    BeakHeight = 0.8*size

    #right eye
    REyeTranslateX = 0.4*size
    REyeTranslateZ = 0.2*size
    eyeSizeW = 0.2*size
    BREyeTranslateX = 0.1*size
    BREyeTranslateZ = 0.1*size
    eyeSizeB = 0.1*size

    #left eye
    LEyeTranslateX = -0.4*size
    LEyeTranslateZ = 0.2*size
    BLEyeTranslateX = -0.1*size
    BLEyeTranslateZ = 0.1*size

    #tail
    TailTranslateY = 0.8*size
    TailTranslateZ = -1.2*size
    TailBase = 0.8*size
    TailTop = 0.005*size
    TailHeight = 1.5*size

    #make vertices
    penguin = [[-0.3*size,0,0], #foot coordinates 0
               [0.3*size,0,0],  #1
               [0,0,-0.5*size], #2
    
               [-0.6*size,0,0], #right leg 3
               [0,0,0],  #4
               [0,0,-0.2*size], #5
               [-0.6*size,0,-0.2*size], #6

               #top part
               [-0.6*size,size,0], #7
               [-0.6*size,size,-0.2*size], #8
    
               [0,0,0], #left leg 9
               [0.6*size,0,0],  #10
               [0.6*size,0,-0.2*size], #11
               [0,0,-0.2*size], #12
    
               #top part
               [0.6*size,size,0], #13
               [0.6*size,size,-0.2*size], #14
    
               #tie coordinates
               [-0.2*size,0.1*size,0], #15
               [-0.1*size,-0.1*size,0], #16
               [0.1*size,-0.1*size,0], #17
               [0.2*size,0.1*size,0], #18

               #bottom part of the tie
               [-0.1*size,-0.1*size,0], #19
               [-0.2*size,-1.5*size,0], #20
               [0,-1.8*size,0], #21
               [0.2*size,-1.5*size,0], #22
               [0.1*size,-0.1*size,0] #23
               ]

    glShadeModel(GL_SMOOTH)
  
    #right foot
    twColor(orange,0.7,5)
    glPushMatrix()
    glTranslatef(RFootTranslateX,0,RFootTranslateZ)
    glPushMatrix()
    glRotatef(30,0,1,0)
    glRotatef(90,1,0,0)
  
    twDisk(FootSize,6)
    glPopMatrix()
  
    glBegin(GL_TRIANGLES)   
    glNormal3f(0,1,0);
    glVertex3fv(penguin[0])
    glVertex3fv(penguin[1])
    glVertex3fv(penguin[2])
    glEnd()

    glBegin(GL_POLYGON)
    glNormal3f(0,1,0)
    glVertex3fv(penguin[3])
    glVertex3fv(penguin[4])
    glVertex3fv(penguin[5])
    glVertex3fv(penguin[6])
    glEnd();

    glBegin(GL_POLYGON)
    glNormal3f(1,0,0)
    glVertex3fv(penguin[3])
    glVertex3fv(penguin[6])
    glVertex3fv(penguin[8])
    glVertex3fv(penguin[7])
    glEnd()

    glPopMatrix() # back to the origin

    #left foot
    glPushMatrix()
    glTranslatef(LFootTranslateX,0,LFootTranslateZ)
    glPushMatrix()
    glRotatef(30,0,1,0)
    glRotatef(90,1,0,0)
  
    twDisk(FootSize,6)
    glPopMatrix()
  
    glBegin(GL_TRIANGLES)
    glNormal3f(0,1,0)
    glVertex3fv(penguin[0])
    glVertex3fv(penguin[1])
    glVertex3fv(penguin[2])
    glEnd()

    glBegin(GL_POLYGON)
    glNormal3f(0,1,0)
    glVertex3fv(penguin[9])
    glVertex3fv(penguin[10])
    glVertex3fv(penguin[11])
    glVertex3fv(penguin[12])
    glEnd()

    glBegin(GL_POLYGON)
    glNormal3f(-1,0,0)
    glVertex3fv(penguin[10])
    glVertex3fv(penguin[13])
    glVertex3fv(penguin[14])
    glVertex3fv(penguin[11])
    glEnd()
    
    glPopMatrix() # back to origin

    #body
    twColor(white,5,10);

    glPushMatrix()
    glTranslatef(0,penguinHeight,BodyTranslateZ)
    glPushMatrix()
    glScalef(0.7,1.5,0.7)
    glutSolidSphere(bodySize,20,20)
    glPopMatrix()

    #black part of body
    twColor(black, 5, 10)

    glTranslatef(0,BBodyTranslateY,BBodyTranslateZ)
    glPushMatrix()
    glRotatef(10,1,0,0)
    glScalef(1,1.8,1)
    glutSolidSphere(bodySize,20,20)
    glPopMatrix()


    glPopMatrix() # back to origin

    #right arm
    glPushMatrix()
    glTranslatef(0,penguinArms,ArmTranslateZ)
    
    glPushMatrix()
    glTranslatef(RArmTranslateX,0,0)
    glRotatef(-30,0,0,1)
    glPushMatrix()
    glScalef(10,.5,3)
    glutSolidCube(armSize)
    glPopMatrix()

    glTranslatef(RArmTranslateX,RArmTranslateY,0)
    glRotatef(30,0,1,0)
    twSolidCylinder(armCylinderB,armCylinderB,armCylinderH,6,6)
    glPopMatrix()

    #left arm
    glTranslatef(LArmTranslateX,0,0)
    glRotatef(30,0,0,1)
    glPushMatrix()
    glScalef(10,.5,3)
    glutSolidCube(armSize)
    glPopMatrix()
  
    glTranslatef(LArmTranslateX,LArmTranslateY,0)
    glRotatef(30,0,1,0)
    twSolidCylinder(armCylinderB,armCylinderB,armCylinderH,6,6)

    glPopMatrix() # back to origin

    #tie
    twColor(tie,5,10)

    glPushMatrix()
    glTranslatef(0,tieHeight,TieTranslateZ)
    glRotatef(-10,1,0,0)
    
    glBegin(GL_POLYGON)
    glNormal3f(0,0,1)
    glVertex3fv(penguin[15])
    glVertex3fv(penguin[16])
    glVertex3fv(penguin[17])
    glVertex3fv(penguin[18])
    glEnd()

    glBegin(GL_POLYGON)
    glNormal3f(0,0,1)
    glVertex3fv(penguin[19])
    glVertex3fv(penguin[20])
    glVertex3fv(penguin[21])
    glVertex3fv(penguin[22])
    glVertex3fv(penguin[23])
    glEnd()
    glPopMatrix()

    #head
    twColor(black,5,10)
  
    glPushMatrix()
    glTranslatef(0,penguinHead,HeadTranslateZ)
    glutSolidSphere(headSize,20,20)

    #beak
    twColor(orange,5,10)

    glPushMatrix()
    glTranslatef(0,BeakTranslateY,BeakTranslateZ)
    glRotatef(-20,1,0,0)
    glutSolidCone(BeakBase,BeakHeight,20,20)
    glPopMatrix()

    #right eye
    glPushMatrix()
    twColor(white,0.7,1)
    glTranslatef(REyeTranslateX,0,REyeTranslateZ)
    glutSolidSphere(eyeSizeW,20,20)
    twColor(black,0.7,1)
    glTranslatef(BREyeTranslateX,0,BREyeTranslateZ)
    glutSolidSphere(eyeSizeB,20,20)
    glPopMatrix()

    #left eye
    glPushMatrix()
    twColor(white,0.7,1)
    glTranslatef(LEyeTranslateX,0,LEyeTranslateZ)
    glutSolidSphere(eyeSizeW,20,20)
    twColor(black,0.7,1)
    glTranslatef(BLEyeTranslateX,0,BLEyeTranslateZ)
    glutSolidSphere(eyeSizeB,20,20)

    glPopMatrix()

    glPopMatrix() # origin

    #tail
    twColor(black,5,10)
  
    glPushMatrix()
    glTranslatef(0,TailTranslateY,TailTranslateZ)
    glRotatef(55,1,0,0)
    twSolidCylinder(TailBase, TailTop, TailHeight, 20,20)
    glPopMatrix() # origin

def display():
    
    twDisplayInit()
    twCamera()
    
    sjudgePenguin(10)
    
    glFlush()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twBoundingBox(-10,10,-10,40,-20,10)
    twMainInit()            
    glutMainLoop()

if __name__ == '__main__':
    main()

