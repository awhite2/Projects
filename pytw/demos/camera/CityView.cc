/* Demo of perspective. Callbacks to modify fovy, near and far.  

Implemented Summer 2003
Scott D. Anderson and Caroline Geiersbach
*/

#include <stdio.h>
#include <tw.h>

/* variables for gluPerspective */
GLfloat myFovy;
GLfloat myAspectRatio = 1;
GLfloat myNear;
GLfloat myFar;

void setCamera() {
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(myFovy,myAspectRatio,myNear,myFar);
    twCameraPosition(); 
}

/* Allows the user to pick a color (arg 1), translate the building to
the desired location x,y,and z locations (args 2-4), and scale the 
object (args 5-7)*/
void drawBuilding(int i, GLfloat xPos, GLfloat yPos, GLfloat zPos,
                   GLfloat xScale, GLfloat yScale, GLfloat zScale) {
  glPushMatrix();
  twColorName(i);
  glTranslatef(xPos,yScale/2+yPos,zPos);// y transl.affected by scaling
  glScalef(xScale,yScale,zScale); // scales from center of glutWireCube
  glutSolidCube(1);
  glPopMatrix();
}
                
void display(void) {
    twDisplayInit();
    setCamera();
    //twCamera();
 
    twColorName(TW_GREEN);
    twGround();

    /* draw buildings */
    drawBuilding(TW_MAGENTA,-5,0,-20,10,20,10);
    drawBuilding(TW_OLIVE,-20,0,-20,15,45,15);
    drawBuilding(TW_PURPLE,-40,0,-20,10,20,10);
    drawBuilding(TW_RED,10,0,-20,15,60,10);
    drawBuilding(TW_ORANGE,50,0,-20,10,40,20);
    drawBuilding(TW_MAROON,30,0,-20,10,50,10);
    drawBuilding(TW_BLUE,-60,0,-20,8,40,8);

    /* done */
    glFlush();
    glutSwapBuffers();
}

/* Specify functions for each key */
void myCamSettings (unsigned char key, int x, int y) {
    switch (key) {
    case '+': myFovy++; glutPostRedisplay(); break;
    case '-': myFovy--; glutPostRedisplay(); break;
    case 'n': myNear--; glutPostRedisplay(); break;
    case 'N': myNear++; glutPostRedisplay(); break;
    case 'f': myFar--;  glutPostRedisplay(); break;
    case 'F': myFar++;  glutPostRedisplay(); break;
    }
}

void printCamSettings(unsigned char key, int x, int y) {
    printf("near=%f, far=%f, fovy=%f\n",myNear,myFar,myFovy);
}

void initVals () {
    twNearFarSet(myNear,myFar); 
    twFovySet(myFovy);
}

void myReset(unsigned char key, int x, int y) {
    initVals();
    twReset(key, x, y);
}

/* Initialize new key settings */
void keyInit () {  
    twKeyCallback('+', myCamSettings, "Increase the field of view angle by 1");
    twKeyCallback('-', myCamSettings, "Decrease the field of view angle by 1");
    twKeyCallback('n', myCamSettings, "Decrease near value by 1");
    twKeyCallback('N', myCamSettings, "Increase near value by 1");
    twKeyCallback('f', myCamSettings, "Decrease far value by 1");
    twKeyCallback('F', myCamSettings, "Increase far value by 1");
    twKeyCallback('r', myReset, "Reset to original screen");
    twKeyCallback('=', printCamSettings, "print camera settings");
}

int main(int argc, char** argv) {
    glutInit(&argc,argv);
    glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH );
    twInitWindowSize(500, 500);
    glutCreateWindow(argv[0]);
    glutDisplayFunc(display);   
    twBoundingBox(-50,50,0,60,-50,50);
    twMainInit();                // calculate near and far 
    initVals();
    keyInit();       
    glutMainLoop();
    return 0;
}
