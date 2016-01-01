''' Demo of my classic barn object.  This uses two helper functions that
improve the abstraction and brevity of the code.

Implemented from the C++ predecessor, Fall 2009
Scott D. Anderson
scott.anderson@acm.org
'''

import sys

from TW import *

def makeBarnVertexArray( w, h, len ):
    '''Creates and returns an array of vertices for the barn.
w is the width, h is the height, len is the length'''
    front = [ [ 0, 0, 0 ],       # left bottom 
              [ w, 0, 0 ],       # right bottom
              [ w, h, 0 ],       # right top 
              [ 0, h, 0 ],       # left top
              [ w*0.5, h+w*0.5, 0 ] # ridge 
              ]
    # list comprehension to construct back just like front except for Z
    back = [ [v[0], v[1], -len] for v in front ]
    # NOT "append," which only adds one item, even given a list
    front.extend(back)          
    return front

# Global variable to hold the vertex array, initialized when this file loads

BarnVertices = makeBarnVertexArray(30,40,50)

# =====================================================================
# Two useful helper functions.  Probably general enough to move to a
# library like TW, but that hides too much for this early demo.

def drawTri(verts, a, b, c):
    '''Draw a triangle, given an vertex array and three indices into it,
in counter-clockwise (CCW) order'''
    glBegin(GL_TRIANGLES)
    glVertex3fv(verts[a])
    glVertex3fv(verts[b])
    glVertex3fv(verts[c])
    glEnd()

def drawQuad(verts, a, b, c, d):
    '''Draw a quad, given an vertex array and four indices into it,
in CCW order'''
    glBegin(GL_QUADS)
    glVertex3fv(verts[a])
    glVertex3fv(verts[b])
    glVertex3fv(verts[c])
    glVertex3fv(verts[d])
    glEnd()

# ================================================================

def drawBarn(b):
    '''draws the barn, given an array of its vertices'''
    twColorName(TW_RED)
    drawQuad(b, 0, 1, 2, 3)     # front
    drawTri(b, 3, 2, 4)
    twColorName(TW_GREEN)
    drawQuad(b, 5, 6, 7, 8)
    drawTri(b, 7, 8, 9)
    twColorName(TW_PURPLE)
    drawQuad(b, 0, 3, 8, 5)     # left side
    twColorName(TW_MAROON)
    drawQuad(b, 1, 2, 7, 6)     # right side
    twColorName(TW_OLIVE)
    drawQuad(b, 3, 4, 9, 8)     # left roof
    drawQuad(b, 2, 4, 9, 7)     # right roof

# ================================================================
# a callback function, to draw the scene, as necessary

def display():
    twDisplayInit(0.7, 0.7, 0.7) # clear background to 70% gray
    twCamera()                   # set up the camera

    drawBarn(BarnVertices)      # draw the barn

    glFlush()                   # clear the graphics pipeline
    glutSwapBuffers()           # make this the active framebuffer

# ================================================================

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(500,500)
    twVertexArray(BarnVertices) # set up the bounding box
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)    # register the callback
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()
