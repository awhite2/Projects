### Displays a sphere and allows you to change the stacks and slices.

### Written by Scott D. Anderson
### scott.anderson@acm.org
### Fall 2003
### Adapted to use python Fall 2009

import sys

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''
### ================================================================

Radius = 5                      # size of the sphere
Stacks = 4
Slices = 4
Wire = True               	# when true, draw a wire-frame figure.
                                # Controlled by a key callback.

def display():
    twDisplayInit()
    twCamera()

    twColorName(TW_BLUE);
    if Wire:
        glutWireSphere(Radius,Slices,Stacks)
    else:
        glutSolidSphere(Radius,Slices,Stacks)
    glFlush()
    glutSwapBuffers()

def adjust(key, x, y):
    global Slices, Stacks, Wire
    if key == '1':
        Slices += 1
    elif key == '2':
        Slices -= 1
    elif key == '3':
        Stacks += 1
    elif key == '4':
        Stacks -= 1
    elif key == 'w':
        Wire = not Wire
    elif key == 'p':
        print "Stacks is %d and Slices is %d" % (Stacks,Slices)
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-Radius,Radius,-Radius,Radius,-Radius,Radius)
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    twKeyCallback('1',adjust,"More Slices");
    twKeyCallback('2',adjust,"Fewer Slices");
    twKeyCallback('3',adjust,"More Stacks");
    twKeyCallback('4',adjust,"Fewer Stacks");
    twKeyCallback('p',adjust,"print Slices and Stacks values");
    twKeyCallback('w',adjust,"toggle wireframe mode");
    glutMainLoop()

if __name__ == '__main__':
  main()
