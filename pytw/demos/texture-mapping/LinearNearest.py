"""
 * 2D texturing demo using squares.  Based on an original demo by Michael
 * Sweet.
 *
 * Written by Scott D. Anderson, Fall 2001 
"""

from TW import *

win_width  = 500                # Width of window 
win_height = 500                # Height of window

tex_width = None                # Width of texture 
tex_height = None               # Height of texture 

interpolation_mode = GL_NEAREST        # GL_NEAREST or GL_LINEAR

def checkError():
    err = glGetError();
    if err == GL_NO_ERROR:
        return
    print "error = 0x%4x" % (err)

def init_checkerboard(pixels_per_square):
    '''Returns an array of pixels, a red and green checkerboard, with the given number of pixels per square.'''
    pps = pixels_per_square
    return [ (255,0,0,255) if (i&pps)^(j&pps) else (0,255,0,255)
             for i in range(8 * pps)
             for j in range(8 * pps) ]

textures = [ range(8) ]

def square(pps):
    texels = init_checkerboard(pps)
    glTexImage2D(GL_TEXTURE_2D, # target, always this value 
                 0,             # level of detail; always zero 
                 3,      # number of color components.  This is RGB color 
                 8*pps,  # number of columns.  Must be a power of 2 
                 8*pps,  # number of rows.  Also a power of 2 
                 0,      # border width:  zero or one 
                 GL_RGBA,          # format of pixel data 
                 GL_UNSIGNED_BYTE, # datatype of pixel data 
                 texels            # pointer to texture (pixel) data 
                 );
    checkError();
    glScalef(0.9,0.9,1);
    glBegin(GL_POLYGON); 
    glTexCoord2f(0,0);        glVertex3f(-1,-1,0);
    glTexCoord2f(0,1);        glVertex3f(-1,+1,0);
    glTexCoord2f(1,1);        glVertex3f(+1,+1,0);
    glTexCoord2f(1,0);        glVertex3f(+1,-1,0);
    glEnd();

### Display a normal texture-mapped square in the center and variations
### around it.

def display():
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    twCamera();

    # added this, to make the squares stand out.  SDA 
    glClearColor(0.5,0.5,0.5,1);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    # Textures are decals 
    glEnable(GL_TEXTURE_2D);        # use textures from now on 
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL);
    
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, interpolation_mode);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, interpolation_mode);

    glPushMatrix();
    glTranslatef(-1,-1,0);
    square(1);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(-1,+1,0);
    square(2);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(+1,-1,0);
    square(4);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(+1,+1,0);
    square(4);
    glPopMatrix();

    glFlush();
    glutSwapBuffers();

def resize(width, height):
    global win_width, win_height
    half=2;
    # compute aspect ratio 
    ar = GLfloat(width) / GLfloat( height )
    # Save the new width and height 
    win_width  = width;
    win_height = height;

    # Reset the viewport... 
    glViewport(0, 0, width, height);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    if width <= height:
        gluOrtho2D(-half * ar, half * ar, -half, half);
    else:
        gluOrtho2D(-half, half, -half * ar, half * ar);

def usage():
    print "Usage: %s L/N" % (sys.argv[0])
    print "Uses either linear or nearest interpolation"

def main():
    global interpolation_mode
    if len(sys.argv) < 2:
        usage()
        sys.exit()
    if sys.argv[1] == 'L':
        interpolation_mode = GL_LINEAR
    elif sys.argv[1] == 'N':
        interpolation_mode = GL_NEAREST
    else:
        usage()
        sys.exit()
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutReshapeFunc(resize)
    glutDisplayFunc(display)
    glEnable(GL_DEPTH_TEST);
    twBoundingBox(-1,+1,-1,+1,-1,+1);
    twMainInit();
    glutMainLoop()
    return 0

if __name__ == '__main__':
    main()



