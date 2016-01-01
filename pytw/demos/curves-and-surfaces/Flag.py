""" Simple flag surface.  Just an object, not a standalone program.

   Scott D. Anderson
   Fall 2000 original version
   Fall 2003 adapted to use TW
   Fall 2009 ported to Python
"""

try:
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
        '''

### ================================================================

class Flag():
    """flag in a unit box, origin at lower left (not idea)"""
    def __init__(self):
        self.cp = (
                   ((0.0, 0.0, 0.0), # ll corner (= A)
                    (0.1, 0.2, 0.0), # ll edge 
                    (0.1, 0.8, 0.0), # ul edge 
                    (0.0, 1.0, 0.0)), # ul corner (= B)

                   ((0.2, 0.1, 0.2), # ll edge, curving forward 
                    (0.2, 0.2, 0.2), # ll interior corner 
                    (0.2, 0.8, 0.1), # ul interior corner 
                    (0.2, 0.9, 0.1)), # top left edge 

                   ((0.8, 0.2, -0.2), # lr edge, curving forward from behind 
                    (0.8, 0.2, -0.1), # lr interior corner 
                    (0.7, 0.8, -0.1), # ur interior corner 
                    (0.7, 0.9,  0.0)), # ur edge 

                   ((0.9, 0.3, 0.0), # lr corner (= C)
                    (0.8, 0.4, -0.1), # lr edge 
                    (0.8, 0.8, 0.0),  # ur edge 
                    (0.9, 0.9, -0.1)) # ur corner (= D)
                   )
        self.tcp = (((0,0.8125), # corresponds to vertex A
                     (0,0)),     # corresponds to vertex B
                    
                    ((0.77,0.8125), # corresponds to vertex C
                     (0.77,0)))     # corresponds to vertex D
        self.tid = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D,self.tid)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glPixelStorei(GL_UNPACK_ALIGNMENT,1)
        twUSFlag()

    def draw(self,u_steps,v_steps,Wire,ShowCP):
        """Draws the flag, possibly wireframe, possibly with control points"""
        twDrawBezierSurface(self.cp,u_steps,v_steps,GL_LINE if Wire else GL_FILL)
        if ShowCP:
            twDrawBezierControlPoints(self.cp)

    def drawTextured(self,u_steps,v_steps,Wire,ShowCP):
        """Draws the flag, possibly wireframe, possibly with control points"""
        twDrawBezierSurfaceTextured(self.cp,self.tcp,u_steps,v_steps,GL_LINE if Wire else GL_FILL)
        if ShowCP:
            twDrawBezierControlPoints(self.cp)

