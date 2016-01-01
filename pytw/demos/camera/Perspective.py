'''Contrast of perspective as a function of FOVY. Both scenes are viewing
   a wire cube of the same size.  The camera moved farther from the scene
   and the NEAR is changed so that the image plane is the same distance
   from the cube in each scene.  The aspect ratio of the cameras is the
   same.  The only difference in the camera shapes is the FOVY.

Implemented Fall 2003
Scott D. Anderson

Ported to Python, Fall 2009
'''

import sys
import math                     # for atan and others

from TW import *

## ================================================================

GAP = 25      			# gap around subwindows
leftWinWidth=300;
leftWinHeight=300;
rightWinWidth=300;
rightWinHeight=300;

def parentDisplay():
    twDisplayInit();
    glFlush();
    glutSwapBuffers();

def aspectRatio(w, h):
    '''Returns the aspect ratio of a rectangle, given width w and height h.'''
    return float(w)/float(h)

LeftWinEyeZ = 2

def leftDisplay():
    '''display function for the left subwindow'''
    twDisplayInit(0.8,1.0,1.0);
    ar = aspectRatio(leftWinWidth,leftWinHeight)
    eyedist = LeftWinEyeZ - 1   # from top of frustum
    fovy = 2*math.atan(1/eyedist)*180/M_PI
    if fovy != 90.0:
        print "fovy in left window is not 90!!"
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(fovy,ar,eyedist,eyedist+2);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    ## Eye is 2 units from the origin, so 1.5 units from the near face
    ## of the cube and 2.5 units from the far face, so we see a big
    ## difference in apparent dimensions (the front face is 3/5s the
    ## size of the back face)
    gluLookAt(0,0,LeftWinEyeZ, 0,0,0, 0,1,0);

    twColorName(TW_RED);
    glutWireCube(1);            # from z=0.5 to z=-0.5, etc.
  
    glFlush();
    glutSwapBuffers();

AdditionalEyeDistance = 2.0     # additive term.  Eye in Right window
                                # is this many units farther.

def rightDisplay():
    '''display function for the right subwindow'''
    twDisplayInit(0.8,1.0,0.8);
    ar = aspectRatio(leftWinWidth,leftWinHeight)
    RightWinEyeZ = LeftWinEyeZ + AdditionalEyeDistance
    eyedist = RightWinEyeZ - 1  # from top of frustum
    ## The following code calculates a fovy based on a right triangle
    ## where the vertical leg is length 1 (on the frustum) and the
    ## other is eyedist (from the frustum).  The fovy is double that
    ## angle, converted to degrees.
    fovy = 2*math.atan(1/eyedist)*180/M_PI
    print "eyez is %f, eye distance is %f so fovy = %f degrees" % (
        RightWinEyeZ,eyedist,fovy)
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(fovy,ar,eyedist,eyedist+2);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(0,0,RightWinEyeZ, 0,0,0, 0,1,0);

    twColorName(TW_MAGENTA);
    glutWireCube(1);
  
    glFlush();
    glutSwapBuffers();

### These hold window identifiers, which are integers returned by the
### windowing system.
parentWin = 0
leftWin = 0
rightWin = 0

def redisplayAll():
    glutSetWindow(leftWin)      # makes leftWin be the current window
    glutPostRedisplay();        # say it needs redisplay
    glutSetWindow(rightWin);
    glutPostRedisplay();

def modifyM(key, x, y):
    '''Modify the distance that the eye is from the cube in the right window.'''
    global AdditionalEyeDistance
    if key == '+':
        AdditionalEyeDistance += 1.0
    elif key == '-':
        AdditionalEyeDistance -= 1.0
        if AdditionalEyeDistance < 0.0:
            AdditionalEyeDistance = 0.0
    print "AdditionalEyeDistance is now ", AdditionalEyeDistance
    eyedist = LeftWinEyeZ+AdditionalEyeDistance
    #print "Relative size of front and back is ", 2*(M-2)/(M-1)
    #print " Back projects to size ", 2*(M-2)/(M+1)
    redisplayAll();

def main():
    global parentWin, leftWin, rightWin
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    # create a main window with enough room for both subwindows and the gaps
    glutInitWindowSize(
      GAP+leftWinWidth+GAP+rightWinWidth+GAP, # widths from left to right
      GAP+leftWinHeight+GAP                   # heights from top to bottom
      )
    parentWin = glutCreateWindow(sys.argv[0]);
    glutDisplayFunc(parentDisplay);

    twBoundingBox(-1,1,-1,1,-1,1); # twMainInit will complain if BB not set
    twMainInit();

    ## glutCreateSubWindow returns the ID of the sub-window and takes 
    ## arguments:(int parent,int x,int y,int width,int height).
    ## Origin at x,y; height equals distance from y _down_
    leftWin = glutCreateSubWindow(parentWin,GAP,GAP,leftWinWidth,leftWinHeight);

    ## Each time you create a new window you need to give it its own 
    ## callbacks and initialization. These can be the same as those
    ## from other windows but you must call them each time
    twBoundingBox(-10,10,-10,10,-10,10);
    glutDisplayFunc(leftDisplay);
    twMainInit(); 

    rightWin = glutCreateSubWindow(parentWin,GAP*2+leftWinWidth,GAP,rightWinWidth,rightWinHeight);
    glutDisplayFunc(rightDisplay);
    twMainInit();
    twKeyCallback('+',modifyM,'Increase distance in right window')
    twKeyCallback('-',modifyM,'Decrease distance in right window')
    glLineWidth(2);
  
    redisplayAll(); 
    glutMainLoop();

if __name__ == '__main__':
    main()
