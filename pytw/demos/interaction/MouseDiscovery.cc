/* A bunch of mouse callbacks that just report the event in the window.

Implemented Fall 2005
Scott D. Anderson
*/

#include <stdio.h>
#include <stdlib.h>             // for exit
#include <tw.h>

char keytext[255]; // buffer for putting key/button information for display
char motiontext[255]; // buffer for putting mouse motion information for display

void display(void) {
    twDisplayInit();
    twCamera();
    
    twTriple sides = {1,0,0};   // red
    twTriple ends  = {0,0,1};   // blue
    twTriple roof  = {0,1,0};   // green

    twSolidBarn(ends,sides,roof);

    twColorName(TW_BLACK);
    twDrawString(-0.05,-0.05,0.05,keytext);
    twDrawString(-0.05,-0.10,0.05,motiontext);

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

char* buttonNames[3];
char* buttonStates[2];

void initButtonNames() {
    buttonNames[GLUT_LEFT_BUTTON] = "GLUT_LEFT_BUTTON";
    buttonNames[GLUT_MIDDLE_BUTTON] = "GLUT_MIDDLE_BUTTON";
    buttonNames[GLUT_RIGHT_BUTTON] = "GLUT_RIGHT_BUTTON";
    buttonStates[GLUT_DOWN] = "GLUT_DOWN";
    buttonStates[GLUT_UP] = "GLUT_UP";
}

void mouseClick(int button, int state, int x, int y) {
    sprintf(keytext,"%s %s %d %d",
            buttonNames[button],
            buttonStates[state],
            x,y);
    glutPostRedisplay();
}          

void mouseDrags(int x, int y) {
    sprintf(motiontext,"mouse moves to %d %d",x,y);
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
    glutDetachMenu(GLUT_RIGHT_BUTTON);
   
    initButtonNames();
    glutKeyboardFunc(normalKeys);
    glutMouseFunc(mouseClick);
    glutMotionFunc(mouseDrags);
    // glutPassiveMotionFunc(mouseMoves);
    glutMainLoop();
    return 0;
}
