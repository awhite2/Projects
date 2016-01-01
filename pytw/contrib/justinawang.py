'''Object created by Justina Wang
Copyright (C) 2005 by Justina Wang under the GNU GPL

Ported from C to python by Hanhong Lu for CS307
2/22/2012

This program constructs a bouquet of three flowers.
'''

import sys
try:
    from TW import *
except:
    print '''ERROR: Couldn't import TW.'''

def drawPetal():
    '''Draw one petal'''
    glPushMatrix()
    glRotatef(-75,1,0,0)
    glTranslatef(0,0.25,0)
    glScalef(0.2,0.5,0.1)
    twDisk(1,20)
    glPopMatrix()

def drawFlower(color, flowerHeight, numPetals):
    '''Draw one flower according to the input color and number of petals'''

    # Draw petals by iteratedly executing drawPetal() which draws one petal 
    twColor(color,0.3,10)
    glPushMatrix()
    glTranslatef(0,flowerHeight,0)
    for i in range(numPetals):
        drawPetal()
        glRotatef(360/numPetals,0,1,0)
    glPopMatrix()

    # Draw flower stem
    twColorName(TW_GREEN) # all flower stems are green
    glPushMatrix()
    glTranslatef(0,flowerHeight/2.0,0)
    glScalef(0.1,flowerHeight,0.1)
    glutSolidCube(1)
    glPopMatrix()

    # Draw flower pistil
    twColorName(TW_YELLOW) # all flower pistils are yellow
    glPushMatrix()
    glTranslatef(0,flowerHeight,0) 
    glScalef(0.15,0.15,0.15)
    glutSolidSphere(1,20,20)
    glPopMatrix()

def jwangFlowerBouquet(color1, num1, color2, num2, color3, num3, flowerHeight):
    '''FlowerBouquet object consists of three flowers, which can have different color and number of petals but have the same height.
    Each of them is 25 degrees away from y-axis, and the degree between each of them is 120 degrees.
    Its origin lies at the bottom of the flower stem.
    '''

    # Draw the first flower
    glPushMatrix()
    glRotatef(25,1,0,0)
    drawFlower(color1,flowerHeight,num1)
    glPopMatrix()

    # Draw the second flower
    glPushMatrix()
    glRotatef(120,0,1,0)
    glRotatef(25,1,0,0)
    drawFlower(color2,flowerHeight,num2)
    glPopMatrix()

    # Draw the third flower
    glPushMatrix()
    glRotatef(240,0,1,0)
    glRotatef(25,1,0,0)
    drawFlower(color3,flowerHeight,num3)
    glPopMatrix()

if __name__ == '__main__':
    # global variable:
    flowerHeight=5

    def display():
        '''A callback function to draw the flower bouquet'''

        twDisplayInit()
        twCamera()
  
        red = (1,0,0) # the first flower is red
        blue = (0,0,1) # the second flower is blue
        purple = (0.5,0,0.5) # the third flower is purple
        # the first flower has three petals, the second one has six petals, and the third one has four petals
        jwangFlowerBouquet(red,3,blue,6,purple,4,flowerHeight)

        glFlush()
        glutSwapBuffers()

    def main():
        '''Main function'''
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        twInitWindowSize(500,500)
        glutCreateWindow(sys.argv[0])
        glutDisplayFunc(display)
        twBoundingBox(-flowerHeight/4.0, flowerHeight/4.0,
                      0, flowerHeight+0.5,
                      -1, 1);
        twMainInit();
        glutMainLoop();

    main()
