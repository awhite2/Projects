''' Demo to demonstrate the properties of vectors in 2-dimensional space

Written by Caroline Geiersbach and Scott D. Anderson
scott.anderson@acm.org
Summer 2003

ported to Python, Fall 2009
'''

import sys
import math                     # for atan and others

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''
## ================================================================

### We have two windows, the world window on the left, which shows the
### vectors, and the command window on the right, which shows the
### vector coordinates and allows them to be changed.

GAP = 25                        # gap between subwindows

wWinWidth=500               # world window width
wWinHeight=500              # world window height 
cWinWidth=400               # command window width
cWinHeight=500              # command window height
angle = 0

# mouseMode = 1: draw vectors in world; mouseMode = 0: tw mouse
mouseMode = 1

# keeps track of the number of clicks
ClickCount = 0

selection = 0                   # selected cell; zero is no cell selected

## window ids
window = None
world = None
screen = None
command = None

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

# values for the command window
# adjustable point cells

PointA = [
    cell(1,90,80,-10,10,0,1.0, "Specifies the X coordinate of point A", "%.1f"),
    cell(2,160,80,-10,10,0,1.0,"Specifies the Y coordinate of point A", "%.1f"),
    cell(3,230,80,-10,10,0,1.0,"Specifies the Z coordinate of point A", "%.1f")
    ]
    
PointB = [
    cell(4,90,120,-10,10,0,1.0,"Specifies the X coordinate of point B", "%.1f"),
    cell(5,160,120,-10,10,0,1.0,"Specifies the Y coordinate of point B", "%.1f"),
    cell(6,230,120,-10,10,0,1.0,"Specifies the Z coordinate of point B", "%.1f")
    ]

PointC = [
    cell(7,90,160,-10,10,0,1.0, "Specifies the X coordinate of point C", "%.1f"),
    cell(8,160,160,-10,10,0,1.0,"Specifies the Y coordinate of point C", "%.1f"),
    cell(9,230,160,-10,10,0,1.0,"Specifies the Z coordinate of point C", "%.1f")
    ]

# non-adjustable vector cells
VectorAB = [
    cell(10,130,240,-50,50,0,1, "Specifies the magnitude in the X direction for B-A", "%.1f"),
    cell(11,200,240,-50,50,0,1, "Specifies the magnitude in the Y direction for B-A", "%.1f"),
    cell(12,270,240,-50,50,0,1, "Specifies the magnitude in the Z direction for B-A", "%.1f")
    ]

VectorAC = [
    cell(13,130,280,-50,50,0,1, "Specifies the magnitude in the X direction for C-A", "%.1f"),
    cell(14,200,280,-50,50,0,1, "Specifies the magnitude in the Y direction for C-A", "%.1f"),
    cell(15,270,280,-50,50,0,1, "Specifies the magnitude in the Z direction for C-A", "%.1f")
    ]

def commandToWorld():
    '''sets the point values in world to the new values from command window'''
    print "is this really necessary?"
    pointA[0] = pA[0].value;
    pointA[1] = pA[1].value;
    pointA[2] = pA[2].value;

    pointB[0] = pB[0].value;
    pointB[1] = pB[1].value;
    pointB[2] = pB[2].value;

    pointC[0] = pC[0].value;
    pointC[1] = pC[1].value;
    pointC[2] = pC[2].value;

def assignVectorValues():
    global VectorAB, VectorAC, angle
    VectorAB[0].value = PointB[0].value-PointA[0].value; 
    VectorAB[1].value = PointB[1].value-PointA[1].value;
    VectorAB[2].value = PointB[2].value-PointA[2].value;

    VectorAC[0].value = PointC[0].value-PointA[0].value;
    VectorAC[1].value = PointC[1].value-PointA[1].value;
    VectorAC[2].value = PointC[2].value-PointA[2].value;

    v = (VectorAB[0].value, VectorAB[1].value, VectorAB[2].value)
    w = (VectorAC[0].value, VectorAC[1].value, VectorAC[2].value)
  
    if v == (0,0,0) or w == (0,0,0):
        angle = None
    else:
        angle = twRadiansToDegrees(math.acos(twCosAngle(v,w)))

def cellDraw(cell):
    '''Draws a cell as text on the screen.'''
    glColor3f(1,1,1)              # color of numbers when not selected
    if (selection == cell.id):
        glColor3f(0,1,1)            # color of info text
        twDrawString2(10, 20,cell.info);
    twDrawString2(cell.x, cell.y, cell.format % (cell.value))

def cellHit(cell, x, y):
    '''Returns cell id if the x,y location is in the cell, otherwise
zero.  A cell is always 70 pixels wide and 40 pixels high.'''
    if (x > cell.x and x < cell.x + 70 and
        y > cell.y-30 and y < cell.y+10):
        return cell.id
    else:
        return 0;

def cellUpdate(cell, update):
    '''Modifies a cell's value, sensitive to step size, min and max.'''
    if (selection != cell.id):
        return;
    cell.value += update * cell.step;
    
    # tests for min and max values of the points
    if (cell.value < cell.min):
        cell.value = cell.min;
    elif (cell.value > cell.max):
        cell.value = cell.max;

def mainDisplay():
    twDisplayInit();
    glutSwapBuffers();

def drawVector(p1, p2, color):
    '''draw vector from point p1 to p2, including arrow.  The points
p1 and p2 are points in the command window, so they are lists of
cells.'''
    twColorName(color);
    glLineWidth(2);
    glBegin(GL_LINES);
    glVertex3f(p1[0].value,p1[1].value,p1[2].value)
    glVertex3f(p2[0].value,p2[1].value,p2[2].value)
    glEnd();
    ## draw arrowhead as a cone
    glPushMatrix();
    glTranslatef(p2[0].value,p2[1].value,p2[2].value)
    negZ = (0,0,-1)
    arrow = (p2[0].value-p1[0].value, 
             p2[1].value-p1[1].value, 
             p2[2].value-p1[2].value)
    axis = twCrossProduct(negZ,arrow)
    ## rotate so minus Z axis points along arrow
    glRotatef(-90,axis[0],axis[1],axis[2])
    glutSolidCone(0.5, 1, 20, 20)
    glPopMatrix();

def worldDisplay():
    twCamera();
    glClearColor(1,1,1,1);      # clear sub-window to white
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
 
    glLineWidth(1);
    twAxes();
    glPointSize(5);

    if(ClickCount==1):
        ## First click is for first point, which is in red
        glBegin(GL_POINTS);
        twColorName(TW_RED);
        glVertex3f(PointA[0].value, PointA[1].value, PointA[2].value);
        glEnd();
    elif (ClickCount==2):
        ## Second click 
        glBegin(GL_POINTS);
        twColorName(TW_RED);
        glVertex3f(PointA[0].value, PointA[1].value, PointA[2].value);
        twColorName(TW_GREEN);
        glVertex3f(PointB[0].value, PointB[1].value, PointB[2].value);
        glEnd();
        drawVector(PointA, PointB, TW_CYAN);
    else:
        glBegin(GL_POINTS);
        twColorName(TW_RED);
        glVertex3f(PointA[0].value, PointA[1].value, PointA[2].value);
        twColorName(TW_GREEN);
        glVertex3f(PointB[0].value, PointB[1].value, PointB[2].value);
        twColorName(TW_BLUE);
        glVertex3f(PointC[0].value, PointC[1].value, PointC[2].value);
        glEnd();
        drawVector(PointA, PointB, TW_CYAN);
        drawVector(PointA, PointC, TW_ORANGE); 
    glutSwapBuffers()

def worldMouse(button, state, x, y):
    global ClickCount
    if(mouseMode == 0):
        twMouseFunction(button, state, x, y);
    else:
        y = wWinHeight-y;
        winA = (x,y,0)
        winB = (x,y,1)
        A = twUnProject(winA);
        B = twUnProject(winB);
        V = twVector(B,A);
        if (button==GLUT_LEFT_BUTTON and state==GLUT_DOWN):
            if ClickCount == 0:
                ## the first click is point A, or the middle point
                ClickCount += 1
                pointA = twPointOnLine(A, V, 0.5);
                ## set values to cells in command
                PointA[0].value = pointA[0];
                PointA[1].value = pointA[1];
                PointA[2].value = pointA[2];
                twTriplePrint("pointA",pointA);
            elif ClickCount == 1:
                ## the second click is point B
                ClickCount += 1
                pointB = twPointOnLine(A, V, 0.5);
                ## set values to cells in command
                PointB[0].value = pointB[0]
                PointB[1].value = pointB[1]
                PointB[2].value = pointB[2]
                twTriplePrint("pointB",pointB);
            elif ClickCount == 2:
                ## the third click is point C
                ClickCount = 0
                pointC = twPointOnLine(A, V, 0.5);
                PointC[0].value = pointC[0]
                PointC[1].value = pointC[1]
                PointC[2].value = pointC[2]
                twTriplePrint("pointC",pointC);
    redisplayAll();

## to override the current tw motion func
def worldMotion(x, y):
    if(mouseMode == 0): 
        twMotionFunction(x,y)

def commandDisplay():
    '''display for the command sub-window; this is where user can adjust
where points are located.'''
    # camera setup
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0, cWinWidth, cWinHeight, 0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glClearColor(0,0,0,1);      # clear screen to black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    twSetFont("helvetica",18);
    twColorName(TW_RED);

    twDrawString2(10,PointA[0].y,"point A");
    glColor3f(1,1,1);
    twDrawString2(73,PointA[0].y,"=(");
    twDrawString2(PointA[0].x+60,PointA[0].y,",");
    twDrawString2(PointA[1].x+60,PointA[1].y,",");
    twDrawString2(PointA[2].x+60,PointA[2].y,")");

    twColorName(TW_GREEN);
    twDrawString2(10,PointB[0].y,"point B");
    glColor3f(1,1,1);
    twDrawString2(73,PointB[0].y,"=(");
    twDrawString2(PointB[0].x+60,PointB[0].y,",");
    twDrawString2(PointB[1].x+60,PointB[1].y,",");
    twDrawString2(PointB[2].x+60,PointB[2].y,")");

    twColorName(TW_BLUE);
    twDrawString2(10,PointC[0].y,"point C");
    glColor3f(1,1,1);
    twDrawString2(73,PointC[0].y,"=(");
    twDrawString2(PointC[0].x+60,PointC[0].y,",");
    twDrawString2(PointC[1].x+60,PointC[1].y,",");
    twDrawString2(PointC[2].x+60,PointC[2].y,")");
    
    # non-adjustable cells
    twColorName(TW_CYAN);
    twDrawString2(10,VectorAB[0].y,"vector AB = (");
    twDrawString2(VectorAB[0].x+60,VectorAB[0].y,",");
    twDrawString2(VectorAB[1].x+60,VectorAB[1].y,",");
    twDrawString2(VectorAB[2].x+60,VectorAB[2].y,")");

    twColorName(TW_ORANGE);
    twDrawString2(10,VectorAC[0].y,"vector AC = (");
    twDrawString2(VectorAC[0].x+60,VectorAC[0].y,",");
    twDrawString2(VectorAC[1].x+60,VectorAC[1].y,",");
    twDrawString2(VectorAC[2].x+60,VectorAC[2].y,")");

    twColorName(TW_MAGENTA);
    if angle == None:
        twDrawString2(10,320,"angle between v and w is undefined");
    else:
        twDrawString2(10,320,"angle between v and w=%.2f"%(angle))
    
    cellDraw(PointA[0]);
    cellDraw(PointA[1]);
    cellDraw(PointA[2]);
    cellDraw(PointB[0]);
    cellDraw(PointB[1]);
    cellDraw(PointB[2]);
    cellDraw(PointC[0]);
    cellDraw(PointC[1]);
    cellDraw(PointC[2]);

    cellDraw(VectorAB[0]);
    cellDraw(VectorAB[1]);
    cellDraw(VectorAB[2]);
    cellDraw(VectorAC[0]);
    cellDraw(VectorAC[1]);
    cellDraw(VectorAC[2]);
 
    if (selection==0):
        glColor3f(1,1,1);
        twDrawString2(10, 20,
                     "Click on arguments and move mouse to modify values.");
    twDrawString2(10,380, "press 'm' to enable motion mode");
    twDrawString2(10,420, "press 'M' to enable drawing mode");
    glutSwapBuffers();

old_y = None

def commandMouse(button, state, x, y):
    global old_y, selection
    selection = 0;    
    if (state == GLUT_DOWN):
      ## mouse should only hit _one_ of the cells, so adding up all
      ## the hits just propagates a single hit. 
      selection += cellHit(PointA[0], x, y);
      selection += cellHit(PointA[1], x, y);
      selection += cellHit(PointA[2], x, y);

      selection += cellHit(PointB[0], x, y);
      selection += cellHit(PointB[1], x, y);
      selection += cellHit(PointB[2], x, y);

      selection += cellHit(PointC[0], x, y);
      selection += cellHit(PointC[1], x, y);
      selection += cellHit(PointC[2], x, y);
    old_y = y;
    redisplayAll();

def commandMotion(x, y):
    '''Mouse Motion callback in the command window.  The current cell, if any, is updated by the upward or downward movement of the mouse.'''
    global old_y
    dy = old_y - y
    cellUpdate(PointA[0],dy);
    cellUpdate(PointA[1],dy);
    cellUpdate(PointA[2],dy);
    cellUpdate(PointB[0],dy);
    cellUpdate(PointB[1],dy);
    cellUpdate(PointB[2],dy);
    cellUpdate(PointC[0],dy);
    cellUpdate(PointC[1],dy);
    cellUpdate(PointC[2],dy);
    
    old_y = y;
    redisplayAll();

def cellInit():
    '''Resets all point coordinates to zero.'''
    global ClickCount, mouseMode 
    global PointA, PointB, PointC
    global VectorAB, VectorAC
    ClickCount = 0;
    mouseMode = 1;
    
    PointA[0].value = 0;
    PointA[1].value = 0;
    PointA[2].value = 0;

    PointB[0].value = 0;
    PointB[1].value = 0;
    PointB[2].value = 0;

    PointC[0].value = 0;
    PointC[1].value = 0;
    PointC[2].value = 0;

    VectorAB[0].value = 0;
    VectorAB[1].value = 0;
    VectorAB[2].value = 0;

    VectorAC[0].value = 0;
    VectorAC[1].value = 0;
    VectorAC[2].value = 0;

def reinitializeValues(key, x, y):
    '''Keyboard callback to do resets'''
    if key == 'R':
        ## resets all values to 0 (erases the vectors and points)
        cellInit();
    elif key == 'r':
        ## resets back to original view without erasing current vectors
        twZview();
    redisplayAll()

def modeChange(key, x, y):
   '''keyboard callback to change the mouse behavior'''
   if key == 'm':
       mouseMode = 0
   if key == 'M':
       mouseMode = 1
   redisplayAll()

def choosePlane(key, x, y):
    '''keyboard callback to change the 2D plane that the vectors are drawn in'''
    if key == 'X': 
        twXview();
    elif key == 'Y':
        twYview();
    elif key == 'Z':
        twZview();
    redisplayAll()

def keyInit():
    '''set up all keyboard callbacks'''
    twKeyCallback('R',reinitializeValues,"Resets all point and vector values");
    twKeyCallback('r',reinitializeValues, "Resets to original screen");
    twKeyCallback('m', modeChange, "tw mouse mode");
    twKeyCallback('M', modeChange, "vector drawing mouse mode");
    twKeyCallback('Z', choosePlane, "chooses z = 0 plane");
    twKeyCallback('Y', choosePlane, "chooses y = 0 plane");
    twKeyCallback('X', choosePlane, "chooses x = 0 plane");

def redisplayAll():
    assignVectorValues();
    glutSetWindow(command);
    glutPostRedisplay();
    glutSetWindow(world);
    glutPostRedisplay();

def main():
    global window, command, world
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    # parent window
    glutInitWindowSize(wWinWidth+cWinWidth+GAP*3, 
                       wWinHeight+GAP*2)
    glutInitWindowPosition(0, 0); # position on computer screen
    window = glutCreateWindow("Vectors")
    twBoundingBox(-1,1,-1,1,-1,1); # not necessary
    glEnable(GL_DEPTH_TEST);
    glEnable(GL_NORMALIZE);
    glDepthFunc(GL_LEQUAL); 
    glPointSize(5)              # nice big fat dots
    glutDisplayFunc(mainDisplay);
    twMainInit()
    keyInit();

    ## glutCreateSubWindow returns the ID of the sub-window and takes 
    ## arguments:(int parent,int x,int y,int width,int height).
    ## Origin at x,y; height equals distance from y _down_
    ## create sub-window "command" for adjusting values
    command=glutCreateSubWindow(window,GAP*2+wWinWidth,GAP,cWinWidth,cWinHeight);
    glutDisplayFunc(commandDisplay);
    twMainInit();
    keyInit();
    glutMotionFunc(commandMotion);
    glutMouseFunc(commandMouse);

    ## create sub-window "world" for drawing vectors
    world=glutCreateSubWindow(window,GAP,GAP,wWinWidth,wWinHeight);
    ## Each time you create a new window you need to give it its own 
    ## callbacks and initialization. These can be the same as those
    ## from other windows but you must call them each time
    twBoundingBox(-10,10,-10,10,-10,10);
    glutDisplayFunc(worldDisplay);
    twMainInit(); 
    keyInit();
    glutMouseFunc(worldMouse);
    glutMotionFunc(worldMotion);

    redisplayAll(); 
    glutMainLoop()

if __name__ == '__main__':
    main()
