'''
Assignment 6 - Library Contribution
Created by Margaret Perry and Gabriela Lanza
Some nice seaweed
'''

import random
from TW import *

#arrays for random numbers used in generating plants
scaleArr = [ random.uniform(1.0,10.0) for _ in range (10000)] #max height of seaweed is ten units
rotYArr = [ random.uniform(0.0,360.0) for _ in range (10000)]
rotXArr = [ random.uniform(0.0,30.0) for _ in range (10000)]


def glanzaSeaweed(x,y,z,stems,maxheight):
    '''
Draws a cluster of seaweed (aka Bezier curves) at given x,y,z coordinates.
There are 'stems' individual leaves in a given cluster.  All leaves are
generated with the same control points, but they vary in height (no more
than maxheight) and degree of rotation around X/Y axes - these values are
randomly selected for each leaf.'''

    green = (20.0/255,150.0/255,70.0/255) #color is always green    

    #set variables back to 0 on redraw
    scaleArrLocation = 0
    arrLocation = 0

    glPushMatrix()
    glTranslate(x,y,z) #Move to given location
    cp = [
        (0,0,0),  #Control points for all stems
        (.5,.3,.7),
        (-.8,.6,.2),
        (0,1,0) ]
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glLineWidth(2.0)
    twColor(green, 0.1, 0.1);

    for i in range (0,stems): #Generate random values and draw resulting curve
        '''
        scale = random.uniform(1.0,maxheight)
        rotationY = random.uniform(0.0,360.0)
        rotationX = random.uniform(0.0,20.0)
        '''
        for i in range (0,len(scaleArr)):
            if scaleArr[scaleArrLocation] > maxheight:
                scaleArrLocation = scaleArrLocation+1
            else:
                scale = scaleArr[scaleArrLocation]
                break
        rotationY = rotXArr[arrLocation]
        rotationX = rotYArr[arrLocation]
        
        glPushMatrix()
        glScalef(1,scale,1)
        glRotatef(rotationY,0,1,0)
        glRotatef(rotationX,1,0,0)
        twDrawBezierCurve(cp,10)
        glPopMatrix()

        scaleArrLocation = scaleArrLocation+1
        arrLocation = arrLocation+1
    
    glPopAttrib(GL_ALL_ATTRIB_BITS)
    glPopMatrix()


def display():
    
    twDisplayInit(1,1,1)
    twCamera()

    glShadeModel(GL_SMOOTH)
    
    lightPos = ( 5, 15, 10, 1 )
    lightPos1 = (5,20,5,1)
    twGrayLight(GL_LIGHT0,lightPos,0.1,0.4,0.04);
    twGraySpotlight(GL_LIGHT1,lightPos1,0.6,0.9,0.9,
                    (0,-1,0),
                    80,
                    1
                    )
    glEnable(GL_LIGHTING);

    twColor(white, 0.7, 1);

    glanzaSeaweed(5,5,5,35,8.0)
    
    glFlush()
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(0,10,8,18,-3,10);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    glLineWidth(1)
    glutMainLoop();

if __name__ == '__main__':
    main()
