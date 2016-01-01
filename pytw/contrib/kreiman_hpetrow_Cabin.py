'''Kelsey Reiman, Heather Petrow 
  CS 307
  kreiman_hpetrow_Cabin.py'''

import math                     # just for sqrt
from TW import *

'''draws a cabin with an origin in the back left corner. It has two dormer windows and an entryway and takes
in a width,height and length as parameters, as well as ppm files for texturing the walls and roof. It also
has two windows on either side of the entryway that are lit by spotlights in the center of the window.
Therefore, it also takes in two light ids as parameters. '''

yellow = (255/255.0,227/255.0,102/255.0)

def draw_kreiman_hpetrow_Cabin(l,w,h,wallTexture,roofTexture,light1_id,light2_id):
    glPushMatrix()
    glRotate(-90,0,1,0)
    drawBarn(l,w,h,wallTexture,roofTexture)
    glPopMatrix()

    drawWindow((.1*l,.2*h,.85*w),.3*h,.3*l,light1_id)
    drawWindow((1.1*l,.2*h,.85*w),.3*h,.3*l,light2_id)

    glPushMatrix() #draw dormer windows
    glTranslate(.3*l,.75*h,w*.75)
    drawBarn(.2*w,.2*h,.2*l,wallTexture,roofTexture)
    glTranslate(.67*l,0,0)
    drawBarn(.2*w,.2*h,.2*l,wallTexture,roofTexture)
    glPopMatrix()


    glPushMatrix() #draw entryway
    glTranslate(.5*l,0,.7*w)
    glRotate(-90,0,1,0)
    drawBarn(.3*w,.4*h,.5*l,wallTexture,roofTexture)
    glPopMatrix()

def quadDirect(p0,p1,p2,p3):
    '''Draw a quad given four vertices in CCW order'''
    v1 = twVector(p1,p0)
    v2 = twVector(p3,p0)
    n = twVectorNormalize(twCrossProduct(v1,v2))
    glBegin(GL_QUADS)
    glNormal3fv(n)
    glVertex3fv(p0)
    glVertex3fv(p1)
    glVertex3fv(p2)
    glVertex3fv(p3)
    glEnd()

def quadAffine(width,depth,position,z_angle):
    '''Draw a quad (w/normal) with front left corner at given position, originally with y=0 but then rotated around Z by given angle.'''

    glPushMatrix()
    glTranslate(*position)      # unwrap list as args 
    glRotate(z_angle,0,0,1)     # rotate around z
    glScalef(width,1,depth)
    twDrawUnitSquare(10*width,10*depth)
    glPopMatrix()    



def quadTexturedDirect(p0,p1,p2,p3,texturePath,textureRepeat):
    '''Draw a quad given four vertices in CCW order'''
    glEnable(GL_TEXTURE_2D);

    twPPM_Tex2D(twPathname(texturePath,False))
    
    v1 = twVector(p1,p0)
    v2 = twVector(p3,p0)
    n = twVectorNormalize(twCrossProduct(v1,v2)) #normalizes vectors
    glBegin(GL_QUADS)
    glNormal3fv(n)
    glTexCoord2f(0,textureRepeat); glVertex3fv(p0); #maps repeating texture 5 times
    glTexCoord2f(textureRepeat,textureRepeat); glVertex3fv(p1);
    glTexCoord2f(textureRepeat,0); glVertex3fv(p2);
    glTexCoord2f(0,0); glVertex3fv(p3);
    glEnd()

    glDisable(GL_TEXTURE_2D);


def triDirect(p0,p1,p2,texturePath):
    '''Draw a triangle given four vertices in CCW order'''
    glEnable(GL_TEXTURE_2D);

    twPPM_Tex2D(twPathname(texturePath,False))
    
    v1 = twVector(p1,p0)
    v2 = twVector(p2,p0)
    n = twVectorNormalize(twCrossProduct(v1,v2))
    glBegin(GL_TRIANGLES)
    glNormal3fv(n)
    glTexCoord2f(0,2.5); glVertex3fv(p0); #maps repeating texture 2.5 times
    glTexCoord2f(2.5,2.5); glVertex3fv(p1); 
    glTexCoord2f(1.25,0); glVertex3fv(p2);
    glEnd()

    glDisable(GL_TEXTURE_2D);

''' draws a barn with normals all pointing outside of the barn, takes in a width, height and length as
parameters and a texture for the walls and the roof'''
def drawBarn(w,h,l,wallTexture,roofTexture):    
    v = [(0,0,0),(w,0,0),(w,h,0),(.5*w,1.4*h,0),(0,h,0),(0,0,-l),(w,0,-l),(w,h,-l),(.5*w,1.4*h,-l),(0,h,-l)] #vertex array of points on barn
    twColorName(TW_WHITE)

    quadTexturedDirect(v[0], v[1], v[2], v[4], wallTexture,5) #front quad
    quadTexturedDirect(v[6], v[5], v[9], v[7], wallTexture,5) #back quad

    triDirect(v[4], v[2], v[3],wallTexture) #front triangle
    triDirect(v[7], v[9], v[8],wallTexture) #back triangle

    quadTexturedDirect(v[2], v[7], v[8], v[3], roofTexture,5) #top right roof
    quadTexturedDirect(v[1], v[6], v[7], v[2], wallTexture,5) #right side

    quadTexturedDirect(v[9], v[4], v[3], v[8], roofTexture,5) #top left roof
    quadTexturedDirect(v[5], v[0], v[4], v[9], wallTexture,5) #left side

    
'''Draws a window with a spotlight in the center. Takes in the position of the lower left corner, the width
and the height, and the id of the light as parameters. '''
def drawWindow(position,h,w,lightId):
    glPushMatrix()
    glTranslate(*position) #lower left corner 
    glScale(w,h,0)
    twColor(yellow,.7,.7)
    quadDirect((0,0,0),(1,0,0),(1,1,0),(0,1,0))
    glPopMatrix()
    
    twColorName(TW_BLACK);
    glLineWidth(2);
    glBegin(GL_LINES);
    glVertex3f(position[0],h,position[2]);
    glVertex3f(position[0]+w,h,position[2]);
    glVertex3f(position[0]+w*.5,position[1],position[2]);
    glVertex3f(position[0]+w*.5,position[1]+h,position[2]);
    glEnd()

    lightPosition = (position[0]+.5*w,position[1]+.5*h,position[2],1)

    twGraySpotlight(lightId,lightPosition,.4, .4, .4,(0,-2,1), 20, 10)

    glEnable(GL_LIGHTING);

def display():
    twDisplayInit();
    twCamera();
   
    draw_kreiman_hpetrow_Cabin(25,30,40,"siding-128x64.ppm","roofing128x64.ppm",GL_LIGHT0,GL_LIGHT2)
 
    glFlush();
    glutSwapBuffers();
    
        
def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(0,100,0,100,0,100)
    twInitWindowSize(500,500);
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()

