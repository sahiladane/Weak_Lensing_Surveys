from transfer_func import *
from Cl import *
import numpy as np
import matplotlib.pyplot as plt

L=LCDM(0.3,0.7,0.045,0.96,0.894,1,2,1.5) #Parameters are to be given in the order of Omega_m,h,Omega_b,ns,sigma_8,z0, alpha, beta
#l=0.30.3,h=0.7,Ob0=0.045,ns=0.96,sigma_8 = 0.8,z0 = 0.637, alpha=2, beta=1.5


l=[1,5,10,50,60,80,100,200,300,400,500,600,700,800,900,1000]
cl=LCDM.Pl_wh(L,l)
plt.loglog(l,cl)
plt.show()

#print cl
