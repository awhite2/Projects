'''Demo exhibiting the use of a spotlight 

Written by Scott D. Anderson
scott.anderson@acm.org
Fall 2004
Ported to Python Fall 2009
'''

import sys
import math                            # for tan, sin and cos

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''
## ================================================================

numSquares = 4;              # allows user to change number of squares

lightPosition = (0,3,0,1)       # spotlight location

outline = True ;                # whether to draw the squares
lightCutoff = 35;               # the angle of the spotlight cone
smooth = True;                  # whether to use smooth shading

def drawUnitSquare(w, h):
    ''' 1*1 unit square drawn with triangle_strips. In practice, we
would probably just use twDrawUnitSquare(), but this allows us to draw
the triangles if we choose.  The square is in the y=0 plane, and x is
in [0,1] and so is z.'''

    i = 0
    dw = 1.0/w;
    dh = 1.0/h;
    glNormal3f(0,1,0);
    while i < w:
        glBegin( GL_TRIANGLE_STRIP );
        j = 0
        while j <= h:
            glVertex3f(dw*i,0,dh*j);
            glVertex3f(dw*(i+1),0,dh*j);
            j += 1
        glEnd();
        i += 1
    if outline:  ##draw quads of unit square, depending on a global
        glPushMatrix();
        glTranslatef(0,0.03,0); # just above the grid
        twColorName(TW_MAGENTA);
        i = 0
        while i < w:
            j = 1
            while j <= h:
                glBegin( GL_LINE_LOOP );
                glVertex3f(dw*i,0,dh*(j-1));
                glVertex3f(dw*(i+1),0,dh*(j-1));
                glVertex3f(dw*(i+1),0,dh*(j));
                glVertex3f(dw*i,0, dh*(j));
                glEnd();
                j += 1
            i += 1
        glPopMatrix();

def lamp():
    '''this is the actual spotlight'''
    direction = (1,-2,1) # spotlight direction

    twGraySpotlight(GL_LIGHT0, lightPosition, 1, 1, 0.5,
                    direction, lightCutoff, 5);

    ## The following 8 lines are equivalent to the call to twGraySpotlight
    # GLfloat ambient [] = (1,1,1,1)
    # GLfloat diffuse [] = (1,1,1,1)
    # GLfloat specular [] = (0.5,0.5,0.5,1)
    # GLfloat lightExponent = 5;
    # glLightfv(GL_LIGHT0, GL_POSITION, light);
    # glLightfv(GL_LIGHT0, GL_AMBIENT, ambient);
    # glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse);
    # glLightfv(GL_LIGHT0, GL_SPECULAR, specular);
    # glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, direction);
    # glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, lightCutoff);
    # glLightf(GL_LIGHT0, GL_SPOT_EXPONENT, lightExponent);
    # glEnable(GL_LIGHT0); 

def display():
    twDisplayInit();
    twCamera();

    glDisable(GL_LIGHTING);
    ##draw cone at location of light.  Cone will be shown in RGB color, not with lighting.
    if False:
      glPushMatrix();
      twColorName(TW_RED);
      coneHeight = 2;
      base = coneHeight*math.tan(lightCutoff*M_PI/180);
      glTranslatef(lightPosition[0],lightPosition[1],lightPosition[2]);
      glRotatef(90,1,0,0);
      twCylinder(0.01,base,coneHeight,20,1);
      glPopMatrix();
    
    glEnable(GL_LIGHTING);
    lamp();                     ## turn on the light, and enable lighting
    twAmbient(0.1);
    if smooth:
        glShadeModel(GL_SMOOTH);
    else:
        glShadeModel(GL_FLAT);

    glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE);

    ## Draw a surface for the light to illuminate
    twColorName(TW_GREEN);
    glPushMatrix();
    glTranslatef(-10,0,-10);
    glScalef(20,1,20);
    drawUnitSquare(numSquares,numSquares);
    glPopMatrix();
    
    glFlush();
    glutSwapBuffers(); 

def modifySquare (key, x, y):
    global numSquares, outline
    if key == 'h':
        outline = False
    elif key == 'd': 
        outline = True
    elif key == '+': 
        numSquares += 1
    elif key == '-': 
        numSquares -= 1
    glutPostRedisplay()

def modifyCutoff (key, x, y):
    global lightCutoff
    if key == 'w': 
        lightCutoff += 1
    elif key == 'n': 
        lightCutoff -= 1
    glutPostRedisplay()

def modifyShading (key, x, y):
    global smooth
    if key == 's': 
        smooth = True
    elif key == 'f': 
        smooth = False
    glutPostRedisplay()

def keyInit():
    twKeyCallback('h', modifySquare, "hides the lines of the unit square");
    twKeyCallback('d', modifySquare, "draws the lines of the unit square");
    twKeyCallback('+', modifySquare, "increases the number of squares");
    twKeyCallback('-', modifySquare, "decreases the number of squares");
    twKeyCallback('w', modifyCutoff, "widens the cutoff angle");
    twKeyCallback('n', modifyCutoff, "narrows the cutoff angle");
    twKeyCallback('s', modifyShading, "smooth shading");
    twKeyCallback('f', modifyShading, "flat shading");

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    # twBoundingBox(-10,10,0,lightPosition[1],-10,10);
    twBoundingBox(-10,10,0,lightPosition[1],-10,10);
    twInitWindowSize(800,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    keyInit();
    glutMainLoop()

if __name__ == '__main__':
  main()
