'''Objects created by Maui Moore

Copyright (C) 2007 by Marielle Moore under the GNU GPL
   
Modified by Hye Soo Yang

Date Modified: Feb 24, 2012

Includes table object
CS 307
'''
import sys

from OpenGL.GLUT import*
from OpenGL.GL import*
from OpenGL.GLU import*

try:
    from TW import*
except:
    print '''
ERROR: Couldn't import TW.
          '''

def mmoore2DrawPalmTree(palmColor1, palmColor2, palmColor3,
                        coconutColor, trunkColor, treeBase, treeHeight):
    '''This function takes in five color specifications and two length
    information. It creates Palm Tree with two different leaf colors,
    two coconut balls(one hanging, the other on the ground) and a solid trunk.'''
    # Make the trunk using a trunkColored cone
    glColor3fv(trunkColor)

    glPushMatrix()

    # Placement of three in bounding box is related to height of tree
    glTranslatef((treeHeight/2.0), 0, (treeHeight/2.0))
    glRotatef(270, 1, 0, 0)
    glutSolidCone(treeBase, treeHeight, 100, 100)

    glPopMatrix()

    # Make the crown using cones
    # each palm fround is 2/3 height of tree
    # the crown has 3 layers of palm fronds, one of each palmColor#
    # each layers is coded in a separate for loop that changes the
    # axis/axes and angle of rotation of each cone

    # first layer of crown
    glColor3fv(palmColor1)

    # First frond doesn't need to be rotated and so is not encoded in loop
    glPushMatrix()

    # Bases of all fronds placed at apex of cone
    glTranslatef((treeHeight/2.0), treeHeight, (treeHeight/2.0))

    glutSolidCone(treeBase/2.0, (2*treeHeight)/3.0, 100, 100)

    glPopMatrix()

    for i in range(90, 360, 90):
        glPushMatrix()

        glTranslatef((treeHeight/2.0),treeHeight, (treeHeight/2.0))
        glRotatef(i,1,1,0)
        glutSolidCone(treeBase/2, (2*treeHeight)/3.0, 100, 100)

        glPopMatrix()

    # Second layer of crown
    glColor3fv(palmColor2)

    for i in range(45, 360, 90):
        glPushMatrix()

        glTranslatef((treeHeight/2.0), treeHeight, (treeHeight/2.0))
        glRotate(i,0,1,0)
        glutSolidCone(treeBase/2.0, (2*treeHeight)/3.0, 100, 100)

        glPopMatrix()

    # 3rd layer of crown
    glColor3fv(palmColor3)
    for i in range(45, 360, 45):
        glPushMatrix()
        glTranslatef((treeHeight/2.0), treeHeight, (treeHeight/2.0))
        glRotatef(i,0,1,1)
        glutSolidCone(treeBase/2.0, (2*treeHeight)/3.0, 100, 100)
        glPopMatrix()

    # Cononuts
    glColor3fv(coconutColor)

    # One coconut is attached to the tree, 9/10 of the way up, slight set off
    # from the center of base of cone
    glPushMatrix()
    glTranslatef((treeHeight/2.0)-(treeBase/2.0), (9*treeHeight)/10, (treeHeight/2.0))
    glutSolidSphere(treeBase/2.0,100,100)
    glPopMatrix()

    # This coconut is on the ground to the right of the tree
    glPushMatrix()
    glTranslatef((treeHeight/2.0)+(treeBase*2), treeBase/2.0, (treeHeight/2.0))
    glutSolidSphere(treeBase/2.0,100,100)
    glPopMatrix()



palmColor1 = (0, 1.0, 0)
palmColor2 = (0, 0.8, 0.1)
palmColor3 = (0, 0.75, 0.5)
coconutColor = (0.8, 0.25, 0.35)
trunkColor = (1.0, 0.9, 0.0)

treeHeight = 10
treeBase = 2

def display():
    twDisplayInit()
    twCamera()

    mmoore2DrawPalmTree(palmColor2, palmColor2, palmColor3, coconutColor,
                        trunkColor, treeBase, treeHeight)
    glFlush()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(500, 500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twBoundingBox(0,15,0,15,0,15)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()
    
