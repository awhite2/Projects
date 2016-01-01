/* Tutor intended to demonstrate the basics of vectors. 
Based on lightmaterial tutorial by Nate Robins.

Written by Caroline Geiersbach and Scott D. Anderson
scott.anderson@acm.org
Summer 2003    
*/

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <string.h>
#include <tw.h>

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

cell pointA [3] = {
    {1,90,60,-100,100,-100,1.0,
     "Specifies the X coordinate of point A", "%.1f"},
    {2,160,60,-100,100,0,1.0,
     "Specifies the Y coordinate of point A", "%.1f"},
    {3,230,60,-100,100,-100,1.0,
     "Specifies the Z coordinate of point A", "%.1f"},  
};

cell pointB [3] = {
    {4,90,100,-100,100,30,1.0,
     "Specifies the X coordinate of point B", "%.1f"},
    {5,160,100,-100,100,30,1.0,
     "Specifies the Y coordinate of point B", "%.1f"},
    {6,230,100,-100,100,0,1.0,
     "Specifies the Z coordinate of point B", "%.1f"},  
};

cell pointC [3] = {
    {7,90,140,-100,100,30,1.0,
     "Specifies the X coordinate of point C", "%.1f"},
    {8,160,140,-100,100,-30,1.0,
     "Specifies the Y coordinate of point C", "%.1f"},
    {9,230,140,-100,100,0,1.0,
     "Specifies the Z coordinate of point C", "%.1f"},  
};

/* We do not need all of the elements in the struct "cell" for 
the vectors, but for the sake of simplicity we use the struct
anyway */
cell vectorV [3] = {
    {10,170,220,-200,200,0,1,
     "Specifies the magnitude in the X direction for B-A", "%.1f"},
    {11,240,220,-200,200,0,1,
     "Specifies the magnitude in the Y direction for B-A", "%.1f"},
    {12,310,220,-200,200,0,1,
     "Specifies the magnitude in the Z direction for B-A", "%.1f"},  
};

cell vectorW [3] = {
    {13,170,260,-200,200,0,1,
     "Specifies the magnitude in the X direction for C-A", "%.1f"},
    {14,240,260,-200,200,0,1,
     "Specifies the magnitude in the Y direction for C-A", "%.1f"},
    {15,310,260,-200,200,0,1,
     "Specifies the magnitude in the Z direction for C-A", "%.1f"},  
};

cell vectorU [3] = { //cross product of v and w
    {16,170,300,-200,200,0,1,
     "Specifies the magnitude in the X direction for C-A", "%.1f"},
    {17,240,300,-200,200,0,1,
     "Specifies the magnitude in the Y direction for C-A", "%.1f"},
    {18,310,300,-200,200,0,1,
     "Specifies the magnitude in the Z direction for C-A", "%.1f"},  
};

twTriple v,w,u;
GLint selection = 0; // no cell selected
int old_y; //for command mouse

void redisplay_all(void);
GLuint window, world, screen, command;
GLuint sub_width = 256, sub_height = 256;

//Defines each x,y,z value of the vectors v and w
void assignVectorValues() {
    vectorV[0].value = pointB[0].value-pointA[0].value;
    vectorV[1].value = pointB[1].value-pointA[1].value;
    vectorV[2].value = pointB[2].value-pointA[2].value;
    vectorW[0].value = pointC[0].value-pointA[0].value;
    vectorW[1].value = pointC[1].value-pointA[1].value;
    vectorW[2].value = pointC[2].value-pointA[2].value;
    twTriple v = {vectorV[0].value, vectorV[1].value, vectorV[2].value};
    twTriple w = {vectorW[0].value, vectorW[1].value, vectorW[2].value};
    twTriple u;
    twCrossProduct(u,v,w);
    twVectorScale(u,u,0.01);     // makes cross product within window bounds
                                 // (unit vector too small to discern)
    vectorU[0].value = u[0];
    vectorU[1].value = u[1];
    vectorU[2].value = u[2];
    cosAngle = twCosAngle(v,w);
    angle = (180/M_PI*acos(twCosAngle(v,w)));
}

void cell_draw(cell* cell) {
    glColor3f(1,1,1); //color of unselected numbers
    if (selection == cell->id) {
      glColor3f(0,1,1); // color of info text
      twDrawString(10, 20,cell->info);
    }
    twDrawString(cell->x, cell->y, cell->format, cell->value);
}

//returns cell id if cell has been clicked on; 0 otherwise
int cell_hit(cell* cell, int x, int y) {
    if (x > cell->x && x < cell->x + 70 &&
        y > cell->y-30 && y < cell->y+10){
        return cell->id;
    }
    return 0;
}

//updates the cell's value
void cell_update(cell* cell, int update) {
    if (selection != cell->id)
        return;
    cell->value += update * cell->step;
    //tests for min and max values of the points
    if (cell->value < cell->min)
        cell->value = cell->min;
    else if (cell->value > cell->max) 
        cell->value = cell->max;
    assignVectorValues();
}

void mainDisplay(void) {
    glClearColor(0.7, 0.7, 1, 0); //light blue background
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glutSwapBuffers();
}

void worldDisplay(void) {
    twCamera();
    glClearColor(0,0,0,1); //clear sub-window to white
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    
    glPushMatrix();
    glLineWidth(1);
    twAxes();

    glPointSize(5);
    glBegin(GL_POINTS);
    glColor3f(1,1,0);                // A in yellow
    glVertex3f(pointA[0].value,pointA[1].value,pointA[2].value);
    glColor3f(1,0,0);                // B in red
    glVertex3f(pointB[0].value,pointB[1].value,pointB[2].value);
    glColor3f(0,0,1);                // C in blue
    glVertex3f(pointC[0].value,pointC[1].value,pointC[2].value);
    glEnd();
    glLineWidth(3);                // fatter lines
    
    //show vector v
    glPushMatrix();
    glColor3f(1,0.5,0);
    glBegin(GL_LINES);
    glVertex3f(pointA[0].value,pointA[1].value,pointA[2].value);
    glVertex3f(pointB[0].value,pointB[1].value,pointB[2].value);
    glEnd();
    //show vector w
    glBegin(GL_LINES);
    glColor3f(0,1,0);
    glVertex3f(pointA[0].value,pointA[1].value,pointA[2].value);
    glVertex3f(pointC[0].value,pointC[1].value,pointC[2].value);
    glEnd();
    //show vector u (v cross w)
    glBegin(GL_LINES);
    glColor3f(1,0.5,0.5);
    glVertex3f(pointA[0].value,pointA[1].value,pointA[2].value);
    glVertex3f(vectorU[0].value+pointA[0].value,vectorU[1].value
               +pointA[1].value,vectorU[2].value+pointA[2].value);
    glEnd();

    glPopMatrix();
    glutSwapBuffers(); 
}

//display for the command sub-window; this is where user can adjust
//where points are located.
void commandDisplay(void) {
    //camera setup
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0, cWinWidth, cWinHeight, 0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glClearColor(0,0,0,1); //clear screen to black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glColor3f(1,1,0); 
    twSetFont("helvetica",18);
    twDrawString(10,60,"point A");
    glColor3f(1,1,1);
    twDrawString(73,60,"=(");
    twDrawString(pointA[0].x+60,pointA[0].y,",");
    twDrawString(pointA[1].x+60,pointA[1].y,",");
    twDrawString(pointA[2].x+60,pointA[2].y,")");
    glColor3f(1,0,0);
    twDrawString(10,100,"point B");
    glColor3f(1,1,1);
    twDrawString(73,100,"=(");
    twDrawString(pointB[0].x+60,pointB[0].y,",");
    twDrawString(pointB[1].x+60,pointB[1].y,",");
    twDrawString(pointB[2].x+60,pointB[2].y,")");
    glColor3f(0,0,1);
    twDrawString(10,140,"point C");
    glColor3f(1,1,1);
    twDrawString(73,140,"=(");
    twDrawString(pointC[0].x+60,pointC[0].y,",");
    twDrawString(pointC[1].x+60,pointC[1].y,",");
    twDrawString(pointC[2].x+60,pointC[2].y,")");
    glColor3f(1,0.5,0);
    twDrawString(10,vectorV[0].y,"vector v");
    glColor3f(1,1,1);
    twDrawString(83,vectorV[0].y,"=(B-A)=(");
    twDrawString(vectorV[0].x+60,vectorV[0].y,",");
    twDrawString(vectorV[1].x+60,vectorV[1].y,",");
    twDrawString(vectorV[2].x+60,vectorV[2].y,")");
    glColor3f(0,1,0);
    twDrawString(10,vectorW[0].y,"vector w");
    glColor3f(1,1,1);
    twDrawString(83,vectorW[0].y,"=(C-A)=(");
    twDrawString(vectorW[0].x+60,vectorW[0].y,",");
    twDrawString(vectorW[1].x+60,vectorW[1].y,",");
    twDrawString(vectorW[2].x+60,vectorW[2].y,")");
    glColor3f(1,0.5,0.5);
    twDrawString(10,vectorU[0].y,"vector u");
    glColor3f(1,1,1); 
    twDrawString(83,vectorU[0].y,"=(vxw)=(");
    twDrawString(vectorU[0].x+60,vectorU[0].y,",");
    twDrawString(vectorU[1].x+60,vectorU[1].y,",");
    twDrawString(vectorU[2].x+60,vectorU[2].y,")");
    glColor3f(1,0,1);
    twDrawString(10,340,"cos(angle) between v and w=%.2f",cosAngle);
    twDrawString(10,380,"angle between v and w=%.2f",angle);

    cell_draw(&pointA[0]);
    cell_draw(&pointA[1]);
    cell_draw(&pointA[2]);
    cell_draw(&pointB[0]);
    cell_draw(&pointB[1]);
    cell_draw(&pointB[2]);
    cell_draw(&pointC[0]);
    cell_draw(&pointC[1]);
    cell_draw(&pointC[2]);
    cell_draw(&vectorV[0]);
    cell_draw(&vectorV[1]);
    cell_draw(&vectorV[2]);
    cell_draw(&vectorW[0]);
    cell_draw(&vectorW[1]);
    cell_draw(&vectorW[2]);
    cell_draw(&vectorU[2]);
    cell_draw(&vectorU[0]);
    cell_draw(&vectorU[1]);
    cell_draw(&vectorU[2]);
 
    if (selection==0) {
        glColor3f(1,1,1);
        twDrawString(10, 20,
                     "Click on arguments and move mouse to modify values.");
    }   
    //directions at bottom of command window
    twDrawString(10,420, "Hit <R> to reset adjustable to original values.");
    twDrawString(10,460, "Hit <r> to reset adjustable to original view.");
    twColorName(TW_WHITE);
    glutSwapBuffers();
}

void commandMouse(int button, int state, int x, int y) {
    selection = 0;
    if (state == GLUT_DOWN) {
    /* mouse should only hit _one_ of the cells, so adding up all
        the hits just propagates a single hit. */
      selection += cell_hit(&pointA[0], x, y);
      selection += cell_hit(&pointA[1], x, y);
      selection += cell_hit(&pointA[2], x, y);
      selection += cell_hit(&pointB[0], x, y);
      selection += cell_hit(&pointB[1], x, y);
      selection += cell_hit(&pointB[2], x, y);
      selection += cell_hit(&pointC[0], x, y);
      selection += cell_hit(&pointC[1], x, y);
      selection += cell_hit(&pointC[2], x, y);
      }
    old_y = y;
    redisplay_all();
}

void commandMotion(int x, int y) {
    cell_update(&pointA[0],old_y-y);
    cell_update(&pointA[1],old_y-y);
    cell_update(&pointA[2],old_y-y);
    cell_update(&pointB[0],old_y-y);
    cell_update(&pointB[1],old_y-y);
    cell_update(&pointB[2],old_y-y);
    cell_update(&pointC[0],old_y-y);
    cell_update(&pointC[1],old_y-y);
    cell_update(&pointC[2],old_y-y);
    cell_update(&vectorV[0],old_y-y);
    cell_update(&vectorV[1],old_y-y);
    cell_update(&vectorV[2],old_y-y);
    cell_update(&vectorW[0],old_y-y);
    cell_update(&vectorW[1],old_y-y);
    cell_update(&vectorW[2],old_y-y);
    
    old_y = y;
    redisplay_all();
}

//resets the values of the points and vectors to the original settings
void reinitializeValues(unsigned char key, int x, int y) { 
    pointA[0].value=-100;
    pointA[1].value=0;
    pointA[2].value=-100;
    pointB[0].value=30;
    pointB[1].value=30;
    pointB[2].value=0;
    pointC[0].value=30;
    pointC[1].value=-30;
    pointC[2].value=0;
    assignVectorValues();
    redisplay_all();
}

void keyInit () {
  twKeyCallback('R',reinitializeValues,"Resets all point and vector values");
}

void redisplay_all(void) {
    glutSetWindow(command);
    glutPostRedisplay();
    glutSetWindow(world);
    glutPostRedisplay();
}

void myInit() {
    twMainInit();
    keyInit();
}

int main(int argc, char** argv) {
    glEnable(GL_DEPTH_TEST);
    glEnable(GL_NORMALIZE);
    glDepthFunc(GL_LEQUAL); 
    
    glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH | GLUT_DOUBLE);
    glutInitWindowSize(wWinWidth+cWinWidth+GAP*3, 
                       wWinHeight+GAP*2); //parent window
    glutInitWindowPosition(0, 0); //position on computer screen
    glutInit(&argc, argv);
    
    window = glutCreateWindow("Vectors"); //parent window's name
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
    twBoundingBox(-100,100,-100,100,-100,100);
    assignVectorValues();
    myInit();
    
    redisplay_all(); 
    glutMainLoop();
    return 0;
}
