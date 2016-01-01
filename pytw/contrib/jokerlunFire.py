''' Johanna Okerlund

    Copyright (C) 2012 by Johanna Okerlund under the GNU GPL

    Includes fire on a log object
    CS 307
'''

import sys
from TW import *

def drawLight():
    lightPos = (50,50,-50,0)
    twGrayLight(GL_LIGHT0,lightPos,0.6,0.9,0.9)
    glEnable(GL_LIGHTING)

def flame():
    Wire = False
    CP = False

    a = (3,11,0) # top point
    topY = 7 # height of top circle
    topR = 1 # radius of top 
    topOff = -3 # offset from y axis in x direction
        
    midY = 4 # height middle circle
    midR = 2 # radius of middle circle
    midOff = 1 # offset from y axis in x dir

    botY = 0 # height
    botR = .25 # radius
    botOff = -1 # offset

    '''The following calculations calculate the control points
        for each of three circles on the xz plane that determine the 
        shape of the flame. It is divided into 4 quarter circle quadrants, 
        each with 4 control points. The "center" control points of each 
        quarter circle are estimated using .55 * the radius'''
        
    # quarter circle on top, front right
    b = (topOff,topY,topR); c = ((topOff+(topR*.55)),topY,topR); 
    d = ((topR)+topOff,topY,topR*.55);e = (topOff+topR,topY,0)  

    # quarter circle in middle, front right
    f = (midOff,midY,midR); g = (midOff+(midR*.55),midY,midR); 
    h = ((midR)+midOff,midY,midR*.55); i = (midOff+midR,midY,0) 
        
    # quarter circle on bottom, front right
    j = (botOff,botY,botR); k = (botOff+(botR*.55),botY,botR);
    l = ((botR)+botOff,botY,(botR*.55)); m = (botOff+botR,botY,0)
        
    point = [a,a,a,a] # the same for all 4 quadrants
 
    top = [b,c,d,e]
    mid = [f,g,h,i]
    bot = [j,k,l,m]
    cp = [point,top,mid,bot]


    # quarter circle on top, front left quadrant
    b2 = (topOff-topR,topY,0); c2 = (topOff-topR,topY,.55*(topR)); 
    d2 = (topOff-(.55*topR),topY,topR); e2 = (topOff,topY,topR)
        
    # quarter circle in middle, front left quadrant
    f2 = (midOff-midR,midY,0); g2 = (midOff-midR,midY,.55*(midR)); 
    h2 = (midOff-(.55*midR),midY,midR); i2 = (midOff,midY,midR)
        
    # quarter circle on bottom, front left quadrant
    j2 = (botOff-botR,botY,0); k2 = (botOff-botR,botY,.55*botR)
    l2 = (botOff-(.55*botR),botY,botR); m2 = (botOff,botY,botR)
        
    top2 = [b2,c2,d2,e2]
    mid2 = [f2,g2,h2,i2]
    bot2 = [j2,k2,l2,m2]
    cp2 = [point,top2,mid2,bot2]


    # quarter circle on top, back left quadrant
    b3 = (topOff-topR,topY,0); c3 = (topOff-topR,topY,-.55*(topR))
    d3 = (topOff-(.55*topR),topY,-topR); e3 = (topOff,topY,-topR)

    # quarter circle in middle, back left quadrant
    f3 = (midOff-midR,midY,0); g3 = (midOff-midR,midY,-.55*(midR))
    h3 = (midOff-(.55*midR),midY,-midR); i3 = (midOff,midY,-midR)
        
    # quarter circle on bottom, back left quadrant
    j3 = (botOff-botR,botY,0); k3 = (botOff-botR,botY,-.55*(botR))
    l3 = (botOff-(.55*botR),botY,-botR); m3 = (botOff,botY,-botR)
        
    top3 = [e3,d3,c3,b3]
    mid3 = [i3,h3,g3,f3]
    bot3 = [m3,l3,k3,j3]
    cp3 = [point,top3,mid3,bot3]

        
    # quarter circle on top, back right quadrant
    b4 = (topOff,topY,-topR); c4 = (topOff+(.55*topR),topY,-topR)
    d4 = (topOff+topR,topY,-.55*topR); e4 = (topOff+topR,topY,0)
        
    # quarter circle in middle, back right quadrant
    f4 = (midOff,midY,-midR); g4 = (midOff+(.55*midR),midY,-midR)
    h4 = (midOff+midR,midY,-.55*midR); i4 = (midOff+midR,midY,0)
        
    # quarter circle on bottom, back right quadrant
    j4 = (botOff,botY,-botR); k4 = (botOff+(.55*botR),botY,-botR)
    l4 = (botOff+botR,botY,-.55*botR); m4 = (botOff+botR,botY,0)
        
    top4 = [e4,d4,c4,b4]
    mid4 = [i4,h4,g4,f4]
    bot4 = [m4,l4,k4,j4]
    cp4 = [point,top4,mid4,bot4]


    u_steps = 10
    v_steps = 10
    glEnable(GL_AUTO_NORMAL)
    twDrawBezierSurface(cp,u_steps,v_steps,
                          GL_LINE if Wire else GL_FILL)
    twDrawBezierSurface(cp2,u_steps,v_steps,
                           GL_LINE if Wire else GL_FILL)
    twDrawBezierSurface(cp3,u_steps,v_steps,
                             GL_LINE if Wire else GL_FILL)
    twDrawBezierSurface(cp4,u_steps,v_steps,
                           GL_LINE if Wire else GL_FILL)

def jokerlunFire():
    '''The following method draws a fire on top of a log.
        The origin of the object is at (0,0,0),
        which is located at the bottom of the log, in the center.
        The object spans from -4.25 to 4.25 in the x dir,
        0 to 14.5 in the y direction,
        and -3.5 to 2.5 in the z dir.
        '''
    red = (1,0,0)
    orange = (1,140.0/255.0,0)
    orangeRed = (1,69.0/255.0,0)

    twColor(red,0.8,10)
    
    glPushMatrix() 
    glTranslate(.5,1.25,0) # move so that origin of object is at the bottom of the middle of the log

    glPushMatrix()
    glRotate(15,0,0,1)
    flame() # middle flame
    glPopMatrix()
    
    glPushMatrix()  
    glTranslate(1.25,0,0)
    glRotate(160,0,1,0)
    glScale(.85,1.2,.85)
    flame()    # right side flame
    glPopMatrix()

    #flame coming off of right side flame
    glPushMatrix()
    glTranslate(2,6,0)
    glScale(.5,.5,.5)
    flame()
    glPopMatrix()

    twColor(orangeRed,0.8,10)

    glPushMatrix()
    glTranslate(2.75,0,.25)
    glRotate(-15,0,1,0)
    glScale(.5,.7,.5)
    flame()   # far right side flame
    glPopMatrix()

    glPushMatrix()
    glTranslate(-3,0,0)
    glRotate(180,0,1,0)
    glRotate(-15,1,0,0)
    glScale(.7,.7,1)
    flame()    # left side flame
    glPopMatrix()

    twColor(orange,0.8,10)
    
    glPushMatrix()
    glTranslate(0,0,1.5)
    glRotate(-45,0,1,0)
    glScale(.6,.7,.6)
    flame()   # front right flame
    glPopMatrix()

    twColor(orangeRed,0.8,10)

    glPushMatrix()
    glTranslate(.5,0,-.75)
    glRotate(85,0,1,0)
    glRotate(15,1,1,0)
    glScale(.9,.7,.9)
    flame() # back right flame
    glPopMatrix()

    glPushMatrix()
    glTranslate(-2,0,-1)
    glRotate(130,0,1,0)
    glRotate(-10,0,0,1)
    glScale(.6,.7,.6)
    flame()  # back left flame
    glPopMatrix()

    twColor(orangeRed,0.8,10)
    
    glPushMatrix()
    glTranslate(0,0,-.25)
    glRotate(-75,0,1,0)
    glScale(.6,.9,.6)
    flame()  # middle flame in back (facing forward)
    glPopMatrix()

    twColor(orange,0.8,10)
        
    glPushMatrix()
    glTranslate(-1,0,-1.25)
    glRotate(90,0,1,0)
    glScale(.8,.9,.8)
    flame()  # large flame in back (facing back)
    glPopMatrix()
    
    "Draw log:" 
    twColor((138.0/255.0,54.0/255.0,15.0/255.0),0.1,2)
    glPushMatrix()
    glTranslate(-4.5,0,0)
    glRotate(90,0,1,0)
    twTube(1.25,1.25,8.5,40,40)
    glPopMatrix()

    glPopMatrix()
    
if __name__ == '__main__':
    
    def display():
        twDisplayInit()
        twCamera()

        glPushAttrib(GL_ALL_ATTRIB_BITS)
    
        drawLight()

        jokerlunFire()

        glPopAttrib()
        glFlush()
        glutSwapBuffers()

    def main():
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        twInitWindowSize(500,500)
        twBoundingBox(-4.25,4.25,0,14.5,-3.5,2.5)
        glutCreateWindow(sys.argv[0])
        glutDisplayFunc(display)
        twMainInit()
        glutMainLoop()
        
    main()
