#Ported to Python file by Anna Loparev
#CS307
#Homework 2
#10/12/09

#Created by Christina Pong
#Origami Crane
#pset 4 for cs307

#Origami Crane by Christina Pong
#
#cpongOrigamiCrane();
#Draws an origami crane.  
#By default, you see the crane from the side with the head facing toward the right.
#Values are scaled based on the head.  Crane can be scaled via affine transformations.
#Default color at the moment is shades of white.  Lighting will be added soon.
#The origin is the bottom of the crane so the crane can be placed on a surface. 
#In the event that you want to hang the crane off an object via the top of the body,
#the body of the crane is 25/3 units high and  you can translate down by that amount. 

#---------------------------------------------------------------------------------------

import sys
import math

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''

try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print '''
ERROR: PyOpenGL not installed properly.
        '''

#supposed length of the head.  Everything scales to this
head = 10
#the width when looking straight on at the crane's head
#I also think of this as the "poufiness" of the model :)
width = head/5

#the angle of the wings
angle = 45
#height of the tip of the wing
wingTip = head*2
#height of the middle point of the wing
wingMid = head*0.7
#height of the point of the bottom fold
wingFold = head/5

#height of point where these folds meet
intersection = head/4
#distances the top fold from the wing so you can see it
topOffset = head/20
#distances the bottom fold from the top fold
bottomOffset = head/18

#using a vertex array to create half a crane: half a head, body, and tail 
#  as well as one wing.
crane = (
    #the center vertices
    (-head*2,head*.75,0),        #[0] tip of the beak
    (-head*1.2,head*1.2,0),      #[1] top of the head
    (0,head*.8,0),               #[2] top of the body
    (0,head/7,0),                #[3] bottom of the body (middle)
    (head*2,head*2,0),           #[4] tip of the tail
    
    #front side of the body
    (-head/2,head*.5,width),          #[5] top left
    (-head/2+(head/10),0,head/15),    #[6] bottom left
    (0,head/7,head/15),               #[7] middle
    (head/2-(head/10),0,head/15),     #[8] bottom right
    (head/2,head*.5,width),           #[9] top right

    #points for the neck and head
    (-head*1.1,head*1.2,head/15),   #[10] right top of neck
    (-head*1.3,head*1.2,head/15),   #[11] left top of neck  
    (-head*1.2,head*1.2,0),         #[12] center of top of head
    
    #wing coordinates based on wing angle
    ((-(head/2)-(head/10)),wingMid*math.sin(math.radians(angle)),wingMid*math.cos(math.radians(angle))),  #[13] left wing
    (((head/2)+(head/10)),wingMid*math.sin(math.radians(angle)),wingMid*math.cos(math.radians(angle))),   #[14] right wing
    (0,wingTip*math.sin(math.radians(angle)),wingTip*math.cos(math.radians(angle))),                      #[15] tip of the wing

    #points for the top folds on the wings
    ((-(head/2)-(head/10)),wingMid*math.sin(math.radians(angle)),(wingMid*math.cos(math.radians(angle)))+topOffset),    #[16] left top fold point
    (((head/2)+(head/10)),wingMid*math.sin(math.radians(angle)),wingMid*math.cos(math.radians(angle)) + topOffset),     #[17] right top fold point
    (-head/2+(head/10),0,head/15 + topOffset),                                                                          #[18] left bottom corner 
    (head/2-(head/10),0,head/15 + topOffset),                                                                           #[19] right bottom corner 
    (0,intersection*math.sin(math.radians(angle)),intersection*math.cos(math.radians(angle))+topOffset),                #[20] where the above meet

    #points for the bottom folds on the wings
    (-(head/2),wingFold*math.sin(math.radians(angle)),wingFold*math.cos(math.radians(angle))+ bottomOffset),               #[21] left bottom fold
    (head/2,wingFold*math.sin(math.radians(angle)),wingFold*math.cos(math.radians(angle))+ bottomOffset),                  #[22] right bottom fold 
    (-head/2+(head/10),0,head/15 + bottomOffset),                                                                          #[23] left bottom corner 
    (head/2-(head/10),0,head/15 + bottomOffset),                                                                           #[24] right bottom corner 
    (0,intersection*math.sin(math.radians(angle)),intersection*math.cos(math.radians(angle))+bottomOffset),                #[25] where the above meet 
    (0,head/7,bottomOffset),                                                                                               #[26] the bottom middle
              
    #this point makes the body poof out
    (0,head*.5,width),  #[27]
  );

def centerLine():
  #function used to help visualize the points when making the crane
  #this line connects the center vertices
  twColorName(TW_BLACK);
  glLineWidth(2);
  
  glBegin(GL_LINES);

  glVertex3fv(crane[0]);
  glVertex3fv(crane[1]);
  
  glVertex3fv(crane[1]);
  glVertex3fv(crane[2]);
  
  glVertex3fv(crane[2]);
  glVertex3fv(crane[3]);
    
  glVertex3fv(crane[3]);
  glVertex3fv(crane[4]);
  glEnd();

#draws half of the crane (left/right side)
#we can just use this code twice by using it once then reflecting
#NOTE: no matrix stack operations are done here
def drawHalfCrane():

  #front side of the body is made up of 4 panels because it bulges
  glColor3ub(235,235,235);

  #top left panel
  glBegin(GL_TRIANGLES);
  glVertex3fv(crane[2]);
  glVertex3fv(crane[5]);
  glVertex3fv(crane[27]);
  glEnd();
  
  #bottom left panel
  glBegin(GL_QUADS);
  glVertex3fv(crane[5]);
  glVertex3fv(crane[6]);
  glVertex3fv(crane[7]);
  glVertex3fv(crane[27]);
  glEnd();
  
  #top right panel
  glBegin(GL_TRIANGLES);
  glVertex3fv(crane[2]);
  glVertex3fv(crane[9]);
  glVertex3fv(crane[27]);
  glEnd();

  #bottom right panel
  glBegin(GL_POLYGON);
  glVertex3fv(crane[9]);
  glVertex3fv(crane[8]);
  glVertex3fv(crane[7]);
  glVertex3fv(crane[27]);
  glEnd(); 
  
  #right side of the body
  glColor3ub(220,220,225); 
  glBegin(GL_QUADS);
  glVertex3fv(crane[2]);
  glVertex3fv(crane[9]);
  glVertex3fv(crane[8]);
  glVertex3fv(crane[3]);
  glEnd();
  
  #left side of the body
  glBegin(GL_QUADS);
  glVertex3fv(crane[2]);
  glVertex3fv(crane[5]);
  glVertex3fv(crane[6]);
  glVertex3fv(crane[3]);
  glEnd();
  
  #tail
  glColor3ub(240,240,240); 
  glBegin(GL_TRIANGLES);
  glVertex3fv(crane[3]);
  glVertex3fv(crane[4]);
  glVertex3fv(crane[8]);
  glEnd();
  
  #neck
  glBegin(GL_QUADS);
  glVertex3fv(crane[11]);
  glVertex3fv(crane[6]);
  glVertex3fv(crane[3]);
  glVertex3fv(crane[1]);
  glEnd();
  
  #head
  glColor3ub(255,255,255); 
  glBegin(GL_TRIANGLES);
  glVertex3fv(crane[11]);
  glVertex3fv(crane[1]);
  glVertex3fv(crane[0]);
  glEnd();
  
  #wings
  glColor3ub(220,220,213); 
  glBegin(GL_QUADS);
  glVertex3fv(crane[7]);
  glVertex3fv(crane[6]);
  glVertex3fv(crane[13]);
  glVertex3fv(crane[15]);
  glEnd();
  
  glBegin(GL_QUADS);
  glVertex3fv(crane[7]);
  glVertex3fv(crane[8]);
  glVertex3fv(crane[14]);
  glVertex3fv(crane[15]);
  glEnd(); 

 #creases on the wings
  glColor3ub(190,190,190);
  glLineWidth(head/5);
  glBegin(GL_LINES);

  glVertex3fv(crane[15]);
  glVertex3fv(crane[7]);

  glVertex3fv(crane[16]);
  glVertex3fv(crane[20]);

  glVertex3fv(crane[17]);
  glVertex3fv(crane[20]);

  glVertex3fv(crane[21]);
  glVertex3fv(crane[25]);

  glVertex3fv(crane[22]);
  glVertex3fv(crane[25]);
  glEnd();

def cpongOrigamiCrane():
  #centers the crane
  glTranslatef(12,0,12);
  glPushMatrix();
  drawHalfCrane();
  #reflects over plane of symmetry, z = 0
  glScalef(1,1,-1);
  drawHalfCrane();
  glPopMatrix();

def display():
    twDisplayInit();
    twCamera();

    cpongOrigamiCrane();

    glFlush();
    glutSwapBuffers();

def wireToggle(key, x, y):
    global Wirep
    Wirep = not Wirep;
    glutPostRedisplay();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-8,32,0,20,-2,26)
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    twKeyCallback('w',wireToggle,"toggle wire-frame bear body and head");
    glutMainLoop()

if __name__ == '__main__':
  main()
