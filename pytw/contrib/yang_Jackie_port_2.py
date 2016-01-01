'''Objects created by Jackie

Copyright (C) 2012 by Jackie under the GNU GPL
   
Modified by Hye Soo Yang

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

def tablePosts2(x, z):
    '''According to the specifications below
       the height of post is 3,
       the thickness of post is 1.
       Draws posts from the center of the table.'''
    
    lightGray = (0.9, 0.9, 0.9)
    twColor(lightGray, 0.5, 30)

    glBegin(GL_QUADS)
    # Front side of the post (positive z-axis)
    glNormal3f(0,0,1)
    glVertex3f(x - 0.5, 3.0, z + 0.5)
    glVertex3f(x - 0.5, 0.0, z + 0.5)
    glVertex3f(x + 0.5, 0.0, z + 0.5)
    glVertex3f(x + 0.5, 3.0, z + 0.5)

    # Right side of the post (positive x-axis)
    glNormal3f(1,0,0)
    glVertex3f(x + 0.5, 3.0, z + 0.5)
    glVertex3f(x + 0.5, 0.0, z + 0.5)
    glVertex3f(x + 0.5, 0.0, z - 0.5)
    glVertex3f(x + 0.5, 3.0, z - 0.5)

    # Back side of the post (negative z-axis)
    glNormal3f(0,0,-1)
    glVertex3f(x - 0.5, 3.0, z - 0.5)
    glVertex3f(x - 0.5, 0.0, z - 0.5)
    glVertex3f(x + 0.5, 0.0, z - 0.5)
    glVertex3f(x + 0.5, 3.0, z - 0.5)

    # Left side of the post (negative x-axis)
    glNormal3f(-1, 0, 0)
    glVertex3f(x - 0.5, 3.0, z + 0.5)
    glVertex3f(x - 0.5, 0.0, z + 0.5)
    glVertex3f(x - 0.5, 0.0, z - 0.5)
    glVertex3f(x - 0.5, 3.0, z - 0.5)

    glEnd()

def tableTop2(x1, x2, z1, z2):
    '''Draws the top part of the table.
       It has a width and depth of 8 according to the given specifications by the designer.'''

    twColorName(TW_WHITE)
    # Translate position so that the origin is at the center of the table
    glTranslatef((x1+x2)/2.0, 3.5, (z1+z2)/2.0)
    glPushMatrix()
    glScalef(x1-x2+1, 1, z1-z2-1)
    glutSolidCube(1)
    glPopMatrix()

def jweber2Table2(tablePostLeftX, tablePostRightX, tablePostTopZ, tablePostBottomZ):
    '''Draws all four table posts and the table top as well.'''

    tablePosts2(tablePostLeftX, tablePostTopZ)
    tablePosts2(tablePostRightX, tablePostTopZ)
    tablePosts2(tablePostLeftX, tablePostBottomZ)
    tablePosts2(tablePostRightX, tablePostBottomZ)
    tableTop2(tablePostRightX-1, tablePostLeftX+1, tablePostTopZ, tablePostBottomZ)

# =============== Specifications ===============

tablePostLeftX   = -3.0
tablePostRightX  = 5.0
tablePostTopZ    = -5.0
tablePostBottomZ = 5.0

# ===============================================

def display():
    twDisplayInit()
    twCamera()
    jweber2Table2(tablePostRightX, tablePostLeftX, tablePostTopZ, tablePostBottomZ)
    glFlush()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twBoundingBox(-4,6,-1,5,-8,8)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()
    
