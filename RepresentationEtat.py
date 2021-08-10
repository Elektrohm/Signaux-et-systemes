import numpy as np
import scipy.signal as sg
import matplotlib.pyplot as plt

def systemeContinu(A,B,C,D,x=None,tx=None):
    """systemeContinu est une fonction qui ... [description]
    Inputs :
     * A :  ...
     * B :  ...
     * C :  ...
     * D :  ...
     * x :  ...
     * tx : ...

    Outputs :
     * ty :  ...
     * y :   ...

    Creation  : xx-yy-2020
    """
    
    sys = sg.StateSpace(A,B,C,D)
    if (type(x)!= type(None) and type(tx)!= type(None)):
        ty, y, x = sg.lsim(sys,x,tx)
        return (ty,y)
    ty, y = sg.impulse(sys)
    return (ty,y)

def systemeDiscret(A,B,C,D,ts,x=None):
    """systemeDiscret est une fonction qui, pour une représentation d'état, un temps
    d'échantillonage et un signal d'entrée (ou non) retourne la réponse du système.
    
    Inputs :
     * A :  numpy.array représentant la matrice A dans la représentation d'état q[n+1] = Aq[n]+Bx[n].
     * B :  numpy.array représentant la matrice B dans la représentation d'état q[n+1] = Aq[n]+Bx[n].
     * C :  numpy.array représentant la matrice C dans la représentation d'état y[n] = Cq[n]+Dx[n].
     * D :  numpy.array représentant la matrice D dans la représentation d'état y[n] = Cq[n]+Dx[n].
     * ts : int représentant le temps d'échantillonnage (i.e., temps entre deux mesures) du système en secondes.
     * x :  numpy.array représentant un signal d'entrée discret sous forme vectorielle, commençant en t=0 et avec
            un temps d'échantillonage de ts, optionnel.

    Outputs :
     * ty : numpy.array de taille finie le vecteur temps associé au signal y
     * y :  numpy.array de taille finie correspondant à la réponse du système pour l'entrée x si celle-ci est fournie
            (autrement dit si x est différent de None), autrement y est la réponse impulsionnelle du système.

    Creation  : xx-yy-2020
    """
    
    sys = sg.StateSpace(A,B,C,D, dt=ts)
    if (type(x)!= type(None)):
        ty, y, x = sg.dlsim(sys,x,ts)
        return (ty,y)
    ty, y = sg.dimpulse(sys)
    y = np.squeeze(y)
    return (ty,y)

A = np.array([[0.7, 1.5], [0., -1.1]])
B = np.array([[0.], [0.4]])
C = np.array([[0.9, 0.2]])
D = np.array(1.)
ts = 2.0833333333333333e-05
ty, y = systemeDiscret(A,B,C,D,ts)
plt.plot(ty, y)
plt.show()


