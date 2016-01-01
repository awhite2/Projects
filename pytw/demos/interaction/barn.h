/* Provides two barn-building functions.

Scott D. Anderson
Fall 2000
*/

/* ================================================================
   code for the barn.  This is a barn with the origin at its
   bottom, left, front vertex.  The front is red, the back is
   green, and the sides are all blue.  The height is the height of
   the barn's walls, not the height of the ridge.  The roof of the
   barn is always at a 45 degree angle. */

void wire_barn(GLfloat width, GLfloat height, GLfloat length)
{
    /* the following only initializes the front 5 vertices */
    GLfloat barn[10][3] = 
    {
	{0,0,0},		/* left, bottom, front */
	{width,0,0},		/* right, bottom, front */
	{width,height,0},	/* right, top, front */
	{0,height,0},		/* left, top, front */
	{width/2,height+width/2,0}, /* ridge, front */
    };
    int i;

    /* Init the barn's back 5 vertices */
    for(i=0;i<5;++i) {
	barn[5+i][0] = barn[i][0];
	barn[5+i][1] = barn[i][1];
	barn[5+i][2] = -length;
    }
    /* draw the barn */
    glColor3f(1,0,0);		/* front is in red */
    glBegin(GL_LINE_LOOP);
    {
	glVertex3fv(barn[0]);
	glVertex3fv(barn[1]);
	glVertex3fv(barn[2]);
	glVertex3fv(barn[3]);
    }
    glEnd();
    glColor3f(1,0,0);		/* front top is also in red */
    glBegin(GL_LINE_LOOP);
    {
	glVertex3fv(barn[3]);
	glVertex3fv(barn[2]);
	glVertex3fv(barn[4]);
    }
    glEnd();
    glColor3f(0,1,0);		/* back is in green */
    glBegin(GL_LINE_LOOP);
    {
	glVertex3fv(barn[5]);
	glVertex3fv(barn[6]);
	glVertex3fv(barn[7]);
	glVertex3fv(barn[8]);
    }
    glEnd();
    glBegin(GL_LINE_LOOP);
    {
	glVertex3fv(barn[7]);
	glVertex3fv(barn[8]);
	glVertex3fv(barn[9]);
    }
    glEnd();
    glColor3f(0,0,1);		/* side rails in blue */
    glBegin(GL_LINES);
    {
	for(i=0;i<5;++i) {
	    glVertex3fv(barn[i]);
	    glVertex3fv(barn[i+5]);
	}
    }
    glEnd();
}

/* code for the solid barn.  This looks just like the wire barn,
   except the faces are filled polygons.  Made the top gray and
   bottom black. */

void solid_barn(GLfloat width, GLfloat height, GLfloat length)
{
    int i;
    /* the following only initializes the front 5 vertices */
    GLfloat barn[10][3] = 
	{
	    {0,0,0},		/* left, bottom, front */
	    {width,0,0},	/* right, bottom, front */
	    {width,height,0},	/* right, top, front */
	    {width/2,height+width/2,0}, /* ridge, front */
	    {0,height,0},	/* left, top, front */
	};
    GLfloat normals[][3] =
	{
	    {+1, 0, 0},		// 0: +x
	    { 0,+1, 0},		// 1: +y
	    { 0, 0,+1},		// 2: +z
	    {-1, 0, 0},		// 3: -x
	    { 0,-1, 0},		// 4: -y
	    { 0, 0,-1},		// 5: -z
	    { +cos(M_PI/4), sin(M_PI/4), 0 }, // 6: up left
	    { -cos(M_PI/4), sin(M_PI/4), 0 } // 7: up right
	};


    /* Init the barn's back 5 vertices */
    for(i=0;i<5;++i) {
	barn[5+i][0] = barn[i][0];
	barn[5+i][1] = barn[i][1];
	barn[5+i][2] = -length;
    }
    /* draw the barn */
    glColor3f(1,0,0);		/* front is in red */
    glBegin(GL_POLYGON);
    {
	glNormal3fv(normals[2]);
	glVertex3fv(barn[0]);
	glVertex3fv(barn[1]);
	glVertex3fv(barn[2]);
	glVertex3fv(barn[3]);
	glVertex3fv(barn[4]);
    }
    glEnd();
    glColor3f(0,1,0);
    /* back is in green.  Note we have to go counterclockwise */
    glBegin(GL_POLYGON);
    {
	glNormal3fv(normals[5]);
	glVertex3fv(barn[9]);
	glVertex3fv(barn[8]);
	glVertex3fv(barn[7]);
	glVertex3fv(barn[6]);
	glVertex3fv(barn[5]);
    }
    glEnd();
    glColor3f(0,0,1);		/* sides are in blue */
    glBegin(GL_POLYGON);
    {
	/* this is the barn's right side.  Again, must be counterclockwise */
	glNormal3fv(normals[3]);
	glVertex3fv(barn[0]);
	glVertex3fv(barn[4]);
	glVertex3fv(barn[9]);
	glVertex3fv(barn[5]);
    }
    glEnd();
    glBegin(GL_POLYGON);
    {
	/* this is the barn's left side */
	glNormal3fv(normals[0]);
	glVertex3fv(barn[1]);
	glVertex3fv(barn[6]);
	glVertex3fv(barn[7]);
	glVertex3fv(barn[2]);
    }
    glEnd();
    glColor3f(0.5,0.5,0.5);		/* top is in gray */
    glBegin(GL_POLYGON);
    {
	/* this is the barn's right roof */
	glNormal3fv(normals[7]);
	glVertex3fv(barn[4]);
	glVertex3fv(barn[3]);
	glVertex3fv(barn[8]);
	glVertex3fv(barn[9]);
    }
    glEnd();
    glBegin(GL_POLYGON);
    {
	/* this is the barn's left roof */
	glNormal3fv(normals[6]);
	glVertex3fv(barn[7]);
	glVertex3fv(barn[8]);
	glVertex3fv(barn[3]);
	glVertex3fv(barn[2]);
    }
    glEnd();
    glColor3f(0,0,0);		/* bottom is in black */
    glBegin(GL_POLYGON);
    {
	/* this is the bottom */
	glNormal3fv(normals[4]);
	glVertex3fv(barn[0]);
	glVertex3fv(barn[5]);
	glVertex3fv(barn[6]);
	glVertex3fv(barn[1]);
    }
    glEnd();
}
