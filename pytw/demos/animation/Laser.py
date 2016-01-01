""" Demonstrates how to compute the intersection of a line with a plane.
   This is used to compute the intersection of a laser beam with the roof
   of the barn.
   
Written by Scott D. Anderson and Caroline Geiersbach
scott.anderson@acm.org
Summer 2003
Fall 2009, ported to Python
"""
import sys
import math

try:
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
        '''

import random

### ================================================================

UFOpos   = [75,80,-25]
UFOdir   = [-.2,0,-.2]
LaserDir = [0,-1,0]

Frame=0;                    # which frame of animation
SubFrame=0;                 # subframe for shooting photon torpedos

# yes, this recomputes IP every time.  It's not as efficient as it
# could be
def blast(LaserPoint, LaserDir):
    global Frame, SubFrame
    fragments = (
        # ground
        ((0,0,0),(100,0,0),(0,0,-100)),
        # roof, right half
        ((15,40,-50),(15,40,-100),(30,0.7*40,-50))
        );

    LaserDir = list(twVectorNormalize(LaserDir))
    # Compute the parameter of the nearest intersection, if any.  The
    # intersection point, IP, is computed, as is its parameter, r.  "r"
    # is essentially the distance of IP from LaserPoint, in units of
    # LaserDir, which is of unit length.  */
    blast, IP, r = twNearestFragment(fragments,LaserPoint,LaserDir);

    # The maximum distance the torpedo could ever go is approximately
    # sqrt(2)*100, since the UFO is 100 units high and the maximum
    # angle is 45 degrees.  This divides that maximum distance into 10
    # steps (because of the multiplication by 0.1) and determines
    # which step using the SubFrame parameter. The result is the
    # distance of the torpedo from its launch point.  */
    torpedoParam = 0.1*math.sqrt(2)*100*SubFrame;

    twColorName(TW_MAGENTA);
    if( blast and torpedoParam > r ):
        # the torpedo is farther than the intersection point, so draw a
        # blast, of increasing radius, with a minimum radius of 5.
        if( SubFrame < 5 ):
            SubFrame = 5;
        glPushMatrix();
        glTranslatef(IP[0],IP[1],IP[2]);
        glutSolidSphere(SubFrame,20,20);
        glPopMatrix();
    else:
        # draw photonTorpedo, because it hasn't reached the IP yet
        photonTorpedo = twPointOnLine(UFOpos,LaserDir,torpedoParam);
        glPointSize(5);
        glBegin(GL_POINTS);
        glVertex3fv(photonTorpedo);
        glEnd();

def display():
    global LaserDir
    twDisplayInit();
    twCamera();                        # step 1 camera

    twColorName(TW_GREEN);
    twGround();

    glPushMatrix();
    glTranslatef(0,0,-50);
    glScalef(30,40,50);
    red = (1, 0, 0);
    dark = ( 0.2, 0.2, 0.2 )
    twSolidBarn(red,red,dark);        # red barn with dark roof
    glPopMatrix();

    glPushMatrix();
    glTranslatef(UFOpos[0],UFOpos[1],UFOpos[2]);
    glPushMatrix();
    glScalef(10,5,10);
    twColorName(TW_PURPLE);
    glutSolidSphere(1,20,20);  # UFO
    glPopMatrix();
    glLineWidth(3);
    glBegin(GL_LINES);
    glVertex3f(0,0,0);
    LaserDir = list(twVectorNormalize(LaserDir))
    # laser weapon is always 20 units long
    LaserDir = list(twVectorScale(LaserDir,20))
    glVertex3fv(LaserDir);
    glEnd();
    glPopMatrix();

    blast(UFOpos,LaserDir);

    glFlush();
    glutSwapBuffers();

def idle():
    global Frame, SubFrame, LaserDir
    for i in range(3):
        UFOpos[i] += UFOdir[i];
    if( UFOpos[0] < 0 or UFOpos[2] < -100):
        print "stop"
        glutIdleFunc(None);
    Frame += 1;
    SubFrame += 1;
    # New laser blast every 11 frames
    if(SubFrame == 10):
        SubFrame = 0;
        LaserDir[0] = random.gauss(0,5)
        LaserDir[2] = random.gauss(0,5)
        if False:
            down = (0,-1,0)
            LaserDir = twVectorNormalize(LaserDir);
            d = twDot(LaserDir,down);
            print "angle = %f" % (180*Math.acos(d)/M_PI);
    glutPostRedisplay();

def report(key, x, y):
    twTriplePrint("Position",UFOpos);
    twTriplePrint("Dir",LaserDir);

def next(key, x, y):
    idle();

def idleControl(key, x, y):
    global LaserDir, UFOpos, UFOdir
    if key == '+': 
        glutIdleFunc(idle);
    elif key == '-': 
        glutIdleFunc(None); 
    elif key == 'r':
        glutIdleFunc(None);
        glutPostRedisplay();
        report(key,x,y);
        LaserDir = [0,-1,0]
        UFOpos   = [75,80,-25]
        UFOdir   = [-.2,0,-.2]
        Frame=0;
        SubFrame=0;

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(0,100,0,100,-100,0);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    glPointSize(5);
    twKeyCallback('=',report,"report some values");
    twKeyCallback(' ',next,"next frame");
    twKeyCallback('+',idleControl,"go/run");
    twKeyCallback('-',idleControl,"stop");
    twKeyCallback('r',idleControl,"reset idle");
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;


if __name__ == '__main__':
    main()

