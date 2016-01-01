'''Just throws up a torus.

Implemented Fall 2007
Scott D. Anderson

Adapted for Python Fall 2009
'''

import sys

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''

# If you slice through the torus to get a circular section, this is
# the radius of that circular cross-section.

InnerRadius = 0.5;           

# If you think of the torus as a circle, it's the radius of the circle

OuterRadius = 2.0;     

# If you slice through the torus to get a circular section, this is
# how many sides that polygonal approximation has.

Nsides = 5;               

# If you think of the torus as a polygonal approx to a circle, this is
# how many sides the polygon has.

Rings  = 3;               

def display():
    twDisplayInit();
    twCamera();

    glPushMatrix();
    glTranslatef(-OuterRadius,0,0); # move left
    glutSolidTorus(InnerRadius,OuterRadius,Nsides,Rings);
    glTranslatef(OuterRadius*2.0,0,0); # move right
    glutWireTorus(InnerRadius,OuterRadius,Nsides,Rings);
    glPopMatrix();

    glFlush();
    glutSwapBuffers();

def keys(key, x, y):
    global Nsides, Rings, InnerRadius, OuterRadius
    if key == 'n':
        Nsides -= 1
    elif key == 'N':
        Nsides += 1
    elif key == 'r':
        Rings -= 1
    elif key == 'R':
        Rings += 1
    elif key == 'i':
        InnerRadius -= 0.1
    elif key == 'I':
        InnerRadius += 0.1
    elif key == 'o':
        OuterRadius -= 0.1
    elif key == 'O':
        OuterRadius += 0.1
    glutPostRedisplay();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-5,5,-5,5,-5,5);  # 10x10x10 cube around origin
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    twKeyCallback('n',keys,"decrease Nsides");
    twKeyCallback('N',keys,"increase Nsides");
    twKeyCallback('r',keys,"decrease Rings");
    twKeyCallback('R',keys,"increase Rings");
    twKeyCallback('i',keys,"decrease InnerRadius");
    twKeyCallback('I',keys,"increase InnerRadius");
    twKeyCallback('o',keys,"decrease OuterRadius");
    twKeyCallback('O',keys,"increase OuterRadius");
    glutMainLoop()

if __name__ == '__main__':
  main()
