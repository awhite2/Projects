""" A 2D Bezier surface, with 2x3 control points. 

Written by Scott D. Anderson
scott.anderson@acm.org
Fall 2007

Fall 2009 ported to Python
"""

import sys

try:
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
        '''

### ================================================================

Wire = True
ShowControlPoints = True

### ================================================================
"""
   A control-point array for a Bezier patch.  This is flat (all Z
   components are zero), and symmetrical across both X and Y.  The corners
   form an 8x4 rectangle.  
"""

control_points = (
    ((-4, +2, 0),
     (0, 0, 0),
     (+4, +2, 0)),

    ((-4, -2, 0),
     (0, 0, 0),
     (+4, -2, 0)))

def display():
    twDisplayInit();
    twCamera();

    glPushAttrib(GL_ALL_ATTRIB_BITS);

    glColor3f(0,1,0)            # green patch

    if ShowControlPoints:
        glPointSize(5)
        twDrawBezierControlPoints(control_points)

    # the u dimension is the "outer" one, which in this case is linear
    # the v dimension is the "inner" one, which in this case is quadratic
    twDrawBezierSurface(control_points,2,10,
                        GL_LINE if Wire else GL_FILL)

    glPopAttrib();
    glFlush();
    glutSwapBuffers();

def toggles(key, x, y):
    global Wire, ShowControlPoints
    if key == 'w': 
        Wire = not Wire
    elif key == 'c': 
        ShowControlPoints = not ShowControlPoints
    glutPostRedisplay();

# ================================================================

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-4,+4,
                  -2,+2,
                  -1,1);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    twKeyCallback('w',toggles,"toggle wireframe");
    twKeyCallback('c',toggles,"toggle showing control points");
    glutMainLoop();

if __name__ == '__main__':
    main()
