''' Simple demo of computing textures as arrays of values and
   texture-mapping them onto a 2D quad.  There are three textures: the
   classic checkerboard (which is simple but boring because it is
   invariant almost no matter what you do to it), some shades of gray, and
   the US flag.  

   Scott D. Anderson
   Fall 2000 original
   Fall 2003 adapted to use TW
Ported to Python Fall 2009
'''

import sys

from TW import *

## ================================================================

## which flag to show, 0 = checks, 1 = grays, 2 = US
Flag = 0 

# Start with smallest non-trivial flag: 2x2
LogFlagSize = 1
FlagSize = 1 << LogFlagSize
FlagArray = None

def toggleFlag(key, x, y):
    global Flag
    Flag = (Flag+1)%3
    loadFlag()
    glutPostRedisplay();

def loadFlag():
    global LogFlagSize, FlagSize, FlagArray
    if Flag == 0:
        FlagSize = 1 << LogFlagSize
        FlagArray = twMakeCheckTexture(FlagSize, FlagSize)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, FlagSize, FlagSize, 0,
                     GL_LUMINANCE, GL_UNSIGNED_BYTE, FlagArray);
    if Flag == 1:
        FlagSize = 1 << LogFlagSize
        FlagArray = twMakeGrays(FlagSize,FlagSize)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, FlagSize, FlagSize, 0,
                     GL_LUMINANCE, GL_UNSIGNED_BYTE, FlagArray);
    if Flag == 2:
        # This is slow, especially in Python, because it has to
        # repackage the data and send it down the pipeline each time.
        # Use texture binding to improve this.
        twUSFlag();
    
def toggleFlag(key, x, y):
    global Flag
    Flag = (Flag+1)%3
    loadFlag()
    glutPostRedisplay();

def hexbytes(x):
    '''returns a 2 digit uppercase hex number (a string) given a number'''
    return "{0:02X}".format(x)
        
def printflag(flag,width,height):
    '''print a grayscale flag'''
    print flag
    if width == 2:
        # special case for width of 2
        for row in flag:
            subrow = row[0:2]
            print "".join( [ hexbytes(b) for b in subrow ] )
    else:
        for row in flag:
            print "".join( [ hexbytes(b) for b in row ] )

def changeChecks(key, x, y):
    global LogFlagSize, FlagSize, FlagArray
    if key == '.':
        LogFlagSize = min(15,LogFlagSize+1) # double it
    elif key == ',':
        # note that we have to deal with byte-alignment if the texture has
        # a width of 2, so just keep that in mind when looking at the
        # printout
        LogFlagSize = max(1,LogFlagSize-1) # halve it
    loadFlag()
    print "log flag size is", LogFlagSize, "and size is",FlagSize
    printflag(FlagArray,FlagSize,FlagSize)
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
    twBoundingBox(0,10,0,5,-1,1);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    loadFlag()
    twKeyCallback('u',toggleFlag,"cycle through flag to show: checkerboard, grays, and US flag");
    twKeyCallback('.',changeChecks,"double the number of checks");
    twKeyCallback(',',changeChecks,"halve the number of checks");
    glutMainLoop()

if __name__ == '__main__':
    main()
