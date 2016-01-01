/* Tutor intended to demonstrate the basics of vectors. 
Based on lightmaterial tutorial by Nate Robins.

The squares are all at different depths.  They are drawn, however, with
the Depth Mask being false, so the depth buffer is not updated.

Written by Caroline Geiersbach and Scott D. Anderson
scott.anderson@acm.org
Summer 2003    
*/

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <string.h>
#include "tw.h"

bool BackToFront = true;

#define GAP  25      /* gap between subwindows */
int wWinWidth=500;  //world window width
int wWinHeight=500; //world window height 
int cWinWidth=400;  //command window width
int cWinHeight=500;  //command window height
GLfloat cosAngle,angle;  

//cells are used in the command window; each cell has an id; a
//raster location at x,y; min and max values; a current value; the 
//step for adjusting values; info on what the cell specifies; and
//finally the format of the printed values.
typedef struct _cell {
    int id;
    int x, y;
    float min, max;
    float value;
    float step;
    char* info;
    char* format;
} cell;

cell topSquare [4] = {
    {1,100,140,0,1,1.0,0.05,
     "Red color component of the top square", "%.2f"},
    {2,160,140,0,1,0,0.05,
     "Green color component of the top square", "%.2f"},
    {3,220,140,0,1,0,0.05,
     "Blue color component of the top square", "%.2f"},  
    {4,280,140,0,1,0.75,0.05,
     "Alpha component of the top square", "%.2f"},  
};

cell midSquare [4] = {
    {5,100,220,0,1,0,0.05,
     "Red color component of the middle square", "%.2f"},
    {6,160,220,0,1,1,0.05,
     "Green color component of the middle square", "%.2f"},
    {7,220,220,0,1,0,0.05,
     "Blue color component of the middle square", "%.2f"},  
    {8,280,220,0,1,0.75,0.05,
     "Alpha component of the middle square", "%.2f"},  
};

cell bottomSquare [4] = {
    {9,100,300,0,1,0,0.05,
     "Red color component of the bottom square", "%.2f"},
    {10,160,300,0,1,0,0.05,
     "Green color component of the bottom square", "%.2f"},
    {11,220,300,0,1,1,0.05,
     "Blue color component of the bottom square", "%.2f"},
    {12,280,300,0,1,0.75,0.05,
     "Alpha component of the bottom square", "%.2f"}  
};

GLint selection = 0; // no cell selected
int old_y; //for command mouse

void redisplayAll(void);
GLuint window, world, screen, command;
GLuint sub_width = 256, sub_height = 256;

void cellDraw(cell* cell) {
    glColor3f(1,1,1); //color of unselected numbers
    if (selection == cell->id) {
      glColor3f(0,1,1); // color of info text
      twDrawString(10, 20,cell->info);
    }
    twDrawString(cell->x, cell->y, cell->format, cell->value);
}

//returns cell id if cell has been clicked on; 0 otherwise
int cellHit(cell* cell, int x, int y) {
    if (x > cell->x && x < cell->x + 70 &&
        y > cell->y-30 && y < cell->y+10){
        return cell->id;
    }
    return 0;
}

//updates the cell's value
void cellUpdate(cell* cell, int update) {
    if (selection != cell->id)
        return;
    cell->value += update * cell->step;
    //tests for min and max values of the points
    if (cell->value < cell->min)
        cell->value = cell->min;
    else if (cell->value > cell->max) 
        cell->value = cell->max;
}

void mainDisplay() {
    glClearColor(0.7, 0.7, 1, 0); //light blue background
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glutSwapBuffers();
}

//draws a square with the color (red, green, blue, alpha) with its left
//lower corner at the origin.
void drawSquare(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha) {
    glColor4f(red, green, blue, alpha);
    glBegin(GL_POLYGON);
    glVertex3f(0,0,0);
    glVertex3f(2,0,0);
    glVertex3f(2,2,0);
    glVertex3f(0,2,0);
    glEnd();
}

void drawBottomSquare() {
    glPushMatrix();
    glTranslatef(-1.5,-1.5,0);
    drawSquare(bottomSquare[0].value,
	       bottomSquare[1].value, 
	       bottomSquare[2].value,
	       bottomSquare[3].value);
    glPopMatrix();
}

void drawMiddleSquare() {
    glPushMatrix();
    glTranslatef(-1.0,-1.0,0.1);
    drawSquare(midSquare[0].value,
	       midSquare[1].value,
	       midSquare[2].value,
	       midSquare[3].value);
    glPopMatrix();
}

void drawTopSquare() {
    glPushMatrix();
    glTranslatef(-0.5,-1.5,0.1);
    drawSquare(topSquare[0].value,
	       topSquare[1].value,
	       topSquare[2].value,
	       topSquare[3].value);
    glPopMatrix();
}

void worldDisplay() {
    twCamera();
    glClearColor(0,0,0,0); //clear sub-window to black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glDepthMask(GL_FALSE);
    
    if(BackToFront) {
        //draw squares back to front, as we ought because depth mask is false.
	drawBottomSquare();
	drawMiddleSquare();
	drawTopSquare();
        twColorName(TW_WHITE);
        twDrawString(-2,-2,0,"drawn back to front");
    } else {
        //draw backwards
	drawTopSquare();
	drawMiddleSquare();
	drawBottomSquare();
        twColorName(TW_WHITE);
        twDrawString(-2,-2,0,"drawn front to back");
    }

    glFlush();
    glutSwapBuffers(); 
}

//display for the command sub-window; this is where user can adjust
//where points are located.
void commandDisplay() {
    //camera setup
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0, cWinWidth, cWinHeight, 0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glClearColor(0,0,0,1); //clear screen to black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glColor3f(topSquare[0].value,topSquare[1].value,topSquare[2].value); 
    twSetFont("helvetica",18);
    twDrawString(10,100,"TOP SQUARE:");
    glColor3f(1,1,1);
    twDrawString(10,140, "glColor4f(");
    twDrawString(topSquare[0].x+50,topSquare[0].y,",");
    twDrawString(topSquare[1].x+50,topSquare[1].y,",");
    twDrawString(topSquare[2].x+50,topSquare[2].y,",");
    twDrawString(topSquare[3].x+50,topSquare[3].y,")");

    glColor3f(midSquare[0].value,midSquare[1].value,midSquare[2].value);
    twDrawString(10,180,"MIDDLE SQUARE:");
    glColor3f(1,1,1);
    twDrawString(10,220,"glColor4f(");
    twDrawString(midSquare[0].x+50,midSquare[0].y,",");
    twDrawString(midSquare[1].x+50,midSquare[1].y,",");
    twDrawString(midSquare[2].x+50,midSquare[2].y,",");
    twDrawString(midSquare[3].x+50,midSquare[3].y,")");

    glColor3f(bottomSquare[0].value,bottomSquare[1].value,
              bottomSquare[2].value);
    twDrawString(10,260,"BOTTOM SQUARE:");
    glColor3f(1,1,1);
    twDrawString(10,300,"glColor4f(");
    twDrawString(bottomSquare[0].x+50,bottomSquare[0].y,",");
    twDrawString(bottomSquare[1].x+50,bottomSquare[1].y,",");
    twDrawString(bottomSquare[2].x+50,bottomSquare[2].y,",");
    twDrawString(bottomSquare[3].x+50,bottomSquare[3].y,")");

    cellDraw(&topSquare[0]);
    cellDraw(&topSquare[1]);
    cellDraw(&topSquare[2]);
    cellDraw(&topSquare[3]);
    cellDraw(&midSquare[0]);
    cellDraw(&midSquare[1]);
    cellDraw(&midSquare[2]);
    cellDraw(&midSquare[3]);
    cellDraw(&bottomSquare[0]);
    cellDraw(&bottomSquare[1]);
    cellDraw(&bottomSquare[2]);
    cellDraw(&bottomSquare[3]);
 
    if (selection==0) {
        glColor3f(1,1,1);
        twDrawString(10, 20,
                     "Click on arguments and move mouse to modify values.");
    }   
    //directions at bottom of command window
    twDrawString(10,420, "Hit 'R' to reset adjustable to original values.");
    twDrawString(10,450, "Hit 'O' to switch front-to-back ordering");
    twColorName(TW_WHITE);
    glutSwapBuffers();
}

void commandMouse(int button, int state, int x, int y) {
    selection = 0;
    if (state == GLUT_DOWN) {
    /* mouse should only hit _one_ of the cells, so adding up all
        the hits just propagates a single hit. */
      selection += cellHit(&topSquare[0], x, y);
      selection += cellHit(&topSquare[1], x, y);
      selection += cellHit(&topSquare[2], x, y);
      selection += cellHit(&topSquare[3], x, y);
      selection += cellHit(&midSquare[0], x, y);
      selection += cellHit(&midSquare[1], x, y);
      selection += cellHit(&midSquare[2], x, y);
      selection += cellHit(&midSquare[3], x, y);
      selection += cellHit(&bottomSquare[0], x, y);
      selection += cellHit(&bottomSquare[1], x, y);
      selection += cellHit(&bottomSquare[2], x, y);
      selection += cellHit(&bottomSquare[3], x, y);
    }
    old_y = y;
    redisplayAll();
}

void commandMotion(int x, int y) {
    cellUpdate(&topSquare[0],old_y-y);
    cellUpdate(&topSquare[1],old_y-y);
    cellUpdate(&topSquare[2],old_y-y);
    cellUpdate(&topSquare[3],old_y-y);
    cellUpdate(&midSquare[0],old_y-y);
    cellUpdate(&midSquare[1],old_y-y);
    cellUpdate(&midSquare[2],old_y-y);
    cellUpdate(&midSquare[3],old_y-y);
    cellUpdate(&bottomSquare[0],old_y-y);
    cellUpdate(&bottomSquare[1],old_y-y);
    cellUpdate(&bottomSquare[2],old_y-y);    
    cellUpdate(&bottomSquare[3],old_y-y);    
    old_y = y;
    redisplayAll();
}

//resets the values of the points and vectors to the original settings
void reinitializeValues(unsigned char key, int x, int y) { 
    topSquare[0].value=1;
    topSquare[1].value=0;
    topSquare[2].value=0;
    topSquare[3].value=0.75;
    midSquare[0].value=0;
    midSquare[1].value=1;
    midSquare[2].value=0;
    midSquare[3].value=0.75;
    bottomSquare[0].value=0;
    bottomSquare[1].value=0;
    bottomSquare[2].value=1;
    bottomSquare[3].value=0.75;
    redisplayAll();
}

void reorder(unsigned char, int, int) {
    BackToFront = !BackToFront;
    redisplayAll();
}

void keyInit () {
  twKeyCallback('R',reinitializeValues,"Resets all point and vector values");
  twKeyCallback('O',reorder,"Switches front-to-back ordering");
}

void redisplayAll(void) {
    glutSetWindow(command);
    glutPostRedisplay();
    glutSetWindow(world);
    glutPostRedisplay();
}

void myInit() {
    twBoundingBox(-1,1,-1,1,-1,1);
    twMainInit();
    
    keyInit();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_RGBA | GLUT_ALPHA | GLUT_DEPTH | GLUT_DOUBLE);

    glutInitWindowSize(wWinWidth+cWinWidth+GAP*3, 
                       wWinHeight+GAP*2); //parent window
    glutInitWindowPosition(0, 0); //position on computer screen
    
    window = glutCreateWindow("Transparency Tutor"); //parent window's name
    glutDisplayFunc(mainDisplay);
    myInit();

    /*glutCreateSubWindow returns the ID of the sub-window and takes 
      arguments:(int parent,int x,int y,int width,int height).
      Origin at x,y; height equals distance from y _down_ */
 
    //create sub-window "command" for adjusting values
    command=glutCreateSubWindow(window,GAP*2+wWinWidth,GAP,
                                cWinWidth,cWinHeight);
    glutDisplayFunc(commandDisplay);
    myInit();
    glutMotionFunc(commandMotion);
    glutMouseFunc(commandMouse);

    //create sub-window "world" for drawing vectors
    world=glutCreateSubWindow(window,GAP,GAP,wWinWidth,wWinHeight);
    /*Each time you create a new window you need to give it its own 
      callbacks and initialization. These can be the same as those
      from other windows but you must call them each time*/
    glutDisplayFunc(worldDisplay);
    myInit();
    
    glEnable(GL_DEPTH_TEST);
    glEnable(GL_NORMALIZE);
    glDepthFunc(GL_LEQUAL); 

    redisplayAll(); 
    glutMainLoop();
    return 0;
}
