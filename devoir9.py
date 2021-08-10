import numpy as np
import scipy.signal as sg

def filtre(n1,d1,n2,d2,y1,x2,fs):
    """conditionsInitialesD est une fonction qui filtre un message caché par le bruit d'un
    """
    TF = sg.TransferFunction(n1,d1,dt=1/fs)
    TF2 = sg.TransferFunction(n2,d2,dt=1/fs)
    ZPKTF = TF.to_zpk()
    ZPKTF2 = TF2.to_zpk()
    
    numZPK = ZPKTF.zeros
    denZPK = ZPKTF.poles
    gainZPK = ZPKTF.gain
    
    numZPK2 = ZPKTF2.zeros
    denZPK2 = ZPKTF2.poles
    gainZPK2 = ZPKTF2.gain
    
    numH3 = np.append(numZPK,denZPK2)
    denH3 = np.append(denZPK,numZPK)
    gainH3 = gainZPK/gainZPK2
    
    H3 = sg.ZerosPolesGain(numH3,denH3,gainH3,dt=1/fs).to_tf()
    yest = y1 - sg.lfilter(H3.num, H3.den,x2)
 
    return (H3,yest)

from scipy.io.wavfile import write
import pickle
infile = open('sons_dev9.pickle','rb')
data= pickle.load(infile)
infile.close()
H3, yest = filtre(data['n1'],data['d1'],data['n2'],data['d2'],data['yd'],data['xd'],data['fe']);
fs = data['fe'][0]
write("outd.wav", fs, yest)