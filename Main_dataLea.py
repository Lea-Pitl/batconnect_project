################     LAAS STAGE      ################
# Functions File to plot Curves from a csv file
# Author : Léa Pitault
# Date : 2021/07/12
#####################################################


#################################################
#                   IMPORT
#################################################

import Functions_PlotCurves as F_plot

#################################################
#                   VARIABLES
#################################################

file_title = '20210722_Cycle50A_LiFePO4_BATCONNECT_CA1.txt'

#####################################################################
#                           MAIN
#####################################################################

########################
#       LEA DATASET
########################

dic_dataSet, nbCycle, nbSeq = F_plot.readFile(file_title)

#F_plot.plotCurrentVoltage(dic_ataSet["time"], dic_dataSet["current"], dic_dataSet["voltage"])

dic_dataCycle, dic_dataSeq = F_plot.sortData(dic_dataSet)
#F_plot.plotVoltageCapacity(dic_dataSeq["V_c"][1],dic_dataSeq["Q_c"][1])

F_plot.plotICASeq(dic_dataSeq)
