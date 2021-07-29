
from typing import Sequence, Tuple
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import pandas as pd
import csv
import Functions_PlotCurves as F_plot
import scipy.signal
from scipy.interpolate import splrep, splev
import statsmodels.api as sm


file_title = '20210722_Cycle50A_LiFePO4_BATCONNECT_CA1.txt'
title = 'test'

#####################################################################
#                           MAIN
#####################################################################

########################
#       LEA DATASET
########################
dic_dataSet, nbCycle, nbSeq = F_plot.readFile(file_title)

#F_plot.plotCurrentVoltage(dataSet["time"], dataSet["current"], dataSet["voltage"])

dic_dataCycle, dic_dataSeq = F_plot.sortData(dic_dataSet)
F_plot.plotICASeq(dic_dataSeq)
