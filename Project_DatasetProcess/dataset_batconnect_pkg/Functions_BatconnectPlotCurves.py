################     LAAS STAGE      ##############################################################
# UTILITIES FUNCTION FILE TO PLOT CURVES FROM THE TESTBENCH SPECIFIC DATA
# Author : Léa Pitault
# Date : 2021/07/12
###################################################################################################

from dataset_batconnect_pkg import *
from dataset_batconnect_pkg.bat_constants import *
from utilities_pkg import *

##################################################################################################
#                    FUNCTIONS TO PLOT DATA
##################################################################################################

#################################################

def plotBatconnectVoltageCapa(dic_dataset_sort_id, current_id):
    """
    plotBatconnectVoltageCapa : Plot two graphs with the voltage vs time 
    and the capacity vs time for a given battery
    
    Parameters : 
        - dic_datasert_sort_id (dict) : sorted values dictionnary
        - current_id (int) : Id of the battery to study
    """
    
    print("Current ID of the studied battery : ", current_id)

    # Data of the axes of the first graph
    x1 = dic_dataset_sort_id[current_id]["date"]
    y1 = dic_dataset_sort_id[current_id]["voltage"]
    title1 = 'Voltage of the total 16 cells for one battery in function of time'

    # Data of the axes of the second graph
    x2 = dic_dataset_sort_id[current_id]["date"]
    y2 = dic_dataset_sort_id[current_id]["charge"]
    title2 = 'State of charge of one battery in function of time'

    #Plot two different graphs with the data
    plotCurves(x1, x2, y1, y2, BAT_TIME_LABEL, BAT_VOLTAGE_LABEL,
            BAT_TIME_LABEL, BAT_CAPACITY_LABEL, title1, title2, '.')
