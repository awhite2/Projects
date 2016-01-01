''' Demo based on Angel's shadow example 

Scott D. Anderson

ported to Python, April 2012
'''

import sys
import math
from TW import *
from projectionMatrix import *

# variables for the position and angle of "sun"
# (the light source causing the shadow)

SunPos = None
SunDist = 20                    # distance from point it moves around
SunAngle = M_PI/2               # in radians
SunAngleDelta = 0.01            # degrees to adjust angle by

def setSunPos():
    global SunPos
    SunPos = [ SunDist * math.cos(SunAngle),
               SunDist * math.sin(SunAngle),
               0 ]

def initSun():
    global SunAngle
    SunAngle = M_PI/2
    setSunPos()

def sunLightSource():
    lightPoint = SunPos
    lightPoint.append(1)        # point source, so append a 1
    twGrayLight(GL_LIGHT1, lightPoint, 0.5, 1, 0.8)
    glEnable(GL_LIGHT1)
    glEnable(GL_LIGHTING)

def drawSunObject():
    glPushMatrix()
    glTranslatef(*SunPos)
    sunColor = (0.5,0.5,0)
    twColor(sunColor,0,0)
    glutSolidSphere(0.5,20,20)
    glPopMatrix()

def drawTeapot():
    '''draw teapot but let caller choose color'''
    glPushMatrix()
    glTranslatef(0,3,0)
    glRotatef(45,0,1,0)         # so we can see shadow of handle and spout
    glutSolidTeapot(4)
    glPopMatrix()

def drawTeapotNormal():
    glPushMatrix()
    glTranslatef(0.0, 3.0, 0.0)
    teapotColor = (0,0.6,0)
    twColor(teapotColor,0,64)
    drawBasicTeapot()
    glPopMatrix()

def drawWireCube():
    glPushMatrix()
    glTranslatef(0.0, 1, 0.0)
    glutWireCube(2)
    glPopMatrix()

def drawSolidCube():
    glPushMatrix()
    glTranslatef(0.0, 1, 0.0)
    glutSolidCube(2)
    glPopMatrix()

def drawWireSphere():
    glPushMatrix()
    glTranslatef(0, 2.0, 0)
    glutWireSphere(2,8,8)
    glPopMatrix()

def drawSolidSphere():
    glPushMatrix()
    glTranslatef(0, 2.0, 0)
    glutWireSphere(2,8,8)
    glPopMatrix()

def drawSolidTorus():
    glPushMatrix()
    glTranslatef(0, 4, 0)
    glRotatef(90,0,1,0)
    glutSolidTorus(1,3,8,8)
    glPopMatrix()

### ================================================================

DrawBlockp = True

DrawObjectId = 0
ObjectDrawers = [ drawWireCube, drawSolidCube,
                  drawWireSphere, drawSolidSphere,
                  drawSolidTorus, drawTeapot ]

Red = (1,0,0)

def display():
    twDisplayInit(1,1,1)
    twCamera()
    sunLightSource()                       # as a light source

    twGround()
    drawSunObject()
    if DrawBlockp:
        twColor(Red,0,0)
        ObjectDrawers[DrawObjectId]()

    # we don't want lighting effects on the shadow!
    glDisable(GL_LIGHTING) 

    glPushMatrix()
    glTranslatef(*SunPos)       # STEP 1: move origin to light pos

    # project onto negative of sun's Y coordinate
    PM = projectionMatrix(-1*SunPos[1])
    glMultMatrixf(PM);          # STEP 2: flattens out the objects

    glTranslatef(*twVectorScale(SunPos,-1)) # STEP 3: translate back
    
    shadowColor = (0.5,0.5,0.5)
    twColor(shadowColor,0,0)
    ObjectDrawers[DrawObjectId]()

    glPopMatrix()

    glFlush()
    glutSwapBuffers()

def timeLapse():
    global SunAngle, SunAngleDelta
    SunAngle += 0.01;
    if SunAngle > M_PI:
        SunAngle -= M_PI
    setSunPos()
    glutPostRedisplay()

def step(key, x, y):
    timeLapse()

def restart(key, x, y):
    initSun()
    glutIdleFunc(timeLapse)
    glutPostRedisplay()

def resume(key, x, y):
    glutIdleFunc(timeLapse)
    glutPostRedisplay()

def faster(key, x, y):
    global SunAngleDelta
    SunAngleDelta *= 2

def slower(key, x, y):
    global SunAngleDelta
    SunAngleDelta /= 2

def toggleBlock(key, x, y):
    global drawBlockp
    drawBlockp = not drawBlockp
    glutPostRedisplay()

def cycleObject(key, x, y):
    global DrawObjectId
    DrawObjectId += 1
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(500, 500)
    twBoundingBox(-20,20,0,25,-5,5)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    glShadeModel(GL_SMOOTH)
    twMainInit()
    initSun()
    twKeyCallback('1', step, "steps by one frame")
    twKeyCallback('s', restart, "starts animation from beginning")
    twKeyCallback('r', resume, "resumes animation")
    twKeyCallback('+', faster, "double speed of animation")
    twKeyCallback('-', slower, "halve speed of animation")
    twKeyCallback('d', toggleBlock, "toggle drawing the object")
    twKeyCallback('o', cycleObject, "cycle through the objects")
    glutIdleFunc(None)
    glutMainLoop()

if __name__ == '__main__':
    main()
