### Rotating hexagon with HSV color wheel on front. 

#    Each vertex is given a hue based on its angle.  The whole hexagon has
#    the same intensity (V=1).  Thus, we convert from HSV to RGB to specify
#    the color at each vertex.

# First written by Scott D. Anderson, February, 1999
# Updated to use TW Summer, 2003
# Updated to use Python, Fall 2009

import sys

from TW import *

## ================================================================
## Cone has this radius and height

CONE_HEIGHT = 3
CONE_RADIUS = 2

## ================================================================
##   Information about each vertex of the cone.  This avoids having to
##   calculate the color and position information four times.

class VertexInfo:
    '''records the position and color of a vertex.  Color can either be RGB or HSV.'''
    def setPosition(self,x,y,z):
        self.point = (x,y,z)
    def getPosition(self):
        return self.point
    def setColorRGB(self,r,g,b):
        self.rgb = (r,g,b)
    def getColorRGB(self):
        return self.rgb
    def setColorHSV(self,h,s,v):
        self.hsv = (h,s,v)
        # convert hsv to rgb as well
        self.rgb = twHSV2RGB(self.hsv)
    def getColorHSV(self):
        return self.hsv
    def draw(self):
        glColor3fv(self.rgb)
        glVertex3fv(self.point)

Center   = None                 # special vertex for center of the base
Apex     = None                 # special vertex for apex of the cone
Vertices = None                 # we'll append onto this

NumWedges = 6

def initVertexInfo():
    '''Create a cone with a circular base on the z=0 plane with center at
origin and tip at (0,0,-height)'''
    global Center, Apex, Vertices
    Center = VertexInfo()
    Center.setPosition(0,0,0)
    Center.setColorHSV(0,0,1)   # white
    Apex = VertexInfo()
    Apex.setPosition(0,0,-CONE_HEIGHT)
    Apex.setColorHSV(0,0,0)     # black

    Vertices = []               # no need for a dummy first element
    for i in range(NumWedges):
        v = VertexInfo()
        # the angle of the ith wedge, CCW from 3 o'clock
        angle = i * 360.0/NumWedges # in degrees for HSV
        v.setColorHSV(angle,1,1)
        angle = angle * M_PI/180.0 # convert to radians for sin & cos
        v.setPosition(CONE_RADIUS*math.cos(angle),
                      CONE_RADIUS*math.sin(angle),
                      0)
        Vertices.append(v)
    ## put the first vertex on again, to do the last sector
    Vertices.append(Vertices[0])

def drawColorHexCone():
    '''Draws the entire hexcone as a polyhedron

Draws as a pair of triangle fans, one fanning from the apex and another fanning from the center of the base of the cone.  OpenGL won't interpolate correctly if we draw the base as just a big polygon.'''
    ## First the base
    glBegin(GL_TRIANGLE_FAN)
    Center.draw()
    for v in Vertices:
        v.draw()
    glEnd()
    ## Now the sides
    glBegin(GL_TRIANGLE_FAN); 
    Apex.draw()
    for v in Vertices:
        v.draw()
    glEnd()

def display():
    twDisplayInit()
    twCamera()

    drawColorHexCone()

    glFlush()
    glutSwapBuffers()

def increaseWedges(k, x, y):
    '''Increase the number of wedges and recompute the vertices of the cone'''
    global NumWedges
    NumWedges += 1
    initVertexInfo()
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    initVertexInfo();
    twBoundingBox(-CONE_RADIUS,CONE_RADIUS,-CONE_RADIUS,CONE_RADIUS,-CONE_HEIGHT,0);
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    twKeyCallback('w',increaseWedges, "increase the number of wedges");
    glutMainLoop()

if __name__ == '__main__':
    main()
