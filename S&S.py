import numpy as np
import matplotlib.pyplot as plt

def d(n,n0):
    """d est une fonction qui correspond à l'impulsion discrète, dénotée par le Delta-Dirac
    Inputs :
     * n :   array d'int, est un tableau d'entier auxquels nous souhaitons évaluer la fonction
     * n0 :  int, est une variable entière, elle décale le signal vers la gauche ou la droite

    Outputs :
     * y :   array d'int, renvoie le tableau des entiers égaux à 1 si n=n0, 0 sinon

    Creation  : xx-yy-2020
    """
    y = np.zeros(len(n),dtype=int)
    for i in range(0,len(n)):
        y[i] = 1 if n[i]==n0 else 0
    return y

def u(n,n0):
    """u est une fonction qui correspond à l'échelon discret 
    Inputs :
     * n :   array d'int, est un tableau d'entier auxquels nous souhaitons évaluer la fonction
     * n0 :  int, est une variable entière qui décale le signal vers la gauche ou la droite

    Outputs :
     * y :   array d'int, renvoie le tableau des entiers évalués égaux à 1 si n-n0>=0, 0 sinon.
 
    Creation  : xx-yy-2020
    """
    y = np.zeros(len(n),dtype=int)
    for i in range(0,len(n)):
        y[i] = 1 if n[i]-n0>=0 else 0
    return y


def r(n,n0):
    """r est une fonction qui ... [description]
    Inputs :
     * n :   array d'int, est un tableau d'entier auxquels nous souhaitons évaluer la fonction
     * n0 :  [type, taille, description] ...

    Outputs :
     * y :   int, renvoie l'entier correspondant à n-n0 si n-n0>=0, 0 sinon.

    Creation  : xx-yy-2020
    """
    y = np.zeros(len(n),dtype=int)
    for i in range(0,len(n)):
        y[i] = n[i]-n0 if n[i]-n0>=0 else 0
    return y


def plotFig(y,n,name):
    """plotFig est une fonction qui affiche et sauvegarde un graphique de la relation entre n et y.
    Inputs :
     * y :    [numpy.array, de la même taille que n, réprésente les images des abscicces du tableau n] ...
     * n :    [numpy.array, de taille finie , représente les abscisses d'une fonction] ...
     * name : [string, de taille quelconque, représente le nom de sauvegarde du graphique obtenue en sortie ] ...

    Creation  : 16-02-2020
    """
    # Création de la figure, de taille fixe.
    plt.figure(figsize=(6,3))
    plt.stem(n, y, linefmt='b--'    , markerfmt=None, basefmt = ' ')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.title('Signal')
    plt.show()
    plt.savefig(name + '.png', bbox_inches='tight')
    
x = np.arange(-4, 6, 1)
plotFig(r(x,-1),x,"andi")
