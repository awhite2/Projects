""" Demonstrates lighting of a flat patch, to help figure out how normals
   are calculated by GL_AUTO_NORMAL.
   
   The answer is that they are calculated as s x t (u x v): the s
   vector crossed with the t vector.  Therefore, if s increases left
   to right and t increases bottom to top, the normal vector will
   point towards you.  Alternatively, the s vector could increase top
   to bottom and the t vector could increase left to right, and you'd
   get the normal vector facing towards you.  This is convenient if
   you want the upper left corner to be at parameters (0,0).

   The u or s dimension is the 'outer' one in the nested arrays of
   arrays, and v (or t) dimension is the 'inner' one.

   I'm not yet sure what determines whether the quads face backwards
   or forwards (for backface culling).  So don't do backface culling
   with Bezier surfaces.
   
Written by Scott D. Anderson
scott.anderson@acm.org
Fall 2005
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

Wire = True
ShowControlPoints = True

### ================================================================

# These are CCW from lower left

A = (0,0,0)                     # lower left
B = (1,0,0)                     # lower right
C = (1,1,0)                     # upper right
D = (0,1,0)                     # upper left

# CP1: culled just like the Quads, so front facing
# u goes up, v goes right, so normal = -Z

FlatCP1 = ((A, B), (D, C))

# CP2: culled, so backwards facing, normal = -Z

FlatCP2 = ((A, D), (B, C))

Z = (0,0,1)

normcp = ((Z, Z), (Z, Z))

### ================================================================

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

### ================================================================

def drawBlackText(x,y,z,text):
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glDisable(GL_LIGHTING)      # use RGB color for text
    twColorName(TW_BLACK)
    twDrawString(x,y,z,text)
    glPopAttrib()

def solidSphere(dx,dy):
    glPushMatrix();
    glTranslatef(dx,dy,0);
    glutSolidSphere(0.5,20,20);
    #glutSolidCube(0.5);
    glPopMatrix();

def unlitQuad(dx,dy):
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glDisable(GL_LIGHTING)      # use RGB color for this one
    twColor((0.6,0.1,0.2),0.9,20,GL_BACK)
    twColor((0.4,0.9,0.8),0.9,20,GL_FRONT)
    glPushMatrix();
    glTranslatef(dx,dy,0);
    glBegin(GL_QUADS);
    glNormal3f(0,0,1);
    glVertex3fv(A)
    glVertex3fv(B)
    glVertex3fv(C)
    glVertex3fv(D)
    glEnd();
    glBegin(GL_POINTS);
    twColorName(TW_BLUE)
    glVertex3fv(A)
    twColorName(TW_MAGENTA)
    glVertex3fv(B)
    twColorName(TW_WHITE)
    glVertex3fv(C)
    twColorName(TW_CYAN)
    glVertex3fv(D)
    glEnd();
    drawBlackText(0,-0.5,0,"unlit Quad");
    glPopAttrib()
    glPopMatrix();


def litQuad(dx,dy):
    glPushMatrix();
    glTranslatef(dx,dy,0);
    glBegin(GL_QUADS);
    glNormal3f(0,0,1);
    glVertex3fv(A)
    glVertex3fv(B)
    glVertex3fv(C)
    glVertex3fv(D)
    glEnd();
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glDisable(GL_LIGHTING)      # use RGB color for marking points
    glBegin(GL_POINTS);
    twColorName(TW_BLUE)
    glVertex3fv(A)
    twColorName(TW_MAGENTA)
    glVertex3fv(B)
    twColorName(TW_WHITE)
    glVertex3fv(C)
    twColorName(TW_CYAN)
    glVertex3fv(D)
    glEnd();
    drawBlackText(0,-0.5,0,"lit Quad");
    glPopAttrib()
    glPopMatrix();

def flatPatch(dx,dy,cp,text):
    glEnable(GL_LIGHTING)
    glEnable(GL_AUTO_NORMAL)
    twColor((0.4,0.9,0.8),0.9,20,GL_FRONT)
    twColor((0.6,0.1,0.2),0.9,20,GL_BACK)
    glNormal3f(0,0,1)
    glPushMatrix();
    glTranslatef(dx,dy,0);
    twDrawBezierControlPoints(cp)
#    twDrawBezierSurfaceUsingNormals(cp,normcp,5,5,GL_FILL)
    twDrawBezierSurface(cp,5,5,GL_FILL)
    drawBlackText(0,-0.5,0,text);
    glPopMatrix();

### ================================================================

CullFace = False;          # the OpenGL default
TwoSided = False;          # the OpenGL default
Local = False              # the OpenGL default

def display():
    twDisplayInit();
    twCamera();

    twGrayLight(GL_LIGHT0,(0,0,1,0), 0, 1, 0) # mostly diffuse light
    glEnable(GL_LIGHT0);

    glEnable(GL_LIGHTING);
    glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER,Local);
    if CullFace:
        glEnable(GL_CULL_FACE)
    else:
        glDisable(GL_CULL_FACE)
    glLightModeli(GL_LIGHT_MODEL_TWO_SIDE,TwoSided)
    glShadeModel(GL_SMOOTH);
    twAmbient(0);

    # every object gets this cyan-like color, and its complement on the back
    twColor((0.4,0.9,0.8),0.9,20,GL_FRONT_AND_BACK)
#    twColor((0.6,0.1,0.2),0.9,20,GL_BACK)

    # the main point is to experiment with this
    glEnable(GL_AUTO_NORMAL)

    solidSphere(0.5,0.5)

    unlitQuad(-1,+1)
    litQuad(-1,-1)
    flatPatch(1,1,FlatCP1,"Patch 1")
    flatPatch(1,-1,FlatCP2,"Patch 2")

    twColorName(TW_BLACK)
    msg = "Two Sided" if TwoSided else "One Sided"
    msg += "     "
    msg += "CullFace" if CullFace else "Not CullFace"
    msg += "     "
    msg += "Local" if Local else "Not Local"
    drawBlackText(0, -2, 0, msg)
    glFlush();
    glutSwapBuffers();


def keys(key, x, y):
    global CullFace, TwoSided, Local
    if key == 'c': 
        CullFace = not CullFace
    elif key == '0': 
        twRotateViewpoint(180,(0,1,0))
    elif key == '1': 
        TwoSided = False
    elif key == '2': 
        TwoSided = True
    elif key == 'l':
        Local = not Local
    glutPostRedisplay()

# ================================================================

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-1,2,-1,1,0,0);
    twInitWindowSize(1000,800);
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    glPointSize(6)
    twKeyCallback('c',keys,"toggle backface culling");
    twKeyCallback('0',keys,"180-degree turn");
    twKeyCallback('1',keys,"one-sided lighting");
    twKeyCallback('2',keys,"two-sided lighting");
    twKeyCallback('l',keys,"toggle local viewer");
    glutMainLoop();

if __name__ == '__main__':
    main()
