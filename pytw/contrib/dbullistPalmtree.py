'''

dbullistPalmTree: Creates a palm tree. 

Written by Dana Bullister

February 12, 2012

Copyright (C) 2012 by Dana Bullister. This program is released under the GPL License.

'''

import sys
from TW import *


def dbullistPalmtree(size):
    ''' Draws a palm tree. The input "size" specificies the height of the
    tree. The width is the same as the height. The origin is located at the
    bottom (in the center) of the palm tree, and axes are default, with
    palm tree facing viewer. Colors are by default brown (for the trunk) and
    green (for the leaves). '''    
    # some variables
    trunkColor = (105.0/255.0,81.0/255.0,26.0/255.0)
    leafColor = (26.0/255.0,105.0/255.0,34.0/255.0)
    s = 40 # slices and stacks
    
    # draw trunk
    glPushMatrix()
    twColor(trunkColor, .7, 2);    
    glRotate(-90, 1, 0, 0)
    glutSolidCylinder(size/10,0.8*size,s,s)
    glPopMatrix()
    
    # draw leaves
    twColor(leafColor, .7, 2)
    glTranslate(0,0.8*size,0)
    glPushMatrix()
    y = 1
    for x in range(50):
        y = -y
        glRotate(23, y, 1, y)
        glutSolidCone(size/10,size/2,s,s)
        glRotate(10, 10*y, 1, 10*y)
        glutSolidCone(size/10,size/2,s,s)   
    glPopMatrix()

if __name__ == '__main__':

    def display():
        ' a callback function to draw scene as necessary '    
        twDisplayInit(0.7,0.7,0.7) # set background color
        twCamera() # set up the camera
        dbullistPalmtree(50)
        glFlush() # clear the graphics pipeline
        glutSwapBuffers() # make this the active framebuffer

    def main(): 
        ' a main function that creates and displays scene, sets up the bounding box (again borrowed from BarnTW.py by Scott Anderson)'  
        glutInit(sys.argv)
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        twInitWindowSize(500,500)
        twBoundingBox(-25,25,0,50,-25,25)
        glutCreateWindow(sys.argv[0])
        glutDisplayFunc(display) # register the callback
        twMainInit()
        glutMainLoop()

    main()
