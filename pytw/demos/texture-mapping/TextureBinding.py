""" Demo of using binding to allow the efficient use of multiple textures.
   6 textures are loaded and bound to the sides of a cube.

   Scott D. Anderson
   Fall 2002 original
   Fall 2003 adapted to use TW

Fall 2009, ported to Python
"""

import sys
import math                            # for sin and cos

from TW import *

### ================================================================
### Cube
        
textureIDs = None
        
verbose = True

def face(vertices, a, b, c , d):
    """draw one face of a cube, given vertex indices

We set the color and texture for each vertex. Vertex a is the upper left
(that is, it corresponds to the upper left of the texture, and then we go
counterclockwise, so vertex b is the lower left of the texture.
"""

    glBegin(GL_QUADS);
    glTexCoord2f(0,0);
    glVertex3fv(vertices[a]);
    glTexCoord2f(0,1);
    glVertex3fv(vertices[b]);
    glTexCoord2f(1,1);
    glVertex3fv(vertices[c]);
    glTexCoord2f(1,0);
    glVertex3fv(vertices[d]);
    glEnd();


def texturecube():
    vertices = ( (-1,-1,-1), (+1,-1,-1), (+1,+1,-1), (-1,+1,-1),
                 (-1,-1,+1), (+1,-1,+1), (+1,+1,+1), (-1,+1,+1))
    glBindTexture(GL_TEXTURE_2D, int(textureIDs[0]));
    glNormal3f(0,0,-1)
    face(vertices,0,3,2,1);                # back: z=-1
    glBindTexture(GL_TEXTURE_2D, int(textureIDs[1]));
    glNormal3f(0,1,0)
    face(vertices,6,2,3,7);                # top: y=+1
    glBindTexture(GL_TEXTURE_2D, int(textureIDs[2]));
    glNormal3f(-1,0,0)
    face(vertices,0,4,7,3);                # left: x=-1
    glBindTexture(GL_TEXTURE_2D, int(textureIDs[3]));
    glNormal3f(1,0,0)
    face(vertices,6,5,1,2);                # right: x=+1
    glBindTexture(GL_TEXTURE_2D, int(textureIDs[4]));
    glNormal3f(0,0,1)
    face(vertices,7,4,5,6);                # front: z=+1
    glBindTexture(GL_TEXTURE_2D, int(textureIDs[5]));
    glNormal3f(0,-1,0)
    face(vertices,0,1,5,4);                # bottom: y=-1

def init():
    global textureIDs
    textureIDs = glGenTextures(6); # get all the texture ids 
    
    if verbose:
        for i in range(6):
            print "%d: %d" % (i, textureIDs[i])

    twLoadTexture(textureIDs[0],twPathname("mandrill.ppm"))
    twLoadTexture(textureIDs[1],twPathname("cokecan.ppm"))
    twLoadTexture(textureIDs[2],twPathname("eac512x256.ppm"))
    twLoadTexture(textureIDs[3],twPathname("peterms.ppm"))
    twLoadTexture(textureIDs[4],twPathname("homer2.ppm"))
    twLoadTexture(textureIDs[5],twPathname("USflag.ppm"))

Texturing = False

def display():
    twDisplayInit();
    twCamera();
    glPushAttrib(GL_ALL_ATTRIB_BITS);

    glEnable(GL_LIGHTING)
    twGrayLight( GL_LIGHT0, (1,2,3,0), 0.5, 0.8, 1) # bright light from the upper right

    if Texturing:
        glEnable(GL_TEXTURE_2D); # From now on, we'll use textures
    else:
        glDisable(GL_TEXTURE_2D);   # or not
    twColor( (0.8, 0.8, 0.8), 0, 0) # on light gray matte cube material
    texturecube();

    glPopAttrib();
    glFlush();
    glutSwapBuffers();

def toggleTexturing(key,x,y):
    global Texturing
    Texturing = not Texturing
    glutPostRedisplay()


### ================================================================

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-2,2,-2,2,-1,1);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    init();                     # load the textures from the files
    twKeyCallback('t',toggleTexturing,'Toggle Texturing')
    glutMainLoop()

if __name__ == '__main__':
    main()
