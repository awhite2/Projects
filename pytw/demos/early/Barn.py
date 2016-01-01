## Demo of my classic barn object.  This uses two helper functions
### that improve the abstraction and brevity of the code.

### Implemented from the C++ predecessor, Fall 2009
### Scott D. Anderson
### scott.anderson@acm.org

import sys

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

def makeBarnVertexArray( w, h, len ):
    # w is the width
    # h is the height
    # len is the length
    front = [ [ 0, 0, 0 ],       # left bottom 
              [ w, 0, 0 ],       # right bottom
              [ w, h, 0 ],       # right top 
              [ 0, h, 0 ],       # left top
              [ w*0.5, h+w*0.5, 0 ] # ridge 
              ]
    # list comprehension to construct back just like front except for Z
    back = [ [v[0], v[1], -len] for v in front ]
    front.extend(back)          # NOT "append," which only adds one item, even given a list
    return front

BarnVertices = makeBarnVertexArray(30,40,50)

# The following values are only used to set up the barn vertices

def drawTri(verts, a, b, c):
    glBegin(GL_TRIANGLES)
    glVertex3fv(verts[a])
    glVertex3fv(verts[b])
    glVertex3fv(verts[c])
    glEnd()

def drawQuad(verts, a, b, c, d):
    glBegin(GL_QUADS)
    glVertex3fv(verts[a])
    glVertex3fv(verts[b])
    glVertex3fv(verts[c])
    glVertex3fv(verts[d])
    glEnd()

def drawBarn(b):
    glColor3f(1, 0, 0)
    drawQuad(b, 0, 1, 2, 3)     # front
    drawTri(b, 3, 2, 4)
    glColor3f(0, 1, 0)
    drawQuad(b, 5, 6, 7, 8)
    drawTri(b, 7, 8, 9)
    glColor3f(0.5, 0, 0.5)
    drawQuad(b, 0, 3, 8, 5)     # left side
    glColor3f(0.7, 0.19, 0.38)
    drawQuad(b, 1, 2, 7, 6)     # right side
    glColor3f(0.5, 0.5, 0)
    drawQuad(b, 3, 4, 9, 8)     # left roof
    drawQuad(b, 2, 4, 9, 7)     # right roof

def camera():
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    gluPerspective(90.0, 1, 1, 100)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity ()             # clear the matrix 
    gluLookAt(15, 27, 31,
	      15, 27, 30,
	      0, 1, 0)
    
def display():
    glClearColor(0.7, 0.7, 0.7, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glDisable(GL_LIGHTING)
    glShadeModel(GL_FLAT)

    camera()

    drawBarn(BarnVertices)
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    glEnable(GL_AUTO_NORMAL)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_NORMALIZE)
    glDepthFunc(GL_LEQUAL) 
    glutMainLoop()

if __name__ == '__main__':
    main()

