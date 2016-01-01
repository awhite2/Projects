''' Two figures, one with smooth shading and one with flat.

Written by Scott D. Anderson
scott.anderson@acm.org
Fall 2003

Fall 2009, ported to Python
'''

from TW import *

## ================================================================

def blueball(radius):
    '''Draws a plain blue ball of given radius'''
    S = 16                       # slices and stacks
    cornflower = (100.0/255, 149.0/255, 237.0/255)
    twColor(cornflower, 0.7, 10);
    glPushMatrix();
    glTranslatef(+1,0,0);
    glutSolidSphere(radius,S,S);
    glPopMatrix();
  
def blueballat(radius,height):
    '''Draws a plain blue ball of given radius at given height (y-axis)'''
    # this check isn't really necessary because of the way we compute the
    # height, but still...
    ypos = height if height > radius else radius
    glPushMatrix()
    glTranslatef(0,ypos,0)
    blueball(radius)
    glPopMatrix()

BallRadius = 1
BallHeight = 8                  # of the center

BallBouncePeriod = 3            # in whatever units Time is measured in

MaxBallHeight = 8               # of the center

Time = 0
DeltaT = 0.1

# With a ball bounce period of 3 and a DeltaT of 0.1, it will be 30 frames
# between bounces.

def linearMap(x,minx,maxx,miny,maxy):
    '''Transforms x from [minx,maxx] to y in [miny,maxy]'''
    # t is in [0,1]
    t = (x-minx)/float(maxx-minx)
    y = t*(maxy-miny)+miny
    return y

def updatePosition():
    global Time, BallHeight
    Time += DeltaT
    # rescale the Time dimension so that P, the period of bouncing, maps to pi
    angle = float(Time) * M_PI / BallBouncePeriod 
    abs_cos = abs(math.cos(angle))
    BallHeight = linearMap(abs_cos,0,1,BallRadius,MaxBallHeight)
    glutPostRedisplay()

def display():
    twDisplayInit();
    twCamera();
    lightPos = ( 2, 2, 2, 0 )
    twGrayLight(GL_LIGHT0,lightPos,0.2,0.8,0.8);
    glEnable(GL_LIGHTING);
    glShadeModel(GL_SMOOTH);

    twColor((0.13,0.55,0.13),0,0) # ground is not specular or shiny
    twGround()
    blueballat(BallRadius,BallHeight)
      
    glFlush();
    glutSwapBuffers();

Animating = False

def keys(key,x,y):
    global Time, BallHeight, Animating
    if key == '0':
        Time = 0
        BallHeight = MaxBallHeight
        glutPostRedisplay()
    elif key == '1':
        updatePosition()
        print BallHeight
    elif key == '2':
        Animating = not Animating
        glutIdleFunc(updatePosition if Animating else None)

def main():
    global DeltaT
    glutInit(sys.argv)
    if len(sys.argv) > 1:
        DeltaT = float(sys.argv[1])
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-2, +2,
                   0, MaxBallHeight + BallRadius,
                   -2, +2)
    twInitWindowSize(300,500);
    glutCreateWindow(sys.argv[0])
    twMainInit()
    glutDisplayFunc(display)
    twKeyCallback('0',keys,"reset animation")
    twKeyCallback('1',keys,"one step")
    twKeyCallback('2',keys,"toggle animation")
    glutMainLoop()

if __name__ == '__main__':
    main()
