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
import array

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''

## ================================================================

## which flag to show, 0 = checks, 1 = grays, 2 = US
Flag = 0 

LogFlagSize = 3

def loadFlag():

    if Flag == 0:
        FlagSize = 1 << LogFlagSize
        FlagArray = makechecks(LogFlagSize,LogFlagSize)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, FlagSize, FlagSize, 0,
                     GL_LUMINANCE, GL_UNSIGNED_BYTE, FlagArray);
        
    elif Flag == 1:
        FlagSize = 1 << LogFlagSize
        FlagArray = makegrays(LogFlagSize,LogFlagSize)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, FlagSize, FlagSize, 0,
                     GL_LUMINANCE, GL_UNSIGNED_BYTE, FlagArray);
    elif Flag == 2:
        # This is slow, especially in Python, because it has to
        # repackage the data and send it down the pipeline each time.
        # Use texture binding to improve this.
        twUSFlag();

def toggleFlag(key, x, y):
    global Flag
    Flag = (Flag+1)%3
    loadFlag()
    glutPostRedisplay();

def makechecks(logwidth,logheight):
    '''Make a checkerboard texture where the logs of two dimensions are given'''
    width = 1 << logwidth                      # width is a power of 2
    height = 1 << logheight                    # height is also
    row_odd = width
    col_odd = 1
    ## this is horrendously tricky coding.  The idea is to decode the
    ## element number (i) into the row and column and then grabbing
    ## just the rightmost bit.  If those rightmost bits are the same,
    ## use 255 (white), otherwise 0 (black).  The rightmost bit is
    ## true if the number is odd, so it changes with each step, and
    ## that gives us a checkerboard.
    bytes = [ 255 if ((i&row_odd)>>logwidth == i&col_odd) else 0
              for i in range(0,width*height) ]
    ## Got this coding idea from http://www.python.org/doc/essays/list2str.html
    return array.array('B', bytes).tostring()

def makegrays(logwidth,logheight):
    '''Make a steadily brightening texture where the logs of two dimensions are given'''
    width = 1 << logwidth                      # width is a power of 2
    height = 1 << logheight                    # height is also
    length = width*height
    ## linearly interpolate from black to white
    bytes = [ int(255*(i/float(length-1))) 
              for i in range(0,length) ]
    ## Got this coding idea from http://www.python.org/doc/essays/list2str.html
    return array.array('B', bytes).tostring()

def printchecks(checks):
    def byteletter(x):
        return "B" if x == '\xff' else "W"
    print map(byteletter,checks)

def changeChecks(key, x, y):
    global LogFlagSize
    if key == '.':
        LogFlagSize = min(15,LogFlagSize+1) # double it
    elif key == ',':
        LogFlagSize = max(2,LogFlagSize-1) # halve it
    print "log flag size is", LogFlagSize, "and size is",1 << LogFlagSize
    loadFlag()
    glutPostRedisplay();

def display():
    twDisplayInit();
    twCamera();

    glPushAttrib(GL_ALL_ATTRIB_BITS);
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);

    glEnable(GL_TEXTURE_2D);

    ## There seems to be a roundoff error of some sort in our graphics
    ## card, because the following code ends up with a little bit (1
    ## pixel) of the left edge of the texture on the right edge.  If you
    ## say one=1, you get this effect, but if you change it to 0.99, you
    ## don't get it.
    one = 1;
    glBegin(GL_QUADS);
    glTexCoord2f(0,0);     glVertex3f( 0,5,0); # upper left
    glTexCoord2f(0,one);   glVertex3f( 0,0,0); # lower left
    glTexCoord2f(one,one); glVertex3f(10,0,0); # lower right
    glTexCoord2f(one,0);   glVertex3f(10,5,0); # upper right
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
    loadFlag()
    twKeyCallback('u',toggleFlag,"toggle which flag to show");
    twKeyCallback('.',changeChecks,"double the number of checks");
    twKeyCallback(',',changeChecks,"halve the number of checks");
    glutMainLoop()

if __name__ == '__main__':
  main()
