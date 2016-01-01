'''Demo of a two-sided triangle, to show the effect of "winding order."
Uses interpolated lines to show the direction.

Spring 2012
D. Anderson
anderson@acm.org
'''

import sys
from TW import *

FrontColor = (0,1,1)
BackColor = (1,1,0)

# ================================================================

A = (0,0,0)
B = (1,0,0)
C = (1,1,0)
D = (0,1,0)

def draw_unit_quad_twosided(location):
    glPushMatrix()
    glTranslatef(*location)
    glBegin(GL_QUADS)
    glNormal3f(0,0,1)
    ## CCW from origin
    glVertex3fv(A)
    glVertex3fv(B)
    glVertex3fv(C)
    glVertex3fv(D)
    ## Back has a different normal
    glNormal3f(0,0,-1)
    glVertex3fv(A)
    glVertex3fv(D)
    glVertex3fv(C)
    glVertex3fv(B)
    glEnd()
    glPopMatrix()

Wire = True

def bezier_unit_quad_twosided_auto_normal(location):
    glPushMatrix()
    glTranslatef(*location)
    glEnable(GL_AUTO_NORMAL)
    ## u is parallel to AB, v is parallel to AD
    cp1 = [[D,C],[A,B]]         # this faces backwards (is culled) u=y v=x
    cp2 = [[C,D],[B,A]]         # this faces forwards, but normal = -z; u=y v=x
    twDrawBezierSurface(cp2,
                        5,  # 5 steps in u
                        10, # 10 steps in v
                        GL_LINE if Wire else GL_FILL)
    '''
    twDrawBezierSurface([[B,A],[C,D]],
                        10,10,
                        GL_LINE if Wire else GL_FILL)
    '''                    
    glPopMatrix()

def twDrawBezierSurfaceUsingNormals(cp, normcp, u_steps, v_steps, mode=GL_FILL):
    """Draw the whole Bezier surface, default mode is GL_FILL

Assumes each element is a triple, so you don't need to worry about
strides."""

    umin = 0
    umax = 1
    vmin = 0
    vmax = 1

    glDisable(GL_AUTO_NORMAL)
    glMap2f(GL_MAP2_VERTEX_3, umin, umax, vmin, vmax, cp);
    glEnable(GL_MAP2_VERTEX_3);
    glMap2f(GL_MAP2_NORMAL, umin, umax, vmin, vmax, normcp);
    glEnable(GL_MAP2_NORMAL);
    
    glMapGrid2f(u_steps,0,1,
                v_steps,0,1);
    glEvalMesh2( mode, 0, u_steps, 0, v_steps )

def bezier_unit_quad_twosided_self_normal(location):
    glPushMatrix()
    glTranslatef(*location)
    ## u is parallel to AB, v is parallel to AD
    cp1 = [[D,C],[A,B]]         # this faces backwards (is culled) u=y v=x
    cp2 = [[C,D],[B,A]]         # this faces forwards, but normal = -z; u=y v=x
    Z = (0,0,1)
    normcp = ((Z,Z),(Z,Z))
    twDrawBezierSurfaceUsingNormals(cp2,normcp,5,10,
                        GL_LINE if Wire else GL_FILL)
    '''
    twDrawBezierSurface([[B,A],[C,D]],
                        10,10,
                        GL_LINE if Wire else GL_FILL)
    '''                    
    glPopMatrix()

# ================================================================

def display():
    twDisplayInit(0.7, 0.7, 0.7)
    twCamera()

    twGrayLight(GL_LIGHT0,(0,0,1,0),0.1,1,0)
    glEnable(GL_LIGHTING)

    twColor((0,1,1),0,0)        # everything is cyan
    glPushMatrix()
    glScalef(1,1,0.2)
    glutSolidCube(1)            # centered on the origin, but thin
    glPopMatrix()

    draw_unit_quad_twosided((-2,0,0))
    bezier_unit_quad_twosided_self_normal((1,0,0))

    glFlush()
    glutSwapBuffers()

def toggleWire(key,x,y):
    global Wire
    Wire = not Wire
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(500,500)
    twBoundingBox(-2,2,-1,1,-1,1)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    ## twSetMessages(TW_ALL_MESSAGES)
    twMainInit()
    twKeyCallback('w',toggleWire,"toggle wireframe")
    glCullFace(GL_BACK)         # the default
    glFrontFace(GL_CCW)         # the default
    glEnable(GL_CULL_FACE)      # usually disabled
    glutMainLoop()

if __name__ == '__main__':
    main()

