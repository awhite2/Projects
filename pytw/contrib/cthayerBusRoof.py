'''
Carolyn Thayer
11/17/13
Assignment 6 - creative scene

Bezier Surface that has straight front and back edges but right and left are curved upward. Used as a roof of a
school bus.
'''

from TW import *


class BusRoof():

    def __init__(self):
        #control points for surface
        a = (0,0,0);  b = (1,0,0) # front left and front right
        c = (0,0.5,-0.5);  d = (1,0.5,-0.5)  #mid left and mid right
        e = (0,0,-1);  f = (1,0,-1)   #back left and back right
        front = [a,b]
        mid = [c,d]
        back = [e,f]
        # u is the ace or bdf direction
        self.cp = [back,mid,front] # back is first so that the normal points up (positive y-axis)


    def draw(self,u_steps,v_steps):
        glEnable(GL_AUTO_NORMAL) # normal points out of the upward facing side
        twDrawBezierSurface(self.cp,u_steps,v_steps,GL_FILL)

