################     LAAS STAGE      ##############################################################
# MAIN FILE TO PROCESS THE LAAS TESTBENCH VALUES
# Author : Léa Pitault
# Date : 2021/07/12
###################################################################################################


#################################################
#                   IMPORTS
#################################################

from utilities_pkg import *
from dataset_testbench_pkg import *

#################################################
#                   VARIABLES
#################################################

file_title = 'dataset_testbench_files/20210729_Cycle50A_LiFePO4_BATCONNECT_bat3_CA1.txt'
file_title2 = 'dataset_testbench_files/20210722_Cycle50A_LiFePO4_BATCONNECT_bat3_CA1.txt'
###################################################################################################
#                           MAIN
###################################################################################################

########################
#       LEA DATASET
########################

dic_dataSet, nbCycle, nbSeq = readFile(file_title)

# plotCurrentVoltage(dic_dataSet["time"], dic_dataSet["current"], dic_dataSet["voltage"])

dic_dataCycle, dic_dataSeq = sortData(dic_dataSet)
#plotVoltageCapacity(dic_dataSeq["V_c"][1],dic_dataSeq["Q_c"][1], 0)

plotTestbenchICASeq(dic_dataSeq, 15)
#title = 'Capacity of 15 cycles in function of voltage'

#plotTestbenchOverlaidCurves(dic_dataSeq, "V_c", "Q_c", VOLTAGE_LABEL, CAPACITY_LABEL, title, 15)

#x = dic_dataSeq["T_c"][9]
#y1 = dic_dataSeq["V_c"][9]
#y2 = dic_dataSeq["Q_c"][9]

#plotCurve2yAxis(x, y1, y2, 'Charge capacity and battery voltage through time for one charge', TIME_LABEL, VOLTAGE_LABEL, CAPACITY_LABEL)


#percentageCapa(x, y1, y2)
