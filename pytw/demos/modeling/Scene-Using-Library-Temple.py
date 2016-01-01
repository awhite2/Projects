''' Demonstrates constructing a scene using library objects.  The scene is
not intended to be beautiful, just functional.

Written by Scott D. Anderson
scott.anderson@acm.org
Fall 2006

Adapted for Python Fall 2009
'''

import sys

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''

# This imports from the "contrib" directory, which is in the same
# directory as the "TW.py" file, wherever that is. On the Wellesley Macs,
# it's probably in ~/pytw/contrib.  On the Linux machines,
# ~cs307/pub/pytw/contrib.

print sys.path
print which('jaylmerTemple.py')

try:
  from jaylmer import jaylmerTemple
except:
  print '''
ERROR: Couldn't import jaylmer
'''

MAXBYTE = 255.0

def display():
    twDisplayInit();
    twCamera();

    # draw sky and ground, using default colors
    twGround();
    twSky();

    # Justine's temple might be nice.  This color is Slate Gray
    templeColor = ( 112/MAXBYTE, 128/MAXBYTE, 144/MAXBYTE )
    twColor(templeColor,0,0);
    glPushMatrix();
    glTranslatef(-10,0,-30);
    glRotatef(75,0,1,0);        # mostly side view
    jaylmerTemple();
    glPopMatrix();

    # draw barn
    glPushMatrix();
    glTranslatef(-40,0,-125);
    glRotatef(-90,0,1,0);
    glScalef(40,35,50);
    teal      = (0,0.5,0.5)
    dark_blue = (0,0,0.5)
    cyan      = (0,1,1)
    twSolidBarn(teal,dark_blue,cyan);
    glPopMatrix();

    glFlush();
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-50,50,0,60,-100,0);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
  main()
