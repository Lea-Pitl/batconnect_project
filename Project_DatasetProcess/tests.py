
import numpy as np
from matplotlib.colors import hsv_to_rgb
import matplotlib.pyplot as plt
import colorsys
from utilities_pkg.Utilities_PlotCurves import *
from utilities_pkg import *
# 20210716_Cycle10A_LiFePO4_BATCONNECT_CA2.txt
from dataset_testbench_pkg import *
# '20210722_Cycle50A_LiFePO4_BATCONNECT_CA1.txt'
file_title = '20210722_Cycle50A_LiFePO4_BATCONNECT_CA1.txt'
title = 'test'

#####################################################################
#                           MAIN
#####################################################################

########################
#       LEA DATASET
########################
COLOR2 = (0.1, 0.2, 0.9)


nb_cycle=8

H = 0.55
S = 0.7

for i in range(nb_cycle):
    V = 1-i*(0.4/nb_cycle)
    print(V)
    COLOR = colorsys.hsv_to_rgb(H,S,V)

    x = np.arange(i, 4*np.pi, 0.1)   # start,stop,step
    y = np.sin(x)
    plt.plot(x, y, color=COLOR)

plt.show()
