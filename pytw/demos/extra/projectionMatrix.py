import math

def transpose(square_matrix):
    S = square_matrix
    n = int(math.floor(math.sqrt(len(S))))
    if len(S) != n*n:
        print "matrix is not square"
        sys.exit()
    T = S[:]
    for i in range(n):
        for j in range(n):
            T[ i*n+j ] = S[ j*n+i ]
    return T
            
def projectionMatrix(yp):
    '''Return a projection matrix where the projection plane is at y=yp.'''
    yp = float(yp)
    RM = [ 1, 0, 0, 0,
           0, 1, 0, 0,
           0, 0, 1, 0,
           0, 1/yp, 0, 0 ]
    # the matrix RM is what we want, but it's in row major form,
    # and C and OpenGL want it in column major form, so return
    # the transpose
    return transpose(RM)

