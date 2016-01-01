''' Just draws, using a variety of modes

Implemented Spring 2012
Scott D. Anderson
'''

import sys

from TW import *

# a set of colors to use
colors = [ TW_RED,
           TW_GREEN,
           TW_BLUE,
           TW_YELLOW,
           TW_CYAN,
           TW_MAGENTA,
           TW_MAROON,
           TW_TEAL,
           TW_OLIVE ]

# this set of points is all in a 0-9 bounding box
points = [ [0,5,5],   # center of left side
           [5,0,5],   # center of bottom
           [9,5,5],   # center of right side
           [5,9,5],   # center of top
           [5,5,0],   # center of back
           [5,5,9],   # center of front
           [9,0,0],   # back bottom corner
           [9,9,0]]   # back top corner

drawing_modes = [GL_POINTS, GL_LINES, GL_LINE_STRIP, GL_LINE_LOOP,
                 GL_TRIANGLES, GL_TRIANGLE_FAN, GL_QUADS ]

# which drawing mode is in force
drawing_mode = 0

def drawPicture():
    glPointSize(5)
    glLineWidth(3)
    # always show the points
    if drawing_mode > 0:
        twColorName(TW_BROWN)
        glBegin(GL_POINTS)
        for p in points:
            glVertex3fv(p)
        glEnd()
    # Now, do what the user wanted
    glBegin( drawing_modes[drawing_mode] )
    for i in range(len(points)):
        twColorName(colors[i])
        glVertex3fv(points[i])
    glEnd()


def display():
    twDisplayInit()
    twCamera()

    drawPicture()

    glFlush()
    glutSwapBuffers()

def main():
    if len(sys.argv) == 1:
        print 'Usage: ', sys.argv[0], ' mode number [0-6]'
        sys.exit()
    global drawing_mode
    try:
        drawing_mode = int(sys.argv[1])
    except:
        print 'Usage: ', sys.argv[0], ' mode number [0-6]'
        sys.exit()
    if drawing_mode > 6:
        print 'Usage: ', sys.argv[0], ' mode number [0-6]'
        sys.exit()
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
