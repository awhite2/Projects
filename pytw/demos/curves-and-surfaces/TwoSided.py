'''Demo of a two-sided triangle, to show the effect of "winding order."
Uses interpolated lines to show the direction.

Spring 2012
D. Anderson
anderson@acm.org
'''

import sys
from TW import *

Triangle = [ [ 1, 2, 1 ],
             [ 0, 0, 1 ],
             [ 2, 0, 1 ] ]

def draw_oriented_line(verts, a, b):
    glLineWidth(7)
    glShadeModel(GL_SMOOTH)
    glBegin(GL_LINES)
    twColorName(TW_GREEN)
    glVertex3fv(verts[a])
    twColorName(TW_RED)
    glVertex3fv(verts[b])
    glEnd()

def draw_triangle_two_sided(verts, a, b, c):
    twColorName(TW_YELLOW)
    glBegin(GL_TRIANGLES)
    glVertex3fv(verts[a])
    glVertex3fv(verts[b])
    glVertex3fv(verts[c])
    glEnd()
    glPushAttrib(GL_CURRENT_BIT)
    twColorName(TW_BLUE)
    ## in opposite winding order
    glBegin(GL_TRIANGLES)
    glVertex3fv(verts[c])
    glVertex3fv(verts[b])
    glVertex3fv(verts[a])
    glEnd()
    glPopAttrib()

def display():
    twDisplayInit(0.7, 0.7, 0.7)
    twCamera()

    # the oriented lines is CCW from the *front* 
    draw_oriented_line(Triangle,0,1)
    draw_oriented_line(Triangle,1,2)
    draw_oriented_line(Triangle,2,0)
    draw_triangle_two_sided(Triangle,0,1,2)

    glFlush()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(500,500)
    twBoundingBox(0,2,0,2,0,2)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    glCullFace(GL_BACK)         # the default
    glFrontFace(GL_CCW)         # the default
    glEnable(GL_CULL_FACE)      # usually disabled
    glutMainLoop()

if __name__ == '__main__':
    main()

