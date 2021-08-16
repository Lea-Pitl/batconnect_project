################     LAAS STAGE      ##############################################################
# File with all the useful constants for the BATCONNECT Dataset
# Author : Léa Pitault
# Date : 2021/08/16
###################################################################################################

#                           CONSTANTS

###################################################################################################

#LABELS
BAT_TIME_LABEL = 'Time (s)'
BAT_CURRENT_LABEL = 'Current (A)'
BAT_VOLTAGE_LABEL = 'Voltage (V)'
BAT_CAPACITY_LABEL = 'Capacity (A.h)'
BAT_ICA_LABEL = 'ICA dQ/dV'

#####################################################
#               FOR BATCONNECT FILES
#####################################################

BAT_LINE_BEGIN = 20869
BAT_LINE_END = 105965

# columns of the CSV FILE HEADERS from the batconnect datafile
BAT_ID = 0
BAT_TIME = 1
BAT_DATE = 2
BAT_STATUS = 3
BAT_LATITUDE = 4
BAT_LONGITUDE = 5
BAT_VOLTAGE = 6
BAT_CHARGE = 7
BAT_CURRENT = 8
BAT_TEMPE_MIN = 17
BAT_TEMPE_MAX = 16
