"""/*
 * 1D textured rainbow demo from Chapter 8.
 *
 * Written by Michael Sweet
 */

Added the ability to turn the rainbow on/off using the 'R' keyboard callback
Scott D. Anderson
Fall 2000 original
Fall 2003 adapted to use TW.
Fall 2009 ported to Python
"""

import sys
import math                            # for sin and cos

try:
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
        '''
### ================================================================

Rainbow = True                	# whether to show the rainbow.

def key(key, x, y):
    global Rainbow
    Rainbow = not Rainbow;
    glutPostRedisplay();

def rainbowInit():
    roygbiv = (
        ( 0x3f, 0x00, 0x3f ), # Dark Violet (for 8 colors...)
        ( 0x7f, 0x00, 0x7f ), # Violet 
        ( 0xbf, 0x00, 0xbf ), # Indigo 
        ( 0x00, 0x00, 0xff ), # Blue 
        ( 0x00, 0xff, 0x00 ), # Green 
        ( 0xff, 0xff, 0x00 ), # Yellow
        ( 0xff, 0x7f, 0x00 ), # Orange
        ( 0xff, 0x00, 0x00 )  # Red 
        )
    # Load the texture data
    glTexParameteri(GL_TEXTURE_1D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_1D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexImage1D(GL_TEXTURE_1D, 0, 3, 8, 0, GL_RGB, GL_UNSIGNED_BYTE, roygbiv);
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL);

def display():
    twDisplayInit(0.5,0.5,1.0); # clear to sky blue
    twCamera();

    # this is the green ground, drawn as an enormous circle, which is
    # what gives the horizon its slightly curved appearance. 
    glDisable(GL_TEXTURE_1D);   # have to make sure textures are off
    glColor3f(0.0, 0.8, 0.0);
    glPushMatrix();
    glRotatef(-90,1,0,0);       # now z points up
    twDisk(100,30);
    glPopMatrix();

    rainbowInit();
    # Then a rainbow...  
    inner_radius = 50.0
    outer_radius = 55.0

    # Draw in yellow, but this is irrelevant if 'decal'
    # texture-mapping is enabled.
    twColorName(TW_YELLOW);
                           
    if Rainbow:
        glEnable(GL_TEXTURE_1D);
    glBegin(GL_QUAD_STRIP);
    # go from 0 to PI in 180 steps
    for i in range(181):
        theta = twDegreesToRadians(i)
        cos = math.cos(theta)
        sin = math.sin(theta)
        z = -50.0
        if Rainbow:
            glTexCoord1f(0.0)   # begin at t=0
        glVertex3f(cos*inner_radius,sin*inner_radius,z)
        if Rainbow:
            glTexCoord1f(1.0)   # end at t=0
        glVertex3f(cos*outer_radius,sin*outer_radius,z)
    glEnd();
    
    glFinish();
    glutSwapBuffers();

### ================================================================

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-100,100,0,50,-100,100);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    twKeyCallback('R',key,"Toggle whether to show the rainbow");
    glutMainLoop()

if __name__ == '__main__':
  main()
