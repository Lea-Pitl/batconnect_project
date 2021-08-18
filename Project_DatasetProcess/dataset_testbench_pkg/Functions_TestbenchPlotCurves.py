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
            x[i].append(dic_data[x_str][i+1][j])  # - dic_data[x_str][i+1][0])
            y[i].append(dic_data[y_str][i+1][j])
        plt.plot(x[i], y[i])

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(linestyle='-', linewidth=0.5)
    plt.legend(legend, loc='upper left')
    plt.show()

#################################################


def plotTestbenchICASeq(dic_dataSeq):
    """
    plotTestbenchICASeq : global function to filter the data and plot the ICA

    Parameters :    
        - dic_dataSeq (dict) : dictionary of the data to plot
    """

    legend = []
    for i in range(0, 15):
        x = dic_dataSeq["V_c"][i+1]
        y = dic_dataSeq["Q_c"][i+1]
        x_new, y_new = capaFilter(x, y, 0.1)

        ICA, V = calculICA(x_new, y_new, 1, 3.6, 3.1)

        y_sf = ICAFilter(ICA, 51, 3)
        legend.append('Cycle ' + str(i))
        plt.plot(V, y_sf)

    plt.title('ICA Curve for charges at 30A')
    plt.xlabel(VOLTAGE_LABEL)
    plt.ylabel(ICA_LABEL)
    plt.grid(linestyle='-', linewidth=0.5)
    plt.legend(legend, loc='upper left')
    plt.show()
