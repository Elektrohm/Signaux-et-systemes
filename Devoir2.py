import numpy as np

def convolution(x,nx,y,ny):
    n_x = np.nonzero(x)
    n_y = np.nonzero(y)
    a= min(n_x)+min(n_y)
    b= max(n_x)+max(n_y)
    sup=np.zeros(a+b+1)
    z=np.zeros(a+b+1)
    i = 0
    x_ = x
    nx_ = nx
    for l in range(len(x)):
        x_[l]=x[len(x)-1-l]
        nx_[l]=nx_[len(x)-1-l]
    for j in range(a,b+1):
        sup[i]=j
        i = i+1
    
    for n in sup:
        som = 0
        nx_=nx_-n
        mi=min(min(x_),min(ny))
        ma = max(max(np.nonzero(x_)),max(np.nonzero(ny)))
        for k in range(min,max+1):
            if(k in x_ and k in ny):
                som = x_[k]*ny[k]
            if(k in x_ and k not in ny):
                som = x_[k];
            if(k in ny and k not in x_):
                som = ny[k]
        z[n] = som
                
    return (z,sup)


def plotFig(x,nx,y,ny,z,nz,name):
    plt.subplot(311)
    plt.stem(nx, x, linefmt='b--'    , markerfmt=None, basefmt = ' ')

    plt.subplot(312)
    plt.stem(ny, y, linefmt='b--'    , markerfmt=None, basefmt = ' ')

    plt.subplot(313)
    plt.stem(nz, z, linefmt='b--'    , markerfmt=None, basefmt = ' ')
    plt.show()

nx = np.array([-1,0,1,2])
x = np.array([1,2,2,3])
ny = np.array([-1,0,1])
y = np.array([2,-1,3])
z,nz = convolution(x,nx,y,ny)
plotFig(x,nx,y,ny,z,nz,"théo")
