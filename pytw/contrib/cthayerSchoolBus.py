"""
Carolyn Thayer
11/17/13
cthayerSchoolBus.py

This class creates a school bus with height, length and width of the body of the bus determined
by the user. The origin is at the back, door-side corner of the body of the bus. The height is
along the +y-axis, the length is along the +x-axis and the width is along the -z-axis. The side
of the bus with the door is facing the user. The wheels extend below the body of the bus. The bus
is a somewhat reflective yellow, the windows are a quite reflective grey, the wheels are black
and the headlights are red.
"""


from TW import *
from cthayerBusRoof import *
from cthayerWindow import *
from cthayerDoor import *



### ================================================================

class cthayerSchoolBus():

    def __init__(self):

        # Window(), Door(), and BusRoof() are classes that build parts of the bus
        self.myWindow = Window()   
        self.myDoor = Door()       
        self.myRoof = BusRoof()

        #colors for the different parts of the bus
        self.yellow = (250/255.0,213/255.0,26/255.0)
        self.red = (250/255.0,10/255.0,10/255.0)
        self.black = (0.0,0.0,0.0)


        #control points for a curved slice (the shape of an apple slice silhouette)
        self.cptop = (((0.0, 0.0, 0.0), # ll corner (= A)
                       (0.3, 0.5, 0.0), # ll edge 
                       (0.5, 0.0, 0.0), # ul edge 
                       (0.0, 0.0, 0.0)), # ul corner (= B)

                      ((0.35, 0.0, 0.0), # ll edge 
                       (0.35, 0.2, 0.0), # ll interior corner 
                       (0.35, 0.3, 0.0), # ul interior corner 
                       (0.35, 0.5, 0.0)), # top left edge 

                      ((0.65, 0.0, 0.0), # lr edge
                       (0.65, 0.2, 0.0), # lr interior corner 
                       (0.65, 0.3, 0.0), # ur interior corner 
                       (0.65, 0.5, 0.0)), # ur edge 

                      ((1.0, 0.0, 0.0), # lr corner (= C)
                       (0.7, 0.5, 0.0), # lr edge 
                       (0.5, 0.0, 0.0),  # ur edge 
                       (1.0, 0.0, 0.0)) # ur corner (= D)
                                       )
        

    def draw(self,height,   #height is the height of the body of the bus, not including the
                                #curve of the roof
                length,         #length of the body of the bus, nto including the engine hood area
                width):         #width of the body of the bus, the same as the whole bus


        #variables used in spacing the windows and door
        sideSpace = length/5
        sideEdges = sideSpace/5
        frontWinW = (width-1.5*sideEdges)/2
        frontWinH = (height/2)-2*sideEdges

        
        
        #Side of the bus with the door---------------------------------------------------

        twColor(self.yellow,0.5,0.3)  #semi-reflective

        #Wall of bus
        glBegin(GL_QUADS)
        glNormal3f(0,0,1)
        glVertex3f(0,0,0);
        glVertex3f(length,0,0);
        glVertex3f(length,height,0);
        glVertex3f(0,height,0);
        glEnd()

        #Windows and door will be slightly ahead of the wall so that they aren't existing in
        #the same space
        glPushMatrix()
        glTranslate(0,0,0.1)

        #Loop places three windows along the side of the bus
        for i in range(1,4):
            glPushMatrix()
            glTranslate(i*sideEdges+(i-1)*sideSpace,height/2,0)
            glScale(sideSpace,sideSpace,1)
            self.myWindow.draw(10,10)
            glPopMatrix()

        #Draws the door on the right end of the bus wall
        glPushMatrix()
        glTranslate(4*sideEdges+3*sideSpace,sideEdges,0)
        self.myDoor.draw(sideSpace,height-2*sideEdges)
        glPopMatrix()

        glPopMatrix()


        #Side of the bus with four windows and no door------------------------------------
        glPushMatrix()
        glTranslate(length,0,-width)
        glRotate(180,0,1,0)

        #Wall of the Bus
        twColor(self.yellow,0.5,0.3)
        glBegin(GL_QUADS)
        glNormal3f(0,0,1)
        glVertex3f(0,0,0);
        glVertex3f(length,0,0);
        glVertex3f(length,height,0);
        glVertex3f(0,height,0);
        glEnd()

        #Windows will be slightly ahead of the wall so that they aren't existing in
        #the same space
        glPushMatrix()
        glTranslate(0,0,0.1)

        #Loop places four windows along the side of the bus
        for i in range(1,5):
            glPushMatrix()
            glTranslate(i*sideEdges+(i-1)*sideSpace,height/2,0)
            glScale(sideSpace,sideSpace,1)
            self.myWindow.draw(10,10)
            glPopMatrix()

        glPopMatrix()
        glPopMatrix()


        #Back of the Bus with one large window----------------------------------------------

        glPushMatrix()
        glTranslate(0,0,-width)
        glRotate(-90,0,1,0)

        #Back of the Bus
        twColor(self.yellow,0.5,0.3)
        glBegin(GL_QUADS)
        glNormal3f(0,0,1)
        glVertex3f(0,0,0);
        glVertex3f(width,0,0);
        glVertex3f(width,height,0);
        glVertex3f(0,height,0);
        glEnd()

        #Windows will be slightly ahead of the wall so that they aren't existing in
        #the same space
        glPushMatrix()
        glTranslate(0,0,0.1)

        # One non-square window
        glPushMatrix()
        glTranslate(sideEdges,height/2,0)
        glScale(width-2*sideEdges,sideSpace,1)
        self.myWindow.draw(10,10)
        glPopMatrix()

        glPopMatrix()
        glPopMatrix()

        #Curved piece at the top that fills the curve created by the roof, control points in init

        twColor(self.yellow,0.5,0.3)

        glPushMatrix()
        glTranslate(0,height,-width)
        glRotate(-90,0,1,0)
        glScale(width,height/3,1)
        glEnable(GL_AUTO_NORMAL)
        twDrawBezierSurface(self.cptop,10,10,GL_FILL)
        glPopMatrix()


        #Windshield of the Bus-------------------------------------------------------

        twColor(self.yellow,0.5,0.3)
        glPushMatrix()
        glTranslate(length,height/2,0)
        glRotate(90,0,1,0)

        #Front wall of the Bus
        glBegin(GL_QUADS)
        glNormal3f(0,0,1)
        glVertex3f(0,0,0);
        glVertex3f(width,0,0);
        glVertex3f(width,height/2,0);
        glVertex3f(0,height/2,0);
        glEnd()

        glPushMatrix()
        glTranslate(0,0,0.1)
        

        # loop draws two windows side by side
        for i in range(1,3):
            glPushMatrix()
            glTranslate(i*sideEdges/2+(i-1)*frontWinW,sideEdges/2,0)
            glScale(frontWinW,frontWinH,1)
            self.myWindow.draw(10,10)
            glPopMatrix()

        glPopMatrix()
        glPopMatrix()


        
        #Curved piece at the top that fills the curve created by the roof, control points in init

        twColor(self.yellow,0.5,0.3)
        
        glPushMatrix()
        glTranslate(length,height,0)
        glRotate(90,0,1,0)
        glScale(width,height/3,1)
        twDrawBezierSurface(self.cptop,10,10,GL_FILL)
        glPopMatrix()

        


        #Roof of the bus-------------------------------------------------------------


        twColor(self.yellow,0.5,0.3)
        glPushMatrix()
        glTranslate(0,height,0)
        glScale(length,height/2,width)
        self.myRoof.draw(10,10)
        glPopMatrix()


        #Top of Hood of the Bus-------------------------------------------------------------

        glPushMatrix()

        #Top curve
        glTranslate(length,height/2,-width)
        glRotate(-90,0,1,0)
        glScale(width,height/6,length/4)
        self.myRoof.draw(10,10)

        glPopMatrix()


        #Right Side of Hood-----------------------------------------------------------------
        glPushMatrix()
        glTranslate(length,0,0)
        
        glBegin(GL_QUADS)
        glNormal3f(0,0,1)
        glVertex3f(0,0,0);
        glVertex3f(length/4,0,0);
        glVertex3f(length/4,height/2,0);
        glVertex3f(0,height/2,0);
        glEnd()

        #Curved piece on top of the side
        glPushMatrix()
        glTranslate(0,height/2,0)
        glScale(length/4,height/8,1)
        twDrawBezierSurface(self.cptop,10,10,GL_FILL)
        glPopMatrix()
        
        glPopMatrix()


        #Left Side of Hood------------------------------------------------------------------
        glPushMatrix()
        glTranslate(length,0,-width)
        
        glBegin(GL_QUADS)
        glNormal3f(0,0,-1)
        glVertex3f(0,0,0);
        glVertex3f(length/4,0,0);
        glVertex3f(length/4,height/2,0);
        glVertex3f(0,height/2,0);
        glEnd()

        #Curved piece on top of the side
        glPushMatrix()
        glTranslate(length/4,height/2,0)
        glRotate(180,0,1,0)
        glScale(length/4,height/8,1)
        twDrawBezierSurface(self.cptop,10,10,GL_FILL)
        glPopMatrix()

        glPopMatrix()


        #Front of Hood---------------------------------------------------------------------

        glPushMatrix()
        glTranslate(5*length/4,0,0)
        
        glBegin(GL_QUADS)
        glNormal3f(1,0,0)
        glVertex3f(0,0,0);
        glVertex3f(0,0,-width);
        glVertex3f(0,height/2,-width);
        glVertex3f(0,height/2,0);
        glEnd()


        #Headlights------------------------------------------------------------------------

        twColor(self.red,0.1,0.1)

        #right (doorside) light
        glPushMatrix()
        glTranslate(0,height/6,-width/5)
        glRotate(90,0,1,0)
        glScale(5,5,1)

        glutSolidSphere(1,20,20)

        glPopMatrix()

        #left(driverside) light
        glPushMatrix()
        glTranslate(0,height/6,-4*width/5)
        glRotate(90,0,1,0)
        glScale(5,5,1)

        glutSolidSphere(1,20,20)

        glPopMatrix()
        glPopMatrix()


        #Tires----------------------------------------------------------------------------

        #Back door-side tire
        twColor(self.black,0.1,0.1)
        
        glPushMatrix()
        glTranslate(length/5,0,-width/6)
        glScale(2*sideSpace/3,2*sideSpace/3,sideSpace/3)
        glutSolidSphere(1,60,60)
        glPopMatrix()

        #Back driver-side tire
        glPushMatrix()
        glTranslate(length/5,0,-5*width/6)
        glScale(2*sideSpace/3,2*sideSpace/3,sideSpace/3)
        glutSolidSphere(1,60,60)
        glPopMatrix()

        #Front door-side tire
        glPushMatrix()
        glTranslate(10*length/9,0,-width/6)
        glScale(2*sideSpace/3,2*sideSpace/3,sideSpace/3)
        glutSolidSphere(1,60,60)
        glPopMatrix()

        #Front driver-side tire
        glPushMatrix()
        glTranslate(10*length/9,0,-5*width/6)
        glScale(2*sideSpace/3,2*sideSpace/3,sideSpace/3)
        glutSolidSphere(1,60,60)
        glPopMatrix()
        



        
