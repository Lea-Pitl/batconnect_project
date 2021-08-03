################     LAAS STAGE      ################
# Functions File to plot Curves from a csv file
# Author : Léa Pitault
# Date : 2021/07/12
#####################################################


#################################################
#                   IMPORT
#################################################

import Functions_PlotCurves as F_plot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#################################################
#                   VARIABLES
#################################################

file_title = '20210729_Cycle50A_LiFePO4_BATCONNECT_bat3_CA1.txt'

#####################################################################
#                           MAIN
#####################################################################

########################
#       LEA DATASET
########################

dic_dataSet, nbCycle, nbSeq = F_plot.readFile(file_title)

#F_plot.plotCurrentVoltage(dic_dataSet["time"], dic_dataSet["current"], dic_dataSet["voltage"])

dic_dataCycle, dic_dataSeq = F_plot.sortData(dic_dataSet)
#F_plot.plotVoltageCapacity(dic_dataSeq["V_c"][1],dic_dataSeq["Q_c"][1])

#F_plot.plotICASeq(dic_dataSeq)
title ='Capacity of 15 cycles in function of voltage'

F_plot.plotOverlaidCurves(dic_dataSeq, "V_c", "Q_c", F_plot.VOLTAGE_LABEL, F_plot.CAPACITY_LABEL, title, 15)