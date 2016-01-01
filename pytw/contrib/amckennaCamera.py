##NAME: Alison McKenna
##FILENAME: amckennaCamera.py
##DATE: 30 October 2009
##FOR: CS 307 Problem Set 4, Creative Scene/Object

##=====================================================
''' amckennaCamera draws a black, analog, single lens reflex camera.
    Copyright (C) 2009  Alison McKenna

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see http://www.gnu.org/licenses/.'''

##=====================================================

import sys

try:
	from TW import *
except:
	print '''
ERROR: Couldn't import TW.
        '''
#Global Variables
CAMERALENGTH = 12.0
CAMERAWIDTH = 4.0
CAMERAHEIGHT = 6.0
	
LENSRADIUS = 2.3
LENSLENGTH = 2.5

HUBLENGTH = 3.4
HUBHEIGHT = 0.75

HOTSHOE_HEIGHT = 0.3
HOTSHOE_LENGTH = 2.0

#Color Settings
bodyColor = (0,0,0)
darkGray = (0.1,0.1,0.1)
mediumGray = (0.2,0.2,0.2)
lightGray = (0.4,0.4,0.4)
lightGray2 = (0.6,0.6,0.6)

def amckennaCamera():
	global bodyColor,darkGray,mediumGray,lightGray,lightGray2,CAMERALENGTH,CAMERAWIDTH,CAMERAHEIGHT	
    
	
	#DRAW CAMERA BODY=======================
	drawBody(bodyColor,mediumGray)	
	
	
	#DRAW LENS===============================
	global LENSRADIUS,LENSLENGTH
	
	#main lens body
	twColor(bodyColor,0,0)
	glPushMatrix()
	glTranslate(CAMERALENGTH/2,0.45*CAMERAHEIGHT,CAMERAWIDTH/2)
	twCylinder(LENSRADIUS,LENSRADIUS,LENSLENGTH,40,40)
	
	#f-stop ring (the inner ring around the lens body)
	twColor(darkGray,0,0)
	twTube(LENSRADIUS+0.2,LENSRADIUS+0.2,(0.2)*LENSLENGTH,40,40)
	
	#focus ring	(the outer ring around the lens body)
	twColor(lightGray,0,0)
	twTube(LENSRADIUS+0.1,LENSRADIUS+0.1,(0.4)*LENSLENGTH,40,40)
	
	#inside lens-tapering (tapers the inside of the lens bondy to the physical lens)
	twColor(darkGray,0,0)	
	twCylinder(LENSRADIUS-2,LENSRADIUS,LENSLENGTH,40,40)
	
	#glass (the physical lens)
	twColor(mediumGray,0,0)
	glTranslate(0,0,0.25*LENSLENGTH)
	glutSolidSphere(0.9*LENSRADIUS,20,20)
	glPopMatrix()
	
		
	#DRAW HUB========================
	#This is the large hub that rests on the top of the middle of the camera.
	global HUBLENGTH,HUBHEIGHT
	
	hub = [ [CAMERALENGTH/2 - HUBLENGTH/2, CAMERAHEIGHT, CAMERAWIDTH/2],
			[CAMERALENGTH/2 + HUBLENGTH/2, CAMERAHEIGHT, CAMERAWIDTH/2],
			[CAMERALENGTH/2 + 0.75*(HUBLENGTH/2), CAMERAHEIGHT + HUBHEIGHT, CAMERAWIDTH/2],
			[CAMERALENGTH/2 - 0.75*(HUBLENGTH/2), CAMERAHEIGHT + HUBHEIGHT, CAMERAWIDTH/2] ]
	
	#Creates array of all hub vertices
	hubBack = map( lambda v: [v[0], v[1], -v[2]],hub )
	hub.extend(hubBack)
	
	twColor(lightGray,0,0)
	drawQuad(hub,0,1,2,3)
	drawQuad(hub,1,5,6,2)
	drawQuad(hub,5,4,7,6)
	drawQuad(hub,4,0,3,7)
	drawQuad(hub,3,2,6,7)
	
	#Draw view window (rectangular window on back of hub)
	twColor(lightGray2,0,0)
	glBegin(GL_QUADS)
	glVertex3f(CAMERALENGTH/2 - 0.3*(HUBLENGTH/2), CAMERAHEIGHT + (0.1*HUBHEIGHT), -CAMERAWIDTH/2)
	glVertex3f(CAMERALENGTH/2 + 0.3*(HUBLENGTH/2), CAMERAHEIGHT + (0.1*HUBHEIGHT), -CAMERAWIDTH/2)
	glVertex3f(CAMERALENGTH/2 + 0.3*(HUBLENGTH/2), CAMERAHEIGHT + (0.9*HUBHEIGHT), -CAMERAWIDTH/2)
	glVertex3f(CAMERALENGTH/2 - 0.3*(HUBLENGTH/2), CAMERAHEIGHT + (0.9*HUBHEIGHT), -CAMERAWIDTH/2)
	glEnd()
	
	#Draw Hot Shoe (Metal bracket at the top of the hub)
	global HOTSHOE_HEIGHT,HOTSHOE_LENGTH
	
	twColor(lightGray2,0,0)
	#bottom of hot shoe
	glBegin(GL_QUADS)
	glVertex3f(CAMERALENGTH/2 -HOTSHOE_LENGTH/2,CAMERAHEIGHT+HUBHEIGHT,0)
	glVertex3f(CAMERALENGTH/2 +HOTSHOE_LENGTH/2,CAMERAHEIGHT+HUBHEIGHT,0)
	glVertex3f(CAMERALENGTH/2 +HOTSHOE_LENGTH/2,CAMERAHEIGHT+HUBHEIGHT,-0.8*(CAMERAWIDTH/2))
	glVertex3f(CAMERALENGTH/2 -HOTSHOE_LENGTH/2,CAMERAHEIGHT+HUBHEIGHT,-0.8*(CAMERAWIDTH/2))
	glEnd()
	#left side of hot shoe
	glBegin(GL_QUADS)
	glVertex3f(CAMERALENGTH/2 -HOTSHOE_LENGTH/2,CAMERAHEIGHT+HUBHEIGHT,0)
	glVertex3f(CAMERALENGTH/2 -HOTSHOE_LENGTH/2,CAMERAHEIGHT+HUBHEIGHT+HOTSHOE_HEIGHT,0)
	glVertex3f(CAMERALENGTH/2 -HOTSHOE_LENGTH/2,CAMERAHEIGHT+HUBHEIGHT+HOTSHOE_HEIGHT,-0.8*(CAMERAWIDTH/2))
	glVertex3f(CAMERALENGTH/2 -HOTSHOE_LENGTH/2,CAMERAHEIGHT+HUBHEIGHT,-0.8*(CAMERAWIDTH/2))
	glEnd()
	#right side of hot shoe
	glBegin(GL_QUADS)
	glVertex3f(CAMERALENGTH/2 +HOTSHOE_LENGTH/2,CAMERAHEIGHT+HUBHEIGHT,0)
	glVertex3f(CAMERALENGTH/2 +HOTSHOE_LENGTH/2,CAMERAHEIGHT+HUBHEIGHT+HOTSHOE_HEIGHT,0)
	glVertex3f(CAMERALENGTH/2 +HOTSHOE_LENGTH/2,CAMERAHEIGHT+HUBHEIGHT+HOTSHOE_HEIGHT,-0.8*(CAMERAWIDTH/2))
	glVertex3f(CAMERALENGTH/2 +HOTSHOE_LENGTH/2,CAMERAHEIGHT+HUBHEIGHT,-0.8*(CAMERAWIDTH/2))
	glEnd()
	#left top of hot shoe
	glBegin(GL_QUADS)
	glVertex3f(CAMERALENGTH/2 -HOTSHOE_LENGTH/2,CAMERAHEIGHT+HUBHEIGHT+HOTSHOE_HEIGHT,0)
	glVertex3f(CAMERALENGTH/2 -HOTSHOE_LENGTH/2,CAMERAHEIGHT+HUBHEIGHT+HOTSHOE_HEIGHT,-0.8*(CAMERAWIDTH/2))
	glVertex3f(CAMERALENGTH/2 -HOTSHOE_LENGTH/4,CAMERAHEIGHT+HUBHEIGHT+HOTSHOE_HEIGHT,-0.8*(CAMERAWIDTH/2))
	glVertex3f(CAMERALENGTH/2 -HOTSHOE_LENGTH/4,CAMERAHEIGHT+HUBHEIGHT+HOTSHOE_HEIGHT,0)
	glEnd()
	#right top of hot shoe
	glBegin(GL_QUADS)
	glVertex3f(CAMERALENGTH/2 +HOTSHOE_LENGTH/2,CAMERAHEIGHT+HUBHEIGHT+HOTSHOE_HEIGHT,0)
	glVertex3f(CAMERALENGTH/2 +HOTSHOE_LENGTH/2,CAMERAHEIGHT+HUBHEIGHT+HOTSHOE_HEIGHT,-0.8*(CAMERAWIDTH/2))
	glVertex3f(CAMERALENGTH/2 +HOTSHOE_LENGTH/4,CAMERAHEIGHT+HUBHEIGHT+HOTSHOE_HEIGHT,-0.8*(CAMERAWIDTH/2))
	glVertex3f(CAMERALENGTH/2 +HOTSHOE_LENGTH/4,CAMERAHEIGHT+HUBHEIGHT+HOTSHOE_HEIGHT,0)
	glEnd()
	
	#DRAW FILM ADVANCE WHEEL==================
	#Facing the camera, this is the wheel on the right side. 
	FILMADVANCE_RADIUS = 1.5
	FILMADVANCE_HEIGHT = 0.5
	
	twColor(darkGray,0,0)
	glPushMatrix()
	glTranslate(CAMERALENGTH - 2,CAMERAHEIGHT,0)
	glRotate(-90,1,0,0)
	twCylinder(FILMADVANCE_RADIUS,FILMADVANCE_RADIUS,FILMADVANCE_HEIGHT,20,20)
	twColor(lightGray,0,0)	
	glTranslate(0,0,FILMADVANCE_HEIGHT)
	twDisk(FILMADVANCE_RADIUS,20)					#Draws the top of the wheel
	glPopMatrix()
	
	#DRAW FILM ADVANCE LEVER==================
	#Facing the camera, this is the small polygon on the left side of the top of the camera.
	glPushMatrix()
	glTranslate(0.6,CAMERAHEIGHT,-(CAMERAWIDTH/8.0))
	glRotate(45,0,1,0)
	glScale(0.15,0.05,0.15)
	drawBody(bodyColor,bodyColor)		#lever segment 1
	glPopMatrix()
	glPushMatrix()
	glTranslate(0.65,CAMERAHEIGHT,-(CAMERAWIDTH/5.0))
	glRotate(-90,0,1,0)
	glScale(0.1,0.05,0.15)
	drawBody(bodyColor,bodyColor)		#lever segment 1
	glPopMatrix()
	
	
	#DRAW SHUTTER SETTING=====================
	#Facing the camera, this is the inside wheel on the left.
	SHUTTERSETTING_RADIUS = 1.25
	SHUTTERSETTING_HEIGHT = 0.5
	
	twColor(darkGray,0,0)
	glPushMatrix()
	glTranslate((CAMERALENGTH/2)/2,CAMERAHEIGHT,0)
	glRotate(-90,1,0,0)
	twCylinder(SHUTTERSETTING_RADIUS,SHUTTERSETTING_RADIUS,SHUTTERSETTING_HEIGHT,20,20)
	twColor(lightGray,0,0)	
	glTranslate(0,0,SHUTTERSETTING_HEIGHT)
	twDisk(SHUTTERSETTING_RADIUS,20)			#Draws the top of the wheel
	twColor(darkGray,0,0)
	twDisk(0.35*SHUTTERSETTING_RADIUS,20)		#Draws the shutter release button
	glPopMatrix()
	
	
	#DRAW ISO SETTING=========================
	#Facing the camera, this is the outside wheel on the left.
	ISOSETTINGS_RADIUS = 0.5
	ISOSETTINGS_HEIGHT = 0.3
	
	twColor(lightGray2,0,0)
	glPushMatrix()
	glTranslate(1,CAMERAHEIGHT,1)
	glRotate(-90,1,0,0)
	twTube(ISOSETTINGS_RADIUS,ISOSETTINGS_RADIUS,ISOSETTINGS_HEIGHT,20,20)
	glPopMatrix()
	
	#DRAW LIGHT METER=========================
	#Facing the camera, this is the light circle on the left of the front of the camera.
	LIGHTMETER_RADIUS = .4
	
	twColor(lightGray2,0,0)
	glPushMatrix()
	glTranslate(CAMERALENGTH/2 - (1.25*LENSRADIUS), CAMERAHEIGHT-1,CAMERAWIDTH/2)
	twDisk(LIGHTMETER_RADIUS,20)
	glPopMatrix()
	
	#DRAW FILM PREVIEW WINDOW=================
	#This is the small, vertical, rectangular window on the back of the camera.
	twColor(lightGray2,0,0)
	glBegin(GL_QUADS)
	glVertex3f(CAMERALENGTH-2,1,-CAMERAWIDTH/2)
	glVertex3f(CAMERALENGTH-2.5,1,-CAMERAWIDTH/2)
	glVertex3f(CAMERALENGTH-2.5,CAMERAHEIGHT-1,-CAMERAWIDTH/2)
	glVertex3f(CAMERALENGTH-2,CAMERAHEIGHT-1,-CAMERAWIDTH/2)
	glEnd()
	
	
	#Upon completetion of the camera, the origin is moved to the middle of the bottom of the camera
	glTranslate(CAMERALENGTH/2,0,0)
	
	# Mark the origin
	glPointSize(5);
	twColorName(TW_MAGENTA);
	glBegin(GL_POINTS);
	glVertex3f(0,0,0);
	glEnd();
    
def drawBody(colorSide,colorTop):
	#Draws the camera body.  Takes two arguments, one for the color of the sides of the camera
	#and one for the color of the top and bottom of the camera.
	
	global CAMERALENGTH,CAMERAWIDTH,CAMERAHEIGHT
	
	
	bodyBottomFront = [													
						#origin is at the left-side middle
						[0,0,(CAMERAWIDTH/2)/2],					#left-side right
						[1,0,CAMERAWIDTH/2],						#front left
						[CAMERALENGTH - 1, 0,CAMERAWIDTH/2],		#front right
						[CAMERALENGTH,0,(CAMERAWIDTH/2)/2] ]		#right-side left
						
	#Creates array of all bottom vertices			
	bodyBottomBack = map( lambda v: [v[0], v[1], -v[2] ],bodyBottomFront )
	#Reversed so that all vertices are listed in a counter-clockwise direction
	bodyBottomBack.reverse()
	bodyBottomFront.extend(bodyBottomBack) 
	
	#Creates array of all bottom and top vertices
	bodyTop = map( lambda v: [v[0], v[1] + CAMERAHEIGHT, v[2]],bodyBottomFront )
	bodyBottomFront.extend(bodyTop)
    
	body = bodyBottomFront	#Renamed for convenience
    #body now has a length of 16, corresponding to all the vertices of the body of the camera
    #the bottom vertices are indexed 0-7; the top vertices, 8-15
    #bottom front indices: 0-3; bottom back indices: 4-7
    #top front indicies: 8-11; top back indices: 12-15
    
	twColor(colorSide,0,0)
	drawQuad(body,0,1,9,8)			#left-front angled side
	drawQuad(body,1,2,10,9)			#front
	drawQuad(body,2,3,11,10)		#right-front angled side
	drawQuad(body,3,4,12,11)		#right side
	drawQuad(body,4,5,13,12)		#right-back angled side
	drawQuad(body,5,6,14,13)		#back
	drawQuad(body,6,7,15,14)		#left-back angled side
	drawQuad(body,7,0,8,15)			#left side
	
	#body top covering
	twColor(colorTop,0,0)
	drawQuad(body,9,10,13,14)
	drawQuad(body,8,11,12,15)
	glBegin(GL_TRIANGLES)							#top left triangle
	glVertex3fv( body[15])
	glVertex3f(1,CAMERAHEIGHT,-(CAMERAWIDTH/2)/2)
	glVertex3fv(body[14])
	glEnd()
	glBegin(GL_TRIANGLES)							#bottom left triangle
	glVertex3fv( body[9])
	glVertex3f(1,CAMERAHEIGHT,(CAMERAWIDTH/2)/2)
	glVertex3fv(body[8])
	glEnd()
	glBegin(GL_TRIANGLES)							#bottom right triangle
	glVertex3fv( body[11])
	glVertex3f(CAMERALENGTH-1,CAMERAHEIGHT,(CAMERAWIDTH/2)/2)
	glVertex3fv(body[10])
	glEnd()	
	glBegin(GL_TRIANGLES)							#top right triangle
	glVertex3fv( body[13])
	glVertex3f(CAMERALENGTH-1,CAMERAHEIGHT,-(CAMERAWIDTH/2)/2)
	glVertex3fv(body[12])
	glEnd()
	
	#body bottom covering
	drawQuad(body,1,2,5,6)
	drawQuad(body,0,3,4,7)
	glBegin(GL_TRIANGLES)							#top left triangle
	glVertex3fv(body[7])
	glVertex3f(1,0,-(CAMERAWIDTH/2)/2)
	glVertex3fv(body[6])
	glEnd()
	glBegin(GL_TRIANGLES)							#bottom left triangle
	glVertex3fv(body[1])
	glVertex3f(1,0,(CAMERAWIDTH/2)/2)
	glVertex3fv(body[0])
	glEnd()
	glBegin(GL_TRIANGLES)							#bottom right triangle
	glVertex3fv(body[3])
	glVertex3f(CAMERALENGTH-1,0,(CAMERAWIDTH/2)/2)
	glVertex3fv(body[2])
	glEnd()	
	glBegin(GL_TRIANGLES)							#top right triangle
	glVertex3fv(body[5])
	glVertex3f(CAMERALENGTH-1,0,-(CAMERAWIDTH/2)/2)
	glVertex3fv(body[4])
	glEnd()
	
	
def drawQuad(verts,a,b,c,d):
    glBegin(GL_QUADS)
    glVertex3fv(verts[a])
    glVertex3fv(verts[b])
    glVertex3fv(verts[c])
    glVertex3fv(verts[d])
    glEnd()
    
def display():
	twDisplayInit()
	twCamera()

	amckennaCamera()

	glFlush()
	glutSwapBuffers()      
        
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(500, 500)
	glutCreateWindow(sys.argv[0])
	glutDisplayFunc(display)
	twBoundingBox(0,CAMERALENGTH,
				0,CAMERAHEIGHT + HUBHEIGHT,
				-CAMERAWIDTH/2,CAMERAWIDTH/2 + LENSLENGTH)
	twMainInit()
	glutMainLoop()
  
if __name__ == '__main__':
	main()
