# Ariana Rizzitano
# CS307 Fall 2009
# Assignment 4: Creative Scene

import sys
import math                     # for sqrt

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''

# constants for the clock's dimensions	
CLOCKWIDTH = 6
CLOCKDEPTH = 4
CLOCKHEIGHT = 12
    
CLOCKCOLOR = (0.54, 0.21, 0.06) # color of clock's main body
DOORCOLOR = (0.5, 0.17, 0.02)	# color of doorframe
FACECOLOR = (1, 0.98, 0.8)		# color of clock face
PENDULUMCOLOR = (1,0.84,0)		# color of pendulums and clock guts

# used to move clock elements above the origin
TRANSLATESIZE = CLOCKHEIGHT/2

def arizzitaClock():	
	'''Draws a grandfather clock, facing the viewer, with the origin at the 
	bottom back of the inner chamber. The dimensions and bounding box are based 
	on the size constants defined above.'''
	
	glPushMatrix()
   	
   	# origin cube
	glPushMatrix()
	twColor((1.0, 0, 1.0), 0, 0)
	glutSolidCube(1)
	glPopMatrix()
   	
   	'''Middle part of the clock'''
   	
	# back panel
	glPushMatrix()
	twColor(CLOCKCOLOR,0.8,10)
	glTranslatef(0,TRANSLATESIZE,0)
	glScalef(CLOCKWIDTH*2/3,CLOCKHEIGHT,1)
	glutSolidCube(1)
	glPopMatrix()
	
	# right outer panel
	glPushMatrix()
	glTranslatef(CLOCKWIDTH/2.5,TRANSLATESIZE,CLOCKDEPTH/3)
	glScalef(1,CLOCKHEIGHT,CLOCKDEPTH*3/4)
	glutSolidCube(1)
	glPopMatrix()
	
	# right inner panel
	glPushMatrix()
	glTranslatef(CLOCKWIDTH/3.5,TRANSLATESIZE,CLOCKDEPTH*2/3)
	glScalef(0.5,CLOCKHEIGHT,CLOCKDEPTH*3/4)
	glutSolidCube(1)
	glPopMatrix()
	
	# left outer panel
	glPushMatrix()
	glTranslatef(-CLOCKWIDTH/2.5,TRANSLATESIZE,CLOCKDEPTH/3)
	glScalef(1,CLOCKHEIGHT,CLOCKDEPTH*3/4)
	glutSolidCube(1)
	glPopMatrix()
	
	# left inner panel
	glPushMatrix()
	glTranslatef(-CLOCKWIDTH/3.5,TRANSLATESIZE,CLOCKDEPTH*2/3)
	glScalef(0.5,CLOCKHEIGHT,CLOCKDEPTH*3/4)
	glutSolidCube(1)
	glPopMatrix()
	
	# right cylinder
	glPushMatrix()
	glTranslatef(CLOCKWIDTH/2.5,CLOCKHEIGHT,CLOCKDEPTH*3/4)
	glScalef(1,1,1)
	twSolidCylinder(.5,.5,CLOCKHEIGHT,20,20)
	glPopMatrix()
	
	# left cylinder
	glPushMatrix()
	glTranslatef(-CLOCKWIDTH/2.5,CLOCKHEIGHT,CLOCKDEPTH*3/4)
	glScalef(1,1,1)
	twSolidCylinder(.5,.5,CLOCKHEIGHT,20,20)
	glPopMatrix()
	
	twColor(DOORCOLOR,0.8,10)
	# right front panel
	glPushMatrix()
	glTranslatef(CLOCKWIDTH/4.15,TRANSLATESIZE,CLOCKDEPTH-0.5)
	glScalef(0.75,CLOCKHEIGHT,0.6)
	glutSolidCube(1)
	glPopMatrix()
	
	# left front panel
	glPushMatrix()
	glTranslatef(-CLOCKWIDTH/4.15,TRANSLATESIZE,CLOCKDEPTH-0.5)
	glScalef(0.75,CLOCKHEIGHT,0.6)
	glutSolidCube(1)
	glPopMatrix()
	
	# top front panel
	glPushMatrix()
	glTranslatef(0,CLOCKHEIGHT,CLOCKDEPTH-0.5)
	glScalef(CLOCKWIDTH*2/3,1,0.6)
	glutSolidCube(1)
	glPopMatrix()
	
	# bottom front panel
	glPushMatrix()
	glTranslatef(0,0.5,CLOCKDEPTH-0.5)
	glScalef(CLOCKWIDTH*2/3,1,0.6)
	glutSolidCube(1)
	glPopMatrix()
	
	twColor(CLOCKCOLOR,0.8,10)
	# base 
	glPushMatrix()
	glTranslatef(0,0,(CLOCKDEPTH/2.5))
	glScalef(CLOCKWIDTH,CLOCKHEIGHT/5,CLOCKDEPTH+CLOCKDEPTH/6)
	glutSolidCube(1)
	glPopMatrix()
	
	'''The pendulums'''
	
	twColor(PENDULUMCOLOR,0.9,30)
	# middle pendulum
	glPushMatrix()
	glTranslatef(0,CLOCKHEIGHT/1.3,CLOCKDEPTH*1/3)
	glScalef(1,1,1)
	twSolidCylinder(.5,.5,CLOCKHEIGHT/4,20,20)
	glPopMatrix()
	
	# right pendulum
	glPushMatrix()
	glTranslatef(CLOCKWIDTH/6,CLOCKHEIGHT/1.3,CLOCKDEPTH*1/3)
	glScalef(1,1,1)
	twSolidCylinder(.5,.5,CLOCKHEIGHT/4,20,20)
	glPopMatrix()
	
	# left pendulum
	glPushMatrix()
	glTranslatef(-CLOCKWIDTH/6,CLOCKHEIGHT/1.3,CLOCKDEPTH*1/3)
	glScalef(1,1,1)
	twSolidCylinder(.5,.5,CLOCKHEIGHT/4,20,20)
	glPopMatrix()
	
	# round thing
	glPushMatrix()
	glTranslatef(0,CLOCKHEIGHT/3,CLOCKDEPTH*1/2)
	glScalef(1,1,1)
	glRotatef(90,1,0,0)
	twSolidCylinder(1,1,0.5,20,20)
	glPopMatrix()
	
	# middle chain
	glPushMatrix()
	glTranslatef(0,CLOCKHEIGHT,CLOCKDEPTH*1/3)
	glScalef(1,1,1)
	twSolidCylinder(0.1,0.1,CLOCKHEIGHT/1.5,5,5)
	glPopMatrix()
	
	# right chain
	glPushMatrix()
	glTranslatef(CLOCKWIDTH/6,CLOCKHEIGHT,CLOCKDEPTH*1/3)
	glScalef(1,1,1)
	twSolidCylinder(0.1,0.1,CLOCKHEIGHT/2,5,5)
	glPopMatrix()
	
	# left chain
	glPushMatrix()
	glTranslatef(-CLOCKWIDTH/6,CLOCKHEIGHT,CLOCKDEPTH*1/3)
	glScalef(1,1,1)
	twSolidCylinder(0.1,0.1,CLOCKHEIGHT/2,5,5)
	glPopMatrix()
	
	'''Top part of the clock'''
	
	# middle lip
	twColor(CLOCKCOLOR,0.8,10)
	glPushMatrix()
	glTranslatef(0,CLOCKHEIGHT+0.5,(CLOCKDEPTH/2.5))
	glScalef(CLOCKWIDTH,CLOCKHEIGHT/8,CLOCKDEPTH+CLOCKDEPTH/6)
	glutSolidCube(1)
	glPopMatrix()
	
	# main block
	glPushMatrix()
	glTranslatef(0,CLOCKHEIGHT*1.25,CLOCKDEPTH/3.5)
	glScalef(CLOCKWIDTH,CLOCKHEIGHT/3,CLOCKDEPTH*3/4)
	glutSolidCube(1)
	glPopMatrix()
	
	# right cylinder
	glPushMatrix()
	glTranslatef(CLOCKWIDTH/2.5,CLOCKHEIGHT*1.4,CLOCKDEPTH*3/4)
	glScalef(1,1,1)
	twSolidCylinder(.5,.5,CLOCKHEIGHT/3,20,20)
	glPopMatrix()
	
	# left cylinder
	glPushMatrix()
	glTranslatef(-CLOCKWIDTH/2.5,CLOCKHEIGHT*1.4,CLOCKDEPTH*3/4)
	glScalef(1,1,1)
	twSolidCylinder(.5,.5,CLOCKHEIGHT/3,20,20)
	glPopMatrix()
	
	# middle lip
	glPushMatrix()
	glTranslatef(0,CLOCKHEIGHT*1.4,(CLOCKDEPTH/2.5))
	glScalef(CLOCKWIDTH,CLOCKHEIGHT/8,CLOCKDEPTH+CLOCKDEPTH/6)
	glutSolidCube(1)
	glPopMatrix()
	
	# top crest thingy
	glPushMatrix()
	glTranslatef(0,CLOCKHEIGHT*1.4,CLOCKDEPTH/1.6)
	glScalef(1,1,1)
	glRotatef(90,1,0,0)
	twSolidCylinder(2,2,1,20,20)
	glPopMatrix()
	
	'''Face of the clock'''
	
	# face
	
	twColor(FACECOLOR,0.9,15)
	glPushMatrix()
	glTranslatef(0,CLOCKHEIGHT*1.22,CLOCKDEPTH/1.4)
	glScalef(1,1,1)
	glRotatef(90,1,0,0)
	twSolidCylinder(1.5,1.5,1,20,20)
	
	# center nub thing
	twColor((0,0,0),0.5,10)
	glPushMatrix()
	glTranslatef(0,0.25,0)
	twSolidCylinder(0.2,0.2,1,10,10)
	glPopMatrix()
	
	# minute hand
	glPushMatrix()
	glTranslatef(0,0.15,-0.7)
	glScalef(0.25,0.15,1)
	glutSolidCube(1)
	glPopMatrix()
	
	# hour hand
	glPushMatrix()
	glTranslatef(0.5,0.15,0)
	glScalef(0.7,0.15,0.25)
	glutSolidCube(1)
	glPopMatrix()
	
	glPopMatrix()
    
	glPopMatrix();                # final pop

def setLight():
	# define lighting for scene
	twAmbient(0.5)
	light0 = ( 20, 20, 20, 1 )
	twGrayLight(GL_LIGHT0, light0, 0.1, 0.7, 0.7)
	glEnable(GL_LIGHT0)

def display():
    twDisplayInit();
    twCamera();
    
    # glPushAttrib(GL_ALL_ATTRIB_BITS);
    glEnable(GL_LIGHTING);
    glShadeModel(GL_SMOOTH);
        
    setLight()
    arizzitaClock();

    glFlush();
    glutSwapBuffers();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-(CLOCKWIDTH/2),(CLOCKWIDTH/2),-CLOCKHEIGHT/5,CLOCKHEIGHT*1.6,0,CLOCKDEPTH+0.5);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
  main()


