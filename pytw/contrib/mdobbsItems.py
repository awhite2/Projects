'''
 A small library of objects:
# turret
# unitTetra
# button
# chest
# stair
# torch
# door
'''

from math import *

try: 
    from TW import * 
except: 
    print ''' 
ERROR: Couldn't import TW. 
 '''

#---------------------------------------------------------------------------------------------

def drawface():
    v =  [ [0, 0, 0],
           [1, 0, 0],
           [1, 1, 0],
           [0, 1, 0]]
    glBegin(GL_QUADS)
    glNormal3f(0, 0, 1)
    glVertex3fv(v[0])
    glVertex3fv(v[1])
    glVertex3fv(v[2])
    glVertex3fv(v[3])
    glEnd()
                   
def box():
    
    drawface()

    glPushMatrix()
    glTranslatef(1,0,0)
    glRotate(90,0,1,0)
    drawface()

    glTranslatef(1,0,0)
    glRotate(90,0,1,0)
    drawface()

    glTranslatef(1,0,0)
    glRotate(90,0,1,0)
    drawface()
    glPopMatrix()

    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    drawface()
    glPopMatrix()


# --------------------------------------------------------------------------------------------
def unitTetra(solid):
# a unit tetrehedron flat on the y=0 plane.  reference point is the center of the bottom face.
#this is wrong and I'm going to change it but it's not really important
    glPushMatrix()
    glTranslatef(0, 1.0/sqrt(24), 0)
    glRotatef(90, 0, 0, 1)
    glScalef(1.0/sqrt(3), 1.0/sqrt(3), 1.0/sqrt(3))
    if solid:
        glutSolidTetrahedron()
    elif not(solid):
        glutWireTetrahedron()
    glPopMatrix()    

# ------------------------------------------------------------------------------
up = True
def button(color1, color2):
    '''
    a simple button with two states, up and pushed down.  
    Color1 is the outside color, color2 is the color of the button
    '''
    hButton=1
    twColor(color1, .8, 80)
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    glutSolidCylinder(1, hButton*.8, 20,3)
    twColor(color2, 1, 128)
    if up:
        glutSolidCylinder(.75, hButton*1.3, 20, 3)
        glTranslatef(0, 0, hButton*1.3)
        glScalef(1, 1, .4)
        glutSolidSphere(.75, 20, 10)
    else:
        glutSolidCylinder(.75, hButton*1.05, 15, 3)
    glPopMatrix()


# ----------------------------------------------------------------------------------------------
'''
The only 'enemy' for the game so far.
Its height is the height of the large cylinder, not the head
The long rod projecting in the -Z direction is a lazer motion-detector, I think.
'''
def turret(height):
    ri=.2
    ro=.25
    hTop=ri*1.5
    
    innerColor = (.57, .11, .07) 
    outerColor= (.33, .63, .41)
    eyeColor = (.76, .89, 1.0)
    jewelColor = (1.0, .05, .34)
    
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)

    twColor(innerColor, .8, 80)
    glutSolidCylinder(ri, height, 15, 3) #inner cylinder

    twColor(outerColor, .2, 20)
    glutSolidCylinder(ro, height-(1.5*ri), 15, 3) #outer cylinder

    glTranslatef(0, 0, height-(1.5*ri)+.2) #top cylinder
    glutSolidCylinder(ro, 1.5*ri, 15, 3)
    
    glPushMatrix() #eye
    glTranslatef(0, ri, -.1)#center edge of gap
    
    glScalef(1.5, 1.5, 2)
    twColor(eyeColor, .8, 60)
    glutSolidSphere(ri, 15, 15)
    glPopMatrix()
    
    glPushMatrix()
   
    glTranslatef(0, ro, -.1)    #outer edge
    glPushMatrix()
    glScalef(1, 1, .6)
    twColor(innerColor, .8, 80)
    unitTetra(False)
    
    twColor(jewelColor, 1, 128)
    glScalef(.5, .5, .5)
    unitTetra(True)
    glScalef(-1, 1, 1)
    unitTetra(True)    
    glPopMatrix()

    glRotatef(-90, 1, 0, 0)
    twColor(jewelColor, .1, 10)
    glutSolidCylinder(.01, 10, 5, 5)
    glPopMatrix()
    glPopMatrix()


#---------------------------------------------------------------------------------------------
def lid(slices):
    '''
    Helper method for the treasure chest.  The lid can be any number of sides.
    '''
    h=1 #height of lid
    w=1 #width of lid
    s = slices #number of slices
    deg = 180.0/s
    v = [[0, 0, 0]]
    a = 0
    while(a <= 180):
        t = [0, sin(radians(a)),cos(radians(a))]
        v.append(t)
        a = a+deg
    
    glBegin(GL_TRIANGLE_FAN)
    for x in v:
        glNormal3f(-1, 0, 0)
        glVertex3fv(x)
    glEnd()
    
    vw= map(lambda x:[x[0]+w, x[1], x[2]], v)
    glBegin(GL_TRIANGLE_FAN)
    for x in vw:
        glNormal3f(1, 0, 0)
        glVertex3fv(x)
    glEnd()
    
    i = 1
    while(i <= s):
        glBegin(GL_QUADS)
        n = twCrossProduct(twVector(v[i], vw[i]), twVector(v[i], v[i+1]))
        glNormal3fv(n)
        glVertex3fv(v[i])
        glVertex3fv(vw[i])
        glVertex3fv(vw[i+1])
        glVertex3fv(v[i+1])
        i = i+1
        glEnd()
   
Chest_closed = True
ChestDefault = [0.53725490196078429, 0.28235294117647058, 0.15294117647058825]
def chest(n, color):
    '''
    A treasure chest.  n is the number of sides on the lid.  It is a solid color
    '''    
    unit = 1.0

    twColor(color, .05, 20)
    glPushMatrix()
    glScalef(1, .7, 1)
    box()
    glPopMatrix()

    twColor(color, .05, 20)
    glPushMatrix()
    if Chest_closed:
        glTranslatef(0, .7, -.5)
        glScalef(1, .3, .5)
    else:
        glTranslatef(0, 1.2, -1)
        glRotatef(-90, 1, 0, 0)
        glScalef(1, .3, .5)
        
    lid(n)
    glPopMatrix()

#---------------------------------------------------------------------------------------------

isLocked = True
def door(w, h, color, lcolor):
    '''
    a flat door with a shiny lock on it.  Color is the color of the door, while lcolor is the color of the lock.
    '''

    twColor(color, .05, 5)
    glPushMatrix()
    glScalef(w, h, 0)
    glutSolidCube(1)
    glPopMatrix()

    twColor(lcolor, .8, 80)
    glutSolidCylinder(w/6.0, .1, 10, 10)
    glPushMatrix()
    glTranslatef(0, w/6.0, 0)
    glutSolidTorus(w/18.0, w/12.0, 15, 10)
    glPopMatrix()
    
#-------------------------------------------------------------------------------
def stairCube(h):
#draws a glutSolidCube of size h,centered on the z axis and touching the z=0 and y=0 planes
    glPushMatrix()
    glTranslatef(0, h/2.0, -h/2.0)
    glutSolidCube(h)
    glPopMatrix()

def staircase(h):
    '''
    draws a staircase centered on z axis where each step is 1x(nth step)x1
    dimension of staircase is 1xheightxheight
    '''
    glPushMatrix()

    for i in range(0,h): 
        #print i
        glPushMatrix()
        glScalef(1,1+i,1)
        stairCube(1)
        glPopMatrix()
        glTranslatef(0,0,-1)

    glPopMatrix()

# --------------------------------------------------------------------------------------------

def drawLeg():
    '''
    Helper method for torch
    '''
    glPushMatrix()
    glRotatef(60, 1, 0, 0)
    gluCylinder(gluNewQuadric(), .1, .1, 1.5, 10, 10)
    glPopMatrix()

def torch():
    '''
    Draws a torch in a stand.
    Apparantly an indecipherable object.
    TODO: use bezier curves to make the flame look like flame
    '''
    stand=(.38, .27, .27)
    torchcolor = (.47, .26, .12)
    flame=(1, .73, 0)

    twColor(torchcolor, .5, 20)
    glPushMatrix()
    glTranslatef(0, 1, 0)
    glRotatef(-90, 0, 0, 1)
    glScalef(2.0/sqrt(8),1.0/sqrt(8),1.0/sqrt(8))
    glutSolidTetrahedron()
    glPopMatrix()
    
    twColor(stand, .8, 75)
    glPushMatrix()
    glTranslatef(0,.75,0)
    glRotatef(90, 1, 0, 0)
    glutSolidTorus(.1, .3, 10, 10)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0,.75,0)
    for x in range(1, 5):
        glPushMatrix()
        glTranslatef(0, 0, .3)
        drawLeg()
        glPopMatrix()
        glRotatef(90, 0,1, 0)
    glPopMatrix()

    twColor(flame, 0, 0)
    glPushMatrix()
    glTranslatef(0, 1.2, 0)
    glutSolidSphere(.15, 10, 10)
    glRotatef(-90, 1, 0, 0)
    twColorName(TW_YELLOW)
    glutSolidCone(.13, .5, 10, 10)
    glPopMatrix()

def niceTorch():
    # A scaled version of Torch with dimensions that please the writer of this module
    glPushMatrix()
    glTranslatef(0, 1, 0)
    glScalef(1, 1.5, 1)
    torch()
    glPopMatrix()

# ------------------------------------------------------------------------------
#number of objects in the module. Each has its own demo defined in display().
numObjs = 6
demo = 0

xmax = 1
ymax = 5
zmin = -4

def demoSwitch(key, x, y):
    '''
    Switches between the demos of all the objects in this module.  
    '''
    global demo
    if demo == numObjs:
        demo = 0
    else:
        demo +=1
    glutPostRedisplay()

def lighting():
    
    lightPos=(-5, 10, 10, 1)
    twGrayLight(GL_LIGHT0, lightPos, .1, .5, .5)
    twGrayLight(GL_LIGHT1, (0, 10, 0, 1), .2, .3, .3)
    
def display():
    '''
    Main Display method.
    Has a different display for each object.  There is a light coming from the upper right.
    '''
    global xmax, ymax, zmin
    twDisplayInit(0.7, 0.7, 0.7)
    twCamera()
    lighting()
    if demo == 0:
        turret(2)
        glTranslatef(1, 0, 0)
        turret(1)
    elif demo == 1:
        twColor((.64, 0, .05), 1, 100)
        unitTetra(False)
        glScalef(.5, .5, .5)
        unitTetra(True)
    elif demo == 2:
        button((.75, .75, .75),(.9, .3, .48))
    elif demo == 3:
       chest(3, ChestDefault)
    elif demo == 4:
        twColor((.9, .9, 1), .2, 45)
        staircase(4)
    elif demo == 5:
        niceTorch()
    elif demo == 6:
        glTranslatef(0, 2, 0)
        door(1, 4, ChestDefault, (.76, .76, .76)) 
    glFlush()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-1, xmax, 0, ymax, zmin, 1)
    #twBoundingBox(-.5, .5, 0, 1, -.5, .5)
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    twKeyCallback('~', demoSwitch, "Switch between demonstrations of different objects")
    glutMainLoop()

if __name__ == '__main__':
    main()
