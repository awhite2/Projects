''' Using fog in a scene of pillars receding into the distance

Written by Caroline Geiersbach and Scott D. Anderson
scott.anderson@acm.org
Summer 2003
ported to Python, 2012
'''

from TW import *
from fog import *

FogOption = 0

def display():
    twDisplayInit(0.3,0.3,0.3)
    twCamera()
    fog(FogOption)

    twColorName(TW_GREEN)
    twGround()

    twColorName(TW_MAGENTA)
    glPushMatrix()
    glTranslatef(50,0,50)
    glScalef(1,40,1)                # for tall cubes
    for i in range(50):
        glutSolidCube(0.5)
        glTranslatef(-1,0,-1)
    glPopMatrix()

    glFlush()
    glutSwapBuffers()

def fogToggle(key, x, y):
    global FogOption
    FogOption = (FogOption+1)%4
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(500, 500)
    twBoundingBox(0,50,0,20,0,50)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    twKeyCallback('f',fogToggle,"switch among fog options");
    glutIdleFunc(None)
    print "use 'f' to switch among fog options"
    glutMainLoop()

if __name__ == '__main__':
    main()
