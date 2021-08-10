import numpy as np
import matplotlib.pyplot as plt 

def computeDFT(x,M):
    """computeDFT est une fonction qui ... [description]
    Inputs :
     * x :   [type, taille, description] ...
     * M :   [type, taille, description] ...

    Outputs :
     * DFT :    [type, taille, description] ...
     * wDFT :   [type, taille, description] ...
     * DTFT :   [type, taille, description] ...
     * wDTFT :  [type, taille, description] ...

    Creation  : xx-yy-2020
    """
    
    #fft fait de lui même un zero padding ou crop de x 
    dft = np.fft.fft(x, M)
    DFT = np.fft.fftshift(dft)
    
    for i in range(0,len(DFT)):
        DFT[i] = DFT[i] if abs(DFT[i])> 1e-9 else 0
        
    #le pas dans rappel APE11 p53
    timestep = 2*np.pi/M
    DFTfreqs = np.fft.fftfreq(M, d=timestep)
    wDFT = np.fft.fftshift(DFTfreqs)
    
    for i in range(0,len(wDFT)):
        wDFT[i] = wDFT[i] if abs(wDFT[i])> 1e-9 else 0
    
    
    #je force une taille plus grande pour qu'il fasse lui même le zero padding
    dtft = np.fft.fft(x,10*len(x))
    DTFT = np.fft.fftshift(dtft)
    
    for i in range(0,len(DTFT)):
        DTFT[i] = DTFT[i] if abs(DTFT[i])> 1e-9 else 0
    
    #le pas dans rappel APE11 p53
    timestep = 2*np.pi/len(DTFT)
    DTFTfreqs = np.fft.fftfreq(len(DTFT), d=timestep)
    wDTFT = np.fft.fftshift(DTFTfreqs)
    
    for i in range(0,len(wDTFT)):
        wDTFT[i] = wDTFT[i] if abs(wDTFT[i])> 1e-9 else 0

    return (DFT,wDFT,DTFT,wDTFT)



def plotSignal(DFT,wDFT,DTFT,wDTFT,name):
    
    fig, axs = plt.subplots(2)
    plt.subplots_adjust(hspace=0.8)
    
    #Graphe de DTFT
    modDTFT = np.abs(DTFT)
    
    axs[0].plot(wDTFT,modDTFT, label = "X[k]")
    axs[0].set_title("Module de l'estimation de la DTFT")
    axs[0].set_xlabel("freq ([rad])")
    axs[0].set_ylabel("X[k] ([-])")
    axs[0].legend(loc = "best")
    
    
    #Graphe de DFT
    modDFT = np.abs(DFT)
    
    axs[1].stem(wDFT,modDFT, linefmt=None, markerfmt=None, use_line_collection=True, basefmt=None, label = "X[k]")
    axs[1].set_title("Module des coéfficients de la DFT")
    axs[1].set_xlabel("freq ([rad])")
    axs[1].set_ylabel("X[k] ([-])")
    axs[1].legend(loc = "best")
    
    
    plt.savefig(name + '.png', bbox_inches='tight')
    plt.show()
    
DFT,wDFT,DTFT,wDTFT = computeDFT(np.array([-3,-2,-1,0,1,2,3]),9)
plotSignal(DFT,wDFT,DTFT,wDTFT, "test")
