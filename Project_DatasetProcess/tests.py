
from utilities_pkg.Utilities_PlotCurves import *
from utilities_pkg import *
from dataset_testbench_pkg import * # 20210716_Cycle10A_LiFePO4_BATCONNECT_CA2.txt
 #'20210722_Cycle50A_LiFePO4_BATCONNECT_CA1.txt'
file_title = '20210722_Cycle50A_LiFePO4_BATCONNECT_CA1.txt'
title = 'test'

#####################################################################
#                           MAIN
#####################################################################

########################
#       LEA DATASET
########################
line_up, = plt.plot([1, 2, 3], label='Line 2')
line_down, = plt.plot([3, 2, 1], label='Line 1')
plt.legend([line_up, line_down], ['Line Up', 'Line Down'])

plt.show()