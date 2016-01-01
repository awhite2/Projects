'''Copyright (C) <2013>  <Abra White>


'''
"""import sys

from TW import *;"""

#angles for FOVY start with a wide angle and end with a telephoto like lens -- zoom in
StartAngle=45
EndAngle=25

#initialize the FOVY as the start angle
FOVY = StartAngle

#stair size values
stairL=6
stairW=0.5
stairH=2
stairnum = 5
stairlevels = 11
Height = ((stairW+stairH)*stairnum*stairlevels) #of the entire staircase
Width = stairH*(stairnum-1)+(stairL)-(stairW*stairnum)

#camera angle
ViewMode = '1'

#Y placement of the camera Y1 is the initial height
cameraY1=Height-stairL
cameraY=cameraY1

#do not animate at first
Animating = False

Time = 0
DeltaT = 0.1
'''
## ================================================================
### We have two subwindows, the staircase/animation
### the left, and the command window on the right,
### which shows the values and allows them to be changed.

GAP = 25                        # gap between subwindows

objWinWidth=597
objWinHeight=537
comWinWidth=537               # command window width
comWinHeight=597              # command window height

mWinWidth=GAP+objWinWidth+GAP+comWinWidth+GAP   # main window width
mWinHeight=max(GAP+objWinHeight+GAP+objWinHeight+GAP,
               GAP+comWinHeight+GAP) # main window height 

## colors used in program
plainText = (1,1,1);            # white
headerText = (0,1,1);           # cyan
infoText = (1,0,0);             # red
gray = (0.8,0.8,0.8);
green = (0.8,1,0.6);

##cells are used in the command window; each cell has an id; a
##raster location at x,y; min and max values; a current value; the 
##step for adjusting values; info on what the cell specifies; and
##finally the format of the printed values.

class cell(object):
    def __init__(self, id, x, y, min, max, value, step, info, format):
        self.id =id
        self.x  =x
        self.y  =y
        self.min = min
        self.max = max
        self.value = value
        self.step = step
        self.info = info
        self.format = format

cameraPosition = (
    cell( 1, 225, 120, Height, 100.0, cameraY1, 0.2,
    "Specifies the initial Y position of the camera", "%.2f" )
    )
cameraAngles = (
    cell( 2, 225, 160, 35, 55, StartAngle, 0.2,
    "Specifies the initial Start Angle of the camera", "%.2f" ),
    cell( 3, 285, 120, 20, 30, EndAngle, 0.2,
    "Specifies the initial End Angle of the camera", "%.2f" )
    )

selection = 0 # the index (id) of the selected cell
old_y=0 # for command mouse

savedPosition = None
savedStartA = None
savedEndA = None

global projection, modelview, inverse;
global window, adjustable, saved, command;

def cellDraw(cell):
    #Draws a cell as text on the screen.
    if (selection == cell.id):
        glColor3fv(infoText);
        twDrawString2(10, 20, cell.info);
        twDrawString2(cell.x, cell.y, cell.format % (cell.value))
    else:
        glColor3fv(plainText)
        twDrawString2(cell.x, cell.y, cell.format % (cell.value))

def cellHit(cell, x, y):
    #returns cell id if cell has been clicked on; 0 otherwise
    if (x > cell.x and x < cell.x+55 and
        y > cell.y-15 and y < cell.y+15):
        return cell.id
    return 0

def cellUpdate(cell, update):
    #updates the cells value based on an update delta
    if selection != cell.id:
        return;
    cell.value += update * cell.step;
    ##tests for min and max values of the points
    if cell.value < cell.min:
        cell.value = cell.min
    elif cell.value > cell.max:
        cell.value = cell.max   

def cellVector(dst, cell, num):
    #copies values from cells to the destination vector DST
    if len(dst) < num:
        print "length of destination vector is too short %d < %d " % (len(dst),num)
    if len(cell) < num:
        print "length of source vector is too short %d < %d " % (len(cell),num)
    while (num >= 0):
        num -= 1
        dst[num] = cell[num].value
'''
## ================================================================

def stairs(levels, num, l, w, h):
    ''' Draws a set of stairs with landings in a spiral for 'levels' levels 
    the entire staircase is achieved recursively
    a level is one set of stairs with a landing
    Num is the number of steps
    l is the length along the z
    w is the 'thickness' of the piece of wood
    h plus w is the height of one step
    h minus w is the distance from the edge of one step to the start of the next
    shown sideways so if you were going up the stairs you'd be walking along the x-axis. The origin is in the center of the front of the first step '''
    if(levels!=0):
        a = num*2
        glPushMatrix()
        while a>0:
            if a==1: #draws the last plank and the landing
                glPushMatrix()
                glScaled(h,w,l)
                glutSolidCube(1)
                glPopMatrix()
                glTranslated(.5*l,0,0)
                glPushMatrix()
                glScale(l,w,l)
                glutSolidCube(1)
                glPopMatrix()

            elif a%2==0: #draws the vertical planks
                glPushMatrix()
                glScaled(w,h,l)
                glutSolidCube(1)
                glPopMatrix()
                glTranslated(.5*h-.5*w,.5*h+.5*w,0)
            else: #draws the horizontal planks
                glPushMatrix() 
                glScaled(h,w,l)
                glutSolidCube(1)
                glPopMatrix()
                glTranslated(.5*h+.5*w,.5*h-.5*w,0)
            a=a-1
            
        '''move to the next set of stairs and call the stairs method
        recursive to save the matrix position'''
        glRotate(90,0,1,0)
        glTranslate(.5*l-.5*w,.5*h,0)
        stairs(levels-1,num,l,w,h)

        '''final pop. It doesn't pop until now so that the staircase can keep getting higher'''
        glPopMatrix()
     

def setCamera():
    '''Two Camera options
    if the user presses one, or the default camera it is just a twCamera
    if the user presses two they are given camera view based on the dimensions of the staircase
    it should be in the middle of the staircase looking directly down with the up vector along the positive z axis.
    '''
    if ViewMode == '2':
        #twCamera()
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        gluPerspective(FOVY,1,stairnum/2*(stairH+stairW),cameraY+1);
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
        gluLookAt((stairnum*stairH)/2,cameraY,-.5*stairL-(stairnum*stairH)/2,
                  (stairnum*stairH)/2,0,-.5*stairL-(stairnum*stairH)/2,
                  0,0,1);
    else:
        twCamera()

cameratext =  ""     
        
def update():
    '''Updates the camera to achieve the dolly zoom effect
    as time increases the FOV decreases (zoom in)
    and the y position of the camera increases (dolly out)
    '''
    global Time, FOVY, cameraY, cameratext
    Time +=DeltaT
    if FOVY>EndAngle:
        FOVY = FOVY-DeltaT
        cameraY = cameraY + DeltaT
        cameratext = "FOVY: "+ str(FOVY) + " Camera Height: "+ str(cameraY)
        #print "The TIME is now %f " % (Time)
        #print "The FOVY is now %f " % (FOVY)
    glutPostRedisplay()

def init():
    '''Sets the camera and time to their initial values'''
    global Time, FOVY, StartAngle, cameraY, cameraY1
    Time = 0
    FOVY = StartAngle
    cameraY = cameraY1
    #print (Time)
    glutPostRedisplay()

'''For creating multiple panes
def mainDisplay():

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0,mWinWidth,mWinHeight,0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glClearColor(0.7, 0.7, 1.0, 0.0); ##light blue background
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    twColorName(TW_BLACK);
    twSetFont("helvetica", 12);
    twDrawString2(GAP,20, "Animation");
    '''

def adjustableDisplay():
    twDisplayInit();
    setCamera();

    '''use material and lighting to emphasize the changing perspective'''
    lightPos1 = ((stairnum*stairH)/2, Height/2, -.5*stairL-(stairnum*stairH)/2, 1 )
    twGrayLight(GL_LIGHT1,lightPos1,0.4,0.5,0.8);

    glColorMaterial ( GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE )
    glEnable ( GL_COLOR_MATERIAL )

    glEnable(GL_LIGHTING);
    glShadeModel(GL_SMOOTH);

    twGround()
    
    '''grey sandy color like in vertigo'''
    glColor3d(139.0/255.0,134.0/255.0,130.0/255.0)
    stairs(stairlevels,stairnum, stairL, stairW, stairH)

    twDrawString((stairnum*stairH)/2,cameraY-10,-.5*stairL-(stairnum*stairH)/2,cameratext);
    
    glFlush()
    glutSwapBuffers();

def myCamSettings (key, x, y):
    '''sets the camera view ... twCamera or the dolly zoom camera'''
    global ViewMode
    ViewMode = key;
    glutPostRedisplay();

def myAnimationSettings(key, x, y):
    '''turns on animation or resets the animation by pressing p'''
    global Animating
    if key == 'p':
        Animating = not Animating
        glutIdleFunc(update if Animating else init)
'''
def redisplayAll():
    glutSetWindow(adjustable);
    glutPostRedisplay();'''

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    #glutInitWindowSize(mWinWidth, mWinHeight); 
    #glutInitWindowPosition(0, 0);
    twInitWindowSize(500,500);
    twBoundingBox(-10,20,0,100,-20,5)
    '''
    window = glutCreateWindow("Light & Material Tutor 2");
    glutDisplayFunc(mainDisplay);

    adjustable = glutCreateSubWindow(window, GAP, GAP*2+objWinHeight, objWinWidth, objWinHeight);
    twBoundingBox(-10,20,0,100,-20,5)
    glutDisplayFunc(adjustableDisplay);
    '''
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(adjustableDisplay)
    twMainInit()
    twKeyCallback('1', myCamSettings, "Stairs Side View");
    twKeyCallback('2', myCamSettings, "Animation View");
    twKeyCallback('p', myAnimationSettings, "Play Animation");
    #redisplayAll();
    glutMainLoop()

if __name__ == '__main__':
    main()

        
            

    
