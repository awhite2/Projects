'''
Jacquelin Shaw's OpenGL Guitar
Copyright (c) 2007 Jacquelin Shaw

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 3
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
<http://www.gnu.org/licenses/>

drawGuitar(float scale);
Draws a gutiar
This can be used by placing it in any kind of scene, room, with other
instruments, etc. 
Every point and value is relative to the radius of the guitar's hole. 
it is resized by an affine transformation, and the only method that requries
a parameter is the drawGuitar method. Therefore, the size of the guitar 
will be determined by the input. A radius of 1 will result in a guitar of 9.5
units in height. Any input will become a multiple of that, or in other words,
any number you submit as the "scale" is the radius. 
The origin of the guitar is at the center of the guitar's hole. No matter what 
the size of the radius, the guitar will always be drawn starting at the center 
of your current coordinate system's origin.

MODIFICATIONS:
J.Shaw's Guitar file ported from C++ to Python by Iva Gishin, October 2009.

'''


import sys

try:
  from TW import *
except:
  print '''
ERROR: Couldn't import TW.
        '''

RAD = 2;                    #this is the radius of the guitar's hole
zcoord = 0.0;               #a z coordinate accesible as 0.0
zcoord2 = -2.0*RAD;         #a z coordinate for the back of the guitar
RAD2 = RAD;                 #originally had this in a seperate file. 
                            #instead of changing all RAD2, simply set it to RAD.
zcoord3 = 0;                #the same applies to zcoord3 and zcoord. it will 
                            #be used only in functions concerning the neck/head
zcoord4 = (0.5/2.0)*RAD2;   #z coordinates 4 and 5 will be used to draw the 
zcoord5 = (-.45/2)*RAD2;    #neck and strings of the guitar





''' ----------------------- THE GUITAR BASE/SIDES ----------------------

These next two arrays contains all the points for the top face and 
bottom face of the guitar. All points are determined relative to the
radius of the guitar hole. '''

top_points = [                   #just for the top face
                [0, 0, zcoord],                                   # 0
                [0, 3.0*RAD, zcoord],                             # 1  
                [-RAD/2.0, 3.0*RAD, zcoord],                      # 2 
                [-RAD, (5.95/2.0)*RAD, zcoord],                   # 3
                [(-3.0/2.0)*RAD,(5.8/2.0)*RAD, zcoord],           # 4
                [(-2.0)*RAD, (5.45/2.0)*RAD, zcoord],             # 5 
                [(-4.5/2.0)*RAD, (5.1/2.0)*RAD, zcoord],          # 6
                [(-4.9/2.0)*RAD, (4.7/2.0)*RAD, zcoord],          # 7
                [(-5.3/2.0)*RAD, (2.0)*RAD, zcoord],              # 8
                [(-5.55/2.0)*RAD, (3.0/2.0)*RAD, zcoord],         # 9
                [(-5.5/2.0)*RAD, RAD, zcoord],                    # 10
                [(-5.4/2.0)*RAD, (1.5/2.0)*RAD, zcoord],          # 11
                [(-5.2/2.0)*RAD, (1.0/2.0)*RAD, zcoord],          # 12
                [(-5.0/2.0)*RAD, (.5/2.0)*RAD, zcoord],           # 13
                [(-4.8/2.0)*RAD, 0, zcoord],                      # 14


  # end of top left quarter, beginning bottom left quarter 

                [(-4.6/2.0)*RAD, (-.5/2.0)*RAD, zcoord],          # 15
                [(-4.5/2.0)*RAD, (-1.0/2.0)*RAD, zcoord],         # 16
                [(-4.7/2.0)*RAD, (-1.5/2.0)*RAD, zcoord],         # 17
                [(-5.0/2.0)*RAD, -RAD, zcoord],                   # 18
                [(-5.5/2.0)*RAD, (-3.0/2.0)*RAD, zcoord],         # 19
                [(-6.0/2.0)*RAD, -2.0*RAD, zcoord],               # 20
                [-3.0*RAD, -2.0*RAD, zcoord],                     # 21
                [(-6.5/2.0)*RAD, (-5.0/2.0)*RAD, zcoord],         # 22
                [(-6.85/2.0)*RAD, -3.0*RAD, zcoord],              # 23

                [(-6.95/2.0)*RAD, (-6.4/2.0)*RAD, zcoord],        # 24
                [(-7.1/2.0)*RAD, (-7.0/2.0)*RAD, zcoord],         # 25
                [(-7.15/2.0)*RAD, (-7.2/2.0)*RAD, zcoord],        # 26
                [(-7.2/2.0)*RAD, -4.0*RAD, zcoord],               # 27
                [(-7.15/2.0)*RAD, (-8.5/2.0)*RAD, zcoord],        # 28
                [(-7.1/2.0)*RAD, (-9.0/2.0)*RAD, zcoord],         # 29
                [(-6.9/2.0)*RAD, -5.0*RAD, zcoord],               # 30

                [(-6.6/2.0)*RAD, (-10.5/2)*RAD, zcoord],          # 31
                [(-6.3/2.0)*RAD, (-10.9/2)*RAD, zcoord],          # 32
                [(-5.8/2.0)*RAD, (-11.4/2)*RAD, zcoord],          # 33
                [(-5.3/2.0)*RAD, (-11.8/2.0)*RAD, zcoord],        # 34
                [(-4.9/2.0)*RAD, (-12.1/2.0)*RAD, zcoord],        # 35
                [-2.0*RAD, (-12.5/2)*RAD, zcoord],                # 36
                [(-3/2.0)*RAD, (-12.8/2.0)*RAD, zcoord],          # 37
                [-RAD, (-12.9/2.0)*RAD, zcoord],                  # 38
                [0, (-13.0/2.0)*RAD, zcoord],                     # 39
     
#end of bottom left quarter, beginning bottom right quarter
#this is essentially the reflection of the bottom left across
#the Y axis, so we can use almost the same points with 
#the X values of the opposite sign

                [(4.6/2.0)*RAD, 0, zcoord],                       # 40
                [(4.5/2.0)*RAD, (-1.0/2.0)*RAD, zcoord],          # 41
                [(4.7/2.0)*RAD, (-1.5/2.0)*RAD, zcoord],          # 42
                [(5.0/2.0)*RAD, -RAD, zcoord],                    # 43
                [(5.5/2.0)*RAD, (-3.0/2.0)*RAD, zcoord],          # 44
                [(6.0/2.0)*RAD, -2.0*RAD, zcoord],                # 45
                [3.0*RAD, -2.0*RAD, zcoord],                      # 46
                [(6.5/2.0)*RAD, (-5.0/2.0)*RAD, zcoord],          # 47
                [(6.85/2.0)*RAD, -3.0*RAD, zcoord],               # 48

                [(6.95/2.0)*RAD, (-6.4/2.0)*RAD, zcoord],         # 49
                [(7.1/2.0)*RAD, (-7.0/2.0)*RAD, zcoord],          # 50
                [(7.15/2.0)*RAD, (-7.2/2.0)*RAD, zcoord],         # 51
                [(7.2/2.0)*RAD, -4.0*RAD, zcoord],                # 52
                [(7.15/2.0)*RAD, (-8.5/2.0)*RAD, zcoord],         # 53
                [(7.1/2.0)*RAD, (-9.0/2.0)*RAD, zcoord],          # 54
                [(6.9/2.0)*RAD, -5.0*RAD, zcoord],                # 55

                [(6.6/2.0)*RAD, (-10.5/2)*RAD, zcoord],           # 56
                [(6.3/2.0)*RAD, (-10.9/2)*RAD, zcoord],           # 57
                [(5.8/2.0)*RAD, (-11.4/2)*RAD, zcoord],           # 58
                [(5.3/2.0)*RAD, (-11.8/2.0)*RAD, zcoord],         # 59
                [(4.9/2.0)*RAD, (-12.1/2.0)*RAD, zcoord],         # 60
                [2.0*RAD, (-12.5/2.0)*RAD, zcoord],               # 61
                [(3.0/2.0)*RAD, (-12.8/2.0)*RAD, zcoord],         # 62
                [RAD, (-12.9/2.0)*RAD, zcoord],                   # 63
                [0, (-13.0/2.0)*RAD, zcoord],                     # 64

  # end of bottom left quarter, beginning top right quarter 

                [0, 0, zcoord],                                   # 65
                [0, 3.0*RAD, zcoord],                             # 66
                [RAD/2.0, 3.0*RAD, zcoord],                       # 67
                [(1.1/2.0)*RAD, (5.0/2.0)*RAD, zcoord],           # 68
                [(1.3/2.0)*RAD, (4.6/2.0)*RAD, zcoord],           # 69 
                [(1.6/2.0)*RAD, (4.2/2.0)*RAD, zcoord],           # 70
                [(1.9/2.0)*RAD, (3.9/2.0)*RAD, zcoord],           # 71
                [(2.5/2.0)*RAD, (3.75/2.0)*RAD, zcoord],          # 72
                [(3.0/2.0)*RAD, (3.8/2.0)*RAD, zcoord],           # 73
                [2.0*RAD, (3.9/2.0)*RAD, zcoord],                 # 74
                [(5.1/2.0)*RAD, 2.0*RAD, zcoord],                 # 75
                [(5.6/2.0)*RAD, (3.9/2.0)*RAD, zcoord],           # 76
                [(5.7/2.0)*RAD, (3.8/2.0)*RAD, zcoord],           # 77
                [(5.9/2.0)*RAD, (3.7/2.0)*RAD, zcoord],           # 78       
                [(6.1/2.0)*RAD, (3.0/2.0)*RAD, zcoord],           # 79
                [(6.0/2.0)*RAD, (2.3/2.0)*RAD, zcoord],           # 80
                [(5.9/2.0)*RAD, RAD, zcoord],                     # 81
                [(5.7/2.0)*RAD, (1.5/2.0)*RAD, zcoord],           # 82
                [(5.3/2.0)*RAD, (1.0/2.0)*RAD, zcoord],           # 83
                [(4.9/2.0)*RAD, (.5/2.0)*RAD, zcoord],            # 84
                [(4.6/2.0)*RAD, 0, zcoord]                        # 85 
            ]

#similar to top_pionts, simply move the z coordinate

b_points = [            #just for the bottom face
  [0, 0, zcoord2],                                    # 0
  [0, 3.0*RAD, zcoord2],                              # 1  
  [-RAD/2.0, 3.0*RAD, zcoord2],                       # 2 
  [-RAD, (5.95/2.0)*RAD, zcoord2],                    # 3
  [(-3.0/2.0)*RAD,(5.8/2.0)*RAD, zcoord2],            # 4
  [(-2.0)*RAD, (5.45/2.0)*RAD, zcoord2],              # 5 
  [(-4.5/2.0)*RAD, (5.1/2.0)*RAD, zcoord2],           # 6
  [(-4.9/2.0)*RAD, (4.7/2.0)*RAD, zcoord2],           # 7
  [(-5.3/2.0)*RAD, (2.0)*RAD, zcoord2],               # 8
  [(-5.55/2.0)*RAD, (3.0/2.0)*RAD, zcoord2],          # 9
  [(-5.5/2.0)*RAD, RAD, zcoord2],                     # 10
  [(-5.4/2.0)*RAD, (1.5/2.0)*RAD, zcoord2],           # 11
  [(-5.2/2.0)*RAD, (1.0/2.0)*RAD, zcoord2],           # 12
  [(-5.0/2.0)*RAD, (.5/2.0)*RAD, zcoord2],            # 13
  [(-4.8/2.0)*RAD, 0, zcoord2],                       # 14


#  end of top left quarter, beginning bottom left quarter 

  [(-4.6/2.0)*RAD, (-.5/2.0)*RAD, zcoord2],           # 15
  [(-4.5/2.0)*RAD, (-1.0/2.0)*RAD, zcoord2],          # 16
  [(-4.7/2.0)*RAD, (-1.5/2.0)*RAD, zcoord2],          # 17
  [(-5.0/2.0)*RAD, -RAD, zcoord2],                    # 18
  [(-5.5/2.0)*RAD, (-3.0/2.0)*RAD, zcoord2],          # 19
  [(-6.0/2.0)*RAD, -2.0*RAD, zcoord2],                # 20
  [-3.0*RAD, -2.0*RAD, zcoord2],                      # 21
  [(-6.5/2.0)*RAD, (-5.0/2.0)*RAD, zcoord2],          # 22
  [(-6.85/2.0)*RAD, -3.0*RAD, zcoord2],               # 23

  [(-6.95/2.0)*RAD, (-6.4/2.0)*RAD, zcoord2],         # 24
  [(-7.1/2.0)*RAD, (-7.0/2.0)*RAD, zcoord2],          # 25
  [(-7.15/2.0)*RAD, (-7.2/2.0)*RAD, zcoord2],         # 26
  [(-7.2/2.0)*RAD, -4.0*RAD, zcoord2],                # 27
  [(-7.15/2.0)*RAD, (-8.5/2.0)*RAD, zcoord2],         # 28
  [(-7.1/2.0)*RAD, (-9.0/2.0)*RAD, zcoord2],          # 29
  [(-6.9/2.0)*RAD, -5.0*RAD, zcoord2],                # 30

  [(-6.6/2.0)*RAD, (-10.5/2)*RAD, zcoord2],           # 31
  [(-6.3/2.0)*RAD, (-10.9/2)*RAD, zcoord2],           # 32
  [(-5.8/2.0)*RAD, (-11.4/2)*RAD, zcoord2],           # 33
  [(-5.3/2.0)*RAD, (-11.8/2.0)*RAD, zcoord2],         # 34
  [(-4.9/2.0)*RAD, (-12.1/2.0)*RAD, zcoord2],         # 35
  [-2.0*RAD, (-12.5/2)*RAD, zcoord2],                 # 36
  [(-3/2.0)*RAD, (-12.8/2.0)*RAD, zcoord2],           # 37
  [-RAD, (-12.9/2.0)*RAD, zcoord2],                   # 38
  [0, (-13.0/2.0)*RAD, zcoord2],                      # 39
     
#end of bottom left quarter, beginning bottom right quarter
#this is essentially the reflection of the bottom left across
#the Y axis, so we can use almost the same points with 
#the X values of the opposite sign '''

  [(4.6/2.0)*RAD, 0, zcoord2],                       # 40
  [(4.5/2.0)*RAD, (-1.0/2.0)*RAD, zcoord2],          # 41
  [(4.7/2.0)*RAD, (-1.5/2.0)*RAD, zcoord2],          # 42
  [(5.0/2.0)*RAD, -RAD, zcoord2],                    # 43
  [(5.5/2.0)*RAD, (-3.0/2.0)*RAD, zcoord2],          # 44
  [(6.0/2.0)*RAD, -2.0*RAD, zcoord2],                # 45
  [3.0*RAD, -2.0*RAD, zcoord2],                      # 46
  [(6.5/2.0)*RAD, (-5.0/2.0)*RAD, zcoord2],          # 47
  [(6.85/2.0)*RAD, -3.0*RAD, zcoord2],               # 48

  [(6.95/2.0)*RAD, (-6.4/2.0)*RAD, zcoord2],         # 49
  [(7.1/2.0)*RAD, (-7.0/2.0)*RAD, zcoord2],          # 50
  [(7.15/2.0)*RAD, (-7.2/2.0)*RAD, zcoord2],         # 51
  [(7.2/2.0)*RAD, -4.0*RAD, zcoord2],                # 52
  [(7.15/2.0)*RAD, (-8.5/2.0)*RAD, zcoord2],         # 53
  [(7.1/2.0)*RAD, (-9.0/2.0)*RAD, zcoord2],          # 54
  [(6.9/2.0)*RAD, -5.0*RAD, zcoord2],                # 55

  [(6.6/2.0)*RAD, (-10.5/2)*RAD, zcoord2],           # 56
  [(6.3/2.0)*RAD, (-10.9/2)*RAD, zcoord2],           # 57
  [(5.8/2.0)*RAD, (-11.4/2)*RAD, zcoord2],           # 58
  [(5.3/2.0)*RAD, (-11.8/2.0)*RAD, zcoord2],         # 59
  [(4.9/2.0)*RAD, (-12.1/2.0)*RAD, zcoord2],         # 60
  [2.0*RAD, (-12.5/2.0)*RAD, zcoord2],               # 61
  [(3.0/2.0)*RAD, (-12.8/2.0)*RAD, zcoord2],         # 62
  [RAD, (-12.9/2.0)*RAD, zcoord2],                   # 63
  [0, (-13.0/2.0)*RAD, zcoord2],                     # 64

 # end of bottom left quarter, beginning top right quarter 

  [0, 0, zcoord2],                                   # 65
  [0, 3.0*RAD, zcoord2],                             # 66
  [RAD/2.0, 3.0*RAD, zcoord2],                       # 67
  [(1.1/2.0)*RAD, (5.0/2.0)*RAD, zcoord2],           # 68
  [(1.3/2.0)*RAD, (4.6/2.0)*RAD, zcoord2],           # 69 
  [(1.6/2.0)*RAD, (4.2/2.0)*RAD, zcoord2],           # 70
  [(1.9/2.0)*RAD, (3.9/2.0)*RAD, zcoord2],           # 71
  [(2.5/2.0)*RAD, (3.75/2.0)*RAD, zcoord2],          # 72
  [(3.0/2.0)*RAD, (3.8/2.0)*RAD, zcoord2],           # 73
  [2.0*RAD, (3.9/2.0)*RAD, zcoord2],                 # 74
  [(5.1/2.0)*RAD, 2.0*RAD, zcoord2],                 # 75
  [(5.6/2.0)*RAD, (3.9/2.0)*RAD, zcoord2],           # 76
  [(5.7/2.0)*RAD, (3.8/2.0)*RAD, zcoord2],           # 77
  [(5.9/2.0)*RAD, (3.7/2.0)*RAD, zcoord2],           # 78      
  [(6.1/2.0)*RAD, (3.0/2.0)*RAD, zcoord2],           # 79
  [(6.0/2.0)*RAD, (2.3/2.0)*RAD, zcoord2],           # 80
  [(5.9/2.0)*RAD, RAD, zcoord2],                     # 81
  [(5.7/2.0)*RAD, (1.5/2.0)*RAD, zcoord2],           # 82
  [(5.3/2.0)*RAD, (1.0/2.0)*RAD, zcoord2],           # 83
  [(4.9/2.0)*RAD, (.5/2.0)*RAD, zcoord2],            # 84
  [(4.6/2.0)*RAD, 0, zcoord2],                       # 85
    ]


# the next functions are used to make the base/sides of the guitar


def drawTopFace():
  ''' uses a triangle fan beginning at the origin,
  creating a "pizza like" slicing of the guitar,
  in order to create its complex shape'''

  glPushMatrix();
  glBegin(GL_TRIANGLE_FAN);
  glColor3ub(244,164,96);         # "Sandy Brown" for the guitar body
  glVertex3fv(top_points[0]);     # top left quarter
  glVertex3fv(top_points[1]);
  glVertex3fv(top_points[2]);    
  glVertex3fv(top_points[3]);     
  glVertex3fv(top_points[4]);    
  glVertex3fv(top_points[5]);    
  glVertex3fv(top_points[6]);    
  glVertex3fv(top_points[7]);
  glVertex3fv(top_points[8]);
  glVertex3fv(top_points[9]);     
  glVertex3fv(top_points[10]);    
  glVertex3fv(top_points[11]);    
  glVertex3fv(top_points[12]);    
  glVertex3fv(top_points[13]);
  glVertex3fv(top_points[14]);
  #twColorName(TW_BLUE);          #for testing

  glVertex3fv(top_points[15]);    # bottom left quarter
  glVertex3fv(top_points[16]);    
  glVertex3fv(top_points[17]); 
  glVertex3fv(top_points[18]);    
  glVertex3fv(top_points[19]);    
  glVertex3fv(top_points[20]); 
  glVertex3fv(top_points[21]);    
  glVertex3fv(top_points[22]);    
  glVertex3fv(top_points[23]); 
  glVertex3fv(top_points[24]); 
  glVertex3fv(top_points[25]);    
  glVertex3fv(top_points[26]);    
  glVertex3fv(top_points[27]); 
  glVertex3fv(top_points[28]);    
  glVertex3fv(top_points[29]);    
  glVertex3fv(top_points[30]);
  glVertex3fv(top_points[31]);    
  glVertex3fv(top_points[32]);    
  glVertex3fv(top_points[33]); 
  glVertex3fv(top_points[34]);    
  glVertex3fv(top_points[35]);    
  glVertex3fv(top_points[36]);
  glVertex3fv(top_points[37]);    
  glVertex3fv(top_points[38]);    
  glVertex3fv(top_points[39]);
  #twColorName(TW_ORANGE);        #for testing

  glVertex3fv(top_points[40]);    #bottom right quarter
  glVertex3fv(top_points[41]); 
  glVertex3fv(top_points[42]);
  glVertex3fv(top_points[43]);    
  glVertex3fv(top_points[44]);    
  glVertex3fv(top_points[45]); 
  glVertex3fv(top_points[46]);    
  glVertex3fv(top_points[47]);    
  glVertex3fv(top_points[48]); 
  glVertex3fv(top_points[49]);    
  glVertex3fv(top_points[50]);    
  glVertex3fv(top_points[51]);
  glVertex3fv(top_points[52]);    
  glVertex3fv(top_points[53]);
  glVertex3fv(top_points[54]);
  glVertex3fv(top_points[55]);    
  glVertex3fv(top_points[56]);    
  glVertex3fv(top_points[57]); 
  glVertex3fv(top_points[58]);    
  glVertex3fv(top_points[59]);    
  glVertex3fv(top_points[60]); 
  glVertex3fv(top_points[61]);    
  glVertex3fv(top_points[62]);    
  glVertex3fv(top_points[63]);
  glVertex3fv(top_points[64]);
  #twColorName(TW_PURPLE);        #for testing

  glVertex3fv(top_points[65]);    #top right corner
  glVertex3fv(top_points[66]);    
  glVertex3fv(top_points[67]);    
  glVertex3fv(top_points[68]); 
  glVertex3fv(top_points[69]);    
  glVertex3fv(top_points[70]);    
  glVertex3fv(top_points[71]);
  glVertex3fv(top_points[72]);    
  glVertex3fv(top_points[73]);
  glVertex3fv(top_points[74]);
  glVertex3fv(top_points[75]);    
  glVertex3fv(top_points[76]);    
  glVertex3fv(top_points[77]); 
  glVertex3fv(top_points[78]);
  glVertex3fv(top_points[79]);    
  glVertex3fv(top_points[80]);    
  glVertex3fv(top_points[81]);
  glVertex3fv(top_points[82]);    
  glVertex3fv(top_points[83]);
  glVertex3fv(top_points[84]);
  glVertex3fv(top_points[85]); 
   
  glEnd();

  glPopMatrix();


'''drawStrip is a helper function used by drawSides
it creates a polygon on the sides based on input points '''

def drawStrip( a, b):
    glPushMatrix();
    glBegin(GL_POLYGON);
    glVertex3fv(top_points[a]);    
    glVertex3fv(top_points[b]);
    glVertex3fv(b_points[b]);
    glVertex3fv(b_points[a]);
    glEnd();
    glPopMatrix();


'''this function draws the "sides" of the guitar. it simply recognizes that
you will always be drawing a polygon with 2 vertices and the preceeding 2
vertices. It will increase i each time until it reaches the final vertex, 
or the 85th element of the array '''

def drawSides():  
    glColor3ub(139,69,19);               # "Saddle Brown"
    for i in range (2,86):
      drawStrip(i, i-1);       
  


'''draws the center hole of the guitar. it is based on the radius'''
def drawHole():
    twColorName(TW_BLACK);
    glPushMatrix(); 
    glTranslatef(0,0,-.99);
    twTube(RAD, RAD, 1.0, 50, 20);
    glPopMatrix();



'''drawBottomFace draws the back of the guitar. It simply translates
 the coordinate system to the z coordinate where the back will be, 
 and draws a TopFace '''

def drawBottomFace():
    glPushMatrix();
    glTranslatef(0, 0, -2.0*RAD);
    drawTopFace();
    glPopMatrix();





''' --------------------- THE GUITAR NECK AND HEAD ----------------------'''


'''an array for the neck of the guitar. Some points can be ignored since they are not used. '''

neck_points =  [           #just for the top face
  [-RAD2/2.0, RAD2, zcoord3],                          # 0
  [0, RAD2, zcoord3],                                  # 1  
  [RAD2/2.0, RAD2, zcoord3],                           # 2 

  [-RAD2/2.0, RAD2, zcoord4],                          # 3  
  [RAD2/2.0, RAD2, zcoord4],                           # 4 

  [(-.8/2.0)*RAD2, 9.0*RAD2, zcoord3],                 # 5
  [0, 9.0*RAD2, zcoord3],                              # 6
  [(.8/2.0)*RAD2, 9.0*RAD2, zcoord3],                  # 7  

  [(-.8/2.0)*RAD2, 9.0*RAD2, zcoord4],                 # 8  
  [(.8/2.0)*RAD2, 9.0*RAD2, zcoord4],                  # 9 
];

'''all of the strings for the guitar. there are 6 strings, each starting
at the top of the neck and ending at the string base'''

lines = [                #for the 6 strings, 3 points for each
    #top of the fret board
    [(-.75/2.0)*RAD2, 9.0*RAD2, zcoord4],               #0 *furthest left
    [(-.45/2.0)*RAD2, 9.0*RAD2, zcoord4], 
    [(-.15/2.0)*RAD2, 9.0*RAD2, zcoord4], 
    [(.15/2.0)*RAD2, 9.0*RAD2, zcoord4], 
    [(.45/2.0)*RAD2, 9.0*RAD2, zcoord4], 
    [(.75/2.0)*RAD2, 9.0*RAD2, zcoord4],                #6 furthest right

    #bottom of the fret board
    [(-.9/2.0)*RAD2, RAD2, zcoord4],                    #6 *furthest left
    [(-.45/2.0)*RAD2, RAD2, zcoord4], 
    [(-.15/2.0)*RAD2, RAD2, zcoord4], 
    [(.15/2.0)*RAD2, RAD2, zcoord4], 
    [(.45/2.0)*RAD2, RAD2, zcoord4], 
    [(.9/2.0)*RAD2, RAD2, zcoord4],

    #string base
    [(-.9/2.0)*RAD2, -RAD2*3.0, zcoord3],               #12 *furthest left
    [(-.45/2.0)*RAD2, -RAD2*3.0, zcoord3], 
    [(-.15/2.0)*RAD2,-RAD2*3.0, zcoord3], 
    [(.15/2.0)*RAD2, -RAD2*3.0, zcoord3], 
    [(.45/2.0)*RAD2, -RAD2*3.0, zcoord3], 
    [(.9/2.0)*RAD2, -RAD2*3.0, zcoord3],    
  ];

'''the head of the guitar. its implementation will resemble that of 
the guitar body'''

head_points = [         #the right half of the head face.
  
    [RAD2*(.8/2.0), RAD2*(16.0/2.0), zcoord3],       #0
    [(1.7/2.0)*RAD2, (16.8/2.0)*RAD2, zcoord3],      #1  
    [(1.5/2.0)*RAD2, (17.0/2.0)*RAD2, zcoord3],      #2
    [(1.4/2.0)*RAD2, (18.0/2.0)*RAD2, zcoord3],      #3
    [(1.4/2.0)*RAD2, (19.0/2.0)*RAD2, zcoord3],      #4
    [(1.5/2.0)*RAD2, (20.0/2.0)*RAD2, zcoord3],      #5
    [(1.7/2.0)*RAD2, (20.2/2.0)*RAD2, zcoord3],      #6
    [RAD2*(.8/2.0), (21.0/2.0)*RAD2, zcoord3],       #7
    
    #the left half of the head face
    [-RAD2*(.8/2.0), (21.0/2.0)*RAD2, zcoord3],       #8
    [-(1.7/2.0)*RAD2, (20.2/2.0)*RAD2, zcoord3],      #9
    [-(1.5/2.0)*RAD2, (20.0/2.0)*RAD2, zcoord3],      #10
    [-(1.4/2.0)*RAD2, (19.0/2.0)*RAD2, zcoord3],      #11
    [-(1.4/2.0)*RAD2, (18.0/2.0)*RAD2, zcoord3],      #12
    [-(1.5/2.0)*RAD2, (17.0/2.0)*RAD2, zcoord3],      #13
    [-(1.7/2.0)*RAD2, (16.8/2.0)*RAD2, zcoord3],      #14
    [-RAD2*(.8/2.0), RAD2*(16.0/2.0), zcoord3],       #15    

    [0, (18.5/2.0)*RAD2, zcoord3],                    #16 ("ORIGIN")
  ];

headb_points = [        #the right half of the head face.

    [RAD2*(.8/2.0), RAD2*(16.0/2.0), zcoord5],       #0
    [(1.7/2.0)*RAD2, (16.8/2.0)*RAD2, zcoord5],      #1  
    [(1.5/2.0)*RAD2, (17.0/2.0)*RAD2, zcoord5],      #2
    [(1.4/2.0)*RAD2, (18.0/2.0)*RAD2, zcoord5],      #3
    [(1.4/2.0)*RAD2, (19.0/2.0)*RAD2, zcoord5],      #4
    [(1.5/2.0)*RAD2, (20.0/2.0)*RAD2, zcoord5],      #5
    [(1.7/2.0)*RAD2, (20.2/2.0)*RAD2, zcoord5],      #6
    [RAD2*(.8/2.0), (21.0/2.0)*RAD2, zcoord5],       #7
    
    #the left half of the head face

    [-RAD2*(.8/2.0), (21.0/2.0)*RAD2, zcoord5],       #8
    [-(1.7/2.0)*RAD2, (20.2/2.0)*RAD2, zcoord5],      #9
    [-(1.5/2.0)*RAD2, (20.0/2.0)*RAD2, zcoord5],      #10
    [-(1.4/2.0)*RAD2, (19.0/2.0)*RAD2, zcoord5],      #11
    [-(1.4/2.0)*RAD2, (18.0/2.0)*RAD2, zcoord5],      #12
    [-(1.5/2.0)*RAD2, (17.0/2.0)*RAD2, zcoord5],      #13
    [-(1.7/2.0)*RAD2, (16.8/2.0)*RAD2, zcoord5],      #14
    [-RAD2*(.8/2.0), RAD2*(16.0/2.0), zcoord5],       #15    

    [0, (18.5/2.0)*RAD2, zcoord5],                    #16 ("ORIGIN")
  ];




def drawNeckTop():
  '''draws the part of the gutiar neck that is 
  in front of the guitar's body. this will be a
  different color from the rest of the guitar'''
  glPushMatrix();           

  glBegin(GL_POLYGON);    
  glVertex3fv(neck_points[0]);        # top 
  glVertex3fv(neck_points[2]);
  glVertex3fv(neck_points[7]);    
  glVertex3fv(neck_points[5]);    
  glEnd();    
  
  glBegin(GL_POLYGON);
  glVertex3fv(neck_points[3]);        # bottom 
  glVertex3fv(neck_points[4]);
  glVertex3fv(neck_points[9]);    
  glVertex3fv(neck_points[8]);
  glEnd();                
                 
  glBegin(GL_POLYGON);
  glVertex3fv(neck_points[0]);        #left    
  glVertex3fv(neck_points[3]);
  glVertex3fv(neck_points[8]);    
  glVertex3fv(neck_points[5]);
  glEnd();

  glBegin(GL_POLYGON);
  glVertex3fv(neck_points[2]);        #right 
  glVertex3fv(neck_points[4]);
  glVertex3fv(neck_points[9]);    
  glVertex3fv(neck_points[7]);
  glEnd();

  glBegin(GL_POLYGON);
  glVertex3fv(neck_points[0]);        # bottom hole
  glVertex3fv(neck_points[2]);
  glVertex3fv(neck_points[4]);    
  glVertex3fv(neck_points[3]);
  glEnd();
  
  glPopMatrix();  



def drawAllStrings():
  '''draws the stings using a line strip'''

  glColor3ub(139,135,110);    # strings will be a grey color

  glLineWidth(.01);
  glBegin(GL_LINE_STRIP);
  glVertex3fv(lines[0]);
  glVertex3fv(lines[6]);
  glVertex3fv(lines[12]);     #the first string on the left

  glVertex3fv(lines[1]);
  glVertex3fv(lines[7]);
  glVertex3fv(lines[13]);

  glVertex3fv(lines[2]);
  glVertex3fv(lines[8]);
  glVertex3fv(lines[14]);
      
  glVertex3fv(lines[3]);
  glVertex3fv(lines[9]);
  glVertex3fv(lines[15]);
   
  glVertex3fv(lines[4]);
  glVertex3fv(lines[10]);
  glVertex3fv(lines[16]);
      
  glVertex3fv(lines[5]);
  glVertex3fv(lines[11]);
  glVertex3fv(lines[17]);     #the last string on the right
  glEnd();



def guitarHeadFace():
  '''draws the head like the guitar body, using a triangle fan.
  the back is done in the same way as well. A transformation pushes
  the origin back and another guitarHeadFace is drawn.'''
  glPushMatrix();                     
                                    
  glBegin(GL_TRIANGLE_FAN);
  glColor3ub(139,69,19);             # "Saddle Brown"
  glVertex3fv(head_points[16]);      # start at the center  
  glVertex3fv(head_points[0]);       # working way around
  glVertex3fv(head_points[1]);    
  glVertex3fv(head_points[2]);     
  glVertex3fv(head_points[3]);    
  glVertex3fv(head_points[4]);    
  glVertex3fv(head_points[5]);    
  glVertex3fv(head_points[6]);
  glVertex3fv(head_points[7]);    
  glVertex3fv(head_points[8]);     
  glVertex3fv(head_points[9]);    
  glVertex3fv(head_points[10]);    
  glVertex3fv(head_points[11]);    
  glVertex3fv(head_points[12]);
  glVertex3fv(head_points[13]);    
  glVertex3fv(head_points[14]);    
  glVertex3fv(head_points[15]);       
  glVertex3fv(head_points[0]);        #end where you start!
  glEnd();
  
  glPopMatrix();
  

def drawNeckBack():

  glPushMatrix();

  glColor3ub(139,69,19);                  # "Saddle Brown" Brown for the neck back

  glTranslatef(0,0,(-.75/2)*RAD2);
  glScalef(RAD2/4.0, 1, (.1/2.0)*RAD2);   # its width is half the size of the radius

  drawNeckTop();
  glPopMatrix(); 


                           #this was a tricky area that was originally open
                           #and I filled it with a polygon by figuring out the coords.
  glBegin(GL_POLYGON);
  glVertex3f((-.9/2.0)*RAD2, 9.0*RAD2,zcoord3);
  glVertex3f((-.75/2.0)*RAD2, 9.0*RAD2,zcoord5);
  glVertex3f((.75/2.0)*RAD2, 9.0*RAD2,zcoord5);
  glVertex3f((.9/2.0)*RAD2, 9.0*RAD2,zcoord3);
  glEnd();



  glPushMatrix(); 
  glTranslatef(RAD2*(1.3/4.0), 0, -RAD2*(.7/4.0));          
  glRotatef(-60, 0, 1, 0); 
  glScalef(.5,1,.1);
  drawNeckTop();
  glPopMatrix();

  glPushMatrix(); 
  glTranslatef(-RAD2*(1.3/4.0), 0, -RAD2*(.7/4.0));         
  glRotatef(60, 0, 1, 0); 
  glScalef(RAD2/4.0,1,.1);
  drawNeckTop();
  glPopMatrix();

  '''this part below was added to enhance the guitar
  it is a cube that serves as a base for the strings. it is below
  the hole and sits "on top" of the guitar's base, just like the 
  top of the neck.
  it is in the NeckBack method even though it is not geometrically
  on the neck back. '''

  glPushMatrix();
  glTranslatef(0, -RAD2*3.0, zcoord3);
  glScalef(RAD2*2, RAD2/2.0, RAD2/4.0);
  glutSolidCube(1);
  glPopMatrix();


def drawStrip2(a, b):
  glPushMatrix();
  glBegin(GL_POLYGON);
  glVertex3fv(head_points[a]);    
  glVertex3fv(head_points[b]);
  glVertex3fv(headb_points[b]);
  glVertex3fv(headb_points[a]);
  glEnd();
  glPopMatrix();


def drawHeadSides():   
  '''this function is very similar to drawSides. it uses the helper
  function drawStrip2, again, using the same method as drawStrip.'''
  for i in range (1, 16):     
    drawStrip2(i, i-1);       


def drawGuitarHead():
  '''combines several methods
  drawing a head on top of the neck'''
  glPushMatrix(); 
  glTranslatef(0,0,(.1/2.0)*RAD2);  

  guitarHeadFace();  
  drawHeadSides(); 

  glPushMatrix();   
  glTranslatef(0,0,zcoord5); 
  glRotatef(180, 0, 1, 0);
  guitarHeadFace();
  drawHeadSides();  
  glPopMatrix();
  glPopMatrix();



def drawMHead():
  '''draws one machine head '''
  glColor3ub(139,135,110);                    #"a grey/silver color"
  glPushMatrix();
  glTranslatef(RAD2/2.0, 0, 0);
  glScalef(2.5, 1.25, .75);
  glutSolidSphere((.25/2.0)*RAD2, 20, 20);
  glPopMatrix();

  

def drawNeck():
  glPushMatrix();
  glColor3ub(137,34,34);                      # "fire brick" for the neck's color

  drawNeckTop();
  drawNeckBack();
  drawAllStrings();

  glPushMatrix();
  glTranslatef(0,0,zcoord4);
  drawGuitarHead();
  glPopMatrix();

  glTranslatef(RAD2*(.8/2.0),RAD2*8.75, 0);   # translate to draw each machine head
  drawMHead(); 
  glTranslatef(0, (1/2.0)*RAD2, 0);
  drawMHead();
  glTranslatef(0, (1/2.0)*RAD2, 0);
  drawMHead();
  glPopMatrix();


  glPushMatrix();
  glTranslatef(-RAD2*1.4,RAD2*8.75, 0);       # same on the other side
  drawMHead();
  glTranslatef(0, (1/2.0)*RAD2, 0);
  drawMHead();
  glTranslatef(0, (1/2.0)*RAD2, 0);
  drawMHead();
  glPopMatrix();
  
''' ----------------- ALL TOGETHER -----------------------------------'''



'''drawGuitar is the function that actually draws the guitar. It is 
the only function that requires a parameter, namely the Radius. 
the guitar will always be drawn with the origin starting at (0,0,0)'''


def drawGuitar(scale):
  glPushMatrix();
  glScalef(scale,scale,scale);
  drawHole();     
  drawTopFace();   
  drawBottomFace();
  drawSides();    
  drawNeck();
  glPopMatrix();

def display():
  twDisplayInit();
  twCamera();

  drawGuitar(RAD);

  glFlush();
  glutSwapBuffers()

def main():
  glutInit(sys.argv)
  glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
  twBoundingBox(-RAD*6,RAD*6,-RAD*12,RAD*18,-RAD*5,RAD*5);
  twInitWindowSize(500,500)
  glutCreateWindow(sys.argv[0])
  glLineWidth(2);
  glutDisplayFunc(display)
  ## twSetMessages(TW_ALL_MESSAGES)
  twMainInit()
  glutMainLoop()

if __name__ == '__main__':
  main()

