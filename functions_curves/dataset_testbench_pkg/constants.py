################     LAAS STAGE      ##############################################################
# File with all the useful constants
# Author : Léa Pitault
# Date : 2021/08/05
###################################################################################################

#                           CONSTANTS

###################################################################################################

#LABELS
TIME_LABEL = 'Time (s)'
CURRENT_LABEL = 'Current (A)'
VOLTAGE_LABEL = 'Voltage (V)'
CAPACITY_LABEL = 'Capacity (A.h)'
ICA_LABEL = 'ICA dQ/dV'

#####################################################
#           FOR TESTBENCH FILES
#####################################################
CV_LOW = 3.6498
CV_HIGH = 3.6599

# columns of the CSV FILE HEADERS from the testbench
SEQUENCE = 0
TIME = 1
CYCLE = 2
VOLTAGE = 3
CURRENT = 4
CHARGE = 5
DISCHARGE = 6
TEMPERATURE = 7


#####################################################
#               FOR BATCONNECT FILES
#####################################################

BAT_LINE_BEGIN = 20870
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
