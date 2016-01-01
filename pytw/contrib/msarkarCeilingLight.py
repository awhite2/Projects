''' Ceiling Light originally created by Mala Sarkar, ported by Diana Tantillo
    
    Copyright (C) 2005 by Mala Sarkar under GNU GPL

    Includes Ceiling Light object
    CS307
'''

import sys
from TW import *

#global variables
global lightHeight
global MediumGray
global yellow

#default light heigh
lightHeight = 30
#default color of the light structure
MediumGray = (0.5, 0.5, 0.5)
#default color of bulb
yellow = (1, 1, 0)

def msarkarCeilingLight(lh, mat, bulbColor):
    ''' ceilingLight function: Draws a lamp meant to be hung from the ceiling, 
    complete with lightshade and bulb 
    ceilingLight(...) takes 3 parameters in total
    1 lh [int] height of the light pole from which the shade hangs from. 
    2 mat [twTriple] color of the lighting structure
    3 bulbcolor [twTriple] color of the light bulb within the light shade
    
    The shade does not adjust according to 'lh' or the pole height, so in that 
    sense the light is not scalable. Notice that the yellow bulb stays a stark 
    bright yellow if you enable lighting in the msarkarCeilingLight demo; if 
    you want to disable this feature, change the value of light0 within the 
    function to 'false.' '''
    light0 = True

    #draw pole from which light hands from
    twColor(mat, 100, 100)
    glPushMatrix()
    glRotate(90, 1, 0, 0)
    twCylinder(1, 1, lh, 10, 10)
    glPopMatrix()

    #draw light bulb
    glPushMatrix()
    twColor(bulbColor, 0, 50)

    if (light0):
        mat_emission = (1, 1, 0, 0.99)
        glMaterialfv(GL_FRONT, GL_EMISSION, mat_emission)
    else:
        mat_emission2 = (0, 0, 0, 0.0)
        glMaterialfv(GL_FRONT, GL_EMISSION, mat_emission2)

    glTranslatef(0, -lh, 0)
    glutSolidSphere(2, 10, 10)
    glPopMatrix()

    #draw light shade
    glPushMatrix()
    twColor(mat, 100, 100)
    mat_emissionCLEAR = (0, 0, 0, 0.0)
    glMaterialfv(GL_FRONT, GL_EMISSION, mat_emissionCLEAR)

    glTranslatef(0, -lh-lh*0.1, 0)
    glRotate(-90, 1, 0, 0)
    glLineWidth(5)
    glutWireCone(7, 10, 15, 15)
    glPopMatrix()

def setLight():
    glEnable(GL_LIGHTING)
    #directional light
    light0 = (1, 2, 1, 0)
    twGrayLight(GL_LIGHT0, light0, 0.3, 0.1, 0.2)

def display():
    twDisplayInit()
    twCamera()
    setLight()

    glShadeModel(GL_SMOOTH)
    #draw ceiling light)
    msarkarCeilingLight(lightHeight, MediumGray, yellow)

    glFlush()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(650,650)
    glutCreateWindow(sys.argv[0]);
    glutDisplayFunc(display);
    #create a bounding box tailored to fit the hanging light and light shade
    twBoundingBox(-7,7,-lightHeight-lightHeight*0.1,0,-7.5,7.5)
    twMainInit(); 
    glutMainLoop();
    return 0;

if __name__ == '__main__':
    main()
