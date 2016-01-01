''' 
Name: Caroline Boes
Date: April 09, 2012
Purpose: CS307, HW6
Description: Draws a lighthouse object with two tiers of railings.

An OpenGL model of a lighthouse. Copyright (C) 2012 by Caroline Boes. 
This program is released under the GNU General Public License. 
'''

S = 40 # slices and stacks

import sys

try:
  from TW import *
except:
  print #ERROR: Couldn't import TW.
        
def cboeslighthouse(bc):
    '''
    Draws a lighthouse object with base in the plane y=0 and oriented along
    the y-axis. Origin is at the center of the base. Lighthouse origin 
    located at x=0 and z=0. Takes one tuple representing the color of the
    lighthouse's body. Lower set of rails are white and higher set are black.
    '''
    
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    twColor(bc, 0, 0)       
    '''
    The following draws the z=0 plane (y=0 plane in modified coordinate
    system,) which confirms that the base of each cone lies on that plane.
    Used for debugging the base of the lighthouse.
    '''
    
    if False:
        twColorName(TW_PURPLE)
        glBegin(GL_QUADS)
        glVertex3f(-10,-10,0)
        glVertex3f(+10,-10,0)
        glVertex3f(+10,+10,0)
        glVertex3f(-10,+10,0)
        glEnd()
    
    # foundation of lighthouse
    #founColor = (0.20, 0.18, 0.70) # use for the foundation
    #glColor3fv(founColor)
    #twColorName(TW_GRAY)    
    lHeight = 2
    fCutoff = 70             # half-angle at top of the cone, in degrees
    # compute radius of cone at z=0, given angle and height of cone
    fBase = lHeight*math.tan(fCutoff*M_PI/180)
    twCylinder(fBase,1,lHeight,10,S);

    # long body of lighthouse
    coneSize = lHeight*7            # from z=0 to z=10
    coneCutoff = 15;            # half-angle at top of hat, in degrees
    # compute radius of cone at z=0.  This'll be "inside" the brim.
    coneBase = coneSize*math.tan(coneCutoff*M_PI/180)    
    coneHeight = coneSize + 10
    twCylinder(coneBase,lHeight,coneHeight,S,S)

    # draws the structure supporting the top room
    glTranslate(0,0,coneHeight)
    glRotatef(180, 1, 0, 0)
    topRimSize = fBase * 0.6
    twCylinder(topRimSize,1,lHeight,S,S);
    
    # draw the cylinder below the lower railing
    glTranslate(0,0,-1.5)
    twCylinder(topRimSize,topRimSize,1.5,S,S)

    glPushMatrix()
    # draw white railings
    twColorName(TW_WHITE)
    for u in range(0,3):
      glTranslate(0,0,-lHeight*0.3)
      glutSolidTorus(0.1, topRimSize, S, S)
    glPopMatrix()

    # draw four straight up and down railing rods
    glPushMatrix()
    glRotatef(180, 1, 0, 0)
    drawFourRails(topRimSize)
    
    # 2nd set of four rails
    glPushMatrix()
    glRotatef(45, 0, 0, 1)
    drawFourRails(topRimSize)    

    glPopMatrix()
    glPopMatrix()

    # draw the floor to the balcony
    twColor(bc, 0, 0)
    highRimSize = topRimSize-1+.01
    twCylinder(topRimSize,highRimSize,.2,S,S)

    # draw the center cylinder inside balcony
    #twColorName(TW_GRAY)
    glRotatef(180, 1, 0, 0)
    twCylinder(highRimSize,highRimSize,2.5,S,S)
    
    # draw the base supporting the light room
    glTranslatef(0, 0, highRimSize)
    twCylinder(highRimSize,highRimSize+0.5,0.5,S,S)

    glRotatef(180, 1, 0, 0)
    glTranslatef(0, 0, -1)
    twCylinder(highRimSize,highRimSize+0.5,0.5,S,S)

    # draw the four rods of the room that houses the light
    twColorName(TW_BLACK)
    glPushMatrix()
    glRotatef(20, 0, 0, 1) # make so they don't line up with the lower rails
    glRotatef(180, 1, 0, 0)
    drawFourRails(highRimSize)
    # make the upper rails longer    
    glTranslatef(0, 0, 0.5)    
    drawFourRails(highRimSize)
    glPopMatrix()

    # begin drawing top roof
    twColor(bc, 0, 0)       
    # first base and layer
    glRotatef(180, 1, 0, 0)
    glTranslatef(0, 0, 2.5) # 2 + 0.5
    highestRimSize = highRimSize + 0.3
    twCylinder(highRimSize,highestRimSize,0.5,S,S)
    glTranslatef(0, 0, 0.5)
    twCylinder(highestRimSize,1,1,S,S)

    # 2nd tier, highest roof
    glTranslatef(0, 0, 1)
    twCylinder(1,1,0.3,S,S)
    glTranslatef(0, 0, 0.3)
    twCylinder(1,0,0.5,S,S)

    # spindle at very top
    glTranslatef(0, 0, 0.5)
    twTube(.05, .05, 1, S, S)    

    glPopMatrix()

def drawFourRails(radius):
    '''
    Draws four up-and-down rails in a circle of the given radius. Rails are drawn
    in current color.
    '''

    glPushMatrix()
    glTranslatef(radius, 0, 0)
    twTube(.1, .1, 2, S, S)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-radius, 0, 0)
    twTube(.1, .1, 2, S, S)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, radius, 0)
    twTube(.1, .1, 2, S, S)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, -radius, 0)
    twTube(.1, .1, 2, S, S)
    glPopMatrix()

def display():
    twDisplayInit()
    twCamera()

    # Set up basic lights to put some shading on the lighthouse
    glEnable(GL_LIGHTING)
    lightpos = ( 1, 1, 0, 0 )
    twGrayLight(GL_LIGHT0, lightpos, 0.1, 1, 1 )

    # Mark the origin
    if True:
        glPointSize(5)
        twColorName(TW_MAGENTA)
        glBegin(GL_POINTS)
        glVertex3f(0,0,0)
        glEnd()
        
    #Color of lighthouse
    bodyColor = (51/255.0, 204/255.0, 153/255.0) 
    cboeslighthouse(bodyColor) #draw lighthouse

    glFlush();
    glutSwapBuffers();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-10,10, 0,40, -10,10);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
  main()
