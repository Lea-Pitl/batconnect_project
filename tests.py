
import Functions_PlotCurves as F_plot
 # 20210716_Cycle10A_LiFePO4_BATCONNECT_CA2.txt
 #'20210722_Cycle50A_LiFePO4_BATCONNECT_CA1.txt'
file_title = '20210722_Cycle50A_LiFePO4_BATCONNECT_CA1.txt'
title = 'test'

#####################################################################
#                           MAIN
#####################################################################

########################
#       LEA DATASET
########################
dic_dataSet, nbCycle, nbSeq = F_plot.readFile(file_title)

#F_plot.plotCurrentVoltage(dic_dataSet["time"],dic_dataSet["current"],dic_dataSet["voltage"])
dic_dataCycle, dic_dataSeq = F_plot.sortData(dic_dataSet)

#F_plot.plotVoltageCapacity(dic_dataSeq["V_c"][2],dic_dataSeq["Q_c"][2])

F_plot.plotICASeq(dic_dataSeq)
