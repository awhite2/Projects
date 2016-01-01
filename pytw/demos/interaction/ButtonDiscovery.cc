/* A bunch of keyboard callbacks that just report the code for the key
   that was struck.

Implemented Fall 2005
Scott D. Anderson
*/

#include <stdio.h>
#include <stdlib.h>             // for exit
#include <tw.h>

char keytext[255];              // buffer for putting key/button information for display

void display(void) {
    twDisplayInit();
    twCamera();
    
    twTriple sides = {1,0,0};   // red
    twTriple ends  = {0,0,1};   // blue
    twTriple roof  = {0,1,0};   // green

    twSolidBarn(ends,sides,roof);

    twColorName(TW_BLACK);
    twDrawString(-0.05,-0.05,0.05,keytext);

    glFlush();
    glutSwapBuffers();
}

void normalKeys(unsigned char k, int x, int y) {
    sprintf(keytext,"normal key = %c (%d) x = %d y = %d",k,k,x,y);
    if(k=='q') {
        exit(0);
    }
    glutPostRedisplay();
}

char* specialKeyNames[120];

void initSpecialKeyNames() {
    specialKeyNames[ GLUT_KEY_F1 ] = "GLUT_KEY_F1";
    specialKeyNames[ GLUT_KEY_F2 ] = "GLUT_KEY_F2";
    specialKeyNames[ GLUT_KEY_F3 ] = "GLUT_KEY_F3";
    specialKeyNames[ GLUT_KEY_F4 ] = "GLUT_KEY_F4";
    specialKeyNames[ GLUT_KEY_F5 ] = "GLUT_KEY_F5";
    specialKeyNames[ GLUT_KEY_F6 ] = "GLUT_KEY_F6";
    specialKeyNames[ GLUT_KEY_F7 ] = "GLUT_KEY_F7";
    specialKeyNames[ GLUT_KEY_F8 ] = "GLUT_KEY_F8";
    specialKeyNames[ GLUT_KEY_F9 ] = "GLUT_KEY_F9";
    specialKeyNames[ GLUT_KEY_F10 ] = "GLUT_KEY_F10";
    specialKeyNames[ GLUT_KEY_F11 ] = "GLUT_KEY_F11";
    specialKeyNames[ GLUT_KEY_F12 ] = "GLUT_KEY_F12";
    specialKeyNames[ GLUT_KEY_LEFT ] = "GLUT_KEY_LEFT";
    specialKeyNames[ GLUT_KEY_UP ] = "GLUT_KEY_UP";
    specialKeyNames[ GLUT_KEY_RIGHT ] = "GLUT_KEY_RIGHT";
    specialKeyNames[ GLUT_KEY_DOWN ] = "GLUT_KEY_DOWN";
    specialKeyNames[ GLUT_KEY_PAGE_UP ] = "GLUT_KEY_PAGE_UP";
    specialKeyNames[ GLUT_KEY_PAGE_DOWN ] = "GLUT_KEY_PAGE_DOWN";
    specialKeyNames[ GLUT_KEY_HOME ] = "GLUT_KEY_HOME";
    specialKeyNames[ GLUT_KEY_END ] = "GLUT_KEY_END";
    specialKeyNames[ GLUT_KEY_INSERT ] = "GLUT_KEY_INSERT";
}    

void specialKeys(int key, int x, int y) {
    sprintf(keytext,
            "special key %s (%d) at %d %d",
            specialKeyNames[key], key, x, y);
    glutPostRedisplay();
}

char* joystickButtonNames[20];

void initJoystickButtonNames() {
    joystickButtonNames[ GLUT_JOYSTICK_BUTTON_A ] = "GLUT_JOYSTICK_BUTTON_A";
    joystickButtonNames[ GLUT_JOYSTICK_BUTTON_B ] = "GLUT_JOYSTICK_BUTTON_B";
    joystickButtonNames[ GLUT_JOYSTICK_BUTTON_C ] = "GLUT_JOYSTICK_BUTTON_C";
    joystickButtonNames[ GLUT_JOYSTICK_BUTTON_D ] = "GLUT_JOYSTICK_BUTTON_D";
}

void joystickButtons(unsigned int button, int x, int y, int z) {
    if(button == 0) return;
    sprintf(keytext,
            "joystick button key %s (%d) at %d %d %d",
            joystickButtonNames[button], button, x, y, z);
    glutPostRedisplay();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    twInitWindowSize(500,500);
    glutCreateWindow(argv[0]);
    glutDisplayFunc(display);
    twBoundingBox(0,1,0,1,-1,0);
    twMainInit();            
    initSpecialKeyNames();
    initJoystickButtonNames();
    glutKeyboardFunc(normalKeys);
    glutSpecialFunc(specialKeys);
    glutJoystickFunc(joystickButtons,5);
    glutMainLoop();
    return 0;
}
