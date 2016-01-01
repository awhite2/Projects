"""Demonstration of motion blur: teapot falling off a table.  This
   rendering uses increasingly larger coefficients, so that the later
   images are stronger.  Unfortunately, the first image nearly disappears,
   even when there are only three frames.
   
Written by Caroline Geiersbach and Scott D. Anderson
scott.anderson@acm.org
Summer 2003

Fall 2004, Added callbacks to increase/decrease NumFrames.
Fall 2009 ported to Python
"""

try:
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
        '''

### ================================================================

UseAccum = False
Small = False

def drawScene(teapotParameter):
    """Draws a teapot falling off a parson's table.

The parameter is used to compute the position of the teapot.  It should
be in the range 0-1."""
    glEnable(GL_LIGHTING);
    glShadeModel(GL_SMOOTH);

    print "parameter = ",teapotParameter

    # this is saddle brown, according to rgb.txt
    tableColor = (139/255.0, 69/255.0, 19/255.0)
    twColor(tableColor,0.5,5)
    drawTable(10,8,10,1,1)      # 10x10 table, 8 units high

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


def display1():
    """This display function is the "ordinary" one.  It draws the scene
NumFrames times, but doesn't play any tricks with the accumulation
buffer."""
    twDisplayInit(0,0,0);
    twCamera();
    print ""
    for frame in range(NumFrames):
        # this parameter will be 0-1
        drawScene(float(frame)/float(NumFrames-1));
    glFlush();
    glutSwapBuffers();


def displayN():
    """This display function is the one for motion blur.  It draws the
scene NumFrames times, summing them using the accumulation buffer.
The sum is a weighted sum, where the weights add to one and increase
linearly."""

    # Clear the accumulation buffer.  Clearing it to other values has
    # bizarre effects, so always clear to zero, at least if you're using
    # GL_ACCUM
    glClearAccum(0,0,0,0);
    glClear(GL_ACCUM_BUFFER_BIT);
    print ""
    for frame in range(NumFrames):
        # this function clears the color and depth buffers
        twDisplayInit(0,0,0);        
        #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        twCamera();
        drawScene(float(frame)/float(NumFrames-1));
        # copy the scene into the accumulation buffer, multiplying it by
        # this fraction.  This means the most recent frame is strongest.
        glAccum(GL_ACCUM, float(frame+1)/float(SummationTotal));
    # copy the scene from the accumulation buffer into the color buffer
    glAccum(GL_RETURN, 1.0);
    glFlush();
    glutSwapBuffers();

def keys(key, x, y):
    global UseAccum, Small, NumFrames, SummationTotal
    if key == 'm': 
        UseAccum = not UseAccum
        if UseAccum:
            glutDisplayFunc(displayN);
        else:
            glutDisplayFunc(display1);
    elif key == 's': 
        Small = not Small
    elif key == '+': 
        NumFrames += 1
        SummationTotal = NumFrames*(NumFrames+1)/2
    elif key == '-':
        if NumFrames>2:
            NumFrames -= 1
            SummationTotal = NumFrames*(NumFrames+1)/2;
    glutPostRedisplay();

def myInit():
    twBoundingBox(0,12,0,8,0,10);
    twMainInit();

    twGrayLight(GL_LIGHT0, (13,13,13,1), 0.3,0.8,0.8);
    twAmbient(1.0);
    glLightModelf(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE);
    glEnable(GL_LIGHT0);

    twKeyCallback('m',keys,"toggle motion blur");
    twKeyCallback('s',keys,"toggle small motion");
    twKeyCallback('+',keys,"increase frames");
    twKeyCallback('-',keys,"decrease frames");

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_ACCUM);
    twInitWindowSize(600,600);
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display1)
    myInit();
    glutMainLoop();

if __name__ == '__main__':
    main()
