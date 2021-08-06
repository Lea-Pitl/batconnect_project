################     LAAS STAGE      ################
# Functions File to plot Curves from a csv file
# Author : Léa Pitault
# Date : 2021/08/05
#####################################################

#       CONSTANTS

#################################################

TIME_LABEL = 'Time (s)'
CURRENT_LABEL = 'Current (A)'
VOLTAGE_LABEL = 'Voltage (V)'
CAPACITY_LABEL = 'Capacity (A.h)'
ICA_LABEL = 'ICA dQ/dV'
CV_LOW = 3.6498
CV_HIGH = 3.6599

# columns of the CSV FILE HEADERS
SEQUENCE = 0
TIME = 1
CYCLE = 2
VOLTAGE = 3
CURRENT = 4
CHARGE = 5
DISCHARGE = 6
TEMPERATURE = 7
