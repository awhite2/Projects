"""Demonstration of aliasing

Written by Caroline Geiersbach and Scott D. Anderson
scott.anderson@acm.org
Summer 2003
Fall 2009, ported to Python
"""

try:
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
        '''

### ================================================================

ObjectID = 1                # start with the teapot

def drawScene():
    twColorName(TW_CYAN);
    # this is too fancy, but I couldn't resist.  We have an array of
    # functions, and we get one and invoke it.  The normal coding
    # would be a long if elif elif ...
    drawfuns = [ None,
                 lambda: glutSolidTeapot(1),
                 lambda: glutWireCube(2),
                 lambda: glutSolidCube(2),
                 lambda: glutSolidSphere(1,25,25) ]
    drawer = drawfuns[ObjectID]
    drawer()

def display():
    twDisplayInit(0,0,0);
    twCamera();
    drawScene();
    glFlush();
    glutSwapBuffers();

NumFrames = 4

# For anti-aliasing by jittering scene location
def displayN():
    glClearAccum(0,0,0,0);
    glClear(GL_ACCUM_BUFFER_BIT);
    for frame in range(NumFrames):
        twDisplayInit(0,0,0);        
        twCamera();
        glPushMatrix();
        # This jitter amount is entirely made up.
        jitter = 0.01;
        if frame&1:
            glTranslatef(jitter,0,0);
        if frame&2:
            glTranslatef(0,jitter,0);
        drawScene();
        glPopMatrix();
        glAccum(GL_ACCUM, 1.0/NumFrames);
    # copy the scene from the accumulation buffer into the color buffer
    glAccum(GL_RETURN, 1.0);
    glFlush();
    glutSwapBuffers();

AntiAlias = False

def keys(key, x, y):
    global ObjectID, AntiAlias
    if key > '0' and key < '9':
        ObjectID = ord(key)-ord('0')
    if key == 'a':
        AntiAlias = not AntiAlias
        if AntiAlias:
            glutDisplayFunc(displayN)
        else:
            glutDisplayFunc(display)
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_ACCUM);
    twInitWindowSize(600,600);
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display);
    twBoundingBox(-2,2,-1,1,-1,1);
    twMainInit();
    twKeyCallback('a',keys,"toggle anti-aliasing");
    twKeyCallback('1',keys,"show the teapot");
    twKeyCallback('2',keys,"show the wire cube");
    twKeyCallback('3',keys,"show the solid cube");
    twKeyCallback('4',keys,"show the solid sphere");
    glutMainLoop();

if __name__ == '__main__':
    main()
