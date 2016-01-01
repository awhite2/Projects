""" Displays a picture with and without aliasing using jittering to achieve
smooth edges on the picture without aliasing.    

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
try:
  from OpenGL.constant import Constant
except:
  print '''
ERROR: Couldn't import OpenGL.constant
'''

### ================================================================

# figure options, using PyOpenGL's fancy Constant class, just for fun
BEAR = Constant('BEAR', 1)
TEAPOT = Constant('TEAPOT', 2)
ICOSAHEDRON = Constant('ICOSAHEDRON', 3)

menuNum = TEAPOT

#window values
GAP=35
wWidth = 400;
wHeight = 400; 
mainWidth = wWidth*2+GAP*3;
mainHeight = wHeight+GAP*2;

#values for the frustums (frusta?)
near = 3.0;
far = 21.0;
left = -3.0;
right = 3.0;
bottom = -3.0;
top = 3.0;

def myCamera():
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glFrustum(left,right,bottom,top,near,far);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

def lighting():
    twGrayLight(GL_LIGHT0,(1,1,1,0),0.1, 0.8, 1.0)
    glShadeModel(GL_SMOOTH);
    twAmbient(0.3);
    glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER,GL_TRUE);
    glEnable(GL_LIGHTING);

#parent window
def mainDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    #set up camera
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0,mainWidth,mainHeight,0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    twDisplayInit();
    glDisable(GL_LIGHTING);
    glColor3f(0,0,0);
    twSetFont("helvetica", 18);
    twDrawString2(GAP,25,"Original image");
    twDrawString2(GAP*2+wWidth, 25, "Image after antialiasing");
    glEnable(GL_LIGHTING);
    glutSwapBuffers();

def drawObject():
    glPushMatrix();
    if menuNum == BEAR:
        glTranslatef(0,0,-4);
        glScalef(6,6,6);
        twTeddyBear();
    elif menuNum == TEAPOT:
        twColor((1,0,0), 0.7, 128);
        glTranslatef(0,0,-5.5);
        glRotatef(25,1,0,0);
        glScalef(2.5,2.5,2.5);
        glutSolidTeapot(1);
    elif menuNum == ICOSAHEDRON:
        twColor((0,0,1), 0.9, 128);
        glTranslatef(0,0,-6.5);
        glRotatef(90,1,0,0);
        glScalef(3.5,3.5,3.5);
        glutSolidIcosahedron();
        #glutWireIcosahedron();
    glPopMatrix();

def jaggedDisplay():
    """displays image without antialiasing"""
    myCamera();
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    drawObject();
    glFlush();
    glutSwapBuffers();

def smoothDisplay():
    """displays image with antialiasing"""
    glClear(GL_ACCUM_BUFFER_BIT);
    print ""
    for j in range(NumJitters):
        jitter = twJitterTable[j % len(twJitterTable)]
        twAntiAliasingFrustum(left,right,bottom,top,near,far,
                              jitter[0],jitter[1],
                              True)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        drawObject();
        glAccum(GL_ACCUM, 1.0/NumJitters)
    glAccum(GL_RETURN, 1.0);
    glFlush();
    glutSwapBuffers();

def redisplayAll():
    glutSetWindow(leftWin);
    glutPostRedisplay();
    glutSetWindow(rightWin);
    glutPostRedisplay();

def menuCallback(id):
    global menuNum
    glutDestroyMenu(rightMenu);
    myMenu();
    menuNum = id;
    redisplayAll();

def myMenu():
    global rightMenu
    rightMenu = glutCreateMenu(menuCallback);
    glutAddMenuEntry("Teddybear", int(BEAR));
    glutAddMenuEntry("Teapot", int(TEAPOT));
    glutAddMenuEntry("Icosahedron", int(ICOSAHEDRON));
    glutAttachMenu(GLUT_RIGHT_BUTTON);

def reshape(width, height):
    glViewport(0,0,width, height)

def myInit():
    glutReshapeFunc(reshape);
    twBoundingBox(-3,3,-3,3,-3,3);
    twMainInit();
    lighting();
    myMenu();
    #clear
    glClearColor(0.2,0.2,0.2,0); 
    glClearAccum(0,0,0,0);

def main():
    global window,leftWin,rightWin, NumJitters
    if len(sys.argv) < 2:
        NumJitters = len(twJitterTable)
    else:
        NumJitters = int(sys.argv[1])
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_ACCUM);
    glutInitWindowSize(mainWidth,mainHeight); 

    #parent window
    window = glutCreateWindow("Antialiasing");
    glutDisplayFunc(mainDisplay);
    myInit();

    #window for original image
    leftWin = glutCreateSubWindow(window,GAP,GAP,wWidth,wHeight);
    glutDisplayFunc(jaggedDisplay);
    myInit();
 
    #window for image after antialiasing
    rightWin = glutCreateSubWindow(window,GAP*2+wWidth,GAP,wWidth,wHeight);
    glutDisplayFunc(smoothDisplay);
    myInit();
  
    redisplayAll();
    glutMainLoop();

if __name__ == '__main__':
    main()
