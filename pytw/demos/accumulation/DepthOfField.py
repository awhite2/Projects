"""Demonstration of jittering to achieve the depth-of-field effect

Written by Caroline Geiersbach and Scott D. Anderson
scott.anderson@acm.org
Summer 2003
Fall 2009, ported to Python
"""

try:
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
        '''
### ================================================================

def drawTeapot(x, y, z, red, green, blue):
    """Draw teapot at the location (x,y,z) with the color (red, green, blue)"""
    glPushMatrix();
    glTranslatef(x,y,z);
    twColor((red,green,blue),0.9,128.0);
    glutSolidTeapot(1);
    glPopMatrix();
    twDrawString(x-1,y-1.5,z,"(%1.0f,%1.0f,%1.0f)" % (x,y,z))

def display():
    glClear(GL_ACCUM_BUFFER_BIT);
    for jitter in range(len(twJitterTable)):
        twDisplayInit();
        #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        #focus on red object, depth = 6 (from eye at origin)
        twDepthOfFieldCamera(-3,3,-3,3,3,21,
                              twJitterTable[jitter],6,DepthOfField); 

        # teapots, arranged from near to far

        drawTeapot(4,0,-4,1,0,1);   #magenta
        drawTeapot(2,0,-5,0,0,1);   #blue
        drawTeapot(0,0,-6,1,0,0);   #red
        drawTeapot(-2,0,-7,0,1,0);  #green
        drawTeapot(-4,0,-8,1,1,0);  #yellow
        drawTeapot(-6,0,-10,0,1,1); #cyan
        glAccum(GL_ACCUM, 1.0/len(twJitterTable))
    glAccum(GL_RETURN, 1.0);
    glFlush();
    glutSwapBuffers();

# For speed, it's a good idea to keep as much out of the display function
# as possible.
def myInit():
    twMainInit();

    #lighting
    twGrayLight(GL_LIGHT0,(1,3,3,0),1,1,1)
    twAmbient(1.0);
    glLightModelf(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_FALSE);
    glEnable(GL_LIGHTING);

    #clear
    glClearColor(0,0,0,0);
    glClearAccum(0,0,0,0);


def reshape(width, height):
    glViewport(0,0,width,height)

def main():
    global DepthOfField
    if len(sys.argv) < 2:
        print "usage: %s d\nthe smaller d, the blurrier. Try 0.5 < d < 2" % (sys.argv[0])
        exit(0)
    else:
        DepthOfField = float(sys.argv[1])
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_ACCUM);
    twInitWindowSize(600,600);
    glutCreateWindow(sys.argv[0])
    glutReshapeFunc(reshape);
    glutDisplayFunc(display);
    twBoundingBox(-3,3,0,3,-3,3);
    twMainInit();
    myInit();
    glutMainLoop();

if __name__ == '__main__':
    main()
