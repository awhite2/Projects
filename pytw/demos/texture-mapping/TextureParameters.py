""" Demonstration of simple texture mapping.  In this case, we create a
simple checkerboard texture, and use it in several different ways in
rendering a colored cube.

Based on Edward Angel's original cube.c program.

Written by Scott D. Anderson
Fall 2000
Finally ported to Python in Spring 2012
"""

# This program doesn't actually use TW, but tw.h includes the OpenGL functions

import sys
from TW import *

#  Both textures and colors are assigned to the vertices 

vertices = [
    (-1,-1,-1),           # left bottom back
    (1,-1,-1),            # right bottom back
    (1,1,-1),             # right top back
    (-1,1,-1),            # left top back
    (-1,-1,1),            # left bottom front
    (1,-1,1),             # right bottom front
    (1,1,1),              # right top front
    (-1,1,1)]             # left top front

colors = [
    (0,0,0),                    # black
    (1,0,0),                    # red
    (1,1,0),                    # yellow
    (0,1,0),                    # green
    (0,0,1),                    # blue
    (1,0,1),                    # magenta
    (1,1,1),                    # white
    (0,1,1)]                    # cyan

### ================================================================
# Texture stuff. The arrays are used in the texture mapping, and are
# initialized when the program begins, by a call to init_textures. 

TEXTURE_SIZE = 64

# a black and white 8x8 checkerboard we do 8 black then 8 white in a row,
# doing fancy tricks with bitwise operators.  The trick is that i&8 is
# true iff the 8-valued bit is true and that bit will be false for 8 in a
# row, then true for 8 in a row, and so on.  The ^ operator is bitwise
# XOR, which gives us our checkerboard: on even rows, the even columns
# will be false, while the odd columns will be true, and vice versa on the
# odd rows.

checkerboard = [ 255 if (i&8)^(j&8) == 0 else 0
                 for i in range(TEXTURE_SIZE)
                 for j in range(TEXTURE_SIZE) ]

# will be a yellow and dark green checkerboard
checks_rgb = [ (0,128,0,255) if (i&8)^(j&8) else (255,255,0,255)
                         for i in range(TEXTURE_SIZE)
                         for j in range(TEXTURE_SIZE) ]

checks_rgb_flat = [ val
                    for color in checks_rgb
                    for val in color ]

### Polgons as faces of a cube.  We set the color, normal and texture for
### each vertex. 

def polygon(a, b, c, d):
    '''draw a polygon via global lists of vertices and colors, where a, b,
    c, and d are indices into those global lists'''
    glBegin(GL_POLYGON);
    glColor3fv(colors[a]);
    glTexCoord2f(0,0);
    glVertex3fv(vertices[a]);
    glColor3fv(colors[b]);
    glTexCoord2f(0,1);
    glVertex3fv(vertices[b]);
    glColor3fv(colors[c]);
    glTexCoord2f(1,1);
    glVertex3fv(vertices[c]);
    glColor3fv(colors[d]);
    glTexCoord2f(1,0);
    glVertex3fv(vertices[d]);
    glEnd();

def colorcube():
    # map vertices to faces
    polygon(0,3,2,1);
    polygon(2,3,7,6);
    polygon(0,4,7,3);
    polygon(1,2,6,5);
    polygon(4,5,6,7);
    polygon(0,1,5,4);

def label(string):
    glPushAttrib(GL_ALL_ATTRIB_BITS);
    glDisable(GL_TEXTURE_2D);
    glColor3f(1,0,0);
    glRasterPos3f(-1.5,-1.5,0);
    for s in string:
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(s));
    glPopAttrib();

# Globals used in callbacks

theta = [0,0,0]                 # rotation angles 
axis = 2                        # which dimension to rotate around

def display():
    # display callback, clear frame buffer and z buffer,
    # rotate cube and draw, swap buffers 

    glPushAttrib(GL_ALL_ATTRIB_BITS);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();

    glPushMatrix();
    glTranslatef(-1,-1,0);        # lower left cube
    glScalef(0.5,0.5,0.5);
    glRotatef(theta[0], 1, 0, 0);
    glRotatef(theta[1], 0, 1, 0);
    glRotatef(theta[2], 0, 0, 1);
    colorcube();
    label("original cube");
    glPopMatrix();

    # From now on, we'll use textures 

    glEnable(GL_TEXTURE_2D);

    # upper left cube: a luminance decal of a checkerboard on every face
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);

    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D,
                 0,                 # base level, no mipmaps
                 GL_RGB,            # color components in texture 
                 TEXTURE_SIZE,      # texture width 
                 TEXTURE_SIZE,      # texture height
                 0,                 # width of border: either 0 or 1 
                 GL_LUMINANCE,      # format of texture data 
                 GL_UNSIGNED_BYTE,  # data type of texture data 
                 checkerboard       # pointer to array of texture data 
                 );

    glPushMatrix();
    glTranslatef(-1,+1,0);
    glScalef(0.5,0.5,0.5);
    glRotatef(theta[0], 1, 0, 0);
    glRotatef(theta[1], 0, 1, 0);
    glRotatef(theta[2], 0, 0, 1);
    colorcube();
    label("luminance decal");
    glPopMatrix();

    # lower right cube: an rgb decal of a checkerboard on every face

    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);

    glTexImage2D(GL_TEXTURE_2D, 0, 3, TEXTURE_SIZE, TEXTURE_SIZE, 0,
                 GL_RGBA,         # CHANGE!! format of texture data 
                 GL_UNSIGNED_BYTE,  # data type of texture data 
                 checks_rgb         # pointer to array of texture data
                 );

    glPushMatrix();
    glTranslatef(+1,-1,0);
    glScalef(0.5,0.5,0.5);
    glRotatef(theta[0], 1, 0, 0);
    glRotatef(theta[1], 0, 1, 0);
    glRotatef(theta[2], 0, 0, 1);
    colorcube();
    label("RGB decal");
    glPopMatrix();


    # upper right cube: a checkerboard modulates the luminance on every face

    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, TEXTURE_SIZE, TEXTURE_SIZE, 0,
                 GL_LUMINANCE,         # CHANGE!! format of texture data
                 GL_UNSIGNED_BYTE,     # data type of texture data 
                 checkerboard          # pointer to array of texture data 
                 );

    glPushMatrix();
    glTranslatef(+1,+1,0);
    glScalef(0.5,0.5,0.5);
    glRotatef(theta[0], 1, 0, 0);
    glRotatef(theta[1], 0, 1, 0);
    glRotatef(theta[2], 0, 0, 1);
    colorcube();
    label("luminance modulates RBG");
    glPopMatrix();

    glPopAttrib();
    glFlush();
    glutSwapBuffers();


# the number of degrees to rotate the system at each click. 

delta = 2.0;

def mouse(btn, state, x, y):
    # mouse callback, selects an axis about which to rotate 
    global axis, theta

    if btn==GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        axis = 0
    if btn==GLUT_MIDDLE_BUTTON and state == GLUT_DOWN:
        axis = 1
    if btn==GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        axis = 2
    theta[axis] += delta;
    if theta[axis] > 360.0 :
        theta[axis] -= 360.0;
    glutPostRedisplay();

def key(k, xx, yy):
    global delta
    if k == 'q':
        exit(0)
    elif k == '+':
        delta = +2.0
    elif k == '-':
        delta = -2.0
    elif k == '!':
        delta = -delta

def myReshape(w, h):
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    if w <= h:
        ar = float(h) / float(w)  # aspect ratio
        glOrtho(-2, 2, -2 * ar, 2 * ar, -10, 10);
    else:
        ar = float(w) / float(h)
        glOrtho(-2 * ar, 2 * ar, -2, 2, -10, 10);
    glMatrixMode(GL_MODELVIEW);

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutReshapeFunc(myReshape)
    glutDisplayFunc(display)
    glutMouseFunc(mouse)
    glutKeyboardFunc(key)
    glEnable(GL_DEPTH_TEST);
    glutMainLoop()
    return 0

if __name__ == '__main__':
    main()

