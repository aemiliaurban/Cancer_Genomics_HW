import numpy as np
from matplotlib import pyplot as plt

wt = open("wt.regiongs.coverage", "r").readlines()
tumor = open("tumor.regiongs.coverage", "r").readlines()

logs = []
pos = []
   
for el in wt:
    for l in tumor:
        ell = el.split()
        ll = l.split()
        if ell[1] == ll[1] and el[2] != 0:
            logs.append(np.log2(int(ll[2])/int(ell[2])))
            pos.append(ell[1])
            break
        
plt.pyplot.scatter(logs, pos)
plt.title("Solution")
plt.xlabel("Logarithmic values of depth coverage")
plt.ylabel(("Position in genome"))
plt.show()
            
