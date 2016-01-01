""" Builds several barns, with different materials.  Added an overhead
   light source, to produce shading.  Allows the user to walk around in
   the scene by clicking the mouse.

Scott D. Anderson
Fall 2000
ported to Python and TW 2009
"""

import sys
import math # for tan, atan

try:
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
        '''

### ================================================================

""" ================================================================
   code for frustum etc.  In this program, we size the viewport to
   the whole window, compute the gluPerspective parameters from the
   viewport, and finally compute the width and height of the image
   rectangle from the gluPerspective parameters.  The last
   parameters are important because they're used in the navigation.

   everything has the same aspect ratio (width/height): window,
   viewport, and image_rectangle, so we just need the aspect_ratio
   parameter and the heights.  To get widths, just multiply the
   height by the aspect ratio. 
"""

aspect_ratio = None

# This is the height of the window, in pixels 

window_height=400
window_width=600

# Initialize the fovy to always be 90 degrees. In fact, we never
#   change it, but we could.

fovy=90
near=10
far=1000

# the dimensions of the top of the frustum, in world coordinates
image_rectangle_height = None
image_rectangle_width  = None

# The reshape callback is executed whenever the window changes size.
def myReshape(w, h):
    """ The math here is a simple mapping from window coordinates
       (pixels) to world coordinates.  The height of the image
       rectangle is proportional to the height of the window, and
       the ratio of half the image height to near equals the
       tangent of the field of view angle.

       tan(fovy/2) = (irh/2)/near

       Solve that for irh.  Remember that we have to deal with
       degrees and radians as well.
    """
    global aspect_ratio, window_width, window_height
    global image_rectangle_width, image_rectangle_height
    aspect_ratio = float(w)/float(h)
    window_width=w
    window_height=h
    # use the whole window as the viewport
    glViewport(0,0,w,h)
    # set up the camera again, using new aspect ratio
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(fovy,aspect_ratio,near,far);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    # dimensions of top of frustum, in world units
    # the height is actually a constant, and the width varies by the
    # aspect ratio of the window
    image_rectangle_height = 2*near*math.tan(fovy*((M_PI/180)/2));
    image_rectangle_width = image_rectangle_height*aspect_ratio;

def cameraDrawing():
    '''Draws stuff in the camera frame, as if on the lens of the camera

The following code will put in our viewport and the cross-hairs.
We're still in a coordinate system where the camera is at the
origin and the image rectangle is centered about the negative z
axis at a distance of near. '''
    glDisable(GL_LIGHTING)
    glColor3f(0,0,0);

    # This "if" statement allows me to easily disable this code, by just
    # changing the True to False
    if True:
        # This draws the box at the edge of the window
        glBegin(GL_LINE_LOOP);
        irw=image_rectangle_width/2;
        irh=image_rectangle_height/2;
        glVertex3f(-irw,-irh,-near-1);
        glVertex3f(+irw,-irh,-near-1);
        glVertex3f(+irw,+irh,-near-1);
        glVertex3f(-irw,+irh,-near-1);
        glEnd();
    # this draws the cross hairs
    glBegin(GL_LINES);
    cx=image_rectangle_width/2;
    cy=image_rectangle_height/2;
    glVertex3f(-cx,0,-near-1);
    glVertex3f(+cx,0,-near-1);
    glVertex3f(0,-cy,-near-1);
    glVertex3f(0,+cy,-near-1);
    glEnd();
    


""" The first is the view reference point (VRP), which is the same as the
eye location for the gluLookAt function.  The second is the view plane
normal (VPN).  The VRP is modified by moving forward and backward in the
scene.  The VPN is modified by turning left and right. 
"""

VRP = [300,20,0]
VPN = [-1,0,-1]

def place_camera():
    gluLookAt(VRP[0],VRP[1],VRP[2],
              VRP[0]+VPN[0],VRP[1]+VPN[1],VRP[2]+VPN[2],
              0,1,0)
    
def sun():
    twAmbient(0.2)
    twGrayLight(GL_LIGHT0, (-5,5,5,0), 0.1, 1.0, 0.4)
    glEnable(GL_LIGHTING);


def drawTown():
    walls = (1,0.8,0.8)   # reddish
    roof  = (0.2,0.1,0.3)   # dark
    sides = walls
    ends = walls

    glPushMatrix()
    glTranslatef(100,0,-200)
    glScalef(50,60,50)
    twSolidBarn(ends,sides,roof);
    glPopMatrix()

    glPushMatrix();
    glTranslatef(200,0,-200);
    glRotatef(-30,0,1,0);
    glScalef(80,80,100)
    twSolidBarn(ends,sides,roof);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(180,0,-100);
    glRotatef(180,0,1,0);
    glScalef(60,70,70)
    twSolidBarn(ends,sides,roof);
    glPopMatrix();


def drawGround():
    # Mark the ground in a dark green, no specularity
    twColor((0,0.5,0),0,0)
    glBegin(GL_POLYGON);
    glVertex3i(0,0,0);
    glVertex3i(400,0,0);
    glVertex3i(400,0,-400);
    glVertex3i(0,0,-400);
    glEnd();


def display():
    glPushAttrib(GL_ALL_ATTRIB_BITS);
    glClearColor(1,1,1,1);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    cameraDrawing()
    glPushMatrix();             # enter town frame
    # At this point, the camera moves to a new location, in town frame
    place_camera();
    sun()
    drawGround()
    drawTown()
    
    glPopMatrix();              # leave town frame
    glFlush();
    glutSwapBuffers();
    glPopAttrib();

def motion(mx,my):
    # convert to first quadrant
    my=window_height-my;
    # measure from center
    mx=mx-(window_width/2);
    my=my-(window_height/2);
    """ Figure out what angle to rotate.  This computation is based
       on the fact that the tangent of the angle of rotation equals
       x/near, after x has been scaled to image_rectangle
       units. That scaling is easy, because:

       x : window_width :: ix : image_rectangle_width

       Solve that for ix. """

    ix = (image_rectangle_width*mx)/window_width;
    # Now, do the rotation of the view plane normal (VPN) 
    theta=-math.atan(ix/near);       # flip the sign

    global VPN, VRP

    # temporary values 
    x = VPN[0];
    z = VPN[2];
    # for efficiency and brevity, compute these once
    c = math.cos(theta)
    s = math.sin(theta)

    VPN[0] =  x*c+z*s;
    VPN[2] = -x*s+z*c;

    """Now, move forward, if necessary. The math here is simpler;
       we just move forward by an amount proportional to the
       distance above the midline.  """

    factor=(20.0*my)/window_height;
    VRP[0] += factor*VPN[0];
    VRP[2] += factor*VPN[2];
    glutPostRedisplay();

def mouse(btn, state, mx, my):
    if not (btn==GLUT_LEFT_BUTTON and state==GLUT_DOWN):
        return
    # same a the motion function
    motion(mx,my)

def key(k, x, y):
    if k == 'q':
        exit(0);
    glutPostRedisplay();

# ================================================================

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twInitWindowSize(window_width,window_height)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
#    glEnable(GL_NORMALIZE)      # twMainInit does this
    twBoundingBox(0,1,0,1,0,1)   # fake, just to avoid complaints
    twMainInit()
    myReshape(window_width,window_height)
    glutReshapeFunc(myReshape);
    glutKeyboardFunc(key);
    glutMouseFunc(mouse);
    glutMotionFunc(motion);
#    glEnable(GL_DEPTH_TEST);    # twMainInit does this
    glutMainLoop();

if __name__ == '__main__':
    main()
