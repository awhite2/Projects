from TW import *

def fog(kind):
    glEnable(GL_FOG)
    fogColor=(0.3,0.3,0.3,1)
    glFogfv(GL_FOG_COLOR,fogColor)
    glHint(GL_FOG_HINT,GL_NICEST)
    if kind == 0:
        glDisable(GL_FOG);
    elif kind == 1:
        glFogi(GL_FOG_MODE, GL_LINEAR)
        glFogf(GL_FOG_START, 10)
        glFogf(GL_FOG_END, 60)
    elif kind == 2:
        glFogi(GL_FOG_MODE, GL_EXP);
        glFogf(GL_FOG_DENSITY, 0.01);
    elif kind == 3:
        glFogi(GL_FOG_MODE, GL_EXP2);
        glFogf(GL_FOG_DENSITY, 0.01);


        
