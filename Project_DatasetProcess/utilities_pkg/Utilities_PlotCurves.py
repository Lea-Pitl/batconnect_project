################     LAAS STAGE      ##############################################################
# YTULITIES FUNCTION FILE TO PLOT CURVES
# Author : Léa Pitault
# Date : 2021/07/12
###################################################################################################

from dataset_testbench_pkg import *
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

def plotCurrentVoltage(time, current, voltage, bat_data):
    """
    plotCurrentVoltage : Plot curves of current and voltage in funciton of time on two different figures

    Parameters :
        - time, current, voltage (lists) : data lists
    """

    plot1 = plt.figure(1)
    color = 'tab:red'

    plotCurve1yAxis(time, current, TIME_LABEL, CURRENT_LABEL, color, bat_data)
    plt.title('Current in function of time')
    plt.grid(linestyle='-', linewidth=0.5)
    color = 'tab:blue'

    plot1 = plt.figure(2)

    plotCurve1yAxis(time, voltage, TIME_LABEL, VOLTAGE_LABEL, color, bat_data)
    plt.title('Voltage in function of time')
    plt.grid(linestyle='-', linewidth=0.5)

    plotShow()


#################################################

def plotVoltageCapacity(voltage, capacity, bat_data):
    """
    plotVoltageCapacity : Plot the capacity in function of voltage

    Parameters :
        - voltage, capacity (lists) : data lists
    """

    plotCurve1yAxis(voltage, capacity, VOLTAGE_LABEL, CAPACITY_LABEL, 'green', bat_data)
    plt.title('Capacity in function of voltage')
    plt.grid(linestyle='-', linewidth=0.5)

    plotShow()


#################################################

def plotVoltageICA(voltage, ICA, bat_data):
    """
    plotVoltageICA : Plot dQ/dV in function of voltage

    Parameters :
        - voltage, ICA (lists) : data lists
    """

    plotCurve1yAxis(voltage, ICA, VOLTAGE_LABEL, ICA_LABEL, bat_data)
    plt.title('ICA')
    plt.grid(linestyle='-', linewidth=0.5)

    plotShow()
