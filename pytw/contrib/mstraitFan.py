'''
AUTHOR: Megan Strait
LAST MODIFIED: Oct 11, 2009

DESCRIPTION:
Creates a fan object whose blades can rotate (ported from Micquie Bradford's Object for the C Object Library).

'''


import sys

try:
  from TW import *
except:
  print '''ERROR: Couldn't import TW.'''

# VARIABLES
# rgb colors
bladeColor = (0.29,0.29,0.29);		# light gray
cageColor = (0.12,0.12,0.12);		# dark gray
fanColor = (0.2,0,0);				# dark red

# blade vertices
blade = [ [1,4.5,-1],
		[6,6,-6],
		[9,6,-1],
		[1,4.5,0] ]

# rotation
rotA = 0;

def drawCage():						# draws the wire cage around the fan blades using one large torus for the frame, loops to create four smaller toruses of equal size, and rotates accordingly to place them around the frame
    glPushMatrix();
    glTranslatef(0,6,0);
    glRotatef(90,1,0,0);
    glutWireTorus(0.05,10,50,50);
    for i in range(1,5):
      glPushMatrix();
      glRotatef(i*40,0,0,1);		# rotate around z-axis to place around frame
      glRotatef(90,1,0,0);			# rotate around x-axis
      glScalef(1,0.3,1);
      glutWireTorus(0.05,10,50,50);
      glPopMatrix();
    glPopMatrix();
    
def drawBlades():					# draws four blades in a loop using the blade vertices defined, and rotates around the y-axis to place them around the frame
    glPushMatrix();
    for i in range(1,5):
      glRotatef(90,0,1,0);
      glBegin(GL_POLYGON);
      glVertex3fv(blade[0]);
      glVertex3fv(blade[1]);
      glVertex3fv(blade[2]);
      glVertex3fv(blade[3]);
      glEnd();
    glPopMatrix();

def drawFan():
    glPushMatrix();
    
    twColor(fanColor,0,0);
    glPushMatrix();
    glTranslatef(10,5,-10);
    glRotatef(90,1,0,0);
    twTube(8,8,1,30,30);		# very bottom of base
    
    glTranslatef(0,0,-1);		# upper base level
    twTube(7,7,1,30,30);
    
    glTranslatef(0,0,-10);		# standing part of base
    twTube(2,6,10,30,30);
    
    glTranslatef(0,0,-2);
    
    glPushMatrix();				# sphere center behind wire frame
    glScalef(0.8,1,0.8);
    glutSolidSphere(4,20,20);
    glPopMatrix();
    
    glPushMatrix();				# isolate positioning of fan head
    glTranslatef(0,4,0);
    glRotatef(90,0,1,0);
    glRotatef(90,1,0,0);
    twTube(2,3,4,30,30);
    glTranslatef(0,0,-0.8);
    twColor(cageColor,0.3,0.6);
    twTube(1,1,0.8,30,30);
    glPopMatrix();
  
    drawCage();					# create the cage
    
    twColor(bladeColor,3,2);	# place the blades on the front of the fan head
    glRotatef(rotA,0,1,0);
    drawBlades();
    glPopMatrix();				# pop from origin in progress
    
    glPopMatrix();				# final pop

def display():
    twDisplayInit();
    twCamera();
    
    lightPos = [0,25,10,0];		# adjust the lighting so that each part of the fan is defined
    twGrayLight(GL_LIGHT1,lightPos,0,1.0,1);
    
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT1);
    glShadeModel(GL_SMOOTH);
    twAmbient(3);

    drawFan();

    glFlush();
    glutSwapBuffers();
    
def rotateFan(key, x, y):		# allow the blades to rotate
	global rotA
	if key == '+':
		rotA -= 15;
	glutPostRedisplay();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(0,20,5,30,0,-20);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    twKeyCallback('+',rotateFan,"rotate fan");
    glutMainLoop()

if __name__ == '__main__':
  main()
