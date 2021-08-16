################     LAAS STAGE      ################
# Functions File to plot Curves from a csv file
# Author : Léa Pitault
# Date : 2021/08/16
#####################################################


#################################################
#                   IMPORT
#################################################

from dataset_testbench_pkg import *
from dataset_batconnect_pkg import *

#################################################
#                   VARIABLES
#################################################

file_title = 'Batconnect_files/batconnect_out_date.csv'

#####################################################################
#                           MAIN
#####################################################################

################################
#       BATCONNECT DATASET
################################

dic_bat_dataSet = readBatFile(file_title)

for i in range(0,100):
    print(dic_bat_dataSet["time"][i])

#plotCurve1yAxis()
