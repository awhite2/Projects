'''Demo of a two-sided triangle, to show the effect of "winding order."
Uses interpolated lines to show the direction.

Spring 2012
D. Anderson
anderson@acm.org
'''

import sys
from TW import *

FrontColor = (0,1,1)
BackColor = (1,1,0)

# ================================================================

Triangle = [ [ 0.5, 1, 0 ],
             [ 0, 0, 0 ],
             [ 1, 0, 0 ] ]

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
    twColor(FrontColor,0,0)
    glBegin(GL_TRIANGLES)
    glVertex3fv(verts[a])
    glVertex3fv(verts[b])
    glVertex3fv(verts[c])
    glEnd()
    glPushAttrib(GL_CURRENT_BIT)
    twColor(BackColor,0,0)
    ## in opposite winding order
    glBegin(GL_TRIANGLES)
    glVertex3fv(verts[c])
    glVertex3fv(verts[b])
    glVertex3fv(verts[a])
    glEnd()
    glPopAttrib()

def draw_triangle(location):
    glPushMatrix()
    glTranslatef(*location)
    # the oriented lines is CCW from the *front* 
    draw_oriented_line(Triangle,0,1)
    draw_oriented_line(Triangle,1,2)
    draw_oriented_line(Triangle,2,0)
    draw_triangle_two_sided(Triangle,0,1,2)
    glPopMatrix()

# ================================================================

A = (0,0,0)
B = (1,0,0)
C = (1,1,0)
D = (0,1,0)

def draw_unit_quad_twosided(location):
    glPushMatrix()
    glTranslatef(*location)
    glBegin(GL_QUADS)
    twColor(FrontColor,0,0)
    ## CCW from origin
    glVertex3fv(A)
    glVertex3fv(B)
    glVertex3fv(C)
    glVertex3fv(D)
    twColor(BackColor,0,0)
    glVertex3fv(A)
    glVertex3fv(D)
    glVertex3fv(C)
    glVertex3fv(B)
    glEnd()
    glPopMatrix()

Wire = False

def bezier_unit_quad_twosided(location):
    glPushMatrix()
    glTranslatef(*location)
    twColor(FrontColor,0,0)
    twDrawBezierSurface([[A,B],[D,C]],
                        10,10,
                        GL_LINE if Wire else GL_FILL)
    twColor(BackColor,0,0)
    twDrawBezierSurface([[B,A],[C,D]],
                        10,10,
                        GL_LINE if Wire else GL_FILL)
    glPopMatrix()

# ================================================================

def display():
    twDisplayInit(0.7, 0.7, 0.7)
    twCamera()

    draw_triangle((1,0,0))
    draw_unit_quad_twosided((0,0,0))
    bezier_unit_quad_twosided((2,0,0))

    glFlush()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(500,500)
    twBoundingBox(0,3,0,1,-0.1,0.1)
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

