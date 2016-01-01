# File Name: yangTemple.py
# Purpose: CS307 Computer Graphics assignment #6 Contribution
# Written By: Hye Soo Yang
# Date Created: April 9, 2012
# Description: Creates an object(capitol buildling) for creative scene

'''
An OpenGL model of a bicycle.
Copyright (C) 2012 by Hye Soo Yang. All rights reserved

'''

################# Description in Detail ##################
# def yangTemple(width, height, depth, numColumn, columnRadius,
#            baseRatio, pedRatio, tri=True)
'''The main function in this module is temple() which takes in a number
of parameters that specify and determine the appearance of a parthenon
architectural structure. The user can choose to make it tall, thin, fat,
slim by manipulating the values for width, height and depth.

The user also can choose to make however many columns for the front
facade of the building. The number of columns on the side is relative
to the front ones. The thickness of the column can be modified by
changing columnRadius values.

The parameter 'baseRatio' is how high the podium (where the main block
structure sits on) should be relative to the whole height of the structure.

Similarly, the parameter 'pedRatio' is how high the pediment structure
should be in relation to the overall height of the structure.

If the user decides not to make a pediment structure on top, then
'tri' parameter can be set to False. It is set to True by default.

Individual instances of this module (or a temple object) will be used
to build up a capitol building.

Currently, appropriate textures for a capitol building is yet to be acquired.
An image from the Disney movie 'Tangled' is used as a temporary texture
for now. (It is my favorite movie in the world!)

If a texture is not specified, an image of green roof will be applied
as the texture. 

It runs the textures on the GL_MODULATE mode.'''
##############################################################

from TW import *

templeCoord = None
mainHeight = None

# width, height, depth, protruding amount, base height, pediment)
def createCoord(w, h, d, pa, bh, p, triangle=True):
    '''Creates coordinates for the temple base structure, main block structure,
    and the roofs. Takes in 7 arguments: width, height, depth, protruding amount,
    base height and vertical length of pediment.

    bh or 'base height' is how high the base structure should rise in relation
    to the overall height of building. 

    pa or 'protruding amount' is the distance from the front face of the main block
    structure to the fron face of the base structure. Difference in z-coordinate.

    Every parts of the structure will reside inside the space within the specified
    width, height, depth because base height and pediment heights are relative. 
    '''
    global templeCoord

    sideSpace = w/7.0

    if triangle == True:
        pBaseHeight = p*0.3
        pTriHeight = p*0.7
    else:
        pBaseHeight = p
        pTriHeight = 0
        
    mainHeight = h-p

    
    templeCoord = (
        # Base structure coordinates
        (0,0,0),       # [0] left, bottom, front
        (w,0,0),       # [1] right, bottom, front
        (w,bh,0),      # [2] right, top, front
        (0,bh,0),      # [3] left, top, front
        (0,0,-d),      # [4] left, bottom, back (echo 0)
        (w,0,-d),      # [5] right, bottom, back (echo 1)
        (w,bh,-d),     # [6] right, top, back (echo 2)
        (0,bh,-d),     # [7] left, top, back (echo 3)
        
        # Main block structure coordinates
        # It stands on top of the base structure
        # If pediment height is given, it shortens by the given pediment height
        # It is smaller than the base
        # sideSpace variable is how much space there is between one side of
        # the base to corresponding side of the structure
        # mh variable represents the heght of this main structure

        # sideSpace = w/8.0
        
        (sideSpace,bh,-pa),              # [8] left, bottom, front
        (w-sideSpace,bh,-pa),            # [9] right, bottom, front
        (w-sideSpace,mainHeight,-pa),    # [10] right, top, front 
        (sideSpace,mainHeight,-pa),      # [11] left, top, front
        (sideSpace,bh,-d),               # [12] left, bottom, back (echo of 8)
        (w-sideSpace,bh,-d),             # [13] right, bottom, back (echo of 9)
        (w-sideSpace,mainHeight,-d),     # [14] right, top, back (echo of 10)
        (sideSpace,mainHeight,-d),       # [15] left, top, back (echo of 11)

        # Pediment Base coordinates
        # It stands on top of main block structure
        # If trangle is true, then the coordinates for triangle pediment
        # will be created
        # pBaseHeight is the height of the base structure for pediment
        # pTriHeight is the height of the pediment 

        (0,mainHeight,0),              # [16] left, bottom, front
        (w,mainHeight,0),              # [17] right, bottom, front
        (w,mainHeight+pBaseHeight,0),  # [18] right, top, front
        (0,mainHeight+pBaseHeight,0),  # [19] left, top, front
        (0,mainHeight,-d),             # [20] left, bottom, back (echo of 16)
        (w,mainHeight,-d),             # [21] right, bottom, back (echo of 17)
        (w,mainHeight+pBaseHeight,-d), # [22] right, top, back (echo of 18)
        (0,mainHeight+pBaseHeight,-d), # [23] left, top, back (echo of 19)

        # Pediment coordinates (the triangle)
        (0,mainHeight+pBaseHeight,0),     # [24] left, bottom, front
        (w,mainHeight+pBaseHeight,0),     # [25] right, bottom, front
        (w*0.5,mainHeight+pTriHeight,0),  # [26] middle, front
        (0,mainHeight+pBaseHeight,-d),    # [27] left, bottom, back
        (w,mainHeight+pBaseHeight,-d),    # [28] right, bottom, back
        (w*0.5,mainHeight+pTriHeight,-d)  # [29] middle, back
    )
    return templeCoord

def makeQuad(cd1, cd2, cd3, cd4, texture):
    '''Creates either a quad or a triangle and assigns texture.
    Takes in five arguments:first four are the coordinates for the quad,
    the fifth is the texture image file. If a file is not given, then it is
    set to a default texture file named 'roof.ppm' which is a pretty green roof.

    If third and fourth argument (coordinates) are the same,
    then it creates a triangle.'''

    #if texture == type(twUSFlag()):
        #twPPM_Tex2D(twPathname(texture,False))
    if texture == "":
        twUSFlag()
    else:
        twPPM_Tex2D(twPathname(texture,False))

    glEnable(GL_TEXTURE_2D)
    glBegin(GL_POLYGON)

    if cd3 == cd4:
        glTexCoord2f(0,1); glVertex3fv(cd1)
        glTexCoord2f(1,1); glVertex3fv(cd2)
        glTexCoord2f(0.5,0); glVertex3fv(cd3)
        glTexCoord2f(0.5,0); glVertex3fv(cd4)
    else:
        glTexCoord2f(0,1); glVertex3fv(cd1)
        glTexCoord2f(1,1); glVertex3fv(cd2)
        glTexCoord2f(1,0); glVertex3fv(cd3)
        glTexCoord2f(0,0); glVertex3fv(cd4)
    glEnd()
    glDisable(GL_TEXTURE_2D)        

def yangTemple(width, height, depth, numColumn, columnRadius,
               baseRatio, pedRatio, tri=True, txtr=""):
    '''Creates temple that looks similar to parthenon. Takes in eight arguments:
        width: width of the overall structure
        height: height of the overall structure(including roof, pediment and its base)
        depth: depth of the overall structure. (the length in -z direction)
        numColumn: number of columns you want in the front face.
        columnRadius: adjust this number to find the right thickness for your columns
        baseRatio: the ratio of the height of the base(podium) in relation to the
                   overall height.
                        e.g.) 0.5 will have the base structure half the height of the
                              temple. The columns will therefore be very short.
        pedRadio: similar to baseRatio. This is the ratio of the height of the pediment
                  base and the pediment(triangular one) in relation to the overall
                  height of the structure.
                      e.g.) 0.5 will have a very tall pediment and will look like it's
                            about to fall down because it's so heavy.
        tri: This is a boolean that allows you to choose whether you want the triangular
             pediment on top. If you want a rectangular piece, just set it to False. 
             It is set to True (make the pediment!) by default.
        txtr: Texture for the temple. If nothing is given, then twUSFlag() texture
              will be used. If use the twUSFlag(), then it takes some time for the
              window to pop up because it is calculating texture coordinates for the
              flag.Provide the name of image texture you want to you in double quote.
              the image file and the file have to be in the same directory so that
              the program can find & read it. 
    ''' 
    global templeCoord

    # def createCoord(w, h, d, pa, bh, p, triangle=True):

    pro = depth*0.2
    bHei = height*baseRatio #0.1
    ped = height*pedRatio #0.18
    columnRad = columnRadius #0.75

    cd = createCoord(width, height, depth, pro, bHei, ped, tri)

    # NOTE TO MYSELF:
    # Polygon surface with glColor3f() does not work with lighting unless it has
    # many subdivided faces (probably using twDrawUnitSuare()).
    # However, when the texture is applied, it the surface interacts to the
    # lighting when in the GL_MODULATE mode for glTexEnvf().
    # If in GL_DECAL mode, it is flat. 

    tex = txtr
    
    ###############<----- BASE ----->###############
    # front 
    glNormal3f(0,0,1)
    makeQuad(cd[0],cd[1],cd[2],cd[3], tex)
    # right side
    glNormal3f(1,0,0)
    makeQuad(cd[1],cd[5],cd[6],cd[2], tex)
    # back
    glNormal3f(0,0,-1)
    makeQuad(cd[5],cd[4],cd[7],cd[6], tex)
    # left side
    glNormal3f(-1,0,0)
    makeQuad(cd[4],cd[0],cd[3],cd[7], tex)
    # top
    glNormal3f(0,1,0)
    makeQuad(cd[3],cd[2],cd[6],cd[7], tex)


    #########<----- MAIN STRUCTURE ----->############
    # front
    glNormal3f(0,0,1)
    makeQuad(cd[8],cd[9],cd[10],cd[11], tex)
    # right side
    glNormal3f(1,0,0)
    makeQuad(cd[9],cd[13],cd[14],cd[10], tex)
    # back side
    glNormal3f(0,0,-1)
    makeQuad(cd[12],cd[13],cd[14],cd[15], tex)
    # left side
    glNormal3f(-1,0,0)
    makeQuad(cd[12],cd[8],cd[11],cd[15], tex)

    ###########<------- PEDIMENT --------> ###########
    #===== pediment base =====#
    # front
    glNormal3f(0,0,1)
    makeQuad(cd[16],cd[17],cd[18],cd[19], tex)
    # right side
    glNormal3f(1,0,0)
    makeQuad(cd[17],cd[21],cd[22],cd[18], tex)
    # back
    glNormal3f(0,0,-1)
    makeQuad(cd[20],cd[21],cd[22],cd[23], tex)
    # left side
    glNormal3f(-1,0,0)
    makeQuad(cd[20],cd[16],cd[19],cd[23], tex)
    # bottom
    glNormal3f(0,-1,0)
    makeQuad(cd[16],cd[17],cd[21],cd[20], tex)

    #===== pediment triangle =====#
    # front
    glNormal3f(0,0,1)
    makeQuad(cd[24],cd[25],cd[26], cd[26], tex)
    # back
    glNormal3f(0,0,-1)
    makeQuad(cd[27],cd[28],cd[29],cd[29], tex)
    # right roof
    v1 = twVector(cd[25],cd[28])
    v2 = twVector(cd[25],cd[26])
    n = twVectorNormalize(twCrossProduct(v1,v2))
    glNormal3fv(n)
    makeQuad(cd[25],cd[28],cd[29],cd[26], tex)
    # left roof
    v3 = twVector(cd[24],cd[26])
    v4 = twVector(cd[24],cd[27])
    n = twVectorNormalize(twCrossProduct(v3,v4))
    glNormal3fv(n)
    makeQuad(cd[27],cd[24],cd[26],cd[29], tex)


    ######### CREATE COLUMNS

    createColumn(height,width,depth,bHei,ped,columnRad,numColumn)

    # Create side columns
    # They are smaller in size (radius) than the frontal columns

    sideWidth = depth - pro # pro is the space between the base and the main structure
    sideColumnRad = columnRad*0.8
    sideDepth = width
    numCol = 5
    
    glPushMatrix()
    glRotate(-90, 0,1,0)
    glTranslatef(-depth,0,0)
    createColumn(height,sideWidth,sideDepth,bHei,ped,sideColumnRad,numCol)

    glPushMatrix()
    # the side space was width/7.0 in createCoord()
    # To be exact, since moveIn is depth*0.02 in createColumn(), subtract that distance
    #glTranslatef(0,0,-width+width*0.02 + leftWidth/(numCol*1.45))
    #glTranslatef(0,0,-sideWidth+(sideWidth*0.02*2)+sideWidth/(numCol*1.45))
    # translation in z-axis:
    #       sideWidth*0.02*3
    #           This equation is from moveIn variable in createColumn() function. 
    #           Since it is translating from the origin of the first of the left side
    #           column, it has gone in the distance amount of moveIn in createColumn().
    #           And the right side columns will have moved out twice as far since
    #           the orientation is the same as the leftside.
    #           Therefore multiply by 3.
    #       sideWidth/(numCol*1.45)
    #           This equation is also from createColumn().
    #           This is the computation to calculate the width of the columnbase           
    glTranslatef(0,0,-sideDepth+(sideWidth*0.02*3)+sideWidth/(numCol*1.45))
    createColumn(height,sideWidth,sideDepth,bHei,ped,sideColumnRad,numCol)
    glPopMatrix()
    
    glPopMatrix()


def createColumn(height,width,depth,bHei,ped,columnRad,numColumn):
    '''Creates a row of columns with base and top. Takes in eight arguments:
        height: the height of the temple
        width: width of the temple
        depth: depth of the temple
        bHei: base height. How high the base structure rises
        ped: pediment height. How tall the pediment is.
        columnRad: radius of the column. How thick it is.
        numColumn: number of columns to be created.'''

    mainHeight = height-ped-bHei
    
    division = width/(numColumn*1.45)
    moveIn = depth*0.02       # distance towards inside from the edge
    baseHei = mainHeight*0.04
    cHei = bHei+baseHei
    coord = ((moveIn,bHei,-moveIn),                   # [0] left,bottom,front
             (moveIn+division,bHei,-moveIn),          # [1] right,bottom,front
             (moveIn+division,cHei,-moveIn),          # [2] right,top,front
             (moveIn,cHei,-moveIn),                   # [3] left,top, front
             (moveIn,bHei,-moveIn-division),          # [4] left,bottom,back(echo 0)
             (moveIn+division,bHei,-moveIn-division), # [5] right,bottom,back(echo 1)
             (moveIn+division,cHei,-moveIn-division), # [6] right,top,back(echo 2)
             (moveIn,cHei,-moveIn-division)           # [7] left,top,back(echo 4)
            )

    tex = "roof.ppm"

    gluQuadric = gluNewQuadric()
    
    # Recursively create columns and column bases 
    for n in range(numColumn):
        #print numColumn
        if n == 0:
            glPushMatrix()
        else:
            glPushMatrix()
            glTranslatef(division*1.5,0,0)
            
        # front
        glNormal3f(0,0,1)
        makeQuad(coord[0],coord[1],coord[2],coord[3], tex)
        # right side
        glNormal3f(1,0,0)
        makeQuad(coord[1],coord[5],coord[6],coord[2], tex)
        # back
        glNormal3f(0,0,-1)
        makeQuad(coord[4],coord[5],coord[6],coord[7], tex)
        # left side
        glNormal3f(0,0,-1)
        makeQuad(coord[4],coord[0],coord[3],coord[7], tex)
        # top
        glNormal3f(0,1,0)
        makeQuad(coord[3],coord[2],coord[6],coord[7], tex)

        # Create the top decorative cubes for the columns
        glPushMatrix()
        glRotate(180, 1,0,0)
        glTranslatef(0,-mainHeight-bHei*2,moveIn*2+division)
        #glRotate(180, 1,0,0)

        # front
        glNormal3f(0,0,1)
        makeQuad(coord[0],coord[1],coord[2],coord[3], tex)
        # right side
        glNormal3f(1,0,0)
        makeQuad(coord[1],coord[5],coord[6],coord[2], tex)
        # back
        glNormal3f(0,0,-1)
        makeQuad(coord[4],coord[5],coord[6],coord[7], tex)
        # left side
        glNormal3f(0,0,-1)
        makeQuad(coord[4],coord[0],coord[3],coord[7], tex)
        # top
        glNormal3f(0,1,0)
        makeQuad(coord[3],coord[2],coord[6],coord[7], tex)        

        glPopMatrix()

        glPushMatrix()
        #glTranslatef(columnRad+moveIn*1.3,bHei,-moveIn-columnRad)
        glTranslatef(moveIn+division*0.5,bHei,-moveIn-division*0.5)
        # moveIn is where the column base is created
        # the column should be on top of column base
        glRotatef(-90, 1,0,0)
        # Creates the cylinder having the center of it at the origin on +z axis
        # So need to move it the distance of column Radius and Rotate it 90 around x 
        gluCylinder(gluQuadric,columnRad,columnRad,mainHeight,30,30)
        glPopMatrix()

        # When get to the last element, popMatrix all at once so that it creates
        # the column recursively
        if n == numColumn-1:
            for n in range(numColumn):
                glPopMatrix()

def display():
    twDisplayInit(0.6,0.6,0.6)  # 60% gray on background
    twCamera()
    twGrayLight(GL_LIGHT0, (20,10,8,0), 0.7, 0.7, 0.7)
    glEnable(GL_LIGHTING)

    yangTemple(20,25,15,5,0.7,0.35,0.4,True,"tangled.ppm")
    glFlush()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH )

    x_min = 0
    y_min = 0
    z_min = -15

    x_max = 45
    y_max = 18
    z_max = 0

    twBoundingBox(x_min, x_max, y_min, y_max, z_min, z_max)
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()

    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    
    glutMainLoop()

if __name__ == '__main__':
    main()
