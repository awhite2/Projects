""" Demos textures receding into the distance and stretched in foreground.
   Use the 'r' key to reveal the underlying quads.

Scott D. Anderson
scott.anderson@acm.org
Fall 2003
Fall 2009, ported to Python
"""

from TW import *

## ================================================================
## code for the grass

## This unit square is on the XZ (y=0) plane, in the ++ quadrant. 
## This function is like twDrawUnitSquare, but allows for showing
## the points instead of the triangles.

RevealSquares = False

def drawUnitSquare(width, height ):
    dw = 1.0/width
    dh = 1.0/height
    glNormal3f(0,1,0);
    for i in range(width):
        glBegin( GL_POINTS if RevealSquares else GL_TRIANGLE_STRIP )
        for j in range(height+1):
            if j%2==1:
                glTexCoord2f(1,0)
            else:
                glTexCoord2f(0,0);
            glVertex3f(dw*i, 0, dh*j);
            if j%2==1: 
                glTexCoord2f(1,1); 
            else:
                glTexCoord2f(0,1);
            glVertex3f(dw*(i+1), 0, dh*j);
        glEnd();

ShowColorInstead = False        # instead of showing the grass texture

NUM_TEXTURES = 3                # we have this many choices of texture

textureIDs = None               # the array of texture IDs
TextureNumber = 0               # which texture we're showing

def init():
    global textureIDs
    textureIDs = glGenTextures(NUM_TEXTURES);
    print textureIDs
    twLoadTexture(textureIDs[0],twPathname("grass.ppm"))
    twLoadTexture(textureIDs[1],twPathname("brick.ppm"))
    twLoadTexture(textureIDs[2],twPathname("wood-laminate.ppm"))

def draw_grass():
    ## draw texture
    if ShowColorInstead:
        glColor3f(0, .7, 0);
        glDisable(GL_TEXTURE_2D);
    else:
        glBindTexture(GL_TEXTURE_2D, int(textureIDs[TextureNumber]));
        glEnable(GL_TEXTURE_2D);
    glPushMatrix();
    glTranslatef(-100, 0, 0);
    glScalef(200, 1, 100);
    drawUnitSquare(20, 2);    # this supplies texture coordinates
    glPopMatrix();

## ================================================================
## Callbacks

def display():
    twDisplayInit();
    twCamera();
    glPushAttrib(GL_ALL_ATTRIB_BITS);
    
    draw_grass();  

    ## draw sky on the XY plane 
    glDisable(GL_TEXTURE_2D);
    glColor3f(.7, .9, 1);
    glBegin(GL_POLYGON);
    glVertex3f(-200, 0, 0);
    glVertex3f(+200, 0, 0);
    glVertex3f(+200, 200, 0);
    glVertex3f(-200, 200, 0);
    glEnd();

    glPopAttrib();
    glutSwapBuffers();
    glFlush();

def keys(key, x, y):
    global RevealSquares, ShowColorInstead, TextureNumber
    if key == 'r':
        RevealSquares = not RevealSquares
    elif key == 'c': 
        ShowColorInstead = not ShowColorInstead
    elif key in list("012"):
        TextureNumber = ord(key)-ord('0')
        print "switching to texture ", TextureNumber
    glutPostRedisplay();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-50,+50,0,50,0,20);  ## lies, all lies
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    twKeyCallback('r',keys,"toggle reveal quads");
    twKeyCallback('c',keys,"toggle color");
    twKeyCallback('0',keys,"texture 0");
    twKeyCallback('1',keys,"texture 1");
    twKeyCallback('2',keys,"texture 2");
    glPointSize(3);             # big dots when revealing the quads
    init()
    glutMainLoop()

if __name__ == '__main__':
    main()
