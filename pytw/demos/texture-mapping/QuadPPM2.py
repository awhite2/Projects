''' Simplest demo of reading in an image and texture-mapping it onto
   something; in this case, a quad.  This does *not* use texture
   binding, and, of course, it should.

   Scott D. Anderson
   Fall 2005
Ported to Python Fall 2009
'''

import sys

try:
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
        '''

### ================================================================

UL = (0,0)                      # in texture space
UR = (1,0)
LL = (0,1)
LR = (1,1)


def display():
    twDisplayInit();
    twCamera();

    twGrayLight(GL_LIGHT0,(-1,0,1,0),0.2,0.9,1)
    twColor((1,1,1),1,64)       # bright white shiny surface

    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    glEnable(GL_TEXTURE_2D);

    ## this is a *square*, so the aspect ratio may not match the
    ## texture's aspect-ratio

    glBegin(GL_QUADS);
    glTexCoord2fv(UL); glVertex3f( -1, 1,0); ## upper left is 0,0 in texture space
    glTexCoord2fv(LL); glVertex3f( -1,-1,0); ## lower left is 0,1 in texture space
    glTexCoord2fv(LR); glVertex3f(  1,-1,0); ## lower right is 1,1
    glTexCoord2fv(UR); glVertex3f(  1, 1,0); ## upper right is 1,0
    glEnd();

    glFlush();
    glutSwapBuffers();

### ================================================================

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-1,+1,-1,+1,0,0.01);
    twInitWindowSize(500,500)
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
