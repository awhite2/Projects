'''Copyright (C) <2013>  <Abra White>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
'''

import sys

from TW import *;

def leaf():
    '''draws a 0x1x1 diamond shape that is green like a leaf. It is a plane that rests on the y axis and goes along the x. The origin is at the left bottom corner'''
    #leaves are green and a diamond shape
    glBegin(GL_QUADS)
    glColor3f(0.4,0.5,0)
    glVertex3d(0.0,0.0,0.0)
    glVertex3d(1.0,1.0,0.0)
    glVertex3d(2.0,0.0,0.0)
    glVertex3d(1.0,-1.0,0.0)
    glNormal(0,0,1)
    glEnd();

#takes a length, base width, angle of branches, shrink rates, and a minimum length
    '''Draws a tree that is always brown (for now)
The tree is defined by the length -- length parameter is the height,
Origin is at the center of the base.  The tree points down the z-axis.'''
def tree(length, width, angle, shrinkL, shrinkW, mini):
    glColor3f(0.4,0.3,0) #tree is constantly brown
    if length<mini:
        glPushMatrix()
        glScale(length*.3,length*.3,0)
        glTranslate(0,length,0)
        leaf()
        glPopMatrix()
    else:
        #draw base cone
        glutSolidCone(width, length, 40, 40)
        glPushMatrix()
        glTranslate(0,0,length*.5)
        #draw right branches
        glPushMatrix()
        glRotate(angle,0,1,0)
        tree(length*shrinkL,width*shrinkW,angle,shrinkL, shrinkW,mini)
        glPopMatrix()
        glPushMatrix()
        glRotate(90,0,0,1)
        #draw back branches
        glPushMatrix()
        glRotate(angle,0,1,0)
        tree(length*shrinkL,width*shrinkW,angle,shrinkL,shrinkW,mini)
        glPopMatrix()
        glPopMatrix()
        #draw left branches
        glPushMatrix()
        glRotate(180,0,0,1)
        glPushMatrix()
        glRotate(angle,0,1,0)
        tree(length*shrinkL,width*shrinkW,angle,shrinkL, shrinkW,mini)
        glPopMatrix()
        glPopMatrix()
        glPushMatrix()
        glRotate(270,0,0,1)
        #draw front branches
        glPushMatrix()
        glRotate(angle,0,1,0)
        tree(length*shrinkL,width*shrinkW,angle,shrinkL, shrinkW,mini)
        glPopMatrix()
        glPopMatrix()

        glPopMatrix()
def display():
    twDisplayInit();
    twCamera();

    lightPos1 = ( 0, 300, 0, 0 )
    twGrayLight(GL_LIGHT1,lightPos1,1.0,0.5,1.0);

    glColorMaterial ( GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE )
    glEnable ( GL_COLOR_MATERIAL )

    glEnable(GL_LIGHTING);
    glShadeModel(GL_SMOOTH);

    glPushMatrix()
    glRotate(-90,1,0,0)
    tree(10,.5,45,.5,.5,.2)
    glPopMatrix()

    glFlush()
    glutSwapBuffers();
    

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500,500)
    twBoundingBox(-5,5,0,10,-5,5)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()
