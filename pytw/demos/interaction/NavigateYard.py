""" Puts up a fence around a scene with a building. Demonstrates
   navigation callbacks, including strafing and moving up/down.  Also
   demonstrates the miner's hat effect.

Written by Caroline Geiersbach and Scott D. Anderson
scott.anderson@acm.org
Summer 2003
Ported to Python 2009
"""

import sys
import math # for tan, atan

try:
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
        '''

import Yard

### ================================================================

# Window dimensions
WinWidth = 600
WinHeight = 400

# Frustum dimensions.  We'll have some distortion if the frustum
# (image rectangle) is square and the window is not
FrustumWidth = 2
FrustumHeight = 2
Near = 1
Far = 200

# Bounding box dimensions

BBXmin = -45;         # bounding box X min
BBXmax = 65;          # X max
BBYmin = 0;           # Y min
BBYmax = 65;          # Y max
BBZmin = -130;        # Z min
BBZmax = 5;           # Z min

### ================================================================

def crosshairs():
    """Draws crosshairs on the image plane

This will only work properly in the default camera frame"""
    glDisable(GL_LIGHTING);
    twColorName(TW_BLACK);
    # draw the crosshairs *just* inside the frustum
    depth = -(Near+0.05);
    glBegin(GL_LINES);
    glVertex3f(-FrustumWidth/2,0,depth);
    glVertex3f(+FrustumWidth/2,0,depth);
    glVertex3f(0,-FrustumHeight/2,depth);
    glVertex3f(0,+FrustumHeight/2,depth);
    glEnd();

VRP = [(BBXmax+BBXmin)/2,
       (BBYmax+BBYmin)/2,
       BBZmax ]
VPN = [0,0,-1]
VRIGHT = [1,0,0]

def display():
    twDisplayInit();
    
    #twCameraShape();
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glFrustum(-FrustumWidth/2,FrustumWidth/2,
              -FrustumHeight/2,FrustumHeight/2,
              Near,Far);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    crosshairs();
    
    # set up a light facing forward.  It travels with us, like a
    # miner's light
    twGraySpotlight(GL_LIGHT1,(0,0,0,1),0,1,1,(0,0,-1),20,5)

    # now, set the camera where we really want it
    # twCameraPosition();
    gluLookAt(VRP[0],VRP[1],VRP[2],
              VRP[0]+VPN[0],VRP[1]+VPN[1],VRP[2]+VPN[2],
              0,1,0);

    Yard.draw()

    glFlush();
    glutSwapBuffers();       # necessary for animation


def turnCamera(radians):
    global VPN, VRIGHT
    c = math.cos(radians);
    s = math.sin(radians);

    # update VPN
    x = VPN[0];
    z = VPN[2];
    VPN[0] = c*x+s*z;
    VPN[2] = -s*x+c*z;

    # update VRIGHT
    x = VRIGHT[0];
    z = VRIGHT[2];
    VRIGHT[0] = c*x+s*z;
    VRIGHT[2] = -s*x+c*z;


def mySpecialFunction( key, x, y ):
    if key == GLUT_KEY_UP:   
        VRP[1] += 1
    elif key == GLUT_KEY_DOWN: 
        VRP[1] -= 1
    elif key == GLUT_KEY_RIGHT:
        VRP[0]+=VRIGHT[0];
        VRP[1]+=VRIGHT[1];
        VRP[2]+=VRIGHT[2];
    elif key == GLUT_KEY_LEFT:
        VRP[0]-=VRIGHT[0];
        VRP[1]-=VRIGHT[1];
        VRP[2]-=VRIGHT[2];
    elif key == GLUT_KEY_PAGE_UP:
        # goes forward
        VRP[0]+=VPN[0];
        VRP[1]+=VPN[1];
        VRP[2]+=VPN[2];
    elif key == GLUT_KEY_PAGE_DOWN:
        # goes backward
        VRP[0]-=VPN[0];
        VRP[1]-=VPN[1];
        VRP[2]-=VPN[2];
    elif key == GLUT_KEY_HOME:
        turnCamera(10*M_PI/180);
    elif key == GLUT_KEY_END:
        # turns 10 degrees right
        turnCamera(-10*M_PI/180);
    glutPostRedisplay();

def myMouseFunction(button, state, mx, my ):
    if button != GLUT_LEFT_BUTTON:
        return
    if state != GLUT_DOWN:
        return
    mx = mx - WinWidth/2;
    my = WinHeight/2 - my;

    ix = (FrustumWidth*mx)/float(WinWidth)
    # print "ix is ", ix
    theta = -math.atan(ix/Near);
    print "mx=%d theta=%f radians (%f degrees)" % (mx,theta, theta*180/M_PI)
    turnCamera(theta);
    glutPostRedisplay();

# ================================================================

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(WinWidth,WinHeight);
    glutCreateWindow(sys.argv[0])
    twBoundingBox(BBXmin,BBXmax,BBYmin,BBYmax,BBZmin,BBZmax);
    glutDisplayFunc(display)
    twMainInit()
    Yard.drawInit()
  # the following two are after twMainInit to override its callback settings
    glutMouseFunc(myMouseFunction);
    glutMotionFunc(None);
    glutSpecialFunc(mySpecialFunction);
    glutReshapeFunc(None);      # Maybe in a future version
    glutMouseFunc(myMouseFunction);
    glutMainLoop();

if __name__ == '__main__':
    main()
