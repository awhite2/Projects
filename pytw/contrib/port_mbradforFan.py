


'''
AUTHOR: Marisol Ardon
DATE: FEbruary 27, 2012
COURSE: CS307

This is a revision from Micuie Bradford's fan.Re-coding from C to python
Micuie Bradford
    CS307 Fall 2007
    Demo of Table Fan object

    Micquie Bradford's Object for the Object Library
    Function: Draws a table fan whose blades can rotate.
    The color of the base of the fan can be chosen by the user.
    mbradforDrawFan takes only 2 parameters, the base color (in the
    form of a twTriple), and the initial rotation angle of the fan
    blades

Copyright (C) 2012 by Micuie Bradford under GNU GPL
    '''

import sys
import math

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
    '''

#=====================================================================
#colors used for the fan

baseColor = (0.2, 0.2, 0.2)
bladeColor = (0.3, 0.3, 0.3);
cageColor = (0.12, 0.12, 0.12);
blade = [ [1, 4.5, -1],
          [6, 6, 6],
          [9, 6, -1],
          [1, 4.5, 0]
          ];



def drawCage():
    glPushMatrix();  #draw cage
    glTranslatef(0,6,0);
    glRotatef(90, 1, 0, 0);
    glutWireTorus(0.05,10, 50, 50);
    for i in range(4):
        glPushMatrix();
        glRotate(i*40, 0, 0, 1);
        glRotatef(90, 1, 0, 0);
        glScalef(1, 0.3, 1);
        glutWireTorus(0.05, 10, 50, 50);
        glPopMatrix();
    glPopMatrix();

#======================================================================

def drawBlades():
    glPushMatrix()
    for i in blade:   #draw blades
        glRotatef(90, 0, 1, 0);
        glBegin(GL_POLYGON);
        glVertex3fv(blade[0]);
        glVertex3fv(blade[1]);
        glVertex3fv(blade[2]);
        glVertex3fv(blade[3]);
        glEnd();
    glPopMatrix();

#======================================================================

def mbradforDrawFan():
    glPushMatrix();     #initial push

    twColor(baseColor, 0, 0.2);  #draw base
    glPushMatrix();
    glTranslatef(10, 5, -10);
    glRotatef(90, 1, 0, 0);
    twTube(8, 8, 1, 30, 30);    #very bottom of base

    glTranslatef(0, 0, -1);     #upper base level
    twTube(7, 7, 1, 30, 30);

    glTranslatef(0,0,-10)       #standing part of base
    twTube(2,6,10,30,30)

    glTranslatef(0,0,-2)

    glPushMatrix()          #isolate scale of sphere
    glScalef(0.8,1,0.8)
    glutSolidSphere(4,20,20)
    glPopMatrix()

    glPushMatrix()      #isolate positioning of fan head
    glTranslatef(0,4,0)
    glRotatef(90,0,1,0)
    glRotatef(90,1,0,0)
    twTube(2,3,4,30,30)
    glTranslatef(0,0,-0.8)
    twColor(cageColor,0.3,0.6)
    twTube(1,1,0.8,30,30)
    glPopMatrix()

    drawCage()

    twColor(bladeColor,3,2)

    drawBlades()
    glPopMatrix()       #pop from origin in progress

    glPopMatrix()       #final pop
    
    

#======================================================================

def display():
    twDisplayInit();
    twCamera();

    lightPos = (0, 25, 10, 0);
    twGrayLight(GL_LIGHT1, lightPos, 0, 1.0, 1);

    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT1);
    glShadeModel(GL_SMOOTH);
    twAmbient(3);

    mbradforDrawFan();

    glFlush();
    glutSwapBuffers();

    #end display(void)

#=========================================================================

#=========================================================================

def main ():
    glutInit(sys.argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    twInitWindowSize(500, 500);
    glutCreateWindow(sys.argv[0]);
    twBoundingBox(0, 20, 0, 25, -20, 0);
    twMainInit();
    #glutKeyboardFunc(rotFan);
    glutDisplayFunc(display);
    glutMainLoop();

if __name__ == '__main__' :
    main()
        
    
    
         
        
        
              
          
