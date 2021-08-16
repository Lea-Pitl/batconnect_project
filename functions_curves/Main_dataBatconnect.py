################     LAAS STAGE      ################
# Functions File to plot Curves from a csv file
# Author : Léa Pitault
# Date : 2021/08/16
#####################################################


#################################################
#                   IMPORT
#################################################

from functions_curves.dataset_testbench_pkg.Functions_BatconnectProcessing import readBatFile
from dataset_testbench_pkg import *

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


print(dic_bat_dataSet["time"])

#plotCurve1yAxis()
