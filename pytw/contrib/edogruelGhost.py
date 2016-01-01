##*********** Ghost Object ************

##An OpenGL model of a ghost. 
##Copyright (C) 2006 by Eylul Dogruel/autumnus.net
##This program is released under the GNU General Public Licence.

##fully customizible ghost. 
##Ghosts handle is at the center of where the bottom surface would be
##if ghost is perfectly straight. 

##All sizes and rotations are relative
##for rotations 0 is always the default
##1/-1 is the max/min values that can be kept for a normal looking figure
##e.g. eyeRotateY=1 looks to right but eyeRotateY=1.5 has no visible iris
##the angles are all relative to the previous piece. 
##e.g if chest rotates, everything below chest moves so that body in itself 
##is straight. If torso moves, chest remains in place but legs and hips move.

##for sizes default proportions is always 1. 


##Height: height of the whole figure. Default is 1. (6 Units)
##headHeight: height of the head. Default is 1. (1.2 unit)
##headWidth: width of the head. Default is 1. (1.1 unit)

##neckAngle:XYZ rotation of the neck around the connection of chest and neck
##headAngle: XYZ rotation of the head around the connection of neck and head
##eyeRotateX: if eye is looking up or down
##eyeRotateY: if eye is looking left or right

##chestAngle: the XYZ rotation of chest around the connection of neck and chest
##torsoAngle: the XYZ rot. of torso around the connection of chest and torso
##hipAngle: the XYZ rot. of hip around the connection of torso and hips
##legAngle: the XYZ rot. of legs around the connection of leg and hips

##gColorSkin: RGB color of head and neck
##gColorDress: color of the rest of the body
##gColorEye: color of the eyeball
##gColorIris: color of the iris of the eye
##gColorHair: color of the hair 

##iRotationP: internal rotation point. The joint that stays fixed
##while the rest of the pieces move depending on its position
##this is a future addition. Only one option is implemented at the moment
##so the input is not checked
##0: Bottom (same as the handle)
##1: knees (between legs and hips)
##2: waist (between hips and torso)
##3: center (between torso and chest)
##4*: shoulders (between chest and neck)
##5: chin (between neck and head)
##6: top (above head)

#include <math.h>

import sys

try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print '''
ERROR: PyOpenGL not installed properly.  
        '''

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.

        '''

def draw_Eye(eyeRotateX,eyeRotateY, gColorIris, slices, stacks, rotDegree):
  glutSolidSphere(.5,slices,stacks);
  glPushMatrix();
  glRotatef(eyeRotateX*30,1,0,0);
  glRotatef(eyeRotateY*15,0,1,0);
  if rotDegree>=0:
    glRotatef(rotDegree,.4,1,0); ##rotate left
    glTranslatef(0,0,-.4);
    glRotatef(-rotDegree,.4,1,0); ##rotate left
  else:
    glRotatef(rotDegree,-.4,1,0); ##rotate left
    glTranslatef(0,0,-.4);
    glRotatef(-rotDegree,-.4,1,0); ##rotate left 
  twColor(gColorIris,0,0);
  glutSolidTorus(.15,.28,4,stacks);
  holeColor = (0.0,0.0,0.0);
  twColor(holeColor,0,0);
  glutSolidSphere(.30,slices,stacks);
  glPopMatrix();


def draw_Head(rHeight, rWidth,
	        eyeRotateX, eyeRotateY,
	       gColorEye, gColorIris,
	       slices, stacks, haircolor ):
  ##draw the low half (inside of the head)
  glPushMatrix();
  glTranslatef(0,0,-rWidth*.2); ##chin should be a little in front of the center
  glScalef(rWidth*.8, rHeight, rWidth*.8);
  glutSolidSphere(.5,slices,stacks);
  glPopMatrix();
  
  ##draw left eye
  glPushMatrix();
  glRotatef(-18,.4,1,0); ##rotate left
  glTranslatef(0,0,-math.sqrt(rWidth*rHeight)/2); ##move to surface of the face
  glScalef(rWidth/2.3,rHeight/2.3,rHeight/7); ##scale the eye
  glRotatef(18,.4,1,0); ##look ahead
  twColor(gColorEye,0,0); ##set color to eyeball color
  draw_Eye(eyeRotateX,eyeRotateY,gColorIris,slices,stacks,-18); 
  glPopMatrix();

  ##draw right eye
  glPushMatrix();
  glRotatef(18,-.4,1,0); ##rotate right
  glTranslatef(0,0,-math.sqrt(rWidth*rHeight)/2); ##move to surface of the face
  glScalef(rWidth/2.3,rHeight/2.3,rHeight/7); ##scale the eye
  glRotatef(-18,-.4,1,0); ##look ahead
  twColor(gColorEye,0,0); ##set color to eyeball color
  draw_Eye(eyeRotateX,eyeRotateY,gColorIris,slices,stacks,18); 
  glPopMatrix();

  ##move to upper half to draw hair
  glTranslatef(0,-rHeight/4,0);


  ##draw hair
  glPushMatrix();
  twColor(haircolor,0,0);
  glScalef(rWidth, rHeight/1.5,rWidth);
  glutSolidSphere(.5,slices,stacks);
  glPopMatrix();

  glTranslatef(0,0,rWidth*.6/3);
  glPushMatrix();
  glScalef(rWidth, -rHeight*2,rWidth/2);
  twSolidCylinder(.5,.7,1,slices,stacks);
  glPopMatrix();
  ##draw rest of the hair
  


def eylul_Ghost(height,headHeight, headWidth,
		  neckAngle, headAngle,
		  eyeRotateX,  eyeRotateY,
		  chestAngle, torsoAngle,
		  hipAngle, legAngle,
		  gColorSkin,  gColorDress,
		  gColorEye,  gColorIris, 
		  gColorHair, iRotationP
		  ):
  slices = 30; ## roundness 
  stacks = 30; ## roundness - another dimension from slice

  ##sizes in real units, diameters and heights (no radii)

  rHeight = 6*height; ##height in units
  rHeadHeight = 1.2*headHeight; ##head hight in units
  rHeadWidth = 1.1*headWidth; ##head width in units    
  neckH = (height+headHeight)/5; ##average of proportions*.33 

  ##there are four body pieces. Legs,hip, torso,chest. 
  pieceH = (rHeight -(rHeadHeight+neckH))/10.0;    ##just a unit height
  maxW = 1; ##bottom of skirt, shoulders
  midW = .8;
  minW = .6; ##z axis and 2*the width of neck
  
  

    
  ##move position to rotation center:between neck and chest 
  glPushMatrix();
  glTranslatef(0,pieceH*10,0);
  
  ##start drawing neck and head
  glPushMatrix();
  ##make the cylinder around y axis, and 
  ##add any additional changes to the angle with hardwired constants
  glRotatef(180,1,0,0);
  glRotatef(neckAngle[0]*20,1,0,0);
  glRotatef(neckAngle[2]*20,0,1,0);
  glRotatef(neckAngle[1]*180,0,0,1);
  ##draw the neck in the skin color
  twColor(gColorSkin, 0, 0); ##skin color
  glutSolidSphere(minW/3,slices,stacks);##connection point
  twSolidCylinder(minW/3,minW/3,neckH,slices, stacks); ##neck

  glTranslatef(0,-neckH,0); ##move to the other end of the neck
  glutSolidSphere(minW/3, slices, stacks); ##connection point
  ##draw the head
  glTranslatef(0,-rHeadHeight/2,0); ##move to the center of the head
 

  ##rotate head, keep in mind that now top of the head is on +z
  ##so x remains same, y becomes -z, z becomes y
  glRotatef(headAngle[0]*20,1,0,0);
  glRotatef(headAngle[1]*180,0,1,0);
  glRotatef(headAngle[2]*40,0,0,1);


  ##draw the head
  draw_Head(rHeadHeight, rHeadWidth,
	    eyeRotateX, eyeRotateY,
	    gColorEye, gColorIris,
	    slices, stacks, gColorHair);

  
  ##go back to center
  glPopMatrix();


  ##start drawing the body
  twColor(gColorDress,0,0); ##dress color
  ##glRotatef(90,1,0,0); ## now -Y is the Z axis
  
  ##start drawing the chest
  glRotatef(chestAngle[0]*25,1,0,0);
  glRotatef(chestAngle[1]*30,0,1,0);
  glRotatef(chestAngle[2]*10,0,0,1);  

  ##draw the first connector/shoulders
  glPushMatrix();
  glScalef(maxW,minW,minW);
  glutSolidSphere(.5,slices,stacks);
  glPopMatrix();

  ##draw the chest
  glPushMatrix();
  glScalef(maxW,pieceH*2,minW);
  twSolidCylinder(.5,(midW/maxW)*.5,1,slices,stacks);
  glPopMatrix();
  

  ##move to the other end of the chest
  glTranslatef(0,-pieceH*2,0);

  ##do the half of the rotation for the connector
  glRotatef((torsoAngle[0]*25)/2,1,0,0);
  glRotatef((torsoAngle[1]*30)/2,0,1,0);
  glRotatef((torsoAngle[2]*10)/2,0,0,1);
  

  ##draw the connector between chest and the torso
  glPushMatrix();
  glScalef(midW,minW,minW);
  glutSolidSphere(.5,slices,stacks);
  glPopMatrix();


  ##do the rest of the rotation for the torso
  glRotatef((torsoAngle[0]*25)/2,1,0,0);
  glRotatef((torsoAngle[1]*30)/2,0,1,0);
  glRotatef((torsoAngle[2]*10)/2,0,0,1);


  ##draw the torso
  glPushMatrix();
  glScalef(midW,pieceH*2,minW);
  twSolidCylinder(.5,.5,1,slices,stacks);
  glPopMatrix();

  ##move to the other end of the torso
  glTranslatef(0,-pieceH*2,0);
  
  ##do the half of the rotation for the connector
  glRotatef((hipAngle[0]*25)/2,1,0,0);
  glRotatef((hipAngle[2]*10)/2,0,1,0);
  glRotatef((hipAngle[1]*30)/2,0,0,1);

  ##draw the connector between the torso and hips
  glPushMatrix();
  glScalef(midW,minW,minW);
  glutSolidSphere(.5,slices,stacks);
  glPopMatrix();

  ##do the rest of the rotation for the hips
  glRotatef((hipAngle[0]*25)/2,1,0,0);
  glRotatef((hipAngle[2]*10)/2,0,1,0);
  glRotatef((hipAngle[1]*30)/2,0,0,1);

  
  ##draw the hips
  glPushMatrix();
  glScalef(midW,pieceH*3,minW);
  twSolidCylinder(.5,(minW/midW)*0.5,1,slices,stacks);
  glPopMatrix();

  ##move to the other end of the hips
  glTranslatef(0,-pieceH*3,0);

  ##do the half of the rotation for the connector
  glRotatef((legAngle[0]*25)/2,1,0,0);
  glRotatef((legAngle[2]*10)/2,0,1,0);
  glRotatef((legAngle[1]*30)/2,0,0,1);

  ##draw the connector between hips and legs
  glPushMatrix();
  glScalef(minW,minW,minW);
  glutSolidSphere(.5,slices,stacks);
  glPopMatrix();

  ##do the rest of the rotation for the legs
  glRotatef((legAngle[0]*25)/2,1,0,0);
  glRotatef((legAngle[2]*10)/2,0,1,0);
  glRotatef((legAngle[1]*30)/2,0,0,1);
  
  
  ##draw the legs
  glPushMatrix();
  glScalef(minW,pieceH*2,minW);
  twSolidCylinder(.5,(midW/minW)*0.5,1,slices,stacks);
  glPopMatrix();

  ##move past the legs
  glTranslatef(0,-pieceH*2,0);
  
  ##draw the bottom of the skirt
  
  glScalef(midW,pieceH,minW);
  twSolidCylinder(.5,(maxW/midW)*.5,1,slices,stacks);

  ##move back to bottom with correct orientation
  glPopMatrix();

skinColor = (125.0/255.0, 125.0/255.0, 125.0/255.0); ## light gray
dressColor = (95.0/255.0, 95.0/255.0, 95.0/255.0); ## dark gray
irisColor = (1.0,0.5,0.5); ##pink

hairColor = (0.0,0.0,0.0); ##black
eyeColor = (1.0,1.0,1.0); ##white


nAng = (0,0,0); ##neck angle
hAng = (0,0,0); ##head angle
cAng = (0,0,0); ##chest angle
tAng = (0,0,0); ##torso angle
hipAng = (0,0,0); ##hip angle
lAng = (0,0,0); ##leg angle


def display(): 
  twDisplayInit();
  twCamera(); ## sets up camera based on bounding box coordinates
  
  ## draw the imported object - ghost 
  eylul_Ghost( 1.0, 1.0, 1.0,
               nAng, hAng,
               0, 0,
               cAng, tAng,
               hipAng, lAng,
               skinColor, dressColor,
               eyeColor, irisColor, 
               hairColor, 4
               );
  
  glFlush();
  glutSwapBuffers();


def main() :
  glutInit(sys.argv);
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
  twInitWindowSize(500,500);
  glutCreateWindow(sys.argv[0]);
  glutDisplayFunc(display);
  twVertexArray([(-2,0,0),(2,0,0),(0,-4,0),(0,4,0),(0,0,-2),(0,0,2)]);
  twMainInit();            
  glutMainLoop();


if __name__ == '__main__':
  main()
