""" This program displays a funky curve through the unit cube.  This
   program aims to be as simple as possible.

Scott D. Anderson
Fall 2003
Fall 2009, ported to Python
"""

import sys
from TW import *

### ================================================================

ShowControlPoints = False

def draw_funky_curve():
    curveCP = ((-1,-1,-1,),
               (+0.7,-1,-1),
               (1,-0.7,1),
               (1,1,1))

    glPushAttrib(GL_ALL_ATTRIB_BITS);
    if ShowControlPoints:
        glPointSize(5)
        twColorName(TW_CYAN)
        glBegin(GL_POINTS)
        for cp in curveCP:
            glVertex3fv(cp)
        glEnd()

    glLineWidth(3)
    twColorName(TW_YELLOW)
    twDrawBezierCurve(curveCP,8)
    glPopAttrib()

def display():
    twDisplayInit()
    twCamera()

    draw_funky_curve()

    glFlush()
    glutSwapBuffers()

def toggles(key, x, y):
    global ShowControlPoints
    ShowControlPoints = not ShowControlPoints
    glutPostRedisplay()

# ================================================================

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-1,+1,-1,+1,-1,+1)
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    twKeyCallback('c',toggles,"toggle showing control points")
    glutMainLoop()

if __name__ == '__main__':
    main()
