import numpy as np


def conditionsInitialesD(yf, a0, a1, xi, yi):
    """conditionsInitialesD est une fonction qui calcule la sortie discrète du système caractérisé par l'équation "y[n] = a0*x[n-1] + a1*y[n-1]". 
    @pre: 
       * yf =  numpy array de taille finie, il correspond à la réponse forcée, en temporel, du système (qui suppose les conditions initiales nulles).
       * a0 = int, coefficient réel du système qui multiplie x[n-1] dans l'équation "y[n] = a0*x[n-1] + a1*y[n-1]".
       * a1 = int, coefficient réel du système qui multiplie y[n-1] dans l'équation "y[n] = a0*x[n-1] + a1*y[n-1]".
       * xi = int, réel donnant la condition initiale au pas de temps n = -1 pour x, c'est à dire x[-1].
       * yi = int, réel donnant la condition initiale au pas de temps n = -1 pour y, c'est à dire y[-1].
    @post: 
       return la réponse sortie du système sous forme de numpy array de la même taille que yf.
    """
    yl = np.zeros(len(yf))
    n = np.arange(0,len(yf),1)
    yl = (a1**n)*(a0*xi+a1*yi)
    return yl+yf

def conditionsInitialesC(yf,t,y0,dy0):
    """conditionsInitialesC est une fonction qui renvoie la réponse du système avec l'influence des conditions initiales pour l'équation
    y"(t)+y'(t)=x(t)
    @pre :
       * yf = numpy array de taille finie, réponse forcée du sytème
       * t = numpy array de taille finie, temps auxquels yf a été calculée (t>=0)
       * y0 = int, réel donnant la condition initiale y(0)
       * dy0 = int, réel donnant la condition initiale y'(0)
    @post :
       return numpy array de même taille que yf, réponse du système avec l'influence des conditions initiales y0 et dy0 aux temps t.
    """
    yl = np.zeros(len(yf))
    yl = y0+dy0*(1-e**(-t))
    return yf+yl

