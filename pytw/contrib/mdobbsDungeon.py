'''
A room from a dungeon.  It has a treasure chest with a key, a locked door, and some enemies.
No collision detection yet.

Written by Miranda Dobbs, Fall 2009 for cs307.
'''
import mdobbsItems

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''

'''
Global variables for the scene.
'''
w = 50
l = 20
h = 30

xcenter = 0
ycenter = h/2
zcenter = -l/2

terrainColor=(.5, .7, .6)
wallColor=(.2, .6, .2)

def wall():
  '''
  Draws a wall that is invisible from the outside.
  needs texture coordinates and more vertices for lighting purposes
  '''

  glPushAttrib(GL_POLYGON_BIT)
  glEnable(GL_CULL_FACE)
  glColor3fv(wallColor)
  
  glBegin(GL_QUADS)
  glVertex3f(-.5, 0, 0)
  glVertex3f(-.5, 1, 0)
  glVertex3f(.5, 1, 0)
  glVertex3f(.5, 0, 0)


  glEnd()  

  glPopAttrib()
  
def walls():
  '''
  draws 4 walls + ceiling + floor 
  '''
  glPushMatrix()
  glScalef(w, h, l)
  glPushMatrix()
  
  for i in range(4):
    wall()
    glTranslatef(.5, 0, -.5)
    glRotatef(90, 0, 1, 0)
  glPopMatrix()

  glTranslatef(0, 1, 0)
  glRotatef(-90, 1, 0, 0)
  wall()
  glPopMatrix()


def platform():
  '''
  The platform in the rear with a treasure chest and torches
  '''
  glPushMatrix()

  #The ground
  glPushMatrix()
  glRotatef(90, 1, 0, 0)
  gluDisk(gluNewQuadric(), 0, 3, 20, 10)
  gluCylinder(gluNewQuadric(), 3, 3, 1, 20, 10)
  glPopMatrix()
  
  mdobbsItems.chest(4, [0.54, 0.28, 0.15])  
  
  #the torch
  glPushMatrix()
  glTranslatef(-.7, 0, 0)
  glRotatef(45, 0, 1,0)
  mdobbsItems.niceTorch()
  glPopMatrix()
  
  glPopMatrix()
 
  #more ground
  glPushMatrix()
  glColor3fv(terrainColor)
  glTranslatef(8, 0, 0)
  glScalef(10, 1, 6)
  glutSolidCube(1)
  glPopMatrix()

  #the turret
  glPushMatrix()
  glTranslatef(11, 0, 0)
  glRotatef(90, 0, 1, 0)
  glScalef(1.3, 1.3, 1.3)
  mdobbsItems.turret(3)
  glPopMatrix()


def liquidHazard():
  '''
  Liquid that will be impassable.  I think it's lava.
  '''
  glPushMatrix()
  glTranslatef(xcenter, 0, zcenter) 
  glScalef(w, 0, l)
  twColorName(TW_ORANGE)
  glutSolidCube(1)
  glPopMatrix()

def groundLevel():
  '''
  The lower level of the dungeon, including stairs.
  '''
  glPushMatrix()
  glTranslatef(-w/4, .5, (zcenter/2))
 
  glPushMatrix()
  glScalef(20, 1, -zcenter)
  glColor3fv(terrainColor)
  glutSolidCube(1)
  glPopMatrix()
 
  glTranslatef(w/2.0, 0, 0)
  glScalef(20, 1, -zcenter)
  glutSolidCube(1)
  glPopMatrix()

  glPushMatrix()
  glTranslatef(-w*.5+2, 0, 0)

  glPushMatrix()
  glScalef(4, 1, 1)
  mdobbsItems.staircase(l-5)
  glPopMatrix()
 
  glTranslatef(w-5, 0, 0)
  
  glPushMatrix()
  glTranslatef(-5, 0, -3)
  glScalef(1.5, 1.5, 1.5)
  mdobbsItems.turret(3)
  glPopMatrix()

  glColor3fv(terrainColor)
  glScalef(6, 1, 1)
  mdobbsItems.staircase(l-5)
  glPopMatrix()
  
def mGlTranslatefv(t):
  if len(t)==3:
    glTranslatef(t[0], t[1], t[2]) 

def upperLevel():
  '''
  The level up the stairs.  
  '''
  uh = 15
  #ledges = (length of ledge, length of gap, length of ledge, length of gap,....) left to right
  ledges = [[w/4.0+6, 4], [6, 3], [w-(w/4.0+6+4+6+3), 0]]
  ends = ((-w/2.0, uh, -17.5), (w, uh, -17.5))
  glColor3fv(terrainColor)
  
  glPushMatrix()
  mGlTranslatefv(ends[0])
  
  #this draws the ledges based on the array above. I might generalize this.
  for x in ledges:
    glTranslatef(x[0]/2.0, 0, 0) 
    glPushMatrix()
    glScalef(x[0], 1, 5)
    glutSolidCube(1)
    glPopMatrix()
    glTranslatef(x[0]/2.0+x[1], 0, 0)
  glPopMatrix() 
  glPushMatrix()
  glTranslatef(.5, uh+5, -l+.1)
  mdobbsItems.door(6, 10, terrainColor, (.76, .76, .76))
  glPopMatrix()

  glColor3fv(terrainColor)
  glPushMatrix()
  glTranslatef(-w*.5+2, uh/2.0, -l+2.5)
  glScalef(1, uh/4.0, 5/4.0)
  glutSolidCube(4)
  glTranslatef(w-4, 0, 0)
  glutSolidCube(4)
  glPopMatrix()

def display():
  twDisplayInit(0.7, 0.7, 0.7)
  twCamera()
  twColorName(TW_RED)
  glutSolidSphere(.1, 10, 10)
  
  walls()
  upperLevel()
  liquidHazard()
  groundLevel()
   
  glPushMatrix()
  glTranslatef(-w/4, .5, -l*.85)
  platform()
  glPopMatrix()
 
  glPushMatrix()
  
  glPopMatrix()

  glFlush()
  glutSwapBuffers()
  
def main():
    
  glutInit(sys.argv)
  #glutCreateWindow(sys.argv[0])  #need to create window here to run on my laptop
  glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
  twBoundingBox(-w/3.0, w/3.0, 0, h, -l, 1)
  twInitWindowSize(1000,400)
  glutCreateWindow(sys.argv[0])  
  glutDisplayFunc(display)
  twMainInit()
  glutMainLoop()

if __name__ == '__main__':
    main()
