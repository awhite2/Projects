### Implemented from the C++ predecessor, Fall 2009
### Scott D. Anderson
### scott.anderson@acm.org

import sys

from TW import *

points = (
    (0,0,0),
    (1,0,0),
    (2,1,0),
    (3,3,1),
    (3,3,3),
    (2,4,2),
    (0,5,1),
    (-1,6,-2)
    )

def drawPicture():
    glLineWidth(2)
    glBegin(GL_TRIANGLES)

    twColorName(TW_RED)
    glVertex3fv(points[0])
    glVertex3fv(points[1])
    glVertex3fv(points[2])

    twColorName(TW_GREEN)
    glVertex3fv(points[3])
    glVertex3fv(points[4])
    glVertex3fv(points[5])

    twColorName(TW_BLUE)
    glVertex3fv(points[6])
    glVertex3fv(points[7])
    glVertex3fv(points[0])

    glEnd()

def display():
    twDisplayInit()
    twCamera()

    drawPicture()

    glFlush()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(500,500)
    twVertexArray(points)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()

