### RGB Colored Line with color interpolation

### This is a fancy version that allows us to change the points and colors
### before calling main(). It doesn't quite work yet.

import sys

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''

class Vertex:
    def __init__(self,pos,color):
        self.pos = pos
        self.color = color
    def setPos(self, pos):
        self.pos = pos
    def setColor(self,color):
        self.color = color
    def getPos(self):
        return self.pos
    def getColor(self):
        return self.color
    def draw(self):
        glColor3fv(self.getColor())
        glVertex3fv(self.getPos())

def setPoints(Apos,Acolor,Bpos,Bcolor):
    '''Sets the position and color of A and B in the colored line example'''
    global A, B
    A = Vertex( Apos, Acolor )
    B = Vertex( Bpos, Bcolor )
    (Ax, Ay, Az) = Apos
    (Bx, By, Bz) = Bpos
    twSetMessages(TW_BOUNDING_BOX)
    twBoundingBox( min(Ax,Bx),
                   max(Ax,Bx),
                   min(Ay,By),
                   max(Ay,By),
                   min(Az,Bz),
                   max(Az,Bz))
    twSetMessages(0)

def display():
    twDisplayInit();
    twCamera();

    glShadeModel(GL_SMOOTH)
    glLineWidth(5)

    glBegin(GL_LINES)
    A.draw()
    B.draw()
    glEnd()

    glFlush();
    glutSwapBuffers();



def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    setPoints( (1,2,3), (0,1,1), (6,9,4), (1,1,0) )
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
  main()
