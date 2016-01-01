'''
Gazebo

This program constructs a gazebo.

Written by someone by the username ayip. 
Ported to python from C by Dana Bullister on February 22, 2012

Copyright (C) 2012 by Dana Bullister under the GNU GPL

'''

import sys
from TW import *

def ayipGazebo(gazeboXPos, gazeboYPos, gazeboZPos, gazeboEdge, gazeboHeight):

  ''' Constructs a 2x2x3 (length, width, height) gazebo.
  Origin is at the bottom of the gazebo, in the center.
  Bounding box is from -2 to 2 in the x and y directions and from 0 to 3 in the z direction.'''

  #--------------------------------------
  # defining variables
  #--------------------------------------
  
  # colors
  raisedPlatformColor = (.93, .91, .67) # pale goldenrod
  gazeboTopColor = (.17, .36, .25) ## cucumber green
  standingPlatformColor = (.2, 0, 0) ## maroon
  columnColor = (.93, .85, .68) ## wheat
  
  # structures  
  #--> standing platform
  gazeboPlatformEdge = gazeboEdge  
  gazeboPlatformHeight = .05*gazeboHeight
  
  #--> raised platform
  gazeboRaisedPlatformEdge = .947*gazeboEdge
  gazeboRaisedPlatformHeight = .1*gazeboPlatformHeight
  
  #--> columns on the platform
  gazeboPlatformColEdge = .125*gazeboEdge
  gazeboPlatformColHeight = .3*gazeboHeight
  
  #--> columns below the platform
  gazeboBottomColEdge = .25*gazeboEdge  
  gazeboBottomColHeight = .2*gazeboHeight
  
  #--> gazebo top
  gazeboTopEdge = 1.5*gazeboEdge
  gazeboTopHeight = .445*gazeboHeight
  
  #--> gazebo roof vertices
  points = [(0,gazeboPlatformHeight+gazeboRaisedPlatformHeight+gazeboPlatformColHeight+.9*gazeboTopHeight,0), # top of roof
            (-.5*gazeboTopEdge,gazeboPlatformHeight+gazeboRaisedPlatformHeight+gazeboPlatformColHeight-.27*gazeboTopHeight,.5*gazeboTopEdge), #front left corner of roof
            (.5*gazeboTopEdge,gazeboPlatformHeight+gazeboRaisedPlatformHeight+gazeboPlatformColHeight-.27*gazeboTopHeight,.5*gazeboTopEdge), # front right ""
            (.5*gazeboTopEdge,gazeboPlatformHeight+gazeboRaisedPlatformHeight+gazeboPlatformColHeight-.27*gazeboTopHeight,-.5*gazeboTopEdge), # back right ""
            (-.5*gazeboTopEdge,gazeboPlatformHeight+gazeboRaisedPlatformHeight+gazeboPlatformColHeight-.27*gazeboTopHeight,-.5*gazeboTopEdge) # back left ""
            ]

  #--------------------------------------
  # drawing structures
  #--------------------------------------
 
  glTranslatef(0,gazeboBottomColHeight+.5*gazeboPlatformHeight,0) # translate to center of standing platform

  #-> draw standing platform
  glPushMatrix()  # begin gazebo platform matrix
  glColor3fv(standingPlatformColor) # set color to maroon
  glTranslatef(gazeboXPos,gazeboYPos,gazeboZPos)
  glPushMatrix() 
  glScalef(gazeboPlatformEdge,gazeboPlatformHeight,gazeboPlatformEdge)
  glutSolidCube(1)
  glPopMatrix()
  glPopMatrix() # end gazebo platform matrix

  #-> draw raised platform (on top of the main platform)
  glPushMatrix() # begin gazebo raised platform matrix
  glColor3fv(raisedPlatformColor) # set color to pale goldenrod
  glTranslatef(0,.5*gazeboPlatformHeight+.5*gazeboRaisedPlatformHeight,0)
  glPushMatrix() 
  glScalef(gazeboRaisedPlatformEdge,gazeboRaisedPlatformHeight,gazeboRaisedPlatformEdge)
  glutSolidCube(1)
  glPopMatrix()
  glPopMatrix() # end gazebo raised platform matrix

  #-> draw columns on the platform
  glPushMatrix()  # begin gazebo platform columns matrix
  glColor3fv(columnColor) # set color to wheat
  #---> front left
  glTranslatef(-.5*gazeboPlatformEdge+.5*gazeboPlatformColEdge,.5*gazeboPlatformHeight+.5*gazeboPlatformColHeight,.5*gazeboPlatformEdge-.5*gazeboPlatformColEdge)
  glPushMatrix() 
  glScalef(gazeboPlatformColEdge,gazeboPlatformColHeight,gazeboPlatformColEdge)
  glutSolidCube(1)
  glPopMatrix()  
  #---> front right
  glTranslatef(gazeboPlatformEdge-gazeboPlatformColEdge,0,0)
  glPushMatrix()  
  glScalef(gazeboPlatformColEdge,gazeboPlatformColHeight,gazeboPlatformColEdge)
  glutSolidCube(1)
  glPopMatrix()  
  #---> back right
  glTranslatef(0,0,-gazeboPlatformEdge+gazeboPlatformColEdge)
  glPushMatrix() 
  glScalef(gazeboPlatformColEdge,gazeboPlatformColHeight,gazeboPlatformColEdge)
  glutSolidCube(1)
  glPopMatrix()  
  #---> back left
  glTranslatef(-gazeboPlatformEdge+gazeboPlatformColEdge,0,0)
  glPushMatrix()  
  glScalef(gazeboPlatformColEdge,gazeboPlatformColHeight,gazeboPlatformColEdge)
  glutSolidCube(1)
  glPopMatrix()  
  glPopMatrix() # end gazebo platform columns matrix

  #-> draw columns below the platform
  glPushMatrix()  # begin gazebo bottom columns matrix
  #---> front left
  glTranslatef(-.5*gazeboPlatformEdge+.5*gazeboBottomColEdge,-.5*gazeboPlatformHeight-.5*gazeboBottomColHeight,.5*gazeboPlatformEdge-.5*gazeboBottomColEdge)
  glPushMatrix()  
  glScalef(gazeboBottomColEdge,gazeboBottomColHeight,gazeboBottomColEdge)
  glutSolidCube(1)
  glPopMatrix()  
  #---> front right
  glTranslatef(gazeboPlatformEdge-gazeboBottomColEdge,0,0)
  glPushMatrix() 
  glScalef(gazeboBottomColEdge,gazeboBottomColHeight,gazeboBottomColEdge)
  glutSolidCube(1)
  glPopMatrix()  
  #---> back right
  glTranslatef(0,0,-gazeboPlatformEdge+gazeboBottomColEdge)
  glPushMatrix() 
  glScalef(gazeboBottomColEdge,gazeboBottomColHeight,gazeboBottomColEdge)
  glutSolidCube(1)
  glPopMatrix()  
  #---> back left
  glTranslatef(-gazeboPlatformEdge+gazeboBottomColEdge,0,0)
  glPushMatrix() 
  glScalef(gazeboBottomColEdge,gazeboBottomColHeight,gazeboBottomColEdge)
  glutSolidCube(1)
  glPopMatrix()  
  glPopMatrix()  # end gazebo bottom column matrix

  #-> draw top
  glPushMatrix() # begin gazebo top matrix
  glColor3fv(gazeboTopColor) # set color to cucumber
  glLineWidth(1) # set line width to 1

  glPushMatrix() # begin solid top matrix
  glBegin(GL_TRIANGLE_FAN)
  # front
  glVertex3fv(points[0])
  glVertex3fv(points[1])
  glVertex3fv(points[2])
  
  # right
  glVertex3fv(points[3])
  
  # back
  glVertex3fv(points[4])

  # left
  glVertex3fv(points[1])
  glEnd()
    
  glPopMatrix() # end solid top matrix
  
  glPopMatrix() # end gazebo top matrix


def display():
  '''A callback function to draw the scene, as necessary. '''

    twDisplayInit(0.7, 0.7, 0.7)  # clear background to 70% gray
    twCamera()                    # set up the camera

    ayipGazebo(0,0,0,2,3);        # draw the gazebo

    glFlush()                     # clear the graphics pipeline
    glutSwapBuffers()             # make this the active framebuffer

# ================================================================

def main():
    '''Main function to call and display gazebo. '''
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(500,500)    
    twBoundingBox(-2,2,0,3,-2,2);     
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)      # register the callback
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()
