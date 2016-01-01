"""Prints out the limits of the current OpenGL implementation.

Yes, you need to create a window in order to get the proper results from
glGet*; if you don't, you'll get huge values that change each time.

Implemented Fall 2003
Scott D. Anderson
Ported to Python Fall 2009
"""

try:
    from TW import *
except:
    print '''
ERROR: Couldn't import TW.
        '''

### ================================================================

def report(type, name, value):
    """Print the limit specified by symbolic constant 'value' with text 'name'.  

type is either 'f' or 'i' for float or integer."""
    if type=='f':
        floatv = glGetFloatv(value);
        print "%s is %f" % (name,floatv)
    elif type == 'i':
        intv = glGetIntegerv(value)
        print "%s is %d" % (name,intv)


# a dummy display function
def display():
    pass

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_ALPHA | GLUT_DEPTH | GLUT_ACCUM);
    twInitWindowSize(50,50)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    report('i',"GL_MAX_LIGHTS",GL_MAX_LIGHTS);

    print "Depth of Frame Buffer"
    report('i',"GL_RED_BITS",GL_RED_BITS);
    report('i',"GL_GREEN_BITS",GL_GREEN_BITS);
    report('i',"GL_BLUE_BITS",GL_BLUE_BITS);
    report('i',"GL_ALPHA_BITS",GL_ALPHA_BITS);

    print "Depth of Depth Buffer"
    report('i',"GL_DEPTH_BITS",GL_DEPTH_BITS);

    print "Depth of Accumulation Buffer"
    report('i',"GL_ACCUM_RED_BITS",GL_ACCUM_RED_BITS);
    report('i',"GL_ACCUM_GREEN_BITS",GL_ACCUM_GREEN_BITS);
    report('i',"GL_ACCUM_BLUE_BITS",GL_ACCUM_BLUE_BITS);
    report('i',"GL_ACCUM_ALPHA_BITS",GL_ACCUM_ALPHA_BITS);

    print "Evaluators"
    report('i',"GL_MAX_EVAL_ORDER",GL_MAX_EVAL_ORDER);

if __name__ == '__main__':
    main()
