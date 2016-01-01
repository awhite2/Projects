""" A demo of texture-mapping onto a cylinder, aligning the image two
   different ways.  There is lighting in this demo, so we need normals
   on the cylinder.  The texture is modulated on, so the color of the
   cylinder is important.

Scott D. Anderson,
original, Fall 2002 
Adapted and simplified for TW, Fall 2003
Fall 2009, Ported to Python, and modified to use lighting 
"""

import sys
import math                     # for sin and cos

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''

### ================================================================
### Modeling a cylinder.  Maybe move this into TW someday?

def cylinder(radius, height, around, steps):
    """Draws a texture-mapped cylinder.

This cylinder has texture coordinates on the vertices.  If 'around' is
true, the cylinder has 's' going around the circumference (mapping
s:0-1 as angle:0-2pi) and 't' going along the axis.  If 'around' is
false, 's' and 't' are switched.  The cylinder's axis is aligned with
the z axis. Use transformations if that's not what you want. """

    glBegin(GL_QUAD_STRIP);
    for i in range(steps+1):
        p = i/float(steps)      # the parameter, either s or t
        theta = p*2*M_PI+M_PI/4;
        x = radius*math.cos(theta);
        y = radius*math.sin(theta);
        if around:
            glTexCoord2f(p,0);
        else:
            glTexCoord2f(0,p);
        glNormal3f(x,y,0)       # normal sticks out as for a circle
        glVertex3f(x,y,0);
        if Long:
            glTexCoord2f(p,1);
        else:
            glTexCoord2f(1,p);
        glVertex3f(x,y,height);
    glEnd();

### ====================================================================

CylinderRadius = 1
CylinderHeight = 6
Long = True                     # whether the parameter is parallel to the axis
Sides = 4                       # the number of sides to the cylinder 

Texturing=True

def display():
    twDisplayInit();
    twCamera();
    glPushAttrib(GL_ALL_ATTRIB_BITS);
    glEnable(GL_LIGHTING)

    twGrayLight(GL_LIGHT0, (1,0,0,0), 0.1, 0, 10, True)
    twColor( (0.8, 0.8, 0.8), 0.9, 5)
    if Texturing:
        glEnable(GL_TEXTURE_2D)
    else:
        glDisable(GL_TEXTURE_2D)
    cylinder(CylinderRadius,CylinderHeight,Long,Sides);

    glPopAttrib();
    glutSwapBuffers();
    glFlush();

def keys(key, x, y):
    global Sides, Long, Texturing
    if key == '.':
        Sides += 1
    elif key == ',':
        Sides = Sides - 1 if Sides > 3 else 3
    elif key == 'l':
        Long = not Long
    elif key == 't':
        Texturing = not Texturing
    glutPostRedisplay();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-CylinderRadius,CylinderRadius,
                  -CylinderRadius,CylinderRadius,
                  0,CylinderHeight);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    twKeyCallback('.',keys,"Increase number of Sides");
    twKeyCallback(',',keys,"Decrease number of Sides");
    twKeyCallback('l',keys,"toggle the orientation of the texture");
    twKeyCallback('t',keys,"toggle texturing");
    textureNumber = glGenTextures(1)

    if len(sys.argv) < 2:
        twLoadTexture(textureNumber,twPathname("USflag.ppm",False))
    else:
        twLoadTexture(textureNumber,twPathname(sys.argv[1],True))
    glutMainLoop()

if __name__ == '__main__':
    main()

