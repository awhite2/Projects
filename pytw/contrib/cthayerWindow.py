"""
Carolyn Thayer
11/17/13
Assignment 6 - creative scene

Draws a grey, reflective, squareish window with rounded corners.
"""

try:
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
        '''

### ================================================================

class Window():
    """Window is within a unit square, origin at lower left corner"""
    def __init__(self):
        self.darkGrey = (77/255.0, 77/255.0, 77/255.0)

        #control points
        self.cp = (
                   ((0.5, 0.0, 0.0), # ll corner (= A)
                    (-0.1, 0.0, 0.0), # ll edge 
                    (0.0, -0.1, 0.0), # ul edge 
                    (0.0, 0.5, 0.0)), # ul corner (= B)

                   ((1.0, 0.0, 0.0), # ll edge, curving forward 
                    (0.8, 0.2, 0.0), # ll interior corner 
                    (0.2, 0.8, 0.0), # ul interior corner 
                    (0.0, 1.0, 0.0)), # top left edge 

                   ((1.0, 0.0, 0.0), # lr edge, curving forward from behind 
                    (0.8, 0.2, 0.0), # lr interior corner 
                    (0.2, 0.8, 0.0), # ur interior corner 
                    (0.0, 1.0, 0.0)), # ur edge 

                   ((1.0, 0.5, 0.0), # lr corner (= C)
                    (1.0, 1.1, 0.0), # lr edge 
                    (1.1, 1.0, 0.0),  # ur edge 
                    (0.5, 1.0, 0.0)) # ur corner (= D)
                   )


    def draw(self,u_steps,v_steps):
        """Draws the window"""
        twColor(self.darkGrey,0.9,0.6)   # lots of reflectivity, like glass
        twDrawBezierSurface(self.cp,u_steps,v_steps,GL_FILL)

        
