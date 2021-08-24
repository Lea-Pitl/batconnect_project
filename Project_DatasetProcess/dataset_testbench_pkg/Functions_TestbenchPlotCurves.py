################     LAAS STAGE      ##############################################################
# UTILITIES FUNCTION FILE TO PLOT CURVES FROM THE TESTBENCH SPECIFIC DATA
# Author : Léa Pitault
# Date : 2021/07/12
###################################################################################################

from dataset_testbench_pkg import *
from .Functions_TestbenchComputeData import *
from .Functions_TestbenchFilter import *
from .constants import *
import matplotlib.pyplot as plt

##################################################################################################
#                    FUNCTIONS TO PLOT DATA
##################################################################################################

#################################################


def plotTestbenchOverlaidCurves(dic_data, x_str, y_str, x_label, y_label, title, nb_cycle):
    """Overlay the voltages curves on one plot

    Parameters :    
        - dic_data (dict) : data dictionary of the cycles of the sequences
        - x_str (str) : string for the dictionary ; x-values
        - y_str (str) : string for the dictionary ; y-values
        - x_label & y_label (str) : label for the axis
        - title (str) : title of the graph
        - nb_cycle (int) : number of cycles (== number of curves to plot)
    """

    legend = []
    x = []
    y = []

    for i in range(0, nb_cycle):
        legend.append('Cycle ' + str(i))
        x.append([])
        y.append([])

        for j in range(len(dic_data[x_str][i+1])):
            x[i].append((dic_data[x_str][i+1][j]) - dic_data[x_str][i+1][0])
            y[i].append(dic_data[y_str][i+1][j])
        plt.plot(x[i], y[i])

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(linestyle='-', linewidth=0.5)
    plt.legend(legend, loc='upper left')
    plt.show()

#################################################


def plotTestbenchICASeq(dic_dataSeq, nb_cycle):
    """
    plotTestbenchICASeq : global function to filter the data and plot the ICA

    Parameters :    
        - dic_dataSeq (dict) : dictionary of the data to plot
        - nb_cycle (int) : number of cycle to plot
    """

    legend = []
    for i in range(0, nb_cycle):
        x = dic_dataSeq["V_c"][i+1]
        y = dic_dataSeq["Q_c"][i+1]
        x_new, y_new = capaFilter(x, y, 0.1)

        ICA, V = calculICA(x_new, y_new, 1, 3.6, 3.1)

        y_sf = ICAFilter(ICA, 51, 3)
        legend.append('Cycle ' + str(i))
        plt.plot(V, y_sf)

    plt.title('ICA Curves for 15 cycles for charges at 30A (bat1 at 25°C)')
    plt.xlabel(VOLTAGE_LABEL)
    plt.ylabel(ICA_LABEL)
    plt.grid(linestyle='-', linewidth=0.5)
    plt.legend(legend, loc='upper left')
    plt.show()


#################################################
def plotVoltageTimeDiffTempe(dic_data_25, dicdata_12, nb_cycle_25, nb_cycle_12):
    time = []
    voltage = []
    current = []
    time2 = []
    current2 = []
    voltage2 = []
    found1 = 0
    found2 = 0

    for i in range(len(dic_data_25["time"])):
        if dic_data_25["cycles"][i] > 0:
            if not(found1):
                idx1_begin = i
                found1 = 1
            time.append(dic_data_25["time"][i]-dic_data_25["time"][idx1_begin])
            current.append(dic_data_25["current"][i])
            voltage.append(dic_data_25["voltage"][i])

    for i in range(len(dicdata_12["time"])):
        if dicdata_12["cycles"][i] > 0:
            if not(found2):
                idx2_begin = i
                found2 = 1
            time2.append(dicdata_12["time"][i]-dicdata_12["time"][idx2_begin])
            current2.append(dicdata_12["current"][i])
            voltage2.append(dicdata_12["voltage"][i])

    print('indice debut cycle 1 : ', idx1_begin)
    print('indice debut cycle 1 : ', idx2_begin)
    
    print('----- Total time for the cycles -----')
    print('Total time for the 15 cycles at 25°C : ') 
    printTime(time[-1])
    print('Total time for the 15 cycles at 12°C : ') 
    printTime(time2[-1])
    print('Time average over one cycle at 25°C : ')
    printTime(time[-1]/nb_cycle_25)
    print('Time average over one cycle at 12°C : ') 
    printTime(time2[-1]/nb_cycle_12)

    plotCurve1yAxis(time, voltage, TIME_LABEL, VOLTAGE_LABEL, 'blue', 0, '25°C')
    plotCurve1yAxis(time2, voltage2, TIME_LABEL, VOLTAGE_LABEL, 'orange', 0, '12°C')

    plt.title(
    'Voltage in function of time for 15 cycles for two different temperatures (Bat1)')

    plotShow()


def printTime(seconds_time):
    days = seconds_time // SECONDS_IN_DAY
    hours = (seconds_time - (days * SECONDS_IN_DAY)) // SECONDS_IN_HOUR
    minutes = (seconds_time - (days * SECONDS_IN_DAY) - (hours * SECONDS_IN_HOUR)) // SECONDS_IN_MINUTE

    print('d:h:m -> %d:%d:%d' % (days, hours, minutes))