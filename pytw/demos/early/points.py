''' Just draws points 

Implemented Fall 2006
Scott D. Anderson
'''

import sys

from TW import *

points = [ [0,0,0],
           [1,0,0],
           [2,1,0],
           [3,3,1],
           [3,3,3],
           [2,4,2],
           [0,5,1],
           [-1,6,-2]]

def drawPicture():
    glPointSize(5)
    glBegin(GL_POINTS)

    twColorName(TW_RED)
    glVertex3fv(points[0])

    twColorName(TW_GREEN)
    glVertex3fv(points[1])

    twColorName(TW_BLUE)
    glVertex3fv(points[2])

    twColorName(TW_YELLOW)
    glVertex3fv(points[2])
    
    twColorName(TW_CYAN)
    glVertex3fv(points[3])

    twColorName(TW_MAGENTA)
    glVertex3fv(points[4])

    twColorName(TW_MAROON)
    glVertex3fv(points[5])

    twColorName(TW_TEAL)
    glVertex3fv(points[6])

    twColorName(TW_OLIVE)
    glVertex3fv(points[7])

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
    twVertexArray(points) # set up the bounding box
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)    # register the callback
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()
