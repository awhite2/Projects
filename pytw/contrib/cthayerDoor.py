'''
Carolyn Thayer
11/17/13
Assignment 6 - creative scene

Draws the outline and windows of a school bus door. There are 4 windows in a 2x2 grid.
'''

from TW import *
from cthayerWindow import *

class Door():

    def __init__(self):
        self.window = Window()  #reflective square window with rounded corners


    def draw(self,width,height):
        '''User can specify the width and height of the door.'''

        #draws the rectanglar frame of the door
        glBegin(GL_LINE_LOOP)
        glColor3f(0.0,0.0,0.0)
        glVertex3f(0,0,0)
        glVertex3f(width,0,0)
        glVertex3f(width,height,0)
        glVertex3f(0,height,0)
        glEnd()


        windWidth = width/3.0   #width of each window
        edgeWidth = windWidth/3.0  #horizontal space between windows

        windHeight = 5*height/13.0  #height of each window
        edgeHeight = height/13.0   #vertical space between windows

        # top left window
        glPushMatrix()
        glTranslate(edgeWidth,height-edgeHeight-windHeight,0)
        glScale(windWidth,windHeight,1)
        self.window.draw(10,10)
        glPopMatrix()

        #top right window
        glPushMatrix()
        glTranslate(2*edgeWidth+windWidth, height-edgeHeight-windHeight, 0)
        glScale(windWidth,windHeight,1)
        self.window.draw(10,10)
        glPopMatrix()

        #bottom left window
        glPushMatrix()
        glTranslate(edgeWidth, height-2*edgeHeight-2*windHeight, 0)
        glScale(windWidth,windHeight,1)
        self.window.draw(10,10)
        glPopMatrix()

        #bottom right window
        glPushMatrix()
        glTranslate(2*edgeWidth+windWidth, height-2*edgeHeight-2*windHeight, 0)
        glScale(windWidth,windHeight,1)
        self.window.draw(10,10)
        glPopMatrix()
        
