''' Simple demo of computing textures as arrays of values and
   texture-mapping them onto a 2D quad.  There are two textures:  the
   classic checkerboard (which is simple but boring because it is
   invariant almost no matter what you do to it) and the US flag.  Toggle
   between them using a 'u'.

   Scott D. Anderson
   Fall 2000 original
   Fall 2003 adapted to use TW
Ported to Python Fall 2009
'''

import sys
import math                            # for sin and cos

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''

## ================================================================

USFlag = False                  # which flag to show

def toggleFlag(key, x, y):
    global USFlag
    USFlag = not USFlag;
    glutPostRedisplay();

CheckFlagSize  = 16
CheckFlagArray = [ [ 255 if (i+j)&1 else 0 
                     for i in range(CheckFlagSize) ]
                   for j in range(CheckFlagSize) ]

def changeChecks(key, x, y):
    global CheckFlagSize
    if key == '+':
        CheckFlagSize = CheckFlagSize << 1 # double it
    elif key == '-':
        CheckFlagSize = max(1,CheckFlagSize >> 1) # halve it, min 1
    print "flag is ", CheckFlagSize
    CheckFlagArray = twMakeCheckTexture(CheckFlagSize,CheckFlagSize)
    glutPostRedisplay();

def display():
    twDisplayInit();
    twCamera();

    glPushAttrib(GL_ALL_ATTRIB_BITS);

    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);

    if USFlag:
        # This is slow, especially in Python, because it has to
        # repackage the data and send it down the pipeline each time.
        # Use texture binding to improve this.
        twUSFlag();
    else:
        glTexImage2D(GL_TEXTURE_2D, 0, 3, CheckFlagSize, CheckFlagSize, 0,
                     GL_LUMINANCE, GL_UNSIGNED_BYTE, CheckFlagArray);

    glEnable(GL_TEXTURE_2D);

    ## There seems to be a roundoff error of some sort in our graphics
    ## card, because the following code ends up with a little bit (1
    ## pixel) of the left edge of the texture on the right edge.  If you
    ## say one=1, you get this effect, but if you change it to 0.99, you
    ## don't get it.
    one = 1;
    glBegin(GL_QUADS);
    glTexCoord2f(0,one);   glVertex3f( 0,0,0); 
    glTexCoord2f(one,one); glVertex3f(10,0,0); 
    glTexCoord2f(one,0);   glVertex3f(10,5,0); 
    glTexCoord2f(0,0);     glVertex3f( 0,5,0); 
    glEnd();

    glPopAttrib();
    glFlush();
    glutSwapBuffers();

### ================================================================

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
#    CheckFlagArray = twMakeCheckTexture(CheckFlagSize,CheckFlagSize)
    twBoundingBox(0,10,0,5,-1,1);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    twKeyCallback('u',toggleFlag,"toggle which flag to show");
    twKeyCallback('+',changeChecks,"double the number of checks");
    twKeyCallback('-',changeChecks,"halve the number of checks");
    glutMainLoop()

if __name__ == '__main__':
  main()
