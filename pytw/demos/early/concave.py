''' Demo of a concave quad.

Scott D. Anderson
scott.anderson@acm.org
'''

import sys

from TW import *

Chevron = ( (-5, 0, 0),
            (0, -2, 0),
            (-2, 0, 0),
            (0, 2, 0))

Chevron_flipped = [ (-x,y,z) for x,y,z in Chevron ]

# =====================================================================
# Two useful helper functions.  Probably general enough to move to a
# library like TW, but that hides too much for this early demo.

def drawTri(verts, a, b, c):
    '''Draw a triangle, given an vertex array and three indices into it, in CCW order'''
    glBegin(GL_TRIANGLES)
    glVertex3fv(verts[a])
    glVertex3fv(verts[b])
    glVertex3fv(verts[c])
    glEnd()

def drawQuad(verts, a, b, c, d):
    '''Draw a quad, given an vertex array and four indices into it, in CCW order'''
    glBegin(GL_QUADS)
    glVertex3fv(verts[a])
    glVertex3fv(verts[b])
    glVertex3fv(verts[c])
    glVertex3fv(verts[d])
    glEnd()

# ================================================================
# a callback function, to draw the scene, as necessary

def display():
    twDisplayInit(0.7, 0.7, 0.7) # clear background to 70% gray
    twCamera()                   # set up the camera

    twColorName(TW_GREEN)
    glBegin(GL_TRIANGLES)
    glVertex3fv(Chevron[0])
    glVertex3fv(Chevron[1])
    glVertex3fv(Chevron[2])
    # next triangle
    glVertex3fv(Chevron[2])
    glVertex3fv(Chevron[3])
    glVertex3fv(Chevron[0])
    glEnd()

    twColorName(TW_BLACK)
    glBegin(GL_LINE_LOOP)
    for v in Chevron:
        glVertex3fv(v)
    glEnd()

    twColorName(TW_RED)
    glBegin(GL_QUADS)
    for v in Chevron_flipped:
        glVertex3fv(v)
    glEnd()
    
    twColorName(TW_BLACK)
    glBegin(GL_LINE_LOOP)
    for v in Chevron_flipped:
        glVertex3fv(v)
    glEnd()


    glFlush()                   # clear the graphics pipeline
    glutSwapBuffers()           # make this the active framebuffer

# ================================================================

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(500,500)
    twBoundingBox(-5,5,-2,2,-1,1)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)    # register the callback
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()
