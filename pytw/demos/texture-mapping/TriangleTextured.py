"""Demo of texture mapping onto a triangle in a variety of ways,
including Bezier surfaces.

Implemented Fall 2003
Scott D. Anderson
Fall 2009 Ported to Python
"""

import sys
import math                     # for sin and cos

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''

## ================================================================

def display():
    twDisplayInit();
    twCamera();

    glEnable(GL_TEXTURE_2D);

    # the reference version, mapped onto a quad
    glBegin(GL_QUADS);
    glTexCoord2f(0,1);    glVertex2f(0,0);
    glTexCoord2f(0,0);    glVertex2f(0,2);
    glTexCoord2f(1,0);    glVertex2f(1,2);
    glTexCoord2f(1,1);    glVertex2f(1,0);
    glEnd();

    # when we just use the texture coordinates of the top point, this
    # effectively cuts off the rest of the texture, which may be what
    # we want.
    glPushMatrix();
    glTranslatef(1,0,0);
    glBegin(GL_TRIANGLES);
    glTexCoord2f(0,1);    glVertex2f(0,0);
    glTexCoord2f(0.5,0);  glVertex2f(0.5,2);
    glTexCoord2f(1,1);    glVertex2f(1,0);
    glEnd();
    glPopMatrix();

    # Or, we may want the entire texture to be squeezed into the
    # triangle, warping it in order to fit.
    glPushMatrix();
    glTranslatef(2,0,0);
    glBegin(GL_QUADS);
    glTexCoord2f(0,1);    glVertex2f(0,0);
    glTexCoord2f(0,0);    glVertex2f(0.49,2);
    glTexCoord2f(1,0);    glVertex2f(0.51,2);
    glTexCoord2f(1,1);    glVertex2f(1,0);
    glEnd();
    glPopMatrix();

    # We can improve the warped version by creating interior vertices
    # by using Bezier surfaces (a flat, linear surface in this case).
    glPushMatrix();
    glTranslatef(3,0,0);
    vcp = (((0,0,0), (0.5,2,0)), ((1,0,0), (0.5,2,0)))
    tcp = (((0,1),   (0,0)),     ((1,1),   (1,0)))
    
    glMap2f(GL_MAP2_VERTEX_3, 0, 1, 0, 1, vcp);
    glEnable(GL_MAP2_VERTEX_3);
    glMap2f(GL_MAP2_TEXTURE_COORD_2, 0, 1, 0, 1, tcp);
    glEnable(GL_MAP2_TEXTURE_COORD_2);

    steps = 10;
    glMapGrid2f(steps,0,1,steps,0,1);
    glEvalMesh2(GL_LINE,0,steps,0,steps);

    glPopMatrix();

    # warped with interior vertices and fill
    glPushMatrix();
    glTranslatef(4,0,0);
    
    glMap2f(GL_MAP2_VERTEX_3, 0, 1, 0, 1, vcp);
    glEnable(GL_MAP2_VERTEX_3);
    glMap2f(GL_MAP2_TEXTURE_COORD_2, 0, 1, 0, 1, tcp);
    glEnable(GL_MAP2_TEXTURE_COORD_2);

    glMapGrid2f(steps,0,1,steps,0,1);
    glEvalMesh2(GL_FILL,0,steps,0,steps);

    glPopMatrix();

    glFlush();
    glutSwapBuffers();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
#    twBoundingBox(0,5,0,2,0,0);
    twBoundingBox(2,3,0,2,0,0); # a lie, to get closer
    twInitWindowSize(1000,400)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    textureNumber = glGenTextures(1)
    if len(sys.argv) < 2:
        twLoadTexture(textureNumber,twPathname("homer2.ppm",False))
    else:
        twLoadTexture(textureNumber,twPathname(sys.argv[1],True))
    glutMainLoop()

if __name__ == '__main__':
    main()
