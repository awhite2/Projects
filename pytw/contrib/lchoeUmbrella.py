'''
Lalita Choe, April 2012

Umbrella object: Copyright (C) 2012 by Lalita Choe under the GNU GPL


'''

import sys
import math

from TW import *

def lchoeUmbrella(color1 = (0,0,1), # blue
                  color2 = (1,1,1), # white
                  poleColor = (0.7,0.7,0.7) #gray
                  ):
    '''Umbrella object is 4 units wide in diameter, the pole extends
       3 units in the negative z-axis..
       The triangles that make up the umbrella alternate between 
       color1, default blue,  and color2, default white '''
    points = (
        (0,0,.75),
        (2,0,0),
        (math.sqrt(2),math.sqrt(2),0),
        (0,2,0),
        (-math.sqrt(2),math.sqrt(2),0),
        (-2,0,0),
        (-math.sqrt(2),-math.sqrt(2),0),
        (0,-2,0),
        (math.sqrt(2),-math.sqrt(2),0)
        )
    glLineWidth(2)
    
    glBegin(GL_TRIANGLE_FAN)
    glNormal3fv((0,1,0))
    
    # first triangle
    twColor(color1,0.1,30)
    glVertex3fv(points[0])
    glVertex3fv(points[1])
    glVertex3fv(points[2])

    # second triangle
    twColor(color2,0.1,30)
    glVertex3fv(points[3])

    # third triangle
    twColor(color1,0.1,30)
    glVertex3fv(points[4])

    # fourth triangle
    twColor(color2,0.1,30)
    glVertex3fv(points[5])

    # fifth triangle
    twColor(color1,0.1,30)
    glVertex3fv(points[6])
    
    # sixth triangle
    twColor(color2,0.1,30)
    glVertex3fv(points[7])
    
    # seventh triangle
    twColor(color1,0.1,30)
    glVertex3fv(points[8])
    
    # eighth triangle
    twColor(color2,0.1,30)
    glVertex3fv(points[1])

    glEnd()
    
    # draw the pole
    twColor(poleColor,0.5,40)
    glPushMatrix()
    glTranslate(0,0,-.7)
    glScale(.05,.05,3)
    glutSolidCube(1)
    glPopMatrix()

def display():

    twDisplayInit(0.5, 0.5, 0.5)  # clear background to 50% gray
    twCamera()                    # set up the camera

    lchoeUmbrella()               # draw the umbrella

    glFlush()                     # clear the graphics pipeline
    glutSwapBuffers()             # make this the active framebuffer

# ================================================================

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(500,500)    
    twBoundingBox(-2,2, -2,2, -2.25,0.75);     
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)      # register the callback
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()
