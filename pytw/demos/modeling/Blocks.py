''' Scatters a bunch of blocks around a scene, to demonstrate the
translate-rotate-scale affine transformations.

Written by Scott D. Anderson
scott.anderson@acm.org
Fall 2003

Adapted to use Python, Fall 2009
'''

import sys

from TW import *

### ================================================================

### This program sometimes draws a block "by hand," instead of using
### the GLUT object.  The following array holds the 8 vertices. Unlike
### the GLUT object, which has the origin in the center, this block
### has the origin at one corner.  This makes scaling a little easier
### sometimes. 

vertices = (
    (0,0,0),(1,0,0),(1,1,0),(0,1,0),
    (0,0,1),(1,0,1),(1,1,1),(0,1,1)
)


def face(a, b, c, d):
    """This function draws one face of the wire cube given the indices
of the four vertices.  Since it is wire, it doesn't matter whether the
vertices are counter-clockwise, but we'll try to do that anyhow."""
    glBegin(GL_LINE_LOOP)
    glVertex3fv(vertices[a])
    glVertex3fv(vertices[b])
    glVertex3fv(vertices[c])
    glVertex3fv(vertices[d])
    glEnd()

def myCube():
    '''draws a unit cube where the reference point is the lower left
    front corner (like the barn), rather than the center.'''
    # This is a little inefficient, since every edge gets drawn twice,
    # since each edge is the boundary between two faces. However, this
    # organizes the code, generalizes to solid objects, and introduces
    # the idea of the inside and outside faces of a surface.
    face(0,1,2,3) # front
    face(7,6,5,4) # back
    face(4,5,1,0) # bottom
    face(1,5,6,2) # right
    face(0,3,7,4) # left
    face(2,6,7,3) # top


def display():
    '''An ordinary display function, drawing a succession of blocks.
Each has a different color, so that you can match up the graphic block
with the code that draws it.  For each block, try to figure out where
it is and how it looks, just by visualizing the transformations.
That's good practice for using the affine transformations in your own
modeling.'''

    twDisplayInit()
    twCamera()

    # draw ground
    twColorName(TW_BLACK)
    twGround()

    # origin
    twColorName(TW_WHITE)
    glutWireCube(1)

    # translate only
    twColorName(TW_RED)
    glPushMatrix()
    glTranslatef(2,3,4)
    glutWireCube(1)
    glPopMatrix()

    # translate and scale.  Look out below!
    twColorName(TW_GREEN)
    glPushMatrix()
    glTranslatef(4,0,5)
    glScalef(2,2,2)
    glutWireCube(1)
    glPopMatrix()

    # compensating in the translation
    twColorName(TW_BLUE)
    glPushMatrix()
    glTranslatef(8,1,1)
    glScalef(2,2,2)
    glutWireCube(1)
    glPopMatrix()

    # using a different reference point
    twColorName(TW_MAGENTA)
    glPushMatrix()
    glTranslatef(9,0,1)
    glScalef(2,2,2)
    myCube()
    glPopMatrix()

    # stacking some rotated blocks
    twColorName(TW_YELLOW)
    glPushMatrix()
    glTranslatef(1,1,8)
    glScalef(2,2,2)
    glutWireCube(1)
    glPopMatrix()

    twColorName(TW_ORANGE)
    glPushMatrix()
    glTranslatef(1,3,8)
    glRotatef(30,0,1,0)        # 30 degrees around y
    glScalef(2,2,2)
    glutWireCube(1)
    glPopMatrix()

    twColorName(TW_BROWN)
    glPushMatrix()
    glTranslatef(1,5,8)
    glRotatef(60,0,1,0)        # degrees around y
    glScalef(2,2,2)
    glutWireCube(1)
    glPopMatrix()

    # non-uniform scaling
    twColorName(TW_CYAN)
    glPushMatrix()
    glTranslatef(8,0,8)
    glRotatef(45,0,1,0)        # degrees around y
    glScalef(1,5,1)
    glutWireCube(1)
    glPopMatrix()
    
    twColorName(TW_TEAL)
    glPushMatrix()
    glTranslatef(9,0,9)
    glRotatef(45,0,1,0)        # degrees around y
    glScalef(1,5,1)
    myCube()
    glPopMatrix()

    glFlush()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(0,10,0,5,0,10)
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    # nice fat lines.  In this program, we only need to say this once
    glLineWidth(3)               
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()
