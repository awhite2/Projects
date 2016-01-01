""" Demo of three interpenetrating quads, to show transparency.

Implemented Fall 2003
Scott D. Anderson
Ported to Python Fall 2009
"""

import sys
import math

try:
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
        '''

### ================================================================

BgBlack = True
MidTrans = False
DepthMask = True
DepthTest = True
OpaqueFirst = True

TextLeft = -0.2          # X coordinate for left end of text

# I'm trying to make the cross section have an equilateral triangle, in
# the unit square, so this constant is useful, since it's the slope of
# the non-horizontal lines.
C=math.sqrt(3)

def opaqueRedQuad():
    glBegin(GL_QUADS);

    glColor4f(1,0,0,1);         # solid red
    glVertex3f(0,C/2,-1);       # back left
    glVertex3f(0,C/2,1);        # front left
    glVertex3f(1,C/2,1);        # front right
    glVertex3f(1,C/2,-1);       # back right

    glEnd();

def transparentGreenBlueQuads():
    glBegin(GL_QUADS);

    if MidTrans:
        glColor4f(0,1,0,0.5);        # middle opaque green
    else:
        glColor4f(0,1,0,0.7);        # fairly opaque green
    glVertex3f(0,1,-1);              # back left
    glVertex3f(0,1,1);               # front left
    glVertex3f(1/C,0,1);             # front right
    glVertex3f(1/C,0,-1);            # back right

    if MidTrans:
        glColor4f(0,0,1,0.5);        # middle opaque blue
    else:
        glColor4f(0,0,1,0.3);        # fairly transparent blue
    glVertex3f(1-1/C,0,-1);          # back left
    glVertex3f(1-1/C,0,1);           # front left
    glVertex3f(1,1,1);               # front right
    glVertex3f(1,1,-1);              # back right

    glEnd();

def depthMask():
    twColorName(TW_WHITE if BgBlack else TW_BLACK);
    glDepthMask(GL_TRUE if DepthMask else GL_FALSE);
    text = "Depth Mask %s - 'm' to toggle" % ("TRUE" if DepthMask else "FALSE");
    twDrawString(TextLeft,-0.1,1,text)
           

def depthTest():
    twColorName(TW_WHITE if BgBlack else TW_BLACK);
    if(DepthTest):
        glEnable(GL_DEPTH_TEST);
        twDrawString(TextLeft,-0.3,1, "Depth Test ON - 'd' toggles");
    else:
        glDisable(GL_DEPTH_TEST);
        twDrawString(TextLeft,-0.2,1, "Depth Test OFF - 'd' toggles");

def display():
    if(BgBlack):
        glClearColor(0,0,0,0);        # transparent black
    else:
        glClearColor(1,1,1,1);        # opaque white
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    twCamera();
    depthTest();

    if(OpaqueFirst):
        twColorName(TW_WHITE if BgBlack else TW_BLACK);
        twDrawString(TextLeft,0,1,"Opaque First: red, then green and blue - 'o' to toggle");

        # Normal settings for opaque objects
        glDepthMask(GL_TRUE);        # this is the default
        glDisable(GL_BLEND);

        opaqueRedQuad();
    
        # Settings for transparent objects
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        glEnable(GL_BLEND);

        depthMask();
        
        transparentGreenBlueQuads();
        glDepthMask(GL_TRUE);
        glDisable(GL_BLEND);
    else:
        twColorName(TW_WHITE if BgBlack else TW_BLACK);
        twDrawString(TextLeft,0,1,"Opaque Last:  green and blue, then red - 'o' to toggle");

        # Settings for transparent objects
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        glEnable(GL_BLEND);

        depthMask();

        transparentGreenBlueQuads();
        # Normal settings for opaque objects
        glDepthMask(GL_TRUE);        # this is the default
        glDisable(GL_BLEND);

        opaqueRedQuad();
    
    glFlush();
    glutSwapBuffers();

def keys(key, x, y):
    global BgBlack, DepthTest, DepthMask, MidTrans, OpaqueFirst
    if key == 'b': 
        BgBlack = not BgBlack
    elif key == 'd': 
        DepthTest = not DepthTest
    elif key == 'm': 
        DepthMask = not DepthMask
    elif key == 'M': 
        MidTrans = not MidTrans
    elif key == 'o': 
        OpaqueFirst = not OpaqueFirst
    glutPostRedisplay();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    twBoundingBox(0,1,0,1,-1,1);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    glutDisplayFunc(display);
    twKeyCallback('b',keys,"toggle black/white background");
    twKeyCallback('d',keys,"toggle depth test");
    twKeyCallback('m',keys,"toggle depth mask");
    twKeyCallback('M',keys,"toggle middle transparency: 0.7/0.3 vs 0.5/0.5");
    twKeyCallback('o',keys,"toggle opaque first/last");
    glutMainLoop();
    return 0;

if __name__ == '__main__':
    main()
