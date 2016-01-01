""" This program displays a curve looking vaguely like the outline of a
   Coke bottle.

   The bottle silhouette is three Bezier curves, with the transitions at
   the upper bulge and lower dent, since I'll assume that the tangent is
   vertical at that point.

   This version makes the control point arrays 1D, thereby eliminating a
   horrendous cast that the old version had when passing it to OpenGL.

Scott D. Anderson
April 1999 Original
Fall 2003 revised to use TW
Fall 2009 ported to Python
"""

import sys

from TW import *

### ================================================================
### Global variables, parameters and constants. 

## Upper curve, from diameter of 0.75in at height 5in to diameter of 1.5in
## at height 2.5in. 

upper_cp = ((0.5/2, 5.0, 0.0),
            (0.5/2, 4.0, 0.0),
            (1.5/2, 3.0, 0.0),
            (1.5/2, 2.5, 0.0))

## Middle curve, from upper bulge (see previous) to dent with diameter of
## 1.25in at height of 1.25in. */

middle_cp = ((1.5/2,  2.5,  0.0),
             (1.5/2,  2.0,  0.0),
             (1.25/2, 1.75, 0.0),
             (1.25/2, 1.25, 0.0))
                          
## Lower curve, from dent to base, with a radius the same as the bulge. 

lower_cp = ((1.25/2, 1.25, 0.0),
            (1.25/2, 0.75, 0.0),
            (1.5/2,  0.50, 0.0),
            (1.5/2,  0.00, 0.0))

DrawCP = False

def draw_silhouette():
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glLineWidth(3.0)
    twColorName(TW_MAGENTA)
    twDrawBezierCurve(upper_cp,8)
    twColorName(TW_CYAN)
    twDrawBezierCurve(middle_cp,10)
    twColorName(TW_BROWN)
    twDrawBezierCurve(lower_cp,8)

    # draw a single curve reflected across the x=0 plane
    twColorName(TW_RED)
    glPushMatrix()
    glScalef(-1,1,1)
    twDrawBezierCurve(upper_cp,12)
    twDrawBezierCurve(middle_cp,12)
    twDrawBezierCurve(lower_cp,12)
    if DrawCP:
        glPointSize(5)
        twDrawBezierControlPoints(upper_cp)
        twDrawBezierControlPoints(middle_cp)
        twDrawBezierControlPoints(lower_cp)
    glPopMatrix()
    glPopAttrib()

def display():
    twDisplayInit(1,1,1)
    twCamera()

    draw_silhouette()

    glFlush()
    glutSwapBuffers()

def toggleCP( key, x, y):
    global DrawCP
    DrawCP = not DrawCP
    glutPostRedisplay()

# ================================================================

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-1.5/2,1.5/2,0,5,-0.25,+0.25)
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    twKeyCallback('c',toggleCP,"toggle drawing of control points")
    glutMainLoop()

if __name__ == '__main__':
    main()

