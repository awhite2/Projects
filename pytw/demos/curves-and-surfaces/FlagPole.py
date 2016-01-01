""" Simple demo of a 2D surface in a 3D world, where the surface is defined
   by Bezier curves.  This gives a wire-frame look at a flag on a
   flagpole.

   Scott D. Anderson
   Fall 2000 original version
   Fall 2003 adapted to use TW
   Fall 2009 ported to Python
"""

import sys

try:
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
        '''

### ================================================================

import Flag

Wire = False
ShowControlPoints = False
Textured = False

myFlagObj = None

def draw_flag_and_pole(pole_height,pole_radius,flag_height,flag_width):
    """Draws a flagpole of the given dimensions.  Origin at base of pole"""
    # color is roughly brass.  See 
    # http://acc6.its.brooklyn.cuny.edu/~lscarlat/graphics/SurfMats.html
    twColor( (0.78,0.57,0.11), 0.94, 28)
    glPushMatrix()
    glRotatef(-90,1,0,0)
    twCylinder(pole_radius,pole_radius,pole_height,20,1)
    glPopMatrix()
    
    # knob at the top, a bit above the pole
    
    glPushMatrix();
    glTranslatef(0,pole_height+pole_radius,0);
    glutSolidSphere(pole_radius,10,10);
    glPopMatrix();

    # draw a flag, measure down from top of flagpole
    twColor( (1,1,1), 1, 5)
    glLineWidth(1);                # flag lines are 1 pixel wide 
    glPushMatrix();
    glTranslatef(0,pole_height-flag_height,0);
    glScalef(flag_width,flag_height,max(flag_width,flag_height));
    if not Textured:
        myFlagObj.draw(8,8,Wire,ShowControlPoints)
    else:
        glEnable(GL_TEXTURE_2D);
        myFlagObj.drawTextured(8,8,Wire,ShowControlPoints)
        glDisable(GL_TEXTURE_2D);
    glPopMatrix();


def display():
    twDisplayInit();
    twCamera();
    glPushAttrib(GL_ALL_ATTRIB_BITS);

    twGrayLight(GL_LIGHT0, (0,1,1,0), 0.1, 0.8, 0.8)

    draw_flag_and_pole(6,0.2,3,5);

    glPopAttrib();
    glFlush();
    glutSwapBuffers();

def toggles(key, x, y):
    global Wire, ShowControlPoints, Textured
    if key == 'w': 
        Wire = not Wire
    elif key == 'c': 
        ShowControlPoints = not ShowControlPoints
    elif key == 't': 
        Textured = not Textured
    glutPostRedisplay();

# ================================================================

def main():
    global myFlagObj
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(0,5,0,6,-1,1);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    twKeyCallback('w',toggles,"toggle wireframe");
    twKeyCallback('c',toggles,"toggle showing control points");
    twKeyCallback('t',toggles,"toggle showing texture mapping");
    glPointSize(5)
    myFlagObj = Flag.Flag()
    glutMainLoop();

if __name__ == '__main__':
    main()
