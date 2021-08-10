import numpy as np
import matplotlib.pyplot as plt


def convolution(x,nx,y,ny):
    #liste des indices où les valeurs sont différentes de 0
    n_x = np.nonzero(x)[0]
    n_y = np.nonzero(y)[0]
    
    #a est le min et b le max des indices
    a= nx[n_x[0]]+ny[n_y[0]]
    b= nx[n_x[len(n_x)-1]]+ny[n_y[len(n_y)-1]]
    
    #définissions du support et de Z
    sup=np.arange(a,b+1,1)
    z=np.arange(a,b+1,1)
    
    #obtentions des valeurs min et max de k
    kmin = min(ny)
    kmax = max(ny)
    
    ind = 0 
    for n in sup:  
        som = 0
        for k in range(kmin, kmax+1):
            if(n-k in nx and k in ny):
                k1=np.where(nx == n-k)[0][0]
                k2=np.where(ny==k)[0][0]
                som = som+ x[k1]*y[k2]
        z[ind] = som
        ind=ind+1
                
    return (z,sup)

def plotFig(x,nx,y,ny,z,nz,name):
    """plotFig est une fonction qui affiche le signal x aux abscisses nx et y aux abscisses ny ainsi que leur produit de convolution z aux abscisses nz.
    Inputs :
     * x : np.array, de la même taille que nx, représentant les ordonées d'un signal aux abscisses nx. 
     * nx : np.array,de taille finie, trié par ordre croissant, représentant les abscisses d'un signal x
     * y : np.array, de la même taille que ny, représentant les ordonées d'un signal aux abscisses ny 
     * ny : np.array,de taille finie, trié par ordre croissant, représentant les abscisses d'un signal y
     * z : np.array, de la même taille que nz, représentant les ordonées de la convolution des deux signaux x et y.
     * nz : np.array, de la même taille que nz,trié par ordre croissant, représentant les abscisses des ordonnées du signal z. 
     * name : String, de taille arbitraire, représentant le nom que vous donnez à la figure.

    Création  : 25-02-2019
    """
    
    fig, axs = plt.subplots(3)
    fig.suptitle('Convolution de x*y')
    plt.subplots_adjust(hspace=0.8)
    
    #Graphe de x
    axs[0].stem(nx,x, linefmt=None, markerfmt=None, basefmt=None, label = "x[n]")
    axs[0].set_title("Graphe du signal x")
    axs[0].legend(loc = "upper left")
    
    #Graphe de y
    axs[1].stem(ny,y, linefmt=None, markerfmt=None, basefmt=None, label = "y[n]")
    axs[1].set_title("Graphe du signal y")
    axs[1].legend(loc = "upper left")
    
    #Graphe de z
    axs[2].stem(nz,z, linefmt=None, markerfmt=None, basefmt=None, label = "z[n]")
    axs[2].set_title("Graphe de la convolution x*y")
    axs[2].legend(loc = "upper left")
    
    #labelisation
    plt.xlabel("n ([-])")
    fig.text(0.06, 0.55, 'y[n] ([-])', ha='center', va='center')
    fig.text(0.06, 0.85, 'x[n] ([-])', ha='center', va='top')
    fig.text(0.06, 0.25, 'z[n] ([-])', ha='center', va='bottom')
    
    plt.savefig(name + '.png', bbox_inches='tight')
    plt.show()

nx = np.array([-1,0,1,2])
x = np.array([1,2,2,3])
ny = np.array([-1,0,1])
y = np.array([2,-1,3])
z,nz = convolution(x,nx,y,ny)
print("nz : {}\nz : {}".format(nz,z))
plotFig(x,nx,y,ny,z,nz,"théo")
