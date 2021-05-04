import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

wt = pd.read_table("wt.regiongs.coverage", sep="\t", names=["chr", "pos", "depth"])
tumor = pd.read_table("tumor.regiongs.coverage", sep="\t", names=["chr", "pos", "depth"])
i, j = 1, 1 

positions = []
logs = []

while wt.iloc[i, 0] or tumor.iloc[j, 0]:
    if wt.iloc[i, 2] == 0 or tumor.iloc[j, 2] == 0:
        i += 1
        j += 1
    elif wt.iloc[i, 1] < tumor.iloc[j, 1]:
        i += 1
    elif wt.iloc[i, 1] > tumor.iloc[j, 1]:
        j += 1
    else:
        positions.append(wt.iloc[i, 1])
        logs.append(np.log2(tumor.iloc[j, 2]/wt.iloc[i, 2]))
        i += 1
        j +=1
        
plt.scatter(positions, logs)
plt.title("Read depth scatter plot")
plt.xlabel("Logarithmic values of depth coverage")
plt.ylabel(("Position in genome"))
plt.savefig("coverage_plot")
            
