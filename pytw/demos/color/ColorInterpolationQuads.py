### Demonstration that color interpolation on quads is hard to predict.

#    The pictures in the first row are (1) a quad with RGBW vertices with
#    the first vertex being the upper right one and proceding
#    counterclockwise, (2) two triangles cut along the ul-lr diagonal, (3)
#    two triangles cut along the ur-ll diagonal.  Note that the quad matches
#    the third figure, not the second. This shows that the triangulation is
#    done as you'd expect: the first three vertices are formed into a
#    triangle, then the next three.

#    The pictures in the second row are (4) the quad cut into four triangles
#    using the middle point, and (5) the quad cut into 400 quads using a
#    mesh.

#    The main problem is that the two triangulations are different, when you
#    might think it wouldn't matter.  (With flat shading, they don't,
#    because the fourth vertex determines the color.)  Next, none of the
#    elements on the first row matches the four-part triangulation in the
#    second row.  The fifth version is the smoothest yet, but you might
#    think they should all match.

# Implemented Fall 2006
# Ported to Python Fall 2009
# Scott D. Anderson

import sys

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''

Quads = ((0,0,0),                # vertex 1, lower left
         (0,1,0),                # vertex 2, lower right
         (1,1,0),                # vertex 3, upper right
         (1,0,0)                 # vertex 4, upper left
         );

Colors = ((1,0,0),              # red
          (0,1,0),              # green
          (0,0,1),              # blue
          (1,1,0)               # yellow
          );
        
def drawVertex(index):
    '''Sends a vertex and its associated color down the pipeline

A simple convenience to shorten the code and guarantee that the same
color is always associated with each vertex.  Notice that the color is
given *before* the vertex.'''
    glColor3fv(Colors[index])
    glVertex3fv(Quads[index])

def drawQuad():
    '''Draw a Quad'''
    glBegin(GL_QUADS);
    drawVertex(0);
    drawVertex(1);
    drawVertex(2);
    drawVertex(3);
    glEnd();

def drawQuad1():
    '''This quad is split into two triangles, along the ll-ur (0-2) diagonal.'''
    glBegin(GL_TRIANGLES);
    # first triangle
    drawVertex(0);
    drawVertex(1);
    drawVertex(2);
    # second triangle
    drawVertex(2);
    drawVertex(3);
    drawVertex(0);
    glEnd();

def drawQuad2():
    '''This quad is split into two triangles, along the ul-lr (1-3) diagonal.'''
    glBegin(GL_TRIANGLES);
    # first triangle
    drawVertex(0);
    drawVertex(1);
    drawVertex(3);
    # second triangle
    drawVertex(1);
    drawVertex(2);
    drawVertex(3);
    glEnd();

def drawTri():
    '''This draws a quad by breaking it into four triangles using the middle point.'''
    ## remember to divide by 4.0 not 4
    mid = ((Quads[0][0]+Quads[1][0]+Quads[2][0]+Quads[3][0])/4.0,
           (Quads[0][1]+Quads[1][1]+Quads[2][1]+Quads[3][1])/4.0,
           0)
    colormid = ((Colors[0][0]+Colors[1][0]+Colors[2][0]+Colors[3][0])/4.0,
                (Colors[0][1]+Colors[1][1]+Colors[2][1]+Colors[3][1])/4.0,
                (Colors[0][2]+Colors[1][2]+Colors[2][2]+Colors[3][2])/4.0)
    glBegin(GL_TRIANGLES)
    # the 0,1,middle triangle.
    drawVertex(0);
    drawVertex(1);
    glColor3fv(colormid);        glVertex3fv(mid);

    # the 1,2,middle triangle
    drawVertex(1);
    drawVertex(2);
    glColor3fv(colormid);        glVertex3fv(mid);

    # the 2,3,middle triangle
    drawVertex(2);
    drawVertex(3);
    glColor3fv(colormid);        glVertex3fv(mid);

    # the 3,0,middle triangle
    drawVertex(3);
    drawVertex(0);
    glColor3fv(colormid);        glVertex3fv(mid);
    glEnd();

def drawGrid():
    '''Draws the quad by breaking it into a 20x20 mesh of tiny quads and
drawing each of those.  

With the quads so small, there is little difference between different
ways of triangulating it.  Thus, we're forcing the interpolation by
hand.'''
    steps = 20
    
    ## Don't worry about this code until we get to curves and surfaces
    cp = ( ((0,1,0),
            (0,0,0)),
           ((1,1,0),
            (1,0,0)))
    colors = ( ((0,1,0,1),
                (0,0,1,1)),
               ((1,0,0,1),
                (1,1,0,1)))
    glMap2f(GL_MAP2_VERTEX_3,0,1,0,1,cp);
    glMap2f(GL_MAP2_COLOR_4,0,1,0,1,colors);
    glEnable(GL_MAP2_COLOR_4);
    glEnable(GL_MAP2_VERTEX_3);
    glMapGrid2f(steps,0,1,steps,0,1);
    glEvalMesh2(GL_FILL,0,steps,0,steps);

def display():
    twDisplayInit();
    twCamera();

    glShadeModel(GL_SMOOTH);

    drawQuad();                 # leftmost, top row

    glPushMatrix();
    glTranslatef(1.1,0,0);
    drawQuad1();                # middle top row
    glPopMatrix();

    glPushMatrix();
    glTranslatef(2.2,0,0);
    drawQuad2();                # rightmost, top row
    glPopMatrix();

    glPushMatrix();
    glTranslatef(0.55,-1.1,0);
    drawTri();                  # 
    glPopMatrix();

    glPushMatrix();
    glTranslatef(1.65,-1.1,0);
    drawGrid();
    glPopMatrix();

    glFlush();
    glutSwapBuffers();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(1000,800)
    glutCreateWindow(sys.argv[0])
    glLineWidth(2)
    glutDisplayFunc(display)
    # a lie, to get the camera much closer
    # real BB is x: 0-3.2 y: -1.1 to 1
    twBoundingBox(0.5,2.5,-0.5,0.5,0,0);
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
  main()
