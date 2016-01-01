''' Rendering a Bezier curve using OpenGL calls.  

Click and drag left button to specify first two control points.
Click and drag right button to specify last two control points.

Scott D. Anderson
scott.anderson@acm.org

'''

import sys
from TW import *

Win_Width = 500
Win_Height = 500

Bezier_Control_Points = [ [ 20, 350, 0 ],
           [ 150, 360, 0 ],
           [ 390, 150, 0 ],
           [ 300,  40, 0 ] ]

DrawCP = True
Steps = 8

def display():
    twDisplayInit(0,0,0)
    myReshape(Win_Width,Win_Height)
    if DrawCP:
        twColorName(TW_YELLOW)
        glBegin(GL_POINTS)
        for cp in Bezier_Control_Points:
            glVertex3fv(cp)
        glEnd()
    twColorName(TW_GREEN)
    twDrawBezierCurve(Bezier_Control_Points,Steps)
    glFlush()


Mod_Point_Index = 0             # index of point to modify 
Old_Point = [0,0]               # old point for motion function
Mouse_Motion = False            # true when tracking mouse 

def mouse(button, state, x, y):
    global Old_Point, Mouse_Motion, Mod_Point_Index, Bezier_Control_Points
    # transform (x,y) to world coordinates
    fx=x;
    fy=Win_Height-y;
    if button==GLUT_MIDDLE_BUTTON:
        return
    if state==GLUT_DOWN:
        # start dragging
        twColorName(TW_RED)
        glEnable(GL_COLOR_LOGIC_OP);
        glLogicOp(GL_XOR)
        Mouse_Motion = True
        Old_Point = [ fx, fy, 0 ]
        if button==GLUT_LEFT_BUTTON:
            Mod_Point_Index = 0
        else:
            Mod_Point_Index = 2
    else:
        # releasing the mouse
        twColorName(TW_GREEN)
        glLogicOp(GL_COPY)
        Mouse_Motion = False
        if button==GLUT_LEFT_BUTTON:
            Mod_Point_Index = 1
        else:
            Mod_Point_Index = 3
    # Ready to modify the point
    Bezier_Control_Points[ Mod_Point_Index ] = [ fx , fy, 0 ]
    glutPostRedisplay()

def motion(x, y):
    global Old_Point
    if not Mouse_Motion:
        return
    y=Win_Height-y;
    # draw a line between the Mod_Point and the old location of the mouse
    # and a line from the Mod_Point to the new location of the mouse
    # because we are in XOR mode, this un-draws the old line and draws the
    # new one
    glBegin(GL_LINES)
    glVertex3fv(Bezier_Control_Points[Mod_Point_Index])
    glVertex3fv(Old_Point)
    Old_Point = [ x, y, 0 ]
    glVertex3fv(Bezier_Control_Points[Mod_Point_Index])
    glVertex3fv(Old_Point)
    glEnd()
    glFlush()

def myReshape(w, h):
    global Win_Width, Win_Height
    Win_Width=w
    Win_Height=h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,w,0,h)
    glMatrixMode(GL_MODELVIEW)

def printCP(key,x,y):
    for cp in Bezier_Control_Points:
        print cp

def toggleCP(key,x,y):
    global DrawCP
    DrawCP = not DrawCP
    glutPostRedisplay()

def main():
    global Steps
    if len(sys.argv) < 2:
        print ('''usage: %s num-steps
Click and drag left button to specify first two control points.
Click and drag right button to specify last two control points.''' %
               (sys.argv[0]))
        sys.exit()
    glutInit()
    Steps = int(sys.argv[1])
    # Note!!!  The XOR drawing doesn't work with double-buffering!
    # Must use single buffering!
    glutInitDisplayMode( GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    # irrelvant; we're not using twCamera()
    twBoundingBox(-1,+1,-1,+1,-1,+1)
    twInitWindowSize(Win_Width,Win_Height)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    twKeyCallback('=',printCP,"print control points")
    twKeyCallback('c',toggleCP,"toggle whether to draw control points")
    glutDestroyMenu(RightMenu)
    glutDetachMenu(GLUT_RIGHT_BUTTON)
    glPointSize(5)
    glLineWidth(2)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutReshapeFunc(myReshape)
    myReshape(Win_Width,Win_Height)
    glutMainLoop()

if __name__ == '__main__':
    main()

