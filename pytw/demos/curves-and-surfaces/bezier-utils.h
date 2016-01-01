/* Functions to assist in drawing and debugging Bezier curves and surfaces.
   If they prove useful, they will be included in TW.

   Scott D. Anderson
   November 2007
*/

// ================================================================================
// Curves

/* Simple function to print the control points, to make sure we get the
   order and strides right, as well as all the numbers.  Of course, an
   important purpose of this function is to demonstrate what the different
   strides mean. */

void printBezierCurve(int order, int stride, GLfloat* cp) {
    printf("Printing %d element array with id %x\n",order,cp);
    for( int u=0; u < order; u++ ) {
        printf("\t(%d) = (%4.2f,%4.2f,%4.2f)",
               u,
               // fancy pointer arithmetic:
               cp[u*stride+0],
               cp[u*stride+1],
               cp[u*stride+2]);
    }
    printf("\n");
}


/* Graphically display the control points. Use blue for the dimension, so
   the first CP is black and the last is blue. */

void drawBezierCurveControlPoints(int order, int stride, GLfloat* cp) {
    glPushAttrib(GL_ALL_ATTRIB_BITS); // so that the lighting, current color, point size and line width are not changed.
    glDisable(GL_LIGHTING);

    // map from int in [0,order-1] to float in [0.0,1.0]
    float factor = 1.0/(order-1); 

    glPointSize(6);
    glBegin(GL_POINTS);
    for( int u=0; u < order; u++ ) {
        glColor3f( 0, 0, u*factor); // compute color of this vertex
        glVertex3fv(cp+u*stride);   // fancy pointer arithmetic.
    }
    glEnd();

    glPopAttrib();
}

void drawBezierCurve(int order, int stride, int steps, GLfloat* cp) {
    glMap1f(GL_MAP1_VERTEX_3, 0, 1, stride, order, cp);
    glEnable(GL_MAP1_VERTEX_3);
    glMapGrid1f(steps,0,1);
    glEvalMesh1( GL_LINE, 0, steps );
    twError();
}

// ================================================================================
// Surfaces

/* Simple function to print the control points, to make sure we get the
   order and strides right, as well as all the numbers.  Of course, an
   important purpose of this function is to demonstrate what the different
   strides mean. */

void printBezierSurfaceControlPoints(int u_order, int u_stride, int v_order, int v_stride,
                                     GLfloat* cp) {
    // there are u_order * v_order control points in all.  Use nested loops to iterate over them.
    printf("Printing %dx%d array with id %x\n",u_order,v_order,cp);
    for (int v=0; v < v_order; v++ ) {
        printf("Row %d:",v);
        for( int u=0; u < u_order; u++ ) {
            printf("\t(%d,%d) = (%4.2f,%4.2f,%4.2f)",
                   u, v,
                   // fancy pointer arithmetic:
                   cp[u*u_stride+v*v_stride+0],
                   cp[u*u_stride+v*v_stride+1],
                   cp[u*u_stride+v*v_stride+2]);
        }
        printf("\n");
    }
}

/* Graphically display the control points. The "u" dimension is red, and
   the "v" dimension is green, so the first CP is black and the last is
   yellow. */

void drawBezierSurfaceControlPoints(int u_order, int u_stride, int v_order, int v_stride, GLfloat* cp) {
    glPushAttrib(GL_ALL_ATTRIB_BITS); // so that the lighting, current color, point size and line width are not changed.
    glDisable(GL_LIGHTING);

    // map from int in [0,order-1] to float in [0.0,1.0]
    float u_factor = 1.0/(u_order-1); 
    float v_factor = 1.0/(v_order-1); 

    glPointSize(6);
    glBegin(GL_POINTS);
    // there are u_order * v_order control points in all.  Use nested loops to iterate over them.
    for (int v=0; v < v_order; v++ ) {
        // printf("Row %d:",v);
        for( int u=0; u < u_order; u++ ) {
            // printf("\t%f %f", u*u_factor , v*v_factor); 
            glColor3f( u*u_factor , v*v_factor, 0); // compute color of this vertex
            glVertex3fv(cp+u*u_stride+v*v_stride); // fancy pointer arithmetic.
        }
        // printf("\n");
    }
    glEnd();
    glLineWidth(3);
    // Now draw each of the edges.  Warning: very complicated pointer arithmetic
    glColor3f(1,0,0);           // red for bottom edge, V=0, U=0
    drawBezierCurve(u_order, u_stride, 8, cp);
    glColor3f(0,1,0);           // green for left edge, U=0, V=0
    drawBezierCurve(v_order, v_stride, 8, cp);
    glColor3f(1,1,0);           // yellow for top edge, V=(v_order-1), U=0
    drawBezierCurve(u_order, u_stride, 8, cp+(v_order-1)*v_stride);
    glColor3f(1,1,0);           // yellow for right edge, U=(u_order-1), V=0
    drawBezierCurve(v_order, v_stride, 8, cp+(u_order-1)*u_stride);

    glPopAttrib();
}

/* Draw the whole Bezier surface.  Assumes each element is a triple, so
   you don't need to worry about strides. */

void drawBezierSurface(GLenum mode, int u_order, int u_steps, int v_order, int v_steps, GLfloat* cp) {
    const float umin = 0;
    const float umax = 1;
    const float vmin = 0;
    const float vmax = 1;
    int u_stride = 3;
    int v_stride = u_order*u_stride;
    GLint max_eval_order;

    twError();
    glGetIntegerv(GL_MAX_EVAL_ORDER,&max_eval_order);
    if(u_order > max_eval_order) {
        fprintf(stderr,"u_order (%d) is greater than allowed max: %d\n", u_order, max_eval_order);
        return;
    }
    if(v_order > max_eval_order) {
        fprintf(stderr,"v_order (%d) is greater than allowed max: %d\n", v_order, max_eval_order);
        return;
    }
    glMap2f(GL_MAP2_VERTEX_3, umin, umax, u_stride, u_order, vmin, vmax, v_stride, v_order, cp);
    twError();
    glEnable(GL_MAP2_VERTEX_3);
    
    glMapGrid2f(u_steps,0,1,
                v_steps,0,1);
    twError();
    switch(mode) {
    case GL_POINT: glEvalMesh2( mode, 0, u_steps, 0, v_steps ); break;
    case GL_LINE: glEvalMesh2( mode, 0, u_steps, 0, v_steps ); break;
    case GL_FILL: glEvalMesh2( mode, 0, u_steps, 0, v_steps ); break;
    default:
        fprintf(stderr,"No such mode for glEvalMesh2: %d",mode); break;
    }
    twError();
}

/* Draw the whole Bezier surface with texture coordinates.  Assumes each
   element is a triple, so you don't need to worry about strides.  Assumes
   GL_FILL mode. Assumes the texture coordinates are in a 2x2x2 array. */

void drawBezierSurfaceTextured(GLenum mode, int u_order, int u_steps, int v_order, int v_steps, GLfloat* cp, GLfloat* tcp) {
    const float umin = 0;
    const float umax = 1;
    const float vmin = 0;
    const float vmax = 1;
    int u_stride = 3;
    int v_stride = u_order*u_stride;
    glMap2f(GL_MAP2_VERTEX_3, umin, umax, u_stride, u_order, vmin, vmax, v_stride, v_order, cp);
    glMap2f(GL_MAP2_TEXTURE_COORD_2, umin, umax, 2, 2, vmin, vmax, 2*2, 2, tcp);
    twError();
    glEnable(GL_MAP2_VERTEX_3);
    glEnable(GL_MAP2_TEXTURE_COORD_2);
    
    glMapGrid2f(u_steps,0,1,
                v_steps,0,1);
    twError();
    glEvalMesh2( mode, 0, u_steps, 0, v_steps );
    twError();
}

