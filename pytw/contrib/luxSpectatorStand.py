''' Shirley Lu (xlu2)
Contribution
Spectator Stand '''

import sys

from TW import *


## ==================================================================================================== ##

def luxDrawStand(innerLeft,sideLen,lower,innerlower,height,roofheight,textureName):
	''' Draws a square Spectator Stand. Other than its square base, the stand is completely customizable.

	innerLeft is a vertex indicating the lower left corner of the front facing surface.
	sideLen is the side length of the square base
	lower is the greater height of lower half of the stand
	innerlower is the smaller height of the lower half of the stand
	height is the total height of the stand, excluding the pyramid roof
	roofheight is the height of the pyramid roof
	textureName is a string that indicates the name of the ppm texture. '''

	glPushMatrix()
	twPPM_Tex2D(twPathname(textureName,False))
	drawInside(innerLeft,sideLen,lower,innerlower,height,roofheight)
	drawTopSides(innerLeft,sideLen,lower,innerlower,height,roofheight)
	drawBottomSides(innerLeft,sideLen,lower,innerlower,height,roofheight)
	drawOutside(innerLeft,sideLen,lower,innerlower,height,roofheight)
	drawRoof(innerLeft,sideLen,lower,innerlower,height,roofheight)
	glPopMatrix()

## Draws the roof of the stand

def drawRoof(innerLeft,sideLen,lower,innerlower,height,roofheight):

	#inside
	glBegin(GL_TRIANGLES)
	glNormal3f(1,0,0);
	glTexCoord2f(0.5,0); glVertex3f(innerLeft[0]+0.5*sideLen,innerLeft[1]+height+roofheight,innerLeft[2]-0.5*sideLen); #upper middle
	glTexCoord2f(0,0.7); glVertex3f(innerLeft[0],innerLeft[1]+height,innerLeft[2]); #lower left
	glTexCoord2f(1,0.7); glVertex3f(innerLeft[0]+sideLen,innerLeft[1]+height,innerLeft[2]); #lower right
	glEnd()

	#outside
	glBegin(GL_TRIANGLES)
	glNormal3f(1,0,0);
	glTexCoord2f(0.5,0); glVertex3f(innerLeft[0]+0.5*sideLen,innerLeft[1]+height+roofheight,innerLeft[2]-0.5*sideLen); #upper middle
	glTexCoord2f(0,0.7); glVertex3f(innerLeft[0],innerLeft[1]+height,innerLeft[2]-sideLen); #lower left
	glTexCoord2f(1,0.7); glVertex3f(innerLeft[0]+sideLen,innerLeft[1]+height,innerLeft[2]-sideLen); #lower right
	glEnd()

	#left
	glBegin(GL_TRIANGLES)
	glNormal3f(1,0,0);
	glTexCoord2f(0.5,0); glVertex3f(innerLeft[0]+0.5*sideLen,innerLeft[1]+height+roofheight,innerLeft[2]-0.5*sideLen); #upper middle
	glTexCoord2f(0,0.7); glVertex3f(innerLeft[0],innerLeft[1]+height,innerLeft[2]-sideLen); #lower left
	glTexCoord2f(1,0.7); glVertex3f(innerLeft[0],innerLeft[1]+height,innerLeft[2]); #lower right
	glEnd()

	#right
	glBegin(GL_TRIANGLES)
	glNormal3f(1,0,0);
	glTexCoord2f(0.5,0); glVertex3f(innerLeft[0]+0.5*sideLen,innerLeft[1]+height+roofheight,innerLeft[2]-0.5*sideLen); #upper middle
	glTexCoord2f(0,0.7); glVertex3f(innerLeft[0]+sideLen,innerLeft[1]+height,innerLeft[2]); #lower left
	glTexCoord2f(1,0.7); glVertex3f(innerLeft[0]+sideLen,innerLeft[1]+height,innerLeft[2]-sideLen); #lower right
	glEnd()

#draws the left and right top triangles on the side

def drawTopSides(innerLeft,sideLen,lower,innerlower,height,roofheight):

	glBegin(GL_TRIANGLES)
	glNormal3f(1,0,0);
	glTexCoord2f(0,0); glVertex3f(innerLeft[0],innerLeft[1]+height,innerLeft[2]-sideLen); #upper left
	glTexCoord2f(0,1); glVertex3f(innerLeft[0],innerLeft[1]+lower,innerLeft[2]-sideLen); #lower left
	glTexCoord2f(1,0); glVertex3f(innerLeft[0],innerLeft[1]+height,innerLeft[2]); #upper right
	glEnd()

	glBegin(GL_TRIANGLES)
	glNormal3f(1,0,0);
	glTexCoord2f(0,0); glVertex3f(innerLeft[0]+sideLen,innerLeft[1]+height,innerLeft[2]); #upper left
	glTexCoord2f(0,1); glVertex3f(innerLeft[0]+sideLen,innerLeft[1]+lower,innerLeft[2]-sideLen); #lower right
	glTexCoord2f(1,0); glVertex3f(innerLeft[0]+sideLen,innerLeft[1]+height,innerLeft[2]-sideLen); #upper right
	glEnd()

#draws the left and right bottom trapezoids on the side

def drawBottomSides(innerLeft,sideLen,lower,innerlower,height,roofheight):

	glBegin(GL_QUADS)
	glNormal3f(1,0,0);
	glTexCoord2f(0,0); glVertex3f(innerLeft[0],innerLeft[1]+lower,innerLeft[2]-sideLen); #upper left
	glTexCoord2f(0,6); glVertex3f(innerLeft[0],innerLeft[1],innerLeft[2]-sideLen); #lower left
	glTexCoord2f(1,6); glVertex3f(innerLeft[0],innerLeft[1],innerLeft[2]); #lower right
	glTexCoord2f(1,0.5); glVertex3f(innerLeft[0],innerLeft[1]+innerlower,innerLeft[2]); #upper right
	glEnd()

	glBegin(GL_QUADS)
	glNormal3f(1,0,0);
	glTexCoord2f(0,0.5); glVertex3f(innerLeft[0]+sideLen,innerLeft[1]+innerlower,innerLeft[2]); #upper left
	glTexCoord2f(0,6); glVertex3f(innerLeft[0]+sideLen,innerLeft[1],innerLeft[2]); #lower left
	glTexCoord2f(1,6); glVertex3f(innerLeft[0]+sideLen,innerLeft[1],innerLeft[2]-sideLen); #lower right
	glTexCoord2f(1,0); glVertex3f(innerLeft[0]+sideLen,innerLeft[1]+lower,innerLeft[2]-sideLen); #upper right
	glEnd()

#draws the outside surface

def drawOutside(innerLeft,sideLen,lower,innerlower,height,roofheight):

	glBegin(GL_QUADS)
	glNormal3f(0,0,-1);
	glTexCoord2f(0,0); glVertex3f(innerLeft[0]+sideLen,innerLeft[1]+height,innerLeft[2]-sideLen); #upper left
	glTexCoord2f(0,7); glVertex3f(innerLeft[0]+sideLen,innerLeft[1],innerLeft[2]-sideLen); #lower left
	glTexCoord2f(1,7); glVertex3f(innerLeft[0],innerLeft[1],innerLeft[2]-sideLen); #lower right
	glTexCoord2f(1,0); glVertex3f(innerLeft[0],innerLeft[1]+height,innerLeft[2]-sideLen); #upper right
	glEnd()

#draws the inside surface

def drawInside(innerLeft,sideLen,lower,innerlower,height,roofheight):

    glBegin(GL_QUADS)
    glNormal3f(0,0,1);
    glTexCoord2f(0,0); glVertex3f(innerLeft[0],innerLeft[1]+innerlower,innerLeft[2]); #upper left
    glTexCoord2f(0,5); glVertex3f(innerLeft[0],innerLeft[1],innerLeft[2]); #lower left
    glTexCoord2f(1,5); glVertex3f(innerLeft[0]+sideLen,innerLeft[1],innerLeft[2]); #lower right
    glTexCoord2f(1,0); glVertex3f(innerLeft[0]+sideLen,innerLeft[1]+innerlower,innerLeft[2]); #upper right
    glEnd()

## ==================================================================================================== ##

def display():
	twDisplayInit();
	twCamera()

	glEnable(GL_AUTO_NORMAL)

	glEnable(GL_TEXTURE_2D)
	glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE);

	textureName = "gryffindor.ppm"
	innerLeft = (0,0,0)
	sideLen = 20
	lower = 120
	innerlower = 100
	upper = 20
	height = lower + upper
	roofheight = 14
	luxDrawStand(innerLeft,sideLen,lower,innerlower,height,roofheight,textureName)

	glFlush()
	glutSwapBuffers()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH )
	twInitWindowSize(500,500)
	twBoundingBox(-5,25,-5,160,-25,5)
	glutCreateWindow(sys.argv[0])
	glutDisplayFunc(display)
	twMainInit()
	glutMainLoop()

if __name__ == '__main__':
	main()