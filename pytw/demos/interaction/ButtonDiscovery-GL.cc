/* Demo of joystick input

Implemented Fall 2005
Scott D. Anderson
*/

#include <stdio.h>
// This program doesn't actually use TW, but tw.h includes the GL header files
#include <tw.h>

void display(void) {
    glClearColor(0.7,0.7,0.7,1);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    
    glutWireCube(1);

    glFlush();
    glutSwapBuffers();
}

void joystickButtons(unsigned int button, int x, int y, int z) {
    if(button == 0) return;
    printf("joystick button key %d at %d %d %d\n", button, x, y, z);
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(500,500);
    glutCreateWindow(argv[0]);
    glutDisplayFunc(display);
    glutJoystickFunc(joystickButtons,5);
    glutMainLoop();
    return 0;
}
