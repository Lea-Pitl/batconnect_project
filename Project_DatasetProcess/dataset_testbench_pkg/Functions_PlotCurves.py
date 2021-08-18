################     LAAS STAGE      ##############################################################
# FUNCTIONFILE TO PLOT CURVES FROM A CSV FILE
# Author : Léa Pitault
# Date : 2021/07/12
###################################################################################################

from dataset_testbench_pkg import *
from .Functions_ComputeData import *
from .Functions_Filter import *
from .constants import *
import matplotlib.pyplot as plt

##################################################################################################
#                    FUNCTIONS TO PLOT DATA
##################################################################################################

#################################################


def plotShow():
    """
    plotShow : Function to show the plot

    Parameters :
        - title (str) : title of the graph
    """
    # plt.grid(linestyle='-', linewI_dth=0.5)
    plt.legend()
    plt.show()


#################################################


def plotCurve1yAxis(x, y, xlabel, ylabel, color, bat_data):
    """
    plotCurve2yAxis : Plot a curve from parameters x and one y axis

    Parameters :
        - x (list) and y (list) : Data to plot
        - xlabel (str) and ylabel (str) : title of the axis
        - color (str) : color of the dataset points
        - bat_data (bool) : 0 -> laas testbench data
                            1 -> batconnect data
    """
    plt.xlabel(xlabel)
    plt.ylabel(ylabel, color=color)
    plt.plot(x, y, color=color )#, marker='o')
    plt.tick_params(axis='y', labelcolor=color)
    if bat_data==1:
        plt.xticks(rotation=45)


    plt.grid(linestyle='-', linewidth=0.5)
    # plt.title(title)
    # plt.legend()
    # plt.show()


#################################################

def plotCurve2yAxis(x, y1, y2, title, xlabel, y1label, y2label):
    """
    plotCurve2yAxis : Plot a curve from parameters x and two y axis

    Parameters : 
        - x,y1 and y2 (lists) : Data to plot
        - title (str) : title of the graph
        - xlabel and y-labels (str) : title of the axis
    """
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(y1label, color=color)
    ax1.plot(x, y1, color=color)  # , marker='o')
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    # we already handled the x-label with ax1
    ax2.set_ylabel(y2label, color=color)
    ax2.plot(x, y2, color=color)  # , marker='x')
    ax2.tick_params(axis='y', labelcolor=color)

    plt.grid(linestyle='-', linewidth=0.5)
    plt.title(title)
    plt.legend()
    plt.show()


#################################################

def plotCurves(x1, x2, y1, y2, labelx1, labely1, labelx2, labely2, title1, title2, marker):
    """
    plotCurves : Plot curves on different figures (x1/y1 ; x2/y2)

    Parameters :
        - x & y (lists) : datas
        - labels (str) : title of the different axis
        - title1 & title2 (str) : titles of the graphs
        - marker : marker for the plots, <see matplolib.markers>
    """

    plot1 = plt.figure(1)

    color = 'tab:red'
    plt.xlabel(labelx1)
    plt.ylabel(labely1, color=color)
    plt.plot(x1, y1, color=color, marker=marker)
    plt.tick_params(axis='y', labelcolor=color)
    plt.title(title1)

    plot2 = plt.figure(2)

    color = 'tab:blue'
    plt.xlabel(labelx2)
    plt.ylabel(labely2, color=color)
    plt.plot(x2, y2, color=color, marker=marker)
    plt.tick_params(axis='y', labelcolor=color)

    plt.grid(linestyle='-', linewidth=0.5)
    plt.title(title2)
    plt.legend()
    plt.show()


##################################################################################################
#                    PLOT SPECIFIC DATA (Voltage, current, capacity)
##################################################################################################

#################################################

def plotCurrentVoltage(time, current, voltage):
    """
    plotCurrentVoltage : Plot curves of current and voltage in funciton of time on two different figures

    Parameters :
        - time, current, voltage (lists) : data lists
    """

    plot1 = plt.figure(1)
    color = 'tab:red'

    plotCurve1yAxis(time, current, TIME_LABEL, CURRENT_LABEL, color)
    plt.title('Current in function of time')
    plt.grid(linestyle='-', linewidth=0.5)
    color = 'tab:blue'

    plot1 = plt.figure(2)

    plotCurve1yAxis(time, voltage, TIME_LABEL, VOLTAGE_LABEL, color)
    plt.title('Voltage in function of time')
    plt.grid(linestyle='-', linewidth=0.5)

    plotShow()


#################################################

def plotVoltageCapacity(voltage, capacity):
    """
    plotVoltageCapacity : Plot the capacity in function of voltage

    Parameters :
        - voltage, capacity (lists) : data lists
    """

    plotCurve1yAxis(voltage, capacity, VOLTAGE_LABEL, CAPACITY_LABEL, 'green')
    plt.title('Capacity in function of voltage')
    plt.grid(linestyle='-', linewidth=0.5)

    plotShow()


#################################################

def plotVoltageICA(voltage, ICA):
    """
    plotVoltageICA : Plot dQ/dV in function of voltage

    Parameters :
        - voltage, ICA (lists) : data lists
    """

    plotCurve1yAxis(voltage, ICA, VOLTAGE_LABEL, ICA_LABEL)
    plt.title('ICA')
    plt.grid(linestyle='-', linewidth=0.5)

    plotShow()


#################################################

def plotOverlaidCurves(dic_data, x_str, y_str, x_label, y_label, title, nb_cycle):
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


def plotICASeq(dic_dataSeq):
    """
    plotICASeq : global function to filter the data and plot the ICA

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
