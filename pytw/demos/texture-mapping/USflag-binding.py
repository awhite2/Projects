"""Simple demo of computing textures as arrays of values and
   texture-mapping them onto a 2D quad.  This shows that texture
   parameters (modes) can be associated with a texture id, because the
   checkerboard flag uses repeat and linear, while the flag uses clamp and
   nearest.

   Scott D. Anderson
   Fall 2000 original
   Fall 2003 adapted to use TW

Fall 2009 ported to TW
"""

import sys

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

def toggleFlag(key, x, y):
    global Flag
    Flag = (Flag+1)%3
    glutPostRedisplay();


textureIDs = None

def loadFlags():
    global textureIDs
    textureIDs = glGenTextures(3);

    # Flag == 0
    glBindTexture(GL_TEXTURE_2D,int(textureIDs[0]))
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    FlagSize = 1 << LogFlagSize
    FlagArray = twMakeGrays(FlagSize, FlagSize)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, FlagSize, FlagSize, 0,
                 GL_LUMINANCE, GL_UNSIGNED_BYTE, FlagArray);
        
    # Flag == 1
    glBindTexture(GL_TEXTURE_2D,int(textureIDs[1]))
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    data = twMakeCheckTexture(8,8)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, 8, 8, 0,
                 GL_LUMINANCE, GL_UNSIGNED_BYTE, data);

    # Flag == 2:
    glBindTexture(GL_TEXTURE_2D,int(textureIDs[2]))
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    twUSFlag();


## ================================================================ 

def display():
    twDisplayInit();
    twCamera();

    glPushAttrib(GL_ALL_ATTRIB_BITS);

    ## this is the more efficient way, using texture binding.
    glBindTexture(GL_TEXTURE_2D,int(textureIDs[Flag]))

    glEnable(GL_TEXTURE_2D);
    glColor3f(0.8,0.8,0.8)      # light gray
    glBegin(GL_QUADS);
    glTexCoord2f(0,2); glVertex3f( 0,0,0); 
    glTexCoord2f(2,2); glVertex3f(10,0,0); 
    glTexCoord2f(2,0); glVertex3f(10,5,0); 
    glTexCoord2f(0,0); glVertex3f( 0,5,0); 
    glEnd();

    glPopAttrib();
    glFlush();
    glutSwapBuffers();

## ================================================================

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(0,10,0,5,-1,1);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    twKeyCallback('u',toggleFlag,"switch which flag to show");
    loadFlags()
    glutMainLoop()

if __name__ == '__main__':
  main()
