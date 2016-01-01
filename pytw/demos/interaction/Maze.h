/* Adapted from Dan Cliburn's code, which was in C++.

Maze file format is
rows cols
wall texture filename
floor texture filename
monster texture filename
maze description lines

Each maze description line has the following codes:
w means a wall
f means floor
s means the location of the player. Only one
m means a monster.  Any number of these
L means a downward-facing white light
R means a downward, partly backward facing red light
B means a downward, partly backward facing blue light

Walls are created as 3D blocks (four walls only) and placed in the scene.
This involves a small amount of waste in that if two wall blocks are next
to each other, the two faces where they meet don't need to be drawn.  We
could improve this by encoding different kinds of wall blocks, such as:

w means 4-sided, as before
- means just top and bottom sides
| means just left and right sides

I think each cell of the maze is one unit square (cube).  The player is
put in the center of the cell (r+0.5,c+0.5), facing +x.  Note that this
means that the origin is in the upper left corner of the maze and z
increases down.  Eye's y position is 0.6.

For performance, Dan builds the maze using display lists.  There's
actually one big display-list for the whole maze.

His VPN and NEAR are 0.1 units.  Movement is along the VPN.  Collision
detection is done by examining the fractional part of the new location.
If it is less than 0.1 units from an integer (larger than 0.9 or smaller
than 0.1), a collision is detected.

*/

int monsterCount = 0;           // number of monsters in the maze

char** Maze;                   // the character array that stores the maze
int MazeSizeZ;                  // the maze goes from z=0 to z=MazeSizeZ
int MazeSizeX;                  // the number of columns in that array

GLuint textureIDs[3];         // indices for texture binding

void chomp(char buffer[]) {
    int len = strlen(buffer);
    //printf("len = %d, last is %c (%d)\n",len,buffer[len],buffer[len]);
    buffer[len-1] = 0;
}

void peekchar(FILE * stream) {
    char next = getc(stream);
    printf("next char is %c (%d)\n",next,next);
    ungetc(next,stream);
}

void readTextureFile(FILE* fin, int textureID) {
    const int SIZE = 128;
    char texfilename[SIZE];

    if(NULL == fgets(texfilename,SIZE,fin)) {
        fprintf(stderr,"Couldn't read texture filename\n");
    }
    chomp(texfilename);
    printf("texture is %s!\n",texfilename);
    twLoadTexture(textureID,texfilename);
}    

/* This code is amazingly brittle.  It needs to be fixed! */

void loadMaze(char * mazefile) {
    int r,c,result;
    char* line;
    char* wallTex;
    char* floorTex;
    char* monsterTex;

    monsterCount = 0;  //reset the monster counter back to 0 if it was not here already

    FILE* fin = fopen(mazefile, "r");
    printf("file %s opened!\n",mazefile);

    // read maze size
    result = fscanf(fin,"%d %d\n",&MazeSizeZ,&MazeSizeX);
    if( result != 2) {
        fprintf(stderr,"Couldn't read Maze size: %d\n",result);
        exit(1);
    }
    printf("Maze is %d by %d\n",MazeSizeZ,MazeSizeX);

    // peekchar(fin);
    
    //read names of texture files
    glGenTextures(3,textureIDs);
    readTextureFile(fin,textureIDs[0]);
    readTextureFile(fin,textureIDs[1]);
    readTextureFile(fin,textureIDs[2]);
    
    // peekchar(fin);

    // read maze
    Maze = (char**) malloc(MazeSizeZ*sizeof(char*));
    for (r = 0; r < MazeSizeZ; r++)

    for (r = 0; r < MazeSizeZ; r++) {
        Maze[r] = (char*) malloc(1+MazeSizeX*sizeof(char));
        Maze[r][MazeSizeX] = 0;
        for(c = 0; c < MazeSizeX; c++ ) {
            Maze[r][c] = getc(fin);
            getc(fin);          // throw away space or newline

            char cell = Maze[r][c];
            if(cell == 's') {
                    VRP[0] = c + 0.5; 
                    VRP[2] = r + 0.5;
                    VRP[1] = 0.6;
            }
            if(cell == 'm') {
                monsterCount++;
            }
        }
        // echo the line
        // printf("%d:%s!\n",r,Maze[r]);
        // peekchar(fin);
    }

    // print maze (for debugging)
    for(r=0;r<MazeSizeZ;r++) printf("%s\n",Maze[r]);
}

/* Create the blocks used for wall cells.

The dlWallFace is a vertical wall in the x=0 plane, with the surface
normal pointing to the left (-1,0,0).  The upper left corner of the
texture is the lower left corner of the wall, as you face it.  The
vertices are CCW.

The dlWall is four placements of the wall face.  Viewing the scene from
above, we first draw the left wall of the square, then the bottom one,
then the right, then the top on.  "left" here means x=0, and "right" means
x=1, while "bottom" means z=1 and "top" means z=0.

The dlFloor tile is a unit square in y=0, with the surface normal up
0,1,0.  The upper left corner of the texture is in the lower left corner
of the tile, as you view it from above.

The dlMaze object is a big display list for the whole collection of wall
blocks, built by going through the maze character representation.

We really don't need any of the display lists except the one for the maze,
but I suppose building the maze is marginally faster with those building
blocks.

*/

// display list identifiers
int dlWallFace;
int dlWall;
int dlFloor;
int dlMaze;

void initMaze(float matAmbientDiffuse, float matSpecular) {
    //Create the Wall Face
    dlWallFace = glGenLists(1);
    glNewList(dlWallFace, GL_COMPILE); {
        // the underlying surfaces need to have material. Since we're
        // using textures and modulation, we'll use gray material.
        twTriple gray = {matAmbientDiffuse,matAmbientDiffuse,matAmbientDiffuse};
        twColor(gray,matSpecular,100);

        glBindTexture(GL_TEXTURE_2D, textureIDs[0]);  //Bind Wall Texture:  ID 0
        glBegin(GL_QUADS);
                        
        glNormal3f(-1, 0, 0);  //Normals must be defined for lighting
        glTexCoord2d(0, 0);
        glVertex3f(0, 0, 0);    // lower left

        glTexCoord2d(1, 0);
        glVertex3f(0, 0, 1);    // lower right
                        
        glTexCoord2d(1, 1);
        glVertex3f(0, 1, 1);    // upper right

        glTexCoord2d(0, 1);
        glVertex3f(0, 1, 0);    // upper left
        glEnd();
    }
    glEndList();

    //Create the Wall Cube
    dlWall = glGenLists(1);
    glNewList(dlWall, GL_COMPILE); {
        glPushMatrix();        
                        
        glCallList(dlWallFace); // left wall

        glTranslatef(0,0,1);
        glRotatef(90, 0, 1, 0);
        glCallList(dlWallFace); // bottom wall

        glTranslatef(0,0,1);
        glRotatef(90, 0, 1, 0);
        glCallList(dlWallFace); // right wall

        glTranslatef(0,0,1);
        glRotatef(90, 0, 1, 0);
        glCallList(dlWallFace); // top wall
        glPopMatrix();
    }
    glEndList();

    //Now generate the floor tile
    dlFloor = glGenLists(1);
    glNewList(dlFloor, GL_COMPILE); {
        glBindTexture(GL_TEXTURE_2D, textureIDs[1]);  //Bind Floor Texture:  ID #1
        glBegin(GL_QUADS);
                        
        glNormal3f(0, 1, 0);
        glTexCoord2d(0, 1);
        glVertex3f(0, 0, 0);        // upper left

        glTexCoord2d(0, 0);
        glVertex3f(0, 0, 1);        // lower left
                        
        glTexCoord2d(1, 0);
        glVertex3f(1, 0, 1);        // lower right

        glTexCoord2d(1, 1);
        glVertex3f(1, 0, 0);        // upper right
        glEnd();
    }
    glEndList();

    dlMaze = glGenLists(1);
    glNewList(dlMaze, GL_COMPILE); {
        glPushMatrix();
        for (int r = 0; r < MazeSizeZ; r++) {
            for (int c = 0; c < MazeSizeX; c++) {
                if (Maze[r][c] == 'w')
                    glCallList(dlWall);
                else
                    glCallList(dlFloor);
                glTranslatef(1,0,0);  // Go over 1 units so that next is ready
            }
            glTranslatef(-MazeSizeX, 0, 1); // Go to left edge of next row
        }
        glPopMatrix();
    }
    glEndList();

    /*  ADD FOR MONSTERS 
        //Now we make the array of monsters
        monsterCount = 0;
        monsters = new Monster[totalMonsters];
        //Next, go through the array and make each monster at its location
        for (int row = 0; row < MazeSizeZ; row++) 
            for (int col = 0; col < MazeSizeX; col++) 
                if (Maze[row][col] == 'm') {
                    monsters[monsterCount].setPosition(col + 0.5, 0.5, row + 0.5);
                    //All monsters share a common texture so we only need to make it once
                    monsters[monsterCount].setID(3);
                    monsters[monsterCount].setHitPoints(2);
                    monsterCount++;
                }
        */
}
