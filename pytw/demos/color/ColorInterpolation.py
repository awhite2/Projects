### Demo of color interpolation.  Each vertex of the triangle has a
### different color, and by turning on smooth shading, the interior
### pixel colors are interpolated.

### Implemented Fall 2005
### Modified to remove the Quad, Fall 2006
### Ported to Python, Fall 2009

### Scott D. Anderson
### scott.anderson.@acm.org

import sys

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''

Tri = ( (0,0,0),
        (3,-2,-1),
        (1,4,0)
        )

Colors = ( (1,0,0),             # red
           (1,0,1),             # magenta
           (1,1,0)              # yellow
           )
        
def drawVertex(index):
    '''Sends a vertex and its associated color down the pipeline

A simple convenience to shorten the code and guarantee that the same
color is always associated with each vertex.  Notice that the color is
given *before* the vertex.'''
    glColor3fv(Colors[index])
    glVertex3fv(Tri[index])

def drawTri():
    '''Draw a triangle'''
    glBegin(GL_TRIANGLES);
    drawVertex(0);
    drawVertex(1);
    drawVertex(2);
    glEnd();

def display():
    twDisplayInit();
    twCamera();

    ## glShadeModel(GL_SMOOTH);
    drawTri();

    glFlush();
    glutSwapBuffers();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(0,3,-2,4,-1,0)
    twInitWindowSize(500,300)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
  main()
