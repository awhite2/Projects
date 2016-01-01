
'''
Chloe Fan's OpenGL Piano and Bench
Copyright (c) 2006 Chloe Fan

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

Ported to Python by Lalita Choe
'''

import sys

try:
    from TW import *
except:
    print '''
ERRO: Couldn't import TW.
          '''

pianoColor = (0,0,0); # default color

def cfan2Piano() :
    '''Draws a black baby grand piano. Can be placed in auditorium, 
       living room, etc. Values are scaled based on the width of the 
       piano, or affine transformations can be used to resize piano.
       The origin is on the bottom of the base of the piano, right above 
       the legs, where the cover also matches up horizontally, and halfway 
       through the width. This way, the legs are located on the negative 
       y-axis, and the piano will be symmetrical.'''

    wheelColor = (0.84, 0.68, 0.05);

    # width of piano
    pWidth = 12;
    # length of front: keys, stand
    pFront = pWidth/2.0;
    # length of back: strings, curve
    pBack = pWidth/4.0*3;

    '''=============== PIANO FRONT: KEYS AND BASE ================'''

    glPushMatrix(); # keys
    glColor3f(255,255,255); # white
    glTranslatef(0, pWidth/12.0*3/2.0, pFront*5/6.0-0.75);
    glScalef(pWidth, pWidth/48.0, 0.75);
    glutSolidCube(1);
    glPopMatrix();

    twColor(pianoColor,0,0); # set color to piano color

    glPushMatrix(); # below keys
    glTranslatef(0,pWidth/24.0,pFront*5/6.0-0.5);
    glScalef(pWidth, pWidth/12.0, pWidth/12.0);
    glutSolidCube(1);
    glPopMatrix();

    glBegin(GL_POLYGON); # right keys "cover"
    glVertex3f(pWidth/2.0, 0, pFront);
    glVertex3f(pWidth/2.0, 0, pFront*2/3.0);
    glVertex3f(pWidth/2.0, pWidth/6.0, pFront*2/3.0);
    glVertex3f(pWidth/2.0, pWidth/6.0, pFront);
    glEnd();

    glBegin(GL_POLYGON); # left keys "cover"
    glVertex3f(-pWidth/2.0, 0, pFront*2/3.0);
    glVertex3f(-pWidth/2.0, 0, pFront);
    glVertex3f(-pWidth/2.0, pWidth/6.0, pFront);
    glVertex3f(-pWidth/2.0, pWidth/6.0, pFront*2/3.0);
    glEnd();

    glBegin(GL_POLYGON); # book stand
    glVertex3f(-pWidth/4.0, pWidth/4.0, pWidth/6.0);
    glVertex3f(pWidth/4.0, pWidth/4.0, pWidth/6.0);
    glVertex3f(pWidth/4.0, pWidth*5/12.0, pWidth/8.0);
    glVertex3f(-pWidth/4.0, pWidth*5/12.0, pWidth/8.0);
    glEnd();

    glBegin(GL_POLYGON); # book stand back
    glVertex3f(-pWidth/24.0, pWidth/4.0+pWidth/12.0, pWidth/12.0+pWidth/16.0);
    glVertex3f(pWidth/24.0, pWidth/4.0+pWidth/12.0, pWidth/12.0+pWidth/16.0);
    glVertex3f(pWidth/24.0, pWidth/4.0, pWidth/12.0);
    glVertex3f(-pWidth/24.0, pWidth/4.0, pWidth/12.0);
    glEnd();

    glPushMatrix(); # under book stand
    glTranslatef(0, pWidth/8.0, pWidth/3.0/2.0);
    glScalef(pWidth, pWidth/4.0, pWidth/3.0);
    glutSolidCube(1);
    glPopMatrix();

    glBegin(GL_POLYGON); # piano curved base
    glVertex3f(-pWidth/2.0, pWidth/12.0, 0);
    glVertex3f(-pWidth/2.0, pWidth/12.0, -pBack*5/9.0);
    glVertex3f(-pWidth*5/12.0, pWidth/12.0, -pBack/1.2);
    glVertex3f(-pWidth/3.0, pWidth/12.0, -pBack/12.0*11);
    glVertex3f(-pWidth/4.0, pWidth/12.0, -pBack/45.0*44);
    glVertex3f(-pWidth/6.0, pWidth/12.0, -pBack); # top of big curve
    glVertex3f(-pWidth/12.0, pWidth/12.0, -pBack/45.0*44);
    glVertex3f(0, pWidth/12.0, -pBack/12*11);
    glVertex3f(pWidth/12.0, pWidth/12.0, -pBack/1.2);
    glVertex3f(pWidth/6.0, pWidth/12.0, -pBack*5/9.0);
    glVertex3f(pWidth/4.0, pWidth/12.0, -pBack/18.0*7);
    glVertex3f(pWidth/3.0, pWidth/12.0, -pBack/3.0);
    glVertex3f(pWidth*5/12.0, pWidth/12.0, -pBack/3.6);
    glVertex3f(pWidth/2.0, pWidth/12.0, 0);
    glEnd();

    # glColor3f(255,255,255); # white: testing

    glBegin(GL_QUAD_STRIP); # piano base wall
    glVertex3f(-pWidth/2.0, pWidth/12.0, 0);
    glVertex3f(-pWidth/2.0, pWidth/4.0, 0);
    glVertex3f(-pWidth/2.0, pWidth/12.0, -pBack*5/9.0);
    glVertex3f(-pWidth/2.0, pWidth/4.0, -pBack*5/9.0);

    glVertex3f(-pWidth*5/12.0, pWidth/12.0, -pBack/1.2);
    glVertex3f(-pWidth*5/12.0, pWidth/4.0, -pBack/1.2);

    glVertex3f(-pWidth/3.0, pWidth/12.0, -pBack/12.0*11);
    glVertex3f(-pWidth/3.0, pWidth/4.0, -pBack/12.0*11);

    glVertex3f(-pWidth/4.0, pWidth/12.0, -pBack/45.0*44);
    glVertex3f(-pWidth/4.0, pWidth/4.0, -pBack/45.0*44);

    glVertex3f(-pWidth/6.0, pWidth/12.0, -pBack); # top of big curve
    glVertex3f(-pWidth/6.0, pWidth/4.0, -pBack);

    glVertex3f(-pWidth/12.0, pWidth/12.0, -pBack/45.0*44);
    glVertex3f(-pWidth/12.0, pWidth/4.0, -pBack/45.0*44);

    glVertex3f(0, pWidth/12.0, -pBack/12.0*11);
    glVertex3f(0, pWidth/4.0, -pBack/12.0*11);

    glVertex3f(pWidth/12.0, pWidth/12.0, -pBack/1.2);
    glVertex3f(pWidth/12.0, pWidth/4.0, -pBack/1.2);

    glVertex3f(pWidth/6.0, pWidth/12.0, -pBack*5/9.0);
    glVertex3f(pWidth/6.0, pWidth/4.0, -pBack*5/9.0);

    glVertex3f(pWidth/4.0, pWidth/12.0, -pBack/18.0*7);
    glVertex3f(pWidth/4.0, pWidth/4.0, -pBack/18.0*7);

    glVertex3f(pWidth/3.0, pWidth/12.0, -pBack/3.0);
    glVertex3f(pWidth/3.0, pWidth/4.0, -pBack/3.0);

    glVertex3f(pWidth*5/12.0, pWidth/12.0, -pBack/3.6);
    glVertex3f(pWidth*5/12.0, pWidth/4.0, -pBack/3.6);

    glVertex3f(pWidth/2.0, pWidth/12.0, 0);
    glVertex3f(pWidth/2.0, pWidth/4.0, 0);
    glEnd();

    '''======================= PIANO COVER ========================='''

    glPushMatrix();
    glTranslatef(0.5,3.5,0);
    glRotatef(30, 0, 0, 1);
    glBegin(GL_POLYGON); # piano curved cover
    glVertex3f(-pWidth/2.0, pWidth/4.0, 0);
    glVertex3f(-pWidth/2.0, pWidth/4.0, -pBack*5/9.0);
    glVertex3f(-pWidth*5/12.0, pWidth/4.0, -pBack/1.2);
    glVertex3f(-pWidth/3.0, pWidth/4.0, -pBack/12.0*11);
    glVertex3f(-pWidth/4.0, pWidth/4.0, -pBack/45.0*44);
    glVertex3f(-pWidth/6.0, pWidth/4.0, -pBack); # top of big curve
    glVertex3f(-pWidth/12.0, pWidth/4.0, -pBack/45.0*44);
    glVertex3f(0, pWidth/4.0, -pBack/12.0*11);
    glVertex3f(pWidth/12.0, pWidth/4.0, -pBack/1.2);
    glVertex3f(pWidth/6.0, pWidth/4.0, -pBack*5/9.0);
    glVertex3f(pWidth/4.0, pWidth/4.0, -pBack/18.0*7);
    glVertex3f(pWidth/3.0, pWidth/4.0, -pBack/3.0);
    glVertex3f(pWidth*5/12.0, pWidth/4.0, -pBack/3.6);
    glVertex3f(pWidth/2.0, pWidth/4.0, 0);
    glEnd();
    glPopMatrix();

    # glColor3f(255,255,255); # white: testing

    glBegin(GL_POLYGON); # cover prop
    glVertex3f(pWidth/12.0*5, pWidth/4.0, -pWidth/16.0);
    glVertex3f(pWidth/12.0*5, pWidth/4.0, -pWidth/48.0*5);
    glVertex3f(pWidth/4.0, pBack-pWidth/24.0, -pWidth/48.0*5);
    glVertex3f(pWidth/4.0, pBack-pWidth/24.0, -pWidth/16.0);
    glEnd();

    '''==================== PIANO LEGS AND PEDALS ======================'''

    glBegin(GL_POLYGON); # right front slanted left
    glVertex3f(pWidth/2.0-pWidth/12.0, 0, 0);
    glVertex3f(pWidth/2.0-pWidth/12.0, -pWidth/12.0, pWidth/8.0);
    glVertex3f(pWidth/2.0-pWidth/12.0, -pWidth/12.0, pWidth/8.0+pWidth/12.0);
    glVertex3f(pWidth/2.0-pWidth/12.0, 0, pWidth/3.0);
    glEnd();

    glBegin(GL_POLYGON); # right front slanted right
    glVertex3f(pWidth/2.0, 0, 0);
    glVertex3f(pWidth/2.0, -pWidth/12.0, pWidth/8.0);
    glVertex3f(pWidth/2.0, -pWidth/12.0, pWidth/8.0+pWidth/12.0);
    glVertex3f(pWidth/2.0, 0, pWidth/3.0);
    glEnd();

    glBegin(GL_POLYGON); # left front slanted right
    glVertex3f(-pWidth/2.0+pWidth/12.0, 0, 0);
    glVertex3f(-pWidth/2.0+pWidth/12.0, -pWidth/12.0, pWidth/8.0);
    glVertex3f(-pWidth/2.0+pWidth/12.0, -pWidth/12.0, pWidth/8.0+pWidth/12.0);
    glVertex3f(-pWidth/2.0+pWidth/12.0, 0, pWidth/3.0);
    glEnd();

    glBegin(GL_POLYGON); # left front slanted left
    glVertex3f(-pWidth/2.0, 0, 0);
    glVertex3f(-pWidth/2.0, -pWidth/12.0, pWidth/8.0);
    glVertex3f(-pWidth/2.0, -pWidth/12.0, pWidth/8.0+pWidth/12.0);
    glVertex3f(-pWidth/2.0, 0, pWidth/3.0);
    glEnd();

    glBegin(GL_POLYGON); # back slanted front
    glVertex3f(-pFront/2.0, pWidth/12.0, -pBack+pBack/6.0);
    glVertex3f(-pFront/2.0+pWidth/24.0, 0, -pBack+pBack/6.0);
    glVertex3f((-pFront/2.0+pWidth/24.0)+pWidth/12.0, 0, -pBack+pBack/6.0);
    glVertex3f(-pFront/2.0+pWidth/8.0, pWidth/12.0, -pBack+pBack/6.0);
    glEnd();

    glPushMatrix(); # legs
    glTranslatef(pWidth/2.0-pWidth/24.0, -pWidth*5/24.0, pWidth/6.0);
    glScalef(1, 5, 1);
    glutSolidCube(1); # right leg
    glTranslatef(-pWidth+pWidth/12.0, 0, 0);
    glutSolidCube(1); # left leg
    glPopMatrix();

    glPushMatrix();
    glTranslatef(-pFront/3.0, -pWidth/6.0, -pBack+pBack/9.0);
    glScalef(1,6,1);
    glutSolidCube(1); # back leg
    glPopMatrix();

    glPushMatrix(); # wheels
    twColor(wheelColor,0,0); # set color to wheel color
    glTranslatef(-pWidth/12.0*5-pWidth/24.0, -pWidth*5/12.0-0.25, pWidth/6.0);
    glScalef(0.5,0.5,0.5);
    glutSolidSphere(1,20,20); # left wheel
    glTranslatef((pWidth-pWidth/12.0)*2, 0, 0);
    glutSolidSphere(1,20,20); # right wheel
    glTranslatef((-pWidth*5/8.0)*2, 0, (-pBack-pBack/9.0)*2);
    glutSolidSphere(1,20,20);
    glPopMatrix();

    ''' pedals: all pedals are supposed to stick out behind past the "box" 
        since they are attached to the bottom of the piano base to control 
        string frames'''
    glPushMatrix();
    twColor(pianoColor,0,0); # back to piano color
    glTranslatef(-pWidth/16.0, -pWidth/6.0, pWidth/6.0);
    glScalef(pWidth/24.0, pWidth/3.0, pWidth/24.0);
    glutSolidCube(1); # left supporter
    glTranslatef(pWidth/4.0, 0, 0);
    glutSolidCube(1); # right supporter
    glPopMatrix();

    glPushMatrix();
    glTranslatef(0, -pWidth/3.0, pWidth/6.0);
    glScalef(pWidth/4.0, pWidth/24.0, 1);
    glutSolidCube(1); # pedal box
    twColor(wheelColor,0,0); # set color to wheel color
    glTranslatef(0, 0, 0.25);
    glScalef(pWidth/120, pWidth/48.0, pWidth/12.0);
    glutSolidSphere(1, 20, 20); # middle pedal
    glPushMatrix();
    glTranslatef(-pWidth*5/24.0, 0, 0);
    glutSolidSphere(1,20,20); # left pedal
    glPopMatrix();
    glTranslatef(pWidth*5/24.0, 0, 0);
    glutSolidSphere(1,20,20); # right pedal
    glPopMatrix();

def cfan2Bench(): 
    '''Creates a matching bench for the piano. Symmetrical, origin 
       under seat above legs, same as piano, and centered.'''

    # bench length
    bLength = 8;
    # bench width
    bWidth = 3;
    # bench depth
    bDepth = 1;
    # leg length
    lLength = 3;

    twColor(pianoColor,0,0); # set color to piano color

    glPushMatrix(); # seat
    glTranslatef(0, 0.5, 0);
    glScalef(bLength, bDepth, bWidth);
    glutSolidCube(1);
    glPopMatrix();

    glPushMatrix(); # legs
    glTranslatef(-bLength/2.0+0.5, -lLength/2.0, 1);
    glScalef(0.5, lLength, 0.5);
    glutSolidCube(1);

    glTranslatef(0, 0, -((bWidth-1)*2));
    glutSolidCube(1);

    glTranslatef((bLength-1)*2, 0, 0);
    glutSolidCube(1);

    glTranslatef(0, 0, (bWidth-1)*2);
    glutSolidCube(1);
    glPopMatrix();

### ================================================================

### Testing code.  Note that all the rest of the file is indented, so that
### it is controlled by the "if" statement. This "if" statement runs if
### the file is run as a shell script, but is not run if the file is
### imported.  Thus, if you run it as a shell script, you automatically
### get a demo, but if you import it, you can just use the functions.

if __name__ == '__main__':

    # a global to hold the current function to demo
    # initialized for real in main
    demoObject = lambda : None

    def display():
        twDisplayInit();
        twCamera();

        # draw whatever the current object is; this is a global variable that
        # is set by various functions below.
        demoObject();

        glFlush();
        glutSwapBuffers();

    def objectPiano(key,x,y):
        global demoObject
        twBoundingBox(-12,12, -5.5,9, -9,6)
        twZview()
        # don't put the () after this, this just copies the
        # function definition to a new name
        demoObject = cfan2Piano
        glutPostRedisplay()

    def objectBench(key,x,y):
        global demoObject
        twBoundingBox(-4,4, -3,1, -1.5,1.5)
        twZview()
        # don't put the () after this, this just copies the
        # function definition to a new name
        demoObject = cfan2Bench
        glutPostRedisplay()

    def main():
        glutInit(sys.argv)
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        twInitWindowSize(500,500)
        glutCreateWindow(sys.argv[0])
        glutDisplayFunc(display)
        # default to showing the piano. Note that this call must be
        # put *here*, after glutCreateWindow and before twMainInit
        objectPiano(None,None,None)
        twMainInit()
        # keyboard callbacks to switch among objects
        # don't put () here, because we are passing in a function object,
        # not invoking the function
        twKeyCallback('1',objectPiano, "Show the Piano")
        twKeyCallback('2',objectBench,   "Show the Bench")
        # twSetMessages(TW_CAMERA)
        glutMainLoop()

    main()
