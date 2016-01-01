""" This program displays a 2D surface looking vaguely like a coke bottle.

   The bottle silhouette is three Bezier curves, with the transitions at
   the upper bulge and lower dent, since I'll assume that the tangent is
   vertical at that point.

Scott D. Anderson
April 1999 Original
Fall 2003 Revised to use TW
Fall 2009 Ported to Python
"""

import sys

try:
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
        '''

### ================================================================
### Global variables, parameters and constants.  */

## Upper curve, from diameter of 0.75in at height 5in to diameter of 1.5in
## at height 2.5in. 

upper_cp = ((0.5/2, 5.0, 0.0),
            (0.5/2, 4.0, 0.0),
            (1.5/2, 3.0, 0.0),
            (1.5/2, 2.5, 0.0));

## Middle curve, from upper bulge (see previous) to dent with diameter of
## 1.25in at height of 1.25in. */

middle_cp = ((1.5/2,  2.5,  0.0),
             (1.5/2,  2.0,  0.0),
             (1.25/2, 1.75, 0.0),
             (1.25/2, 1.25, 0.0))
                          
## Lower curve, from dent to base, with a radius the same as the bulge. 

lower_cp = ((1.25/2, 1.25, 0.0),
            (1.25/2, 0.75, 0.0),
            (1.5/2,  0.50, 0.0),
            (1.5/2,  0.00, 0.0))

### ================================================================

# The silhouette is a 1D curve in z=0 plane; this rounds it out to a
# 2D surface with a circular cross-section.

def circular_slice(silhouette_cp):
    surface_cp = [ map(list,silhouette_cp),
                   map(list,silhouette_cp),
                   map(list,silhouette_cp),
                   map(list,silhouette_cp) ]
    # the first list will stay unchanged, lying in z=0
    # the last list (#3) will lie in x=0, by swapping x and z for each one
    for i in range(4):
        surface_cp[3][i][0] = surface_cp[0][i][2] # x = z
        surface_cp[3][i][2] = surface_cp[0][i][0] # z = x
    # base list 1 on list 0 and list 2 on list 3.
    for i in range(4):
        # for list 1, x and y don't change, z gets the radius*0.552
        radius = silhouette_cp[i][0]
        dist = radius*0.552;    # distance of inner control points
        surface_cp[1][i][0] = surface_cp[0][i][0]
        surface_cp[1][i][2] = dist
        surface_cp[2][i][0] = dist
        surface_cp[2][i][2] = surface_cp[3][i][2]
    return surface_cp

# Control points for surfaces (quadrants of the bottle)

upperQ_cp = circular_slice(upper_cp)
middleQ_cp = circular_slice(middle_cp)
lowerQ_cp = circular_slice(lower_cp)


### ================================================================ 

def draw_silhouette():
    glPushAttrib(GL_ALL_ATTRIB_BITS);
    twColorName(TW_RED)
    glLineWidth(3.0);
    twDrawBezierCurve(upper_cp,12);
    twDrawBezierCurve(middle_cp,12);
    twDrawBezierCurve(lower_cp,12);

    # draw a single curve reflected across the x=0 plane
    glPushMatrix();
    glScalef(-1,1,1);
    twDrawBezierCurve(upper_cp,12);
    twDrawBezierCurve(middle_cp,12);
    twDrawBezierCurve(lower_cp,12);
    glPopMatrix();
    glPopAttrib();

## the 2D surface is just 1/4 of a circle/cylinder. This does 4 to
## make it complete.
def draw_figure_of_revolution(cp):
    # q is the quadrant of the circular cross-section that we're drawing.
    glPushMatrix();
    for q in range(4):
        twDrawBezierSurface(cp,10,10)
        glRotatef(90,0,1,0);
    glPopMatrix();

def draw_bottle():
    draw_figure_of_revolution(upperQ_cp)
    draw_figure_of_revolution(middleQ_cp)
    draw_figure_of_revolution(lowerQ_cp)

def set_lighting():
    twGrayLight(GL_LIGHT0, (5,5,2,1), 0.2, 0.7, 0.2)
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);

def display():
    twDisplayInit();
    twCamera();
    
    glDisable(GL_LIGHTING);
    glPushMatrix();
    glTranslatef(2,0,0);
    glLineWidth(2);
    twColorName(TW_CYAN);
    draw_silhouette();
    glPopMatrix();

    set_lighting();
    glShadeModel(GL_SMOOTH);        # smooth shading on the bottle
    
    twColor((0.9, 0.7, 0.5), 1,20);
    draw_bottle();

    glFlush();
    glutSwapBuffers();

# ================================================================

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-2,+5,0,5,-2,2);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    upperQ_cp = circular_slice(upper_cp)
    middleQ_cp = circular_slice(middle_cp)
    lowerQ_cp = circular_slice(lower_cp)
    # print shape(upperQ_cp),shape(middleQ_cp),shape(lowerQ_cp)
    glutMainLoop();

if __name__ == '__main__':
    main()
