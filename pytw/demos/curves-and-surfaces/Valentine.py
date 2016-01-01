""" A 2D Bezier surface looking like a valentine's day heart, built as
 part of a class exercise.  The filename is purposely obscure, so
 that, hopefully, students won't stumble onto it before they've done
 the exercise.

Written by Scott D. Anderson
scott.anderson@acm.org
Fall 2007
Fall 2009, ported to Python
"""

import sys

try:
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
        '''

### ================================================================

Wire = False
ShowControlPoints = False

### ================================================================

def heartHalfCurve( height ):
    """Draws half of the outline of the heart"""
    cp = (
        (0,0,0),                  # the dimple at the top
        (1,1,0),                  # makes the upper chamber
        (1,-height+1,0),          # heads towards the point
        (0,-height,0)             # the point of the heart
        )                  
    if ShowControlPoints:
        twDrawBezierControlPoints(cp)
    
    twDrawBezierCurve(cp,10)

def heartHalfSurface( height ):
    """Draws half of the front surface of the heart

The width of the heart is 1 (at least, its control points) and the
height, from dent to point, is determined by the argument.  The origin is
at the dent, and the point is on the negative Y axis.  The heart comes out
(along Z) by 0.5."""

    # U varies fastest through the array, V slowest.
    # Our heart curve is along V.
    f=1/-3.0;           # move down by thirds

    h=height           # shorthand

    cp = (
        # all CP come together at the dent
        ((0,0,0),
         (0,0,0),
         (0,0,0)),                  # dimple of heart curve

        ((0,h*f,0.5),
         (0.5,h*f,0.5),
         (1,1,0)),                   # second point of heart curve

        ((0,2*h*f,0.5),
         (0.5,2*h*f,0.5),
         (1,-h+1,0)),                # third point of heart curve

        ((0,-h,0),
         (0,-h,0),
         (0,-h,0))                   # fourth point of heart curve
        )
    if ShowControlPoints:
        twDrawBezierControlPoints(cp)
    
    twDrawBezierSurface(cp,16,16,GL_LINE if Wire else GL_FILL)



def heartWholeSurface( height ):
    """Same as heart half, except we do both sides with one surface.  This
gives us less control left-to-right, but is simpler."""

    # U varies fastest through the array, V slowest.
    # Our heart curve is along V.
    f=1/-3.0                   # move down by thirds

    h=height                    # shorthand

    cp = (
        # all CP come together at the dent
        ((0,0,0),
         (0,0,0),
         (0,0,0)),                  # dimple of heart curve

        ((-1,1,0),
         (0,h*f,0.5),
         (+1,1,0)),                   # second point of heart curve

        ((-1,-h+1,0),
         (0,2*h*f,0.5),
         (1,-h+1,0)),                # third point of heart curve

        ((0,-h,0),
         (0,-h,0),
         (0,-h,0))                   # fourth point of heart curve
        )
    if ShowControlPoints:
        twDrawBezierControlPoints(cp)
    
    twDrawBezierSurface(cp,16,16,GL_LINE if Wire else GL_FILL)

HeartHeight = 2

def display():
    twDisplayInit();
    twCamera();

    glPushAttrib(GL_ALL_ATTRIB_BITS);

    glColor3f(1,0,0);           # red hearts

    heartHalfCurve(HeartHeight);
    
    glPushMatrix();
    glTranslatef(2,0,0);
    heartHalfSurface(HeartHeight);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(-2,0,0);
    heartWholeSurface(HeartHeight);
    glPopMatrix();

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
    global HeartHeight
    glutInit(sys.argv)
    if len(sys.argv) > 1:
        HeartHeight = sys.argv[1]
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-3,+3,
                  -2,+0.5,
                  -1,1);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    twKeyCallback('w',toggles,"toggle wireframe");
    twKeyCallback('c',toggles,"toggle showing control points");
    glPointSize(5)
    glutMainLoop();

if __name__ == '__main__':
    main()
