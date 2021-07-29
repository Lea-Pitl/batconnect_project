################     LAAS STAGE      ################
# Functions File to plot Curves from a csv file
# Author : Léa Pitault
# Date : 2021/07/12
#####################################################


#################################################
#                   IMPORT
#################################################

#from typing import Sequence, Tuple
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import pandas as pd
import csv
import Functions_PlotCurves as F_plot


#################################################
#                   VARIABLES
#################################################

fileTitle = 'BAT1_MargotDataset.txt'
title = 'test'

#####################################################################
#                           MAIN
#####################################################################

########################
# EXEMPLE MARGOT DATASET
########################

dataSet, nbCycle, nbSeq = F_plot.readFile(fileTitle)


#F_plot.plotCurrentVoltage(time, current, voltage)

dataCycle, dataSeq = F_plot.sortData(dataSet)
ICA, V = F_plot.calculICA(dataSeq["Vc"][1], dataSeq["Qc"][1],0)
#F_plot.plotVoltageCapacity(dataSeq["Vc"][3], dataSeq["Qc"][3])

F_plot.plotVoltageICA(V, ICA)



#print(dataSeq["Td"][2])

#F_plot.plotVoltageCapacity(dataSeq["Vd"][2],dataSeq["Qd"][2])
