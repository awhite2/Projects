"""Demonstration of using the accumulation buffer to speed up a animation.
The idea is to draw the static parts of the scene once, and copy them to the accumlation buffer.  Then, when animation, just copy *from* the accumlation buffer for the static stuff, and then draw the moving stuff.  
   
Written by Scott D. Anderson
scott.anderson@acm.org
May 2012
"""

from TW import *

### ================================================================

UseAccum = False
Small = False

def drawStaticStuff():
    # this is saddle brown, according to rgb.txt
    tableColor = (139/255.0, 69/255.0, 19/255.0)
    twColor(tableColor,0.5,5)
    drawTable(10,8,10,1,1)      # 10x10 table, 8 units high
    # put a very detailed sphere on the table, to consume
    # computation time
    glPushMatrix()
    glTranslate(5,11,5)
    ballColor = (0.33, 0.42, 0.18) # dark olive green
    twColor(ballColor,1,5)
    glutSolidSphere(3,80,80)    # lots of slices/stacks
    glPopMatrix()

def drawTeapot(teapotParameter):
    """Draws a teapot falling off a parson's table.

The parameter is used to compute the position of the teapot.  It should
be in the range 0-1."""

    glPushMatrix();
    # falling teapot is to the left of the table (x=11), near the front
    # legs (z=9). The parameter interpolates between the following
    # heights
    if Small:
        height0 = 4.2;          # start height
        height1 = 4.5;          # end height
    else:
        height0 = 7.5;
        height1 = 3.5;
    # Interpolate the height between height0 and height1
    glTranslatef(12, height0+teapotParameter*(height1-height0), 9);

    # falling teapot is rotating around the z axis.  
    if Small:
        angle0=-60;             # start angle
        angle1=-64;             # end angle
    else:
        angle0 = -20;
        angle1 = -60;
    # Interpolate between angle0 and angle1
    glRotatef(angle0+teapotParameter*(angle1-angle0), 0,0,1);

    # this color is royal blue, according to rgb.txt
    teapotColor = (65/255.0, 105/255.0, 255/255.0)
    twColor(teapotColor,0.8,32);

    glutSolidTeapot(1);
    glPopMatrix();


NumFrames = 3                   # draw this many frames
SummationTotal = NumFrames*(NumFrames+1)/2


def displayStatic():
    """This display function draws the static stuff and then copies it to
    the accumulation buffer."""
    twDisplayInit(0,0,0);
    twCamera();
    myInit()
    drawStaticStuff()
    # copy to accum buffer
    glClearAccum(0,0,0,0)
    glClear(GL_ACCUM_BUFFER_BIT)
    glAccum(GL_ACCUM, 1.0)
    glFlush()
    glutSwapBuffers()


def displayMoving():
    """This display function is the one for the animation.  It copies the
static scene from the accumulation buffer, then draws the moving
objects."""
    twDisplayInit(0,0,0);
    twCamera();
    myInit()
    # copy the scene from the accumulation buffer into the color buffer
    glAccum(GL_RETURN, 1.0);
    # Now, draw the moving things
    drawTeapot(TeapotParameter)
    glFlush();
    glutSwapBuffers();

def displayNormal():
    twDisplayInit(0,0,0);
    twCamera();
    myInit()
    drawStaticStuff()
    drawTeapot(TeapotParameter)
    glFlush()
    glutSwapBuffers()


TeapotParameter = 0.0

def moveStuff():
    global TeapotParameter
    TeapotParameter += 0.01
    glutPostRedisplay()

def keys(key, x, y):
    global TeapotParameter
    if key == '1':
        glutDisplayFunc(displayNormal)
    if key == '2':
        glutDisplayFunc(displayStatic)
    if key == '3':
        glutDisplayFunc(displayMoving)
    if key == '0':
        TeapotParameter = 0.0
        glutIdleFunc(None)
    if key == 'A':
        glutIdleFunc(moveStuff)
    glutPostRedisplay();

def myInit():
    twGrayLight(GL_LIGHT0, (13,13,13,1), 0.3,0.8,0.8);
    twAmbient(1.0);
    glLightModelf(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE);
    glEnable(GL_LIGHT0);
    glEnable(GL_LIGHTING);
    glShadeModel(GL_SMOOTH);

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_ACCUM);
    twInitWindowSize(600,600);
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(displayNormal)
    twBoundingBox(0,12,0,8,0,10);
    twMainInit();
    twKeyCallback('1',keys,"normal display");
    twKeyCallback('2',keys,"static display");
    twKeyCallback('3',keys,"static+moving display");
    twKeyCallback('0',keys,"reset animation");
    twKeyCallback('A',keys,"start animation");
    glutMainLoop();

if __name__ == '__main__':
    main()
