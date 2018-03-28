from transfer_func import *
from fluids import *
import numpy as np
import matplotlib.pyplot as plt
L=LCDM(0.3)
#l=0.3
l=np.linspace(1,10,10)
cl=LCDM.Pl_wh(L,l,0.637,2.0,1.5)
plt.plot(l,cl)
plt.show()
print cl