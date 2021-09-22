################     LAAS STAGE      ##############################################################
# MAIN FILE TO PROCESS THE LAAS TESTBENCH VALUES
# Author : Léa Pitault
# Date : 2021/07/12
###################################################################################################


#################################################
#                   IMPORTS
#################################################

from dataset_testbench_pkg.Functions_TestbenchComputeData import *
from dataset_testbench_pkg.Functions_TestbenchPlotCurves import *
from utilities_pkg.Utilities_PlotCurves import *
from utilities_pkg import *
from dataset_testbench_pkg import *

#################################################
#                   VARIABLES
#################################################
# 'dataset_testbench_files/20210803_Cycle50A_LiFePO4_BATCONNECT_bat2_CA5.txt'
file_title0 = 'dataset_testbench_files/20210827_50Cycle50A_25deg_LiFePO4_BATCONNECT_bat4_CA5.txt'
file_title1 = 'dataset_testbench_files/20210817_Cycle50A_12deg_LiFePO4_BATCONNECT_bat1_CA1.txt'
#file_title2 = 'dataset_testbench_files/20210803_Cycle50A_LiFePO4_BATCONNECT_bat1_CA1.txt'
file_title3 = 'dataset_testbench_files/20210823_Cycle50A_35deg_LiFePO4_BATCONNECT_bat1_CA1.txt'
file_title2 = 'dataset_testbench_files/20210729_Cycle50A_LiFePO4_BATCONNECT_bat3_CA1.txt'
###################################################################################################
#                           MAIN
###################################################################################################

########################
#       LEA DATASET
########################
print('         ################################ \n '
      'Sort data according to the cycles and the sequences \n'
      '         ################################')
dic_dataSet0, nbCycle0, nbSeq0 = readFile(file_title0)
dic_dataSet1, nbCycle1, nbSeq1 = readFile(file_title1)
dic_dataSet2, nbCycle2, nbSeq2 = readFile(file_title2)
dic_dataSet3, nbCycle3, nbSeq3 = readFile(file_title3)

dic_data_tempe = {}
dic_data_tempe["12deg"] = dic_dataSet1
dic_data_tempe["25deg"] = dic_dataSet2
dic_data_tempe["35deg"] = dic_dataSet3

dic_dataCycle0, dic_dataSeq0 = sortData(dic_dataSet0)
dic_dataCycle1, dic_dataSeq1 = sortData(dic_data_tempe["12deg"])
dic_dataCycle2, dic_dataSeq2 = sortData(dic_data_tempe["25deg"])
dic_dataCycle3, dic_dataSeq3 = sortData(dic_data_tempe["35deg"])

##########
# plot voltage curves in function of time for 15 cycles and 2 different temperatures
##########
current_title = 'Current in function of time for 50 cycles at 25°C for Bat n°3'
volt_title = 'Voltage in function of time for 50 cycles at 25°C for Bat n°3'
titleVoltCurrent = 'Voltage and current in function of time for 15 cycles at 25°C for Bat n°2'
#plotCurve2yAxis(dic_dataSet1["time"], dic_dataSet1["current"], dic_dataSet1["voltage"],titleVoltCurrent, TIME_LABEL,CURRENT_LABEL, VOLTAGE_LABEL)
#plotCurrentVoltage(dic_dataSet0["time"], dic_dataSet0["current"], dic_dataSet0["voltage"], 0, '25°C', current_title, volt_title)
#plotVoltageTimeDiffTempe(dic_data_tempe["12deg"], dic_data_tempe["25deg"], dic_data_tempe["35deg"], nbCycle1, nbCycle2, nbCycle3)
# plotShow()

##########


##########
# plot a voltage/capacity curve for 12°C, 25°C and 35°C on one figure
##########
bat_data = 0
current_cycle = 48

"""x1 = dic_dataSeq1["V_c"][current_cycle]
y1 = dic_dataSeq1["Q_c"][current_cycle]
x2 = dic_dataSeq2["V_c"][current_cycle]
y2 = dic_dataSeq2["Q_c"][current_cycle]
x3 = dic_dataSeq3["V_c"][current_cycle]
y3 = dic_dataSeq3["Q_c"][current_cycle]

getMaxCapa(dic_dataSeq1, current_cycle)
getMaxCapa(dic_dataSeq2, current_cycle)
getMaxCapa(dic_dataSeq3, current_cycle)

plotCurve1yAxis(x1, y1, VOLTAGE_LABEL,
 CAPACITY_LABEL, 'green', bat_data, '25°C')
plotCurve1yAxis(x2, y2, VOLTAGE_LABEL,
 CAPACITY_LABEL, 'orange', bat_data, '12°C')
plotCurve1yAxis(x3, y3, VOLTAGE_LABEL,
 CAPACITY_LABEL, 'blue', bat_data, '35°C')

plt.title('Capacity in function of voltage for one charge at different temperatures for Bat n°1')
plt.grid(linestyle='-', linewidth=0.5)
plotShow()"""


##########


##########
# plot ICA curves
##########
#plotTestbenchICASeq(dic_dataSeq0, int(nbCycle0))


##########


#plotTestbenchICASeq(dic_dataSeq1, 15)
title = 'Voltage of 50 cycles in function of time for Bat n°3 at 25°C (50A/30A)'

#plotTestbenchOverlaidCurves(dic_dataCycle0, "t_cycle", "v_cycle", TIME_LABEL, VOLTAGE_LABEL, title, nbCycle0)

x = dic_dataSeq0["T_c"][current_cycle]
y1 = dic_dataSeq0["V_c"][current_cycle]
y2 = dic_dataSeq0["Q_c"][current_cycle]

percentageCapa(x, y1, y2)
plotCurve2yAxis(x, y1, y2, 'Charge capacity and battery voltage through time for one charge at 25°C (Bat n°3)', TIME_LABEL, VOLTAGE_LABEL, CAPACITY_LABEL)


##########
# Plot the capacity in function of the cycle
"""capa = []
cycle = []
for i in range(1,int(nbCycle2)):
    capa.append(getMaxCapa(dic_dataSeq2, i))
    cycle.append(i)

print(cycle)
print("max capa des 15 cycles :", capa )

plotCurve1yAxis(cycle,capa,"Cycle (n)", CAPACITY_LABEL,'orange',0,'25°C')
plt.title("Max capacity in function of the first 15 cycles for the Bat n°3 at 25°C")
plotShow()"""