################     LAAS STAGE      ################
# Functions File to plot Curves from a csv file
# Author : Léa Pitault
# Date : 2021/08/16
#####################################################


#################################################
#                   IMPORT
#################################################

from dataset_testbench_pkg import *
from dataset_batconnect_pkg import *


#################################################
#                   VARIABLES
#################################################

file_title = 'Batconnect_files/batconnect_out_date.csv'

#####################################################################
#                           MAIN
#####################################################################

################################
#       BATCONNECT DATASET
################################

dic_bat_dataSet, line, data_line = readBatFile(file_title)

# dic_bat_dataSet["date"]=date
#x, y = sortBatData(dic_bat_dataSet, data_line)
# print(dic_bat_dataSet["date"])
#plotCurve1yAxis(x, y, BAT_TIME_LABEL, BAT_VOLTAGE_LABEL, 'blue', 1)
plt.title("Voltage of the total 16 cells in function of time")
plt.legend()
plt.show()
