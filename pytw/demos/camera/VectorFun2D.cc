/*
  Demo to demonstrate the properties of vectors in 2-dimensional space
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
GLfloat angle = 0;  

//mouseMode = 1: draw vectors in world; mouseMode = 0: tw mouse
GLfloat mouseMode = 1;

//values assigned from the world window
twTriple pointA;
twTriple pointB;
twTriple pointC;

//keeps track of the number of clicks
static int count;

twTriple v,w,u;
GLint selection = 0; // no cell selected

void redisplayAll(void);
GLuint window, world, screen, command;

typedef struct _cell {
    int id;
    int x, y;
    float min, max;
    GLfloat value;
    GLfloat step;
    char* info;
    char* format;
} cell;

//values for the command window
//adjustable point cells
cell pA [3] = {
  {1,90,80,-10,10,0,1.0,
   "Specifies the X coordinate of point A", "%.1f"},
  {2,160,80,-10,10,0,1.0,
   "Specifies the Y coordinate of point A", "%.1f"},
  {3,230,80,-10,10,0,1.0,
   "Specifies the Z coordinate of point A", "%.1f"},  
};

cell pB [3] = {
  {4,90,120,-10,10,0,1.0,
   "Specifies the X coordinate of point B", "%.1f"},
  {5,160,120,-10,10,0,1.0,
   "Specifies the Y coordinate of point B", "%.1f"},
  {6,230,120,-10,10,0,1.0,
   "Specifies the Z coordinate of point B", "%.1f"},  
};

cell pC [3] = {
  {7,90,160,-10,10,0,1.0,
   "Specifies the X coordinate of point C", "%.1f"},
  {8,160,160,-10,10,0,1.0,
   "Specifies the Y coordinate of point C", "%.1f"},
  {9,230,160,-10,10,0,1.0,
   "Specifies the Z coordinate of point C", "%.1f"},  
};

//non-adjustable vector cells
cell vectorAB [3] = {
  {10,130,240,-50,50,0,1,
   "Specifies the magnitude in the X direction for B-A", "%.1f"},
  {11,200,240,-50,50,0,1,
   "Specifies the magnitude in the Y direction for B-A", "%.1f"},
  {12,270,240,-50,50,0,1,
   "Specifies the magnitude in the Z direction for B-A", "%.1f"},  
};

cell vectorAC [3] = {
  {13,130,280,-50,50,0,1,
   "Specifies the magnitude in the X direction for C-A", "%.1f"},
  {14,200,280,-50,50,0,1,
   "Specifies the magnitude in the Y direction for C-A", "%.1f"},
  {15,270,280,-50,50,0,1,
   "Specifies the magnitude in the Z direction for C-A", "%.1f"},  
};

//sets the point values in world to the new values in command
void commandToWorld() {
  pointA[0] = pA[0].value;
  pointA[1] = pA[1].value;
  pointA[2] = pA[2].value;

  pointB[0] = pB[0].value;
  pointB[1] = pB[1].value;
  pointB[2] = pB[2].value;

  pointC[0] = pC[0].value;
  pointC[1] = pC[1].value;
  pointC[2] = pC[2].value;
}

void assignVectorValues() {
  vectorAB[0].value = pB[0].value-pA[0].value; 
  vectorAB[1].value = pB[1].value-pA[1].value;
  vectorAB[2].value = pB[2].value-pA[2].value;

  vectorAC[0].value = pC[0].value-pA[0].value;
  vectorAC[1].value = pC[1].value-pA[1].value;
  vectorAC[2].value = pC[2].value-pA[2].value;

  twTriple v = {vectorAB[0].value, vectorAB[1].value, vectorAB[2].value};
  twTriple w = {vectorAC[0].value, vectorAC[1].value, vectorAC[2].value};
  
  angle = (180/M_PI*acos(twCosAngle(v,w)));
}

void cellDraw(cell* cell) {
  glColor3f(1,1,1); //color of numbers when not selected
  if (selection == cell->id) {
    glColor3f(0,1,1); // color of info text
    twDrawString(10, 20,cell->info);
  }
  twDrawString(cell->x, cell->y, cell->format, cell->value);
}

int cellHit(cell* cell, int x, int y) {
    if (x > cell->x && x < cell->x + 70 &&
        y > cell->y-30 && y < cell->y+10){
        return cell->id;
    }
    return 0;
}

void cellUpdate(cell* cell, int update) {
    
  if (selection != cell->id)
        return;
    cell->value += update * cell->step;
    
    //tests for min and max values of the points
    if (cell->value < cell->min)
        cell->value = cell->min;
    else if (cell->value > cell->max) 
        cell->value = cell->max;

    commandToWorld();
}

void mainDisplay(void) {
    twDisplayInit();
    glutSwapBuffers();
}

//draw vector from point p1 to p2, including arrow
void drawVector(twTriple p1, twTriple p2, int color) {
  twColorName(color);
  glLineWidth(2);
  glBegin(GL_LINES);
  glVertex3f(p1[0], p1[1], p1[2]);
  glVertex3f(p2[0], p2[1], p2[2]);
  glEnd();
  //draw arrow
  glPushMatrix();
  glTranslatef(p2[0], p2[1], p2[2]);
  twTriple u;
  twTriple v = {0,0,-1};
  twTriple w = {p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2]};
  twCrossProduct(u,v,w);
  glRotatef(-90,u[0],u[1],u[2]);
  glutSolidCone(0.5, 1, 20, 20);
  glPopMatrix();
}

void worldDisplay(void) {
  twCamera();
  glClearColor(1,1,1,1); //clear sub-window to white
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
 
  glLineWidth(1);
  twAxes();
  glPointSize(5);

  // switch(count) {
  if(count==1) {
    glBegin(GL_POINTS);
    twColorName(TW_RED);
    glVertex3f(pointA[0], pointA[1], pointA[2]);
    glEnd();
    // break;
  } else if (count==2) {
    glBegin(GL_POINTS);
    twColorName(TW_RED);
    glVertex3f(pointA[0], pointA[1], pointA[2]);
    twColorName(TW_GREEN);
    glVertex3f(pointB[0], pointB[1], pointB[2]);
    glEnd();
    drawVector(pointA, pointB, TW_CYAN);
    //break;
  } else {
    glBegin(GL_POINTS);
    twColorName(TW_RED);
    glVertex3f(pointA[0], pointA[1], pointA[2]);
    twColorName(TW_GREEN);
    glVertex3f(pointB[0], pointB[1], pointB[2]);
    twColorName(TW_BLUE);
    glVertex3f(pointC[0], pointC[1], pointC[2]);
    glEnd();
    drawVector(pointA, pointB, TW_CYAN);
    drawVector(pointA, pointC, TW_ORANGE); 
    //break;
  }
  glutSwapBuffers(); 
}

void worldMouse(int button, int state, int x, int y) {
  if(mouseMode == 0) twMouseFunction(button, state, x, y);
  else {
  y = wWinHeight-y;
  twTriple A, B; //world coordinates (correspond to front & back of frustum)
  twTriple winA = {x,y,0};
  twTriple winB = {x,y,1};
  twUnProject(A,winA);
  twUnProject(B,winB);
  twTriple V;
  twVector(V,B,A);
    
  if (button==GLUT_LEFT_BUTTON && state==GLUT_DOWN) {
    switch(count) {
      case(0):    //the first click is point A, or the middle point
        count++;
        twPointOnLine(pointA, A, V, 0.5);
        pA[0].value = pointA[0]; //set values to cells in command
        pA[1].value = pointA[1];
        pA[2].value = pointA[2];
        twTriplePrint("pointA",pointA);
        break;
      case(1): //the second click is point B
        count++;
        twPointOnLine(pointB, A, V, 0.5);
        pB[0].value = pointB[0]; //set values to cells in command
        pB[1].value = pointB[1];
        pB[2].value = pointB[2];
        twTriplePrint("pointB",pointB);
        break;
      case(2): //the third click is point C
        count++;
        twPointOnLine(pointC, A, V, 0.5);
        pC[0].value = pointC[0]; //set values to cells in command
        pC[1].value = pointC[1];
        pC[2].value = pointC[2];
        twTriplePrint("pointC",pointC);
        break;
    } 
  }
  redisplayAll();
  }
}

//to override the current tw motion func
void worldMotion(int x, int y) {
  if(mouseMode == 0) twMotionFunction(x,y);  
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

    twSetFont("helvetica",18);
    twColorName(TW_RED);

    twDrawString(10,pA[0].y,"point A");
    glColor3f(1,1,1);
    twDrawString(73,pA[0].y,"=(");
    twDrawString(pA[0].x+60,pA[0].y,",");
    twDrawString(pA[1].x+60,pA[1].y,",");
    twDrawString(pA[2].x+60,pA[2].y,")");

    twColorName(TW_GREEN);
    twDrawString(10,pB[0].y,"point B");
    glColor3f(1,1,1);
    twDrawString(73,pB[0].y,"=(");
    twDrawString(pB[0].x+60,pB[0].y,",");
    twDrawString(pB[1].x+60,pB[1].y,",");
    twDrawString(pB[2].x+60,pB[2].y,")");

    twColorName(TW_BLUE);
    twDrawString(10,pC[0].y,"point C");
    glColor3f(1,1,1);
    twDrawString(73,pC[0].y,"=(");
    twDrawString(pC[0].x+60,pC[0].y,",");
    twDrawString(pC[1].x+60,pC[1].y,",");
    twDrawString(pC[2].x+60,pC[2].y,")");
    
    //non-adjustable cells
    twColorName(TW_CYAN);
    twDrawString(10,vectorAB[0].y,"vector AB = (");
    twDrawString(vectorAB[0].x+60,vectorAB[0].y,",");
    twDrawString(vectorAB[1].x+60,vectorAB[1].y,",");
    twDrawString(vectorAB[2].x+60,vectorAB[2].y,")");

    twColorName(TW_ORANGE);
    twDrawString(10,vectorAC[0].y,"vector AC = (");
    twDrawString(vectorAC[0].x+60,vectorAC[0].y,",");
    twDrawString(vectorAC[1].x+60,vectorAC[1].y,",");
    twDrawString(vectorAC[2].x+60,vectorAC[2].y,")");

    twColorName(TW_MAGENTA);
    twDrawString(10,320,"angle between v and w=%.2f",angle);
    
    cellDraw(&pA[0]);
    cellDraw(&pA[1]);
    cellDraw(&pA[2]);
    cellDraw(&pB[0]);
    cellDraw(&pB[1]);
    cellDraw(&pB[2]);
    cellDraw(&pC[0]);
    cellDraw(&pC[1]);
    cellDraw(&pC[2]);

    cellDraw(&vectorAB[0]);
    cellDraw(&vectorAB[1]);
    cellDraw(&vectorAB[2]);
    cellDraw(&vectorAC[0]);
    cellDraw(&vectorAC[1]);
    cellDraw(&vectorAC[2]);
 
    if (selection==0) {
        glColor3f(1,1,1);
        twDrawString(10, 20,
                     "Click on arguments and move mouse to modify values.");
    }   
    twDrawString(10,380, "press 'm' to enable motion mode");
    twDrawString(10,420, "press 'M' to enable drawing mode");
    glutSwapBuffers();
}

int old_y;

void commandMouse(int button, int state, int x, int y) {
    selection = 0;    
    if (state == GLUT_DOWN) {
      //mouse should only hit _one_ of the cells, so adding up all
      // the hits just propagates a single hit. 
      selection += cellHit(&pA[0], x, y);
      selection += cellHit(&pA[1], x, y);
      selection += cellHit(&pA[2], x, y);

      selection += cellHit(&pB[0], x, y);
      selection += cellHit(&pB[1], x, y);
      selection += cellHit(&pB[2], x, y);

      selection += cellHit(&pC[0], x, y);
      selection += cellHit(&pC[1], x, y);
      selection += cellHit(&pC[2], x, y);
      }   
    old_y = y;
    
    redisplayAll();
}

void commandMotion(int x, int y) {    
    cellUpdate(&pA[0],old_y-y);
    cellUpdate(&pA[1],old_y-y);
    cellUpdate(&pA[2],old_y-y);
    cellUpdate(&pB[0],old_y-y);
    cellUpdate(&pB[1],old_y-y);
    cellUpdate(&pB[2],old_y-y);
    cellUpdate(&pC[0],old_y-y);
    cellUpdate(&pC[1],old_y-y);
    cellUpdate(&pC[2],old_y-y);
    
    old_y = y;
    redisplayAll();
}

//keyboard callback
void cellInit() {
 count = 0;
 mouseMode = 1;
 twTripleInit(pointA, 0,0,0);
 twTripleInit(pointB, 0,0,0);
 twTripleInit(pointC, 0,0,0);
    
  pA[0].value = 0;
  pA[1].value = 0;
  pA[2].value = 0;

  pB[0].value = 0;
  pB[1].value = 0;
  pB[2].value = 0;

  pC[0].value = 0;
  pC[1].value = 0;
  pC[2].value = 0;

  vectorAB[0].value = 0;
  vectorAB[1].value = 0;
  vectorAB[2].value = 0;

  vectorAC[0].value = 0;
  vectorAC[1].value = 0;
  vectorAC[2].value = 0;
}

void reinitializeValues(unsigned char key, int x, int y) { 
  switch(key) {
  case('R'): //resets all values to 0 (erases the vectors and points)
    cellInit();
    break;
  case('r'): //resets back to original view without erasing current vectors
    twZview();
    break;
  }
  redisplayAll();
}

void modeChange(unsigned char key, int x, int y) {
  switch (key) {
  case 'm': mouseMode = 0;  break;
  case 'M': mouseMode = 1;  break;
  }
  redisplayAll();
}

void choosePlane(unsigned char key, int x, int y) {
  twTriple view;
  switch (key) {
  case 'X': 
      twXview();
      break;
  case 'Y':
      twYview();
      break;
  case 'Z':
      twZview();
    break;
  }
  redisplayAll();
}

void keyInit () {
  twKeyCallback('R',reinitializeValues,"Resets all point and vector values");
  twKeyCallback('r',reinitializeValues, "Resets to original screen");
  twKeyCallback('m', modeChange, "tw mouse mode");
  twKeyCallback('M', modeChange, "vector drawing mouse mode");
  twKeyCallback('Z', choosePlane, "chooses z = 0 plane");
  twKeyCallback('Y', choosePlane, "chooses y = 0 plane");
  twKeyCallback('X', choosePlane, "chooses x = 0 plane");
}

void redisplayAll(void) {
    assignVectorValues();
    glutSetWindow(command);
    glutPostRedisplay();
    glutSetWindow(world);
    glutPostRedisplay();
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
  twBoundingBox(-1,1,-1,1,-1,1); //not necessary
  glutDisplayFunc(mainDisplay);
  twMainInit();
  keyInit();

  /*glutCreateSubWindow returns the ID of the sub-window and takes 
    arguments:(int parent,int x,int y,int width,int height).
    Origin at x,y; height equals distance from y _down_ */
  //create sub-window "command" for adjusting values
  command=glutCreateSubWindow(window,GAP*2+wWinWidth,GAP,cWinWidth,cWinHeight);
  glutDisplayFunc(commandDisplay);
  twMainInit();
  keyInit();
  glutMotionFunc(commandMotion);
  glutMouseFunc(commandMouse);
     
 //create sub-window "world" for drawing vectors
  world=glutCreateSubWindow(window,GAP,GAP,wWinWidth,wWinHeight);
  /*Each time you create a new window you need to give it its own 
   callbacks and initialization. These can be the same as those
   from other windows but you must call them each time*/
  twBoundingBox(-10,10,-10,10,-10,10);
  glutDisplayFunc(worldDisplay);
  twMainInit(); 
  keyInit();
  glutMouseFunc(worldMouse);
  glutMotionFunc(worldMotion);
  
  redisplayAll(); 
  glutMainLoop();
  return 0;
}
