"""
Snare Drum in OpenGL created by Natasha Kellaway 
Draws a snare drum, including snare drum body and four legs

Default Viewing: Drum is oriented with legs facing away from viewer
and drum face parallel to x-y plane. 

Copyright (C) [unknown date] by Natasha Kellaway under the GNU GPL 
Converted from an object file to python by Caroline Boes (Feb 2012) 
"""

import sys

# global colors
red = [1,0,0]
white = [1,1,1]

try:
    from TW import *
except:
    print "ERROR: Couldn't import TW."

def nkellawaDrumLeg(transX, transY, transZ, drumRadius, drumHeight):
    """
    Helper method used to draw legs in nkellawaSnareDrum().    
    
    nkellawaDrumLeg takes five parameters in the following order:
    
    1. x-axis translation of the drum leg
    2. y-axis translation of the drum leg
    3. z-axis translation of the drum leg
    4. radius of the drum
    5. height of the drum
    
    The color of the legs is automatically black.
    """
    glPushMatrix()
    twColorName(TW_BLACK)
    glTranslatef(transX,transY,transZ)
    twCylinder(drumRadius/20.0,drumRadius/20.0,drumHeight,50,50)
    glPopMatrix()

def nkellawaSnareDrum(radius, height, headColor, sideColor, hasLegs):
    """ 
    Draws a snare drum, with or without legs

    The radius of the drum head and the height of the drum can
    be chosen by the user.
    
    Also, the color of the drum head and the side of the drum
    can be chosen by the user.

    The user can decide whether or not the drum has legs.
    
    It takes the parameters in the following order:

    1. radius of drum head
    2. height of drum
    3. color of drum heads
    4. color of drum side
    5. if the drum has legs
    
    The initial view shows only the top drum head, with the body (and legs)
    pointing back along the z-axis.
  
    The original lies at the center of the bottom drum head.
    
    nkellawaSnareDrum employs a helper method called nkellawaDrumLeg if the
    user specifies that they want legs on the drum.    
    """
    
    glPushMatrix()    
    # draw bottom head
    glPushMatrix() 
    twColor(headColor,0,0,0) 
    twDisk(radius,50)
    # draw top head
    glTranslatef(0,0,height)
    twDisk(radius,50)
    glPopMatrix()
    # draw side
    glPushMatrix()
    twColor(sideColor,0,0)
    twCylinder(radius,radius,height,50,50)
    glPopMatrix()
    # draw legs if user specifies
    if(hasLegs):
        glPushMatrix()
        # draw upper-right leg
        nkellawaDrumLeg(radius*0.6,radius*0.6,-height,radius,height)
        # draw upper-left leg
        nkellawaDrumLeg(-radius*0.6,radius*0.6,-height,radius,height)
        # draw lower-right leg
        nkellawaDrumLeg(radius*0.6,-radius*0.6,-height,radius,height)
        # draw lower-left leg
        nkellawaDrumLeg(-radius*0.6,-radius*0.6,-height,radius,height)
        glPopMatrix()
    glPopMatrix()    

def display():
    twDisplayInit()
    twCamera()         # sets up bounding box
    # draws a snare drum with white heads, red side, and legs present
    nkellawaSnareDrum(5,4,white,red,True)
    glFlush()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(650,650)
    glutCreateWindow(sys.argv[0])
    twBoundingBox(-5,5,-5,5,-5,5)
    twMainInit()
    glutDisplayFunc(display)
    glutMainLoop()
    return 0

if __name__ == '__main__':
    main()
