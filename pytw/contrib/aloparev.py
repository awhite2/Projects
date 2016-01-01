### An OpenGL model of a magical staff and a hand. Copyright(C)2009 by Anna Loparev. This program is released under the GNU General Public License (GPL).
### By Anna Loparev
### aloparev.py
### 10/27/09
### Homework: Creative Scene
### Draws a staff and a hand.

import sys
import math

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
########################### Staff ######################################################

# color of the wing
wingColor = (1,1,1)
# feather length
fLen = 3
# width of top of feather
fTopWidth = 0.5
# width of bottom of feather
fBotWidth = fTopWidth/2
# how much feathers warp on z plane
# in the final figure, this warp is on the y plane
fRot = -0.15
# These are used for setting the angle between feathers and how far apart they are
# Angle between feathers for the 2nd and 3rd feathers from the top
fAngle1 = 22
# Distance from each other for the 2nd and 3rd feathers from the top
fDist1 = -0.25
# Angle between feathers for the 4th and 5th feathers
fAngle2 = 18
# Distance from each other for the 4th and 5th feathers
fDist2 = -0.3
# Angle between feathers for the rest of the feathers
fAngle3 = 15
# Distance between each other for the rest of the feathers
fDist3 = -0.4
# Used to tilt the entire wing on the X plane
fFinalAngleX = 30

# Color of the sphere
orbColor = (0,0.625,1)
# Radius of the sphere between the wings
sphereRad = 2
# X distance of each wing from the center of the sphere between the wings
wingXpos = 3
# Y distance of each wing from the center of the sphere between the wings
wingYpos = 2

# Color of the halo
haloColor = (1,1,0)
# Y location of the halo over the sphere
haloYpos = 3
# Inner radius of the halo over the sphere
haloInR = 0.2
# Outer radius of the halo over the sphere
haloOutR = 1.9

# Color of the part of the staff that isn't the orb with wings and a halo
bottomColor = (0.9,0.9,0)

# Distance between the flat part of the cone at the top of the staff and the floating orb
distBotToTop = -1.1

# Length of the main cylinder that makes up the staff
staffLen = 7.5*2*sphereRad
# Height of the cylinder that makes up the small bottom part of the staff
baseHeight = 2

def drawFeather(angleX,distanceY):
    ''' 
    Draws a feather rotated the given angle on the x plane
        (rotated around the z axis) and distance distanceY away
        from the origin in the y direction.
            
    The feather is upright facing the camera.
    Feathers are what make a wing.
    Note that no matrix is pushed or popped even though a transformation occurs.
    This is because the position of each feather is based on the feather that was
        drawn before it.
    The exception to this rule is the first feather, which has a angleX 
        and distanceY of 0.
    '''
    # Move the origin into position
    glRotatef(angleX,0,0,1)
    glTranslatef(0,distanceY,0)
    # Draw the feather
    glBegin(GL_QUADS)
    glVertex3fv((fRot,0,0))
    glVertex3fv((fRot,-fLen,0))
    glVertex3fv((0,-(fLen-1),fTopWidth))
    glVertex3fv((0,0,fBotWidth))
    glEnd()

def drawFeatherSet(angleX,distanceY,num):
    '''
    Draws a sequence of num feathers that are each angleX degrees apart from each other
        on the x plane and distanceY apart in the y direction.
        
    The purpose of this function is to make making the wings less tedious
    Note that no matrix is pushed or popped even though transformations occur.
    This is because the position of each feather is based on the feather that was
        drawn before it.
    If there are more feathers after this set, the positions and angles of those feather
        depend on the position and angle of the last feather that was drawn with this
        function.
    '''
    while (num > 0):
        # draw a feather with the specifications in the first two parameters
        drawFeather(angleX,distanceY)
        # increment num
        num = num - 1

def drawWing():
    '''
    Draws a wing by drawing a sequence of feathers.
    
    '''
    glPushMatrix()
    # we want the wing to have a bit of an angle
    glRotatef(fFinalAngleX,0,0,1)
    twColor(wingColor,0,0)
    # the initial feather is drawn per the default specifications
    #     i.e., there is no rotation or translation done to it
    drawFeather(0,0)
    # every feather depends on the location and rotation of the feather
    #     before it, so no matrices are pushed or popped during the process
    #     of adding feathers
    drawFeatherSet(fAngle1,fDist1,2)
    drawFeatherSet(fAngle2,fDist2,2)
    drawFeatherSet(fAngle3,fDist3,5)
    glPopMatrix()

def drawTop():
    '''
    Draws an orb with two wigs and a halo.
    '''
    glPushMatrix()
    # first draw the orb
    twColor(orbColor,0,0)
    glutSolidSphere(sphereRad,20,20)
    glPushMatrix()
    # move to where the right wing will go
    glTranslatef(0,wingYpos,0)
    glTranslatef(wingXpos,0,0)
    # draw the right Wing
    drawWing()
    glPopMatrix()
    glPushMatrix()
    # move to where the left wing will go
    # the left wing is the same height as the right wing 
    glTranslatef(0,wingYpos,0)
    # the left wing is on the opposite side of the orb as the right wing
    glTranslatef(-wingXpos,0,0)
    # flip the right wing to make the left wing
    glRotatef(180,0,1,0)
    # draw the left wing
    drawWing()
    glPopMatrix()
    glPushMatrix()
    # move to where the halo will go
    glTranslatef(0,haloYpos,0)
    glRotatef(90,1,0,0)
    twColor(haloColor,0,0)
    # draw the halo
    glutSolidTorus(haloInR,haloOutR,20,20)
    glPopMatrix()
    glPopMatrix()

# draw the part of the staff that is not the orb, wings, or halo
def drawBottom():
    '''
    Draws the part of the staff consisting of everything but the orb, wings, and halo.
    
    From now on, I will refer to this set of objects as the bottom part of the staff.
    The bottom part consists of a long cylinder with a cone at the top and a smaller cylinder
        at the bottom.
    '''
    glPushMatrix()
    glPushMatrix()
    # draw the cone at the top of the bottom part of the staff
    # get to the position where the cone will go
    glTranslatef(0,staffLen+baseHeight,0)
    glRotatef(90,1,0,0)
    twColor(bottomColor,0,0)
    # draw the cone
    glutSolidCone(sphereRad,2,20,20)
    glPopMatrix()
    glPushMatrix()
    # now we will draw the large cylinder that makes up the main section of the staff
    # there will be a smaller cylinder below this one, so account for it
    glTranslatef(0,baseHeight,0)
    glRotatef(-90,1,0,0)
    # draw the large cylinder that makes up the bottom of the staff
    gluCylinder(gluNewQuadric(),1,1,staffLen,20,20)
    glPopMatrix()
    glPushMatrix()
    # now we will draw the small cylinder at the bottom of the staff
    glRotatef(-90,1,0,0)
    # draw the cylinder at the bottom of the staff
    gluCylinder(gluNewQuadric(),0.25,1,baseHeight,20,20)
    glPopMatrix()
    glPopMatrix()

# draw the entire staff
def aloparevStaff():
    '''
    Draws a staff facing the camera.
    
    The staff is staffLen+distBotToTop+(2*sphereRad)+5 tall, since we have to take
        the length of the large cylinder, the length of the small cylinder at the bottom,
        the distance between the cone at the top of the bottom part of the staff and the
        orb, the radius of the orb, and an offset for the height of the wings.
    '''
    glPushMatrix()
    # draw the main part of the staff (the part without the orb, wings, and halo)
    drawBottom()
    glTranslatef(0,staffLen + distBotToTop + sphereRad + baseHeight,0)
    # draw the orb, wings, and halo
    drawTop()
    glPopMatrix()

########################### Hand ######################################################

# Color of the hand
handColor = (255.0/255.0,226.0/255.0,176.0/255.0)
# Since there is no lighting, the fingers have to be a different color
fingerColor = (255.0/255.0,188.0/255.0,45.0/255.0)
# Radius of the cylinder of the palm
palmRadius = 5
# Height of the cylinder of the palm
palmWidth = 1.5

# Pinky finger section length
len1 = 1.5
# Ring finger section length
len2 = 1.9
# Middle finger section length
len3 = 2.4
# Index finger section length
len4 = 2.2
# Thumb section length
lenThumb = 1.7

# Width of a non-thumb finger
fingerWidth = 1
# Width of a thumb
thumbWidth = 1.2

def rotateAbit(angleY,angleZ):
    '''
    Rotates around angleY around the y axis and angleZ around the x axis.
    
    These calls are a bit counterintuitive because when we make a finger,
        we initially rotate the entire thing by -90 in the x direction.
    If we didn't do this rotation, we would have to translate the parts of the finger down
        instead of up while drawing from the bottom of the finger to the top, 
        which would also be counter intuitive
    Note that no matrix is pushed or popped, since this function is used to help transform 
        something
    '''
    glRotatef(angleY,0,1,0)
    glRotatef(angleZ,1,0,0)

def drawThirdOfFinger(widthScale,lengthScale):
    '''
    Draws a sphere and cylinder that form a joint and a third of the finger respectively.
    
    widthScale should be the width of the entire finger.
    lengthScale determines the length of each section of the finger.
    Note that no matrix is pushed or popped, since the position and angle of each third 
        of the finger depends on the third that came before it.
    '''
    glutSolidSphere(widthScale,20,20)
    gluCylinder(gluNewQuadric(),widthScale,widthScale,lengthScale,20,20)

# draw the thumb of a hand
# note that a thumb is really the top two thirds of a finger
def drawThumb(widthScale,lengthScale,angleY,angleZ):
    '''
    Draws a thumb for the hand.
    
    The thumb has width widthScale, each of its segments are lengthScale long,
        and the top segment is angleY degrees and angleZ degrees relative to
        the bottom segment.
    The thumb is drawn from the bottom to the top.
    Note that a thumb is really the top two thirds of a finger.
    '''
    # draw the bottom part of the thumb
    drawThirdOfFinger(widthScale,lengthScale)
    glTranslatef(0,0,lengthScale)
    # rotate in case the person's finger is not pointing strait up
    rotateAbit(angleY,angleZ)
    # draw the top third of the finger
    # this top part should be smaller than the other parts because it also has
    #     a sphere at the top, making it longer
    drawThirdOfFinger(widthScale,lengthScale*3.0/4.0)
    # the top of the finger is curved, so we have to add a sphere on the end
    glTranslatef(0,0,lengthScale*3.0/4.0)
    glutSolidSphere(widthScale,20,20)

def drawFinger(widthScale,lengthScale, 
               angleY12, angleZ12, 
               angleY23,angleZ23):
    '''
    Draws a non-thumb finger for the hand.
    
    Note that the top of the finger is the same as the thumb, so we can call
        that function here.
    '''
    glPushMatrix()
    glRotatef(-90,1,0,0)
    # draw the bottom third of the finger
    drawThirdOfFinger(widthScale,lengthScale)
    # translate to the bottom of the middle part of the finger
    glTranslatef(0,0,lengthScale)
    # rotate in case the person's finger is not pointing strait up
    rotateAbit(angleY12,angleZ12)
    drawThumb(widthScale,lengthScale,angleY23,angleZ23)
    glPopMatrix()

# draw the palm of the hand
def drawPalm():
    '''
    Draws the palm of a hand.
    
    The palm consists of a cylinder with spheres on the end.
    The inside part of the palm is less curved than the outside.
    The palm is facing away from the camera in the -z direction.
    '''
    glPushMatrix()
    # front of the palm
    glScalef(palmRadius,palmRadius,palmWidth)
    glutSolidSphere(1,20,20)
    glPopMatrix()
    # the body of the palm
    gluCylinder(gluNewQuadric(),palmRadius,palmRadius,palmWidth,20,20)
    glPushMatrix()
    glTranslate(0,0,palmWidth)
    # back of the palm
    glScalef(palmRadius,palmRadius,palmWidth)
    glutSolidSphere(1,20,20)
    glPopMatrix()

def prepareToDrawFinger(angleY):
    '''
    Goes to the location where a finger will be drawn.
    
    angleY is the angle of the finger along the edge of the palm.
    We are only using the the angle on the y plane, since this is where fingers
        are generally located.
    Note that no matrix is pushed or popped since the purpose of this 
        function is to help translate something.
    '''
    # center the fingers along the perimeter of the palm
    glTranslate(0,0,palmWidth*0.7)
    glRotatef(angleY,0,0,1)
    glScalef(1,palmRadius,palmRadius)
    glTranslatef(1,1,0)
    glScalef(1,1.0/palmRadius,1.0/palmRadius)

def drawPositionedFinger(isThumb,widthScale,lengthScale, angleYSphere,
                         angleY01, angleZ01,
                         angleY12, angleZ12, 
                         angleY23=0,angleZ23=0):
    '''
    Draws a finger in the specified position
    
    isThumb is used to determine if we are drawing a thumb or a non-thumb finger.
    widthScale and lengthScale determine the width of the finger and the length of its
        segments respectively.
    angleYSphere is the angle of the finger in relation to the center of the palm.
    angleY01 and angleZ01 specify the y and z angles of the finger in relation to the part of
        the palm it is connected to.
    angleY12 and angleZ12 specify the y and z angles of the middle portion of the finger with
        relation to the bottom portion of the finger.
    angleY23 and angleZ24 specify the y and z angles of the top portion of the finger with 
        relation to the middle portion of the finger.
    Note that the last two arguments have default 0.
    This is because a thumb only has two segments and therefore does not need these arguments.
    '''
    glPushMatrix()
    # go to where the finger will be
    prepareToDrawFinger(angleYSphere)
    glRotatef(angleY01,1,0,0)
    glRotatef(angleZ01,0,0,1)
    # draw the pinky finger
    glRotatef(180,0,1,0)
    # if the finger is a non-thumb
    if isThumb == "false":
        drawFinger(widthScale,lengthScale,angleY12,angleZ12,angleY23,angleZ23)
    # if the finger is a thumb
    else:
        # we did this rotation when we set up the finger, but not when we set up the thumb
        glRotatef(-90,1,0,0)
        drawThumb(widthScale,lengthScale,angleY12,angleZ12)
    glPopMatrix()

def aloparevHand(f101angleY,f101angleZ,f112angleY,f112angleZ,f123angleY,f123angleZ,
                 f201angleY,f201angleZ,f212angleY,f212angleZ,f223angleY,f223angleZ,
                 f301angleY,f301angleZ,f312angleY,f312angleZ,f323angleY,f323angleZ,
                 f401angleY,f401angleZ,f412angleY,f412angleZ,f423angleY,f423angleZ,
                 thumb01angleY,thumb01angleZ,thumb12angleY,thumb12angleZ):
    '''
    Draws a hand facing away from the camera.
    
    The name scheme for the parameters is as follows:
        If the parameter starts with f#, then # specifies the finger, i.e.,
            1 = pinky, 2 = ring finger, 3 = middle finger, 4 = pointer finger.
        If the parameter starts with f# or thumb, then the two numbers after this
            initial string represent the sections of the finger. For example, 
            f101angleZ means that we are specifying an angle on the z plane between
            the edge of the palm and the bottom segment of the finger for the
            pinky finger.
        The last letter of all of the parameters specifies which plane we are rotating on
    '''
    twColor(handColor,0,0)
    drawPalm()
    twColor(fingerColor,0,0)
    # pinky
    drawPositionedFinger("false",fingerWidth,len1,15-80,
                         f101angleY,f101angleZ,
                         f112angleY,f112angleZ,
                         f123angleY,f123angleZ)
    # ring finger
    drawPositionedFinger("false",fingerWidth,len2,45-80,
                         f201angleY,f201angleZ,f212angleY,
                         f212angleZ,f223angleY,f223angleZ)
    # middle finger
    drawPositionedFinger("false",fingerWidth,len3,75-80,
                         f301angleY,f301angleZ,f312angleY,
                         f312angleZ,f323angleY,f323angleZ)
    # index finger
    drawPositionedFinger("false",fingerWidth,len4,105-80,
                         f401angleY,f401angleZ,f412angleY,
                         f412angleZ,f423angleY,f423angleZ)
    # thumb
    drawPositionedFinger("true",thumbWidth,lenThumb,170-80,
                         thumb01angleY,thumb01angleZ,
                         thumb12angleY,thumb12angleZ)

def demoHand():
    '''
    Draws a hand in a specific way for purposes of demonstration.
    
    '''
    # use this to make sure the bounding box works for the entire hand even if the fingers are spread out all the way
    # drawaloparevHand(0,0,0,0,0,0,
    #                  0,0,0,0,0,0,
    #                  0,0,0,0,0,0,
    #                  0,0,0,0,0,0,
    #                  0,0,0,0)

    aloparevHand(0,30,-30,120,0,30,
                 0,30,-30,120,0,30,
                 0,0,0,0,0,0,
                 0,0,0,0,0,0,
                 90,180,0,-100);

def display():
    twDisplayInit();
    twCamera();



    demoObject();

    glFlush();
    glutSwapBuffers();

def objectStaff(key,x,y):
    global demoObject
    twBoundingBox(-10,10,0,baseHeight+staffLen+distBotToTop+(2*sphereRad)+fLen,-5,5)
    twZview()
    demoObject = aloparevStaff     # don't put the () after this, this just copies the function definition to a new name
    glutPostRedisplay()
    
def objectHand(key,x,y):
    global demoObject
    twBoundingBox(-10,10,-palmRadius,palmRadius*2+2.4,-(palmRadius+1.7),palmRadius+1.5)
    twZview()
    demoObject = demoHand      # don't put the () after this, this just copies the function definition to a new name
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    # default to showing the staff. Note that this call must be put *here*, after glutCreateWindow and before twMainInit
    objectStaff(None,None,None)
    twMainInit()
    ## keyboard callbacks to switch among objects
    ## don't put () here, because we are passing in a function object, not invoking the function
    twKeyCallback('1',objectStaff, "Show the Staff")
    twKeyCallback('2',objectHand, "Show the Hand")
    glutMainLoop()

if __name__ == '__main__':
  main()
