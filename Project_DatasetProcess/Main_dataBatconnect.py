################     LAAS STAGE      ##############################################################
# FUNCTION FILE TO PLOT CURVES FROM A CSV FILE
# Author : Léa Pitault
# Date : 2021/08/16
###################################################################################################


#################################################
#                   IMPORTS
#################################################

from dataset_batconnect_pkg.Functions_BatconnectSortData import *
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

########################
# Test generaux de lecture puis de tri
########################

dic_dataset_sort_id = read_sortBatFile(
    file_title, BAT_LINE_BEGIN, BAT_LINE_END)

IDs = getIDBatteriesFromDict(dic_dataset_sort_id)
nb = getNumberOfIDsFromDict(dic_dataset_sort_id)
print("dic_dataset_sort_id --> ID1 : ", IDs[0], " ; voltage: ", len(
    dic_dataset_sort_id[IDs[0]]["voltage"]))


x1 = dic_dataset_sort_id[IDs[1]]["date"]
y1 = dic_dataset_sort_id[IDs[1]]["voltage"]

x2 = dic_dataset_sort_id[IDs[1]]["date"]
y2 = dic_dataset_sort_id[IDs[1]]["charge"]

title1 = 'Voltage of the total 16 cells for one battery in function of time'
title2 = 'State of charge of the battery in function of time'

plotCurves(x1, x2, y1, y2, BAT_TIME_LABEL, BAT_VOLTAGE_LABEL,
          BAT_TIME_LABEL, BAT_CAPACITY_LABEL, title1, title2, '.')
