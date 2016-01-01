''' Simplest demo of reading in an image and texture-mapping it onto
   something; in this case, a quad.  This does *not* use texture
   binding, and, of course, it should.

   Scott D. Anderson
   Fall 2005
Ported to Python Fall 2009
'''

import sys

from TW import *

### ================================================================

def display():
    twDisplayInit();
    twCamera();

    glEnable(GL_TEXTURE_2D);

    ## this is a *square*, so the aspect ratio may not match the
    ## texture's aspect-ratio

    glBegin(GL_QUADS);
    glTexCoord2f(0,0); glVertex3f( -1, 1,0); ## upper left is 0,0 in texture space
    glTexCoord2f(0,1); glVertex3f( -1,-1,0); ## lower left is 0,1 in texture space
    glTexCoord2f(1,1); glVertex3f(  1,-1,0); ## lower right is 1,1
    glTexCoord2f(1,0); glVertex3f(  1, 1,0); ## upper right is 1,0
    glEnd();

    glFlush();
    glutSwapBuffers();

### ================================================================

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-1,+1,-1,+1,0,0.01);
    twInitWindowSize(512,512)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()

    if len(sys.argv) < 2:
        twPPM_Tex2D(twPathname("USflag.ppm",False))
    else:
        twPPM_Tex2D(twPathname(sys.argv[1],True))
    glutMainLoop()

if __name__ == '__main__':
    main()
