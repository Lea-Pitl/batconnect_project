################     LAAS STAGE      ##############################################################
# FUNCTION FILE TO PLOT CURVES FROM A CSV FILE
# Author : Léa Pitault
# Date : 2021/08/16
###################################################################################################


#################################################
#                   IMPORTS
#################################################

from dataset_batconnect_pkg.Functions_BatconnectSortData import *
from dataset_batconnect_pkg.Functions_BatconnectPlotCurves import *
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

#Sort the data in a dictionnary of dictionnary : dict[id][measure]
dic_dataset_sort_id = read_sortBatFile(
    file_title, BAT_LINE_BEGIN, BAT_LINE_END)

#Get a list of all the different battery ID
IDs = getIDBatteriesFromDict(dic_dataset_sort_id)

current_id=IDs[1]

plotBatconnectVoltageCapa(dic_dataset_sort_id, current_id)
