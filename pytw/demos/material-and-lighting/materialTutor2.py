''' Tutor intended to teach the TW API for materials and lighting, which is
a simplification of the OpenGL API, in which we commit to gray light and
opaque material where the ambient and diffuse values are the same color
and the specular is gray. Thus, a material can be specified with just five
values (instead of 13), and a light can be specified with three values
(instead of 9). The code is based on the lightmaterial tutorial by Nate
Robins.

Written by Caroline Geiersbach and Scott D. Anderson
scott.anderson@acm.org
Summer 2003

Fall 2005, revised to use twGrayLight
Fall 2009, ported to Python
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

### We have three subwindows, the saved and adjustable object windows on
### the left, which show the object, and the command window on the right,
### which shows the values and allows them to be changed.

GAP = 25                        # gap between subwindows

### TODO:  The following should be improved

objWinWidth=256
objWinHeight=256
comWinWidth=537               # command window width
comWinHeight=537              # command window height

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

## The Y coordinate is the 3rd one.  A spacing of about 40 works pretty well for "one line"

lightPosition = (
    cell( 1, 225, 120, -5.0, 5.0, 3.0, 0.05,
    "Specifies X coordinate of light vector.", "%.2f" ),
    cell( 2, 285, 120, -5.0, 5.0, 0.0, 0.05,
    "Specifies Y coordinate of light vector.", "%.2f" ),
    cell( 3, 345, 120, -5.0, 5.0, 2.0, 0.05,
    "Specifies Z coordinate of light vector.", "%.2f" ),
    cell( 4, 405, 120, 0.0, 1.0, 1.0, 1.0,
    "Specifies directional (0) or positional (1) light.", "%.2f" )
    )

lightIntensity = (
    cell(  9, 250, 160, 0.0, 1.0, 0.5, 0.01,
    "Specifies ambient intensity of the gray light.", "%.2f" ),
    cell( 10, 310, 160, 0.0, 1.0, 0.5, 0.01,
    "Specifies diffuse intensity of the gray light.", "%.2f" ),
    cell( 11, 370, 160, 0.0, 1.0, 0.5, 0.01,
    "Specifies specular intensity of the gray light.", "%.2f" )
    )

gAmbient = (
    cell( 17, 115, 200, 0.0, 1.0, 0.3, 0.01,
      "Specifies global ambient light value.", "%.2f" ),
    )

material = (
    cell( 21, 200, 300, 0.0, 1.0, 0.5, 0.01,
    "Specifies red component of the material.", "%.2f" ),
    cell( 22, 280, 300, 0.0, 1.0, 0.7, 0.01,
    "Specifies green component of the material.", "%.2f" ),
    cell( 23, 360, 300, 0.0, 1.0, 0.5, 0.01,
    "Specifies blue component of the material.", "%.2f" ),
    cell( 24, 180, 340, 0.0, 1.0, 0.7, 0.01,
    "Specifies specularity of the material.", "%.2f" ),
    cell( 25, 260, 340, 0.0, 128, 30.0, 1.0,
    "Specifies shininess of the material.", "%.2f" )
    )

savedDraw = GL_TRUE             # Whether to copy the adjustable values to the saved values
selection = 0                   # the index (id) of the selected cell
old_y = 0                       # for command mouse

## saved values for lighting and material (saved image is in upper right)
savedPosition = [ None, None, None, None ]
savedLightIntensity = [ None, None, None ]
savedMaterial = [ None, None, None, None, None ]
savedGlobalAmbient = None

lGATemp = gAmbient[0].value

global projection, modelview, inverse;
global window, adjustable, saved, command;

def cellDraw(cell):
    '''Draws a cell as text on the screen.'''
    if (selection == cell.id):
        glColor3fv(infoText);
        twDrawString2(10, 20, cell.info);
        twDrawString2(cell.x, cell.y, cell.format % (cell.value))
    else:
        glColor3fv(plainText)
        twDrawString2(cell.x, cell.y, cell.format % (cell.value))
        
def cellHit(cell, x, y):
    '''returns cell id if cell has been clicked on; 0 otherwise'''
    if (x > cell.x and x < cell.x+55 and
        y > cell.y-15 and y < cell.y+15):
        return cell.id
    return 0

def cellUpdate(cell, update):
    '''updates the cell's value based on an update delta'''
    if selection != cell.id:
        return;
    cell.value += update * cell.step;
    ##tests for min and max values of the points
    if cell.value < cell.min:
        cell.value = cell.min
    elif cell.value > cell.max:
        cell.value = cell.max   

##
def cellVector(dst, cell, num):
    '''copies values from cells to the destination vector DST'''
    if len(dst) < num:
        print "length of destination vector is too short %d < %d " % (len(dst),num)
    if len(cell) < num:
        print "length of source vector is too short %d < %d " % (len(cell),num)
    while (num >= 0):
        num -= 1
        dst[num] = cell[num].value

def mainDisplay():
    ##set up camera to allow for window labeling
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0,mWinWidth,mWinHeight,0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glClearColor(0.7, 0.7, 1.0, 0.0); ##light blue background
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    twColorName(TW_BLACK);
    twSetFont("helvetica", 12);
    twDrawString2(GAP,20, "Saved");
    twDrawString2(GAP,GAP+objWinWidth+20, "Adjustable");
    glutSwapBuffers();

def adjustableLighting():
    pos = [ None, None, None, None ]
    lI  = [ None, None, None ]
    cellVector(pos, lightPosition, 4);
    cellVector(lI, lightIntensity, 3);
    glShadeModel(GL_SMOOTH);    # dunno why this is *here*
    twAmbient(gAmbient[0].value);
    twGrayLight(GL_LIGHT0, pos, lI[0], lI[1], lI[2]);
    glEnable(GL_LIGHT0);
    glEnable(GL_LIGHTING);

def adjustableDisplay():
    '''display in the lower left (adjustable-space view)'''
    twCamera(); 
    glClearColor(0,0,0,1); ##clear sub-window to black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    adjustableLighting();

    colorVal = [ material[0].value,
                 material[1].value,
                 material[2].value ]
    twColor(colorVal, material[3].value, material[4].value);
    glutSolidTorus(0.25, 0.75, 28, 28);

    # use plain RGB color from now on
    glDisable(GL_LIGHTING);
    glDisable(GL_LIGHT0);

    ## draw line from light source to center of object    
    glPushMatrix();
    twColor(gray,0,0); 
    glBegin(GL_LINE_STRIP);
    glVertex3f(0, 0, 0)
    glVertex3f(lightPosition[0].value,
               lightPosition[1].value,
               lightPosition[2].value)
    glEnd();
    glPopMatrix();
    
    glFlush();
    glutSwapBuffers();

def savedLighting():
    global savedDraw, savedPosition, savedLightIntensity, savedMaterial, savedGlobalAmbient
    if(savedDraw == GL_TRUE):
        # copy new values
        cellVector(savedPosition, lightPosition, 4);
        cellVector(savedLightIntensity, lightIntensity, 3);
        cellVector(savedMaterial, material, 5);
        savedGlobalAmbient = gAmbient[0].value;
    savedDraw = GL_FALSE;
    ##lighting using saved values
    glShadeModel(GL_SMOOTH);    # still not sure why this is *here*
    twAmbient(savedGlobalAmbient);
    twGrayLight(GL_LIGHT1, savedPosition,
                savedLightIntensity[0],
                savedLightIntensity[1],
                savedLightIntensity[2])
    glEnable(GL_LIGHT1);
    glEnable(GL_LIGHTING);

def savedDisplay():
    '''display in the upper left (saved-space view)'''
    twCamera(); 
    glClearColor(0,0,0,1); ##clear sub-window to black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    
    savedLighting();
    colorVal2 = [ savedMaterial[0], savedMaterial[1], savedMaterial[2] ]
    twColor(colorVal2, savedMaterial[3], savedMaterial[4] )
    glutSolidTorus(0.25, 0.75, 28, 28);   

    # use RGB color from now on
    glDisable(GL_LIGHT0);
    glDisable(GL_LIGHTING);

    ##draw line from light source to center of object    
    glPushMatrix();
    twColor(gray,0,0); 
    glBegin(GL_LINE_STRIP);
    glVertex3f(0, 0, 0);    
    glVertex4fv(savedPosition)
    glEnd();
    glPopMatrix();

    glFlush();
    glutSwapBuffers();

def commandDisplay():
    '''display on right side; where user can adjust values'''
    ##set up camera
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0, comWinWidth, comWinHeight, 0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glClearColor(0.0, 0.0, 0.0, 1.0); ##clear to black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    twSetFont("helvetica", 18);
    glColor3fv(plainText);
    twDrawString2(10, lightPosition[0].y, "GLfloat lightPosition[ ] = {");
    twDrawString2(10, lightIntensity[0].y, "twGrayLight( lightPosition, ");
    twDrawString2(10, gAmbient[0].y, "twAmbient (");
    twDrawString2(10, material[0].y, "twTriple colorVals = (");
    twDrawString2(10, material[3].y, "twColor(colorVals,");
    twDrawString2(lightPosition[0].x+50, lightPosition[0].y, ",");
    twDrawString2(lightPosition[1].x+50, lightPosition[1].y, ",");
    twDrawString2(lightPosition[2].x+50, lightPosition[2].y, ",");
    twDrawString2(lightPosition[3].x+50, lightPosition[3].y, "};");
    twDrawString2(lightIntensity[0].x+50, lightIntensity[0].y, ",");
    twDrawString2(lightIntensity[1].x+50, lightIntensity[1].y, ",");
    twDrawString2(lightIntensity[2].x+50, lightIntensity[2].y, ");");
    twDrawString2(gAmbient[0].x+50, gAmbient[0].y, ");");
    twDrawString2(material[0].x+50, material[0].y, ",");
    twDrawString2(material[1].x+50, material[1].y, ",");
    twDrawString2(material[2].x+50, material[2].y, ");");
    twDrawString2(material[3].x+50, material[3].y, ",");
    twDrawString2(material[4].x+60, material[4].y, ");");
    
    ##draw values of each cell
    cellDraw(lightPosition[0]);
    cellDraw(lightPosition[1]);
    cellDraw(lightPosition[2]);
    cellDraw(lightPosition[3]);
    cellDraw(lightIntensity[0]);
    cellDraw(lightIntensity[1]);
    cellDraw(lightIntensity[2]);
    cellDraw(gAmbient[0]);
    cellDraw(material[0]);
    cellDraw(material[1]);
    cellDraw(material[2]);
    cellDraw(material[3]);
    cellDraw(material[4]);
    
    glColor3fv(headerText);
    if (not selection):
        twDrawString2(10, 20,
            "Click on the arguments and move the mouse to modify values.");
    twDrawString2(10,80,"Light Properties");
    twDrawString2(10,260,"Material Properties");
    ##directions at bottom of command window
    twDrawString2(10,420, "Hit <S> to save values, <P> to print saved values.");
    twDrawString2(10,460, "Hit <R> to reset adjustable to original values.");
    twDrawString2(10,500, "Hit <r> to reset adjustable to original view.");
    glutSwapBuffers();

## Because the selection is only set when the button goes down and isn't
## reset to zero when then button goes up, we can then use keyboard
## callbacks to adjust the numbers.

def commandMouse(button, state, x, y):
    global selection, old_y
    if(state == GLUT_DOWN):
        selection = 0;
        ## mouse should only hit _one_ of the cells, so adding up all
        ## the hits just propagates a single hit. */
        ##lighting
        selection += cellHit(lightPosition[0], x, y);
        selection += cellHit(lightPosition[1], x, y);
        selection += cellHit(lightPosition[2], x, y);
        selection += cellHit(lightPosition[3], x, y);
        selection += cellHit(lightIntensity[0], x, y);
        selection += cellHit(lightIntensity[1], x, y);
        selection += cellHit(lightIntensity[2], x, y);
        selection += cellHit(gAmbient[0], x, y);
        selection += cellHit(material[0], x, y);
        selection += cellHit(material[1], x, y);
        selection += cellHit(material[2], x, y);
        selection += cellHit(material[3], x, y);
        selection += cellHit(material[4], x, y);
    old_y = y;
    redisplayAll();

## The "update" argument is the number of steps of the cell's value.
## Anytime we create a new cell (or delete one), this function must be
## modified, which is a design flaw.  We should use a more object-oriented
## and dynamic approach.

def cellUpdateAll(update):
    cellUpdate(lightPosition[0], update);
    cellUpdate(lightPosition[1], update);
    cellUpdate(lightPosition[2], update);
    cellUpdate(lightPosition[3], update);
    cellUpdate(lightIntensity[0], update);
    cellUpdate(lightIntensity[1], update);
    cellUpdate(lightIntensity[2], update);
    cellUpdate(gAmbient[0], update);
    cellUpdate(material[0], update);
    cellUpdate(material[1], update);
    cellUpdate(material[2], update);
    cellUpdate(material[3], update);
    cellUpdate(material[4], update);

##allows for click and drag to adjust cell values
def commandMotion(x, y):
    '''callback when mouse moves.  Adjusts current cell value'''
    global old_y
    cellUpdateAll(old_y - y);
    old_y = y;
    redisplayAll();

def reset(key, x, y):
    if key == 'R':
        lightPosition[0].value = 3;
        lightPosition[1].value = 0;
        lightPosition[2].value = 2;
        lightPosition[3].value = 1;
        lightIntensity[0].value = 0.5;
        lightIntensity[1].value = 0.5;
        lightIntensity[2].value = 0.5;
        gAmbient[0].value = 0.3;
        material[0].value = 0.5;
        material[1].value = 0.7;
        material[2].value = 0.5;
        material[3].value = 0.7;
        material[4].value = 30.0;
    elif key == 'r':
        glutSetWindow(adjustable);
        twZview();
        glutSetWindow(saved);
        twZview();
    redisplayAll()

def myKeyboard(key, x, y):
    global savedDraw
    if key == 'P':
        print "your saved light and material values: "
        print "lightPosition = (%.2f,%.2f,%.2f,%.2f)" % tuple(savedPosition)
        print "lightIntensity = (%.2f,%.2f,%.2f)" % tuple(savedLightIntensity)
        print "twAmbient(%.2f)" % savedGlobalAmbient
        print "colorVals = (%.2f,%.2f,%.2f)" % (savedMaterial[0], savedMaterial[1], savedMaterial[2] )
        print "twColor=(colorVals,%.2f,%.2f)" % (savedMaterial[3], savedMaterial[4] )
    elif key == 'S':
        savedDraw = GL_TRUE
    elif key == '+' or key == '.':
        cellUpdateAll(1);
    elif key == '-' or key == ',':
        cellUpdateAll(-1);
    redisplayAll();

def keyInit():
    twKeyCallback('R',reset,"resets back to original settings");
    twKeyCallback('r',reset,"resets back to original view");
    twKeyCallback('P',myKeyboard,"prints saved values");
    twKeyCallback('S',myKeyboard,"saves current values");
    twKeyCallback('+',myKeyboard,"increment selected value");
    twKeyCallback('-',myKeyboard,"decrement selected value");
    # create these synonyms because they are unshifted and on the < and > keys
    twKeyCallback('.',myKeyboard,"increment selected value");
    twKeyCallback(',',myKeyboard,"increment selected value");

def redisplayAll():
    glutSetWindow(saved);
    glutPostRedisplay();
    glutSetWindow(command);
    glutPostRedisplay();
    glutSetWindow(adjustable);
    glutPostRedisplay();

def myInit():
    twMainInit();
    keyInit();

def main():
    global window, command, adjustable, saved
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH | GLUT_DOUBLE);
    glutInitWindowSize(mWinWidth, mWinHeight); 
    glutInitWindowPosition(0, 0);
    
    ##parent window
    window = glutCreateWindow("Light & Material Tutor 2");
    glutDisplayFunc(mainDisplay);
    myInit();
    
    ##upper left sub-window is the "saved" window
    saved = glutCreateSubWindow(window, GAP, GAP, objWinWidth, objWinHeight);
    twBoundingBox(-1,1,-1,1,-1,1);
    glutDisplayFunc(savedDisplay);
    myInit();
      
    ##right sub-window is the command window
    command = glutCreateSubWindow(window, GAP*2+objWinWidth, GAP, 
                                  comWinWidth,comWinHeight);
    glutDisplayFunc(commandDisplay);
    myInit();
    glutMotionFunc(commandMotion);
    glutMouseFunc(commandMouse);

    ##lower left sub-window is the "adjustable"
    adjustable = glutCreateSubWindow(window, GAP, GAP*2+objWinHeight, objWinWidth, objWinHeight);
    twBoundingBox(-1,1,-1,1,-1,1);
    glutDisplayFunc(adjustableDisplay);
    myInit();
    
    redisplayAll();
    glutMainLoop();

if __name__ == '__main__':
    main()
