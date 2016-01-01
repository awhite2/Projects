""" Simplest demo of transparency. Draws a brass teapot partially
behind a partially transparent ``screen.''

Written by Scott D. Anderson
scott.anderson@acm.org
Fall 2007
Ported to Python Fall 2009
"""

import sys
import math

try:
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
        '''

### ================================================================

ShowScreen = False

def brassTeapot():
    # Draw solid stuff, a nice brass teapot, roughly brass.  
    # I found "brass" at http://www.colourprep.com/hexColorsName.html
    brass = ( 0xB5/255.0, 0xA6/255.0, 0x42/255.0 )
    twColor(brass,0.9,20);
    glutSolidTeapot(1);

def display():
    twDisplayInit(0,0,0);
    twCamera();

    glPushAttrib(GL_ALL_ATTRIB_BITS);

    # Normal depth stuff
    glEnable(GL_DEPTH_TEST);

    # Lighting
    twGrayLight(GL_LIGHT0,(1,1,1,0),0.1,0.8,0.5);
    glEnable(GL_LIGHTING);
    glShadeModel(GL_SMOOTH);

    brassTeapot()

    if(ShowScreen):
        # switch to transparency
        glEnable(GL_BLEND);
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        glDepthMask(GL_FALSE);
        
        # Turn off lighting
        glDisable(GL_LIGHTING);
    
        # Draw a sheer green screen in front of and to one side of the teapot
        glColor4f(0,1,0,0.5);

        Z = 1.0;
        glBegin(GL_QUADS);
        glVertex3f(0,1,Z);
        glVertex3f(0,-1,Z);
        glVertex3f(1,-1,Z);
        glVertex3f(1,1,Z);
        glEnd();
    glPopAttrib();

    glFlush();
    glutSwapBuffers(); 

def keys(key, x, y):
    global ShowScreen
    if key == 's': 
        ShowScreen = not ShowScreen
    glutPostRedisplay();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    twBoundingBox(-1,1,-1,1,-1,1);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    glutDisplayFunc(display);
    twKeyCallback('s',keys,"toggle showing the screen");
    glutMainLoop();
    return 0;

if __name__ == '__main__':
    main()
