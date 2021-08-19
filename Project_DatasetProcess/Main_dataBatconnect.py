################     LAAS STAGE      ##############################################################
# FUNCTION FILE TO PLOT CURVES FROM A CSV FILE
# Author : Léa Pitault
# Date : 2021/08/16
###################################################################################################


#################################################
#                   IMPORTS
#################################################

from Project_DatasetProcess.dataset_batconnect_pkg.Functions_BatconnectSortData import getIDBatteries
from utilities_pkg import *
from dataset_batconnect_pkg.bat_constants import *
from dataset_batconnect_pkg import *
from dataset_testbench_pkg import *


#################################################
#                   VARIABLES
#################################################

file_title = 'Batconnect_files/batconnect_out_date.csv'

###################################################################################################
#                           MAIN
###################################################################################################

################################
#       BATCONNECT DATASET
################################

dic_bat_dataSet, line, data_line = readBatFile(
    file_title, BAT_LINE_BEGIN, BAT_LINE_END)

# dic_bat_dataSet["date"]=date

dic_dataset_id, dic_bat_not_ok = sortBatDataByValues(dic_bat_dataSet, data_line)

print("len status not 0 : ", len(dic_bat_not_ok["voltage"][1]))

x1 = dic_dataset_id["date"][0]
y1 = dic_dataset_id["voltage"][0]

x2 = dic_dataset_id["date"][0]
y2 = dic_dataset_id["charge"][0]

title1 = 'Voltage of the total 16 cells for one battery in function of time'
title2 = 'State of charge of the battery in function of time'

plotCurves(x1, x2, y1, y2, BAT_TIME_LABEL, BAT_VOLTAGE_LABEL,
           BAT_TIME_LABEL, BAT_CAPACITY_LABEL, title1, title2, '.')
