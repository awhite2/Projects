'''Gabe Goodwin
   4/9/2012
An OpenGL model of a Satellite. Copyright (C) 2012 by Gabrielle Goodwin This program is released under the LICENCE INFO HERE.
'''

def init():
    global qobj #so I can use gluCylinder
    qobj = gluNewQuadric();
    gluQuadricNormals(qobj, GLU_SMOOTH);
    gluQuadricTexture( qobj, GL_TRUE )

    global textureIDs
    textureIDs = glGenTextures(6) # get all the texture ids 

    twLoadTexture(textureIDs[0],twPathname("newtech.ppm"))
    twLoadTexture(textureIDs[1],twPathname("iggy.ppm"))
    twLoadTexture(textureIDs[2],twPathname("solarPanel.ppm"))

def ggoodwinSatellite():

'''draws a satellite object'''
    glPushMatrix()

    #Middle square
    glColor3f(1,1,1)
    glEnable(GL_TEXTURE_GEN_S) #enable texture coordinate generation
    glEnable(GL_TEXTURE_GEN_T)
    glBindTexture(GL_TEXTURE_2D, textureIDs[0])
    glutSolidCube(1)
    glDisable(GL_TEXTURE_GEN_S) #disable texture coordinate generation
    glDisable(GL_TEXTURE_GEN_T)


    # Cylinder on top 
    glColor3f(1,1,1)
    glPushMatrix()
    glTranslatef(0,.5,0)
    glRotatef(270,1,0,0)
    glBindTexture(GL_TEXTURE_2D, textureIDs[1])
    gluCylinder(qobj,.3,.3,.3,20,20)
    glPopMatrix()

    #Small right connecting cylinder
    connectorColor = (139.0/255.0, 137.0/255.0, 137.0/255.0)
    glColor3fv(connectorColor)
    glPushMatrix()
    glTranslatef(.5,-.2,0)
    glRotatef(90,0,1,0)
    gluCylinder(qobj,.1,.1,.3,20,20)
    glPopMatrix()

    #Right Wing
    glColor3f(1,1,1)
    glPushMatrix()
    glTranslatef(.7,-.2,0)
    glRotatef(90,0,1,0)
    glScalef(5,.3,.5)
    glBindTexture(GL_TEXTURE_2D, textureIDs[2])
    gluCylinder(qobj,.3,.3,5,20,20)
    glPopMatrix()

    #small left connecting Cylinder
    glColor3fv(connectorColor)
    glPushMatrix()
    glTranslatef(-.5,-.2,0)
    glRotatef(-90,0,1,0)
    gluCylinder(qobj,.1,.1,.3,20,20)
    glPopMatrix()

    #Left Wing
    glColor3f(1,1,1)
    glPushMatrix()
    glTranslatef(-.7,-.2,0)
    glRotatef(-90,0,1,0)
    glScalef(5,.3,.5)
    glBindTexture(GL_TEXTURE_2D, textureIDs[2])
    gluCylinder(qobj,.3,.3,5,20,20)
    glPopMatrix()

    glPopMatrix()

###=================================================================

def display():
    twDisplayInit();
    twCamera();

    glEnable(GL_TEXTURE_2D);

    ggoodwinSatellite()
    
    glFlush();
    glutSwapBuffers()


### ================================================================

def main():
    global DeltaT
    glutInit(sys.argv)
    if len(sys.argv) > 1:
            DeltaT = float(sys.argv[1])
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    twBoundingBox(-3,3,-3,3,-3,3)
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    init()
    glutMainLoop()


if __name__ == '__main__':
    main()


