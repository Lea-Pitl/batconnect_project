################     LAAS STAGE      ##############################################################
# MAIN FILE TO PROCESS THE LAAS TESTBENCH VALUES
# Author : Léa Pitault
# Date : 2021/07/12
###################################################################################################


#################################################
#                   IMPORTS
#################################################

from dataset_testbench_pkg.Functions_TestbenchPlotCurves import *
from utilities_pkg.Utilities_PlotCurves import *
from utilities_pkg import *
from dataset_testbench_pkg import *

#################################################
#                   VARIABLES
#################################################

file_title1 = 'dataset_testbench_files/20210803_Cycle50A_LiFePO4_BATCONNECT_bat1_CA1.txt'
file_title2 = 'dataset_testbench_files/20210817_Cycle50A_12deg_LiFePO4_BATCONNECT_bat1_CA1.txt'
###################################################################################################
#                           MAIN
###################################################################################################

########################
#       LEA DATASET
########################
print('         ################################ \n '
          'Sort data according to the cycles and the sequences \n'
          '         ################################')
dic_dataSet1, nbCycle1, nbSeq1 = readFile(file_title1)
dic_dataSet2, nbCycle2, nbSeq2 = readFile(file_title2)

dic_data_tempe = {}
dic_data_tempe["25deg"] = dic_dataSet1
dic_data_tempe["12deg"] = dic_dataSet2

dic_dataCycle1, dic_dataSeq1 = sortData(dic_data_tempe["25deg"])
dic_dataCycle2, dic_dataSeq2 = sortData(dic_data_tempe["12deg"])

plotVoltageTimeDiffTempe(dic_data_tempe["25deg"], dic_data_tempe["12deg"], nbCycle1, nbCycle2)

plotShow()

bat_data = 0
current_cycle = 10

##########
# plot a voltage/capacity curve for 12°C and 25°C on one figure
##########
x1 = dic_dataSeq1["T_c"][current_cycle]
y1 = dic_dataSeq1["V_c"][current_cycle]
x2 = dic_dataSeq2["T_c"][current_cycle]
y2 = dic_dataSeq2["V_c"][current_cycle]


#plotVoltageCapacity(dic_dataSeq1["V_c"][10], dic_dataSeq1["Q_c"][10], 0)
#plotVoltageCapacity(dic_dataSeq2["V_c"][10], dic_dataSeq2["Q_c"][10], 0)


# plotCurve1yAxis(x1, y1, VOLTAGE_LABEL,
# CAPACITY_LABEL, 'green', bat_data, '25°C')
# plotCurve1yAxis(x2, y2, VOLTAGE_LABEL,
# CAPACITY_LABEL, 'orange', bat_data, '12°C')


"""plt.title(
    'Capacity in function of voltage for one charge for two different temperatures')
plt.grid(linestyle='-', linewidth=0.5)
plotShow()"""


##########


#plotTestbenchICASeq(dic_dataSeq1, 15)
title = 'Voltage of 15 cycles in function of time for Bat1 at 25°C (50A/30A)'

#plotTestbenchOverlaidCurves(dic_dataCycle1, "t_cycle", "v_cycle", TIME_LABEL, VOLTAGE_LABEL, title, 15)

x = dic_dataSeq1["T_c"][9]
y1 = dic_dataSeq1["V_c"][9]
y2 = dic_dataSeq1["Q_c"][9]

#plotCurve2yAxis(x, y1, y2, 'Charge capacity and battery voltage through time for one charge', TIME_LABEL, VOLTAGE_LABEL, CAPACITY_LABEL)


#percentageCapa(x, y1, y2)
