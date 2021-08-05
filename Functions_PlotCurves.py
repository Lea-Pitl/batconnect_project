################     LAAS STAGE      ################
# Functions File to plot Curves from a csv file
# Author : Léa Pitault
# Date : 2021/07/12
#####################################################

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import copy
from scipy.interpolate import splrep, splev
import statsmodels.api as sm
import scipy.signal


#################################################

TIME_LABEL = 'Time (s)'
CURRENT_LABEL = 'Current (A)'
VOLTAGE_LABEL = 'Voltage (V)'
CAPACITY_LABEL = 'Capacity (A.h)'
ICA_LABEL = 'ICA dQ/dV'
CV_LOW=3.6498
CV_HIGH=3.6599

# columns of the CSV FILE HEADERS
SEQUENCE = 0
TIME = 1
CYCLE = 2
VOLTAGE = 3
CURRENT = 4
CHARGE = 5
DISCHARGE = 6
TEMPERATURE = 7


##################################################################################################
#                    FUNCTIONS TO READ FILE AND SORT THE DATA
##################################################################################################

#################################################

def readFile(file_title):
    """
    readFile : Read a csv file and create lists from the different columns
    Parameters : 
        - file_title (str) : Title of the csv file to read
    Return :
        - dic_dataset (dict) : dictionary with the values from the csv file
        - nb_cycle (int) : number of cycle
        - nb_seq (int) : number of different sequences (charge CC, charge CV, discharge, rest, etc...)
    """

    sequence = []
    time = []
    cycles = []
    voltage = []
    current = []
    capacity_charge = []
    capacity_discharge = []
    temperature = []

    with open(file_title, mode='r') as csvfile:
        file = csv.reader(csvfile, delimiter='\t')
        line_count = 0
        for row in file:
            columns = len(row)
            for i in range(columns):
                row[i] = row[i].replace(',', '.')
            if line_count == 0:
                print(f'Columns headers are {", ".join(row)}')
            else:
                # row[0]=First column of the row -> sequence values
                sequence.append(float(row[SEQUENCE]))
                # row[1]=Second column of the row -> Time values
                time.append(float(row[TIME]))
                # row[2]=2nd column of the row -> Number of the cycle
                cycles.append(float(row[CYCLE]))
                # row[3]=3rd column of the row -> Voltage values
                voltage.append(float(row[VOLTAGE]))
                # row[4]=4th column of the row -> Current values
                current.append(float(row[CURRENT])/1000)
                # row[5]=5th column of the row -> Charge capacity values
                capacity_charge.append(float(row[CHARGE])/1000)
                # row[6]=6th column of the row -> Discharge capacity values
                capacity_discharge.append(float(row[DISCHARGE])/1000)
                # row[7]=7th column of the row -> Discharge capacity values
                temperature.append(float(row[TEMPERATURE]))
            line_count += 1
        nb_cycle = cycles[len(cycles)-1]
        nb_seq = sequence[len(sequence)-1]
    dic_dataset = {}
    dic_dataset["sequence"] = sequence
    dic_dataset["time"] = time
    dic_dataset["cycles"] = cycles
    dic_dataset["voltage"] = voltage
    dic_dataset["current"] = current
    dic_dataset["capacity_charge"] = capacity_charge
    dic_dataset["capacity_discharge"] = capacity_discharge
    dic_dataset["temperature"] = temperature
    dic_dataset["line_count"] = line_count

    return dic_dataset, nb_cycle, nb_seq


#################################################
def sortData(dataset):
    """
    sortData : create sublists from the datas depending on the cycle and the sequence
    Parameters : 
        - dataset (dict) : dictionary  
    Return :    
        - dic_data_cycle (dict) : dictionary with the data sorted by cycles (both charge and discharge)
        - dic_data_seq (dict) : dictionary with the data sorted by sequences (charge OR discharge)
    """

    print('         ################################ \n '
          'Sort data according to the cycles and the sequences \n'
          '         ################################')
    j = 0
    while j < len(dataset["cycles"]):
        dataset["cycles"][j] = int(dataset["cycles"][j])
        j += 1

    Nc = dataset["cycles"]
    num_cycle = np.unique(Nc)
    nb_cycle = len(num_cycle)

    # cycles
    t_cycle = []
    i_cycle = []
    v_cycle = []
    Q_c_cycle = []
    Q_d_cycle = []
    tempe_cycle = []

    # charge
    T_c = []
    V_c = []
    I_c = []
    Q_c = []
    tempe_c = []

    # discharge
    T_d = []
    V_d = []
    I_d = []
    Q_d = []
    tempe_d = []

    buff = 0

    for i in range(nb_cycle):
        t_cycle.append([])
        i_cycle.append([])
        v_cycle.append([])
        Q_c_cycle.append([])
        Q_d_cycle.append([])
        tempe_cycle.append([])
        T_d.append([])
        T_c.append([])
        V_d.append([])
        V_c.append([])
        tempe_c.append([])
        I_d.append([])
        I_c.append([])
        Q_d.append([])
        Q_c.append([])
        tempe_d.append([])

        n = num_cycle[i]
        index_cycle = np.where(Nc == n)

        for k in range(np.size(index_cycle)):
            # fill the list with the datas during the different cycles
            t_cycle[i].append(copy.deepcopy(dataset["time"][k+buff]))
            i_cycle[i].append(copy.deepcopy(dataset["current"][k+buff]))
            v_cycle[i].append(copy.deepcopy(dataset["voltage"][k+buff]))
            Q_c_cycle[i].append(copy.deepcopy(
                dataset["capacity_charge"][k+buff]))
            Q_d_cycle[i].append(copy.deepcopy(
                dataset["capacity_discharge"][k+buff]))
            tempe_cycle[i].append(copy.deepcopy(
                dataset["temperature"][k+buff]))

            # separate the cycles lists according to charge or discharge
            if (i_cycle[i][k] > 0):  # positive current -> charge
                T_c[i].append(t_cycle[i][k])
                V_c[i].append(v_cycle[i][k])
                I_c[i].append(i_cycle[i][k]/1000)
                Q_c[i].append(Q_c_cycle[i][k])
                tempe_c[i].append(tempe_cycle[i][k])

            else:  # negative current -> discharge
                T_d[i].append(i_cycle[i][k])
                V_d[i].append(v_cycle[i][k])
                I_d[i].append(i_cycle[i][k]/1000)
                Q_d[i].append(Q_d_cycle[i][k])
                tempe_d[i].append(tempe_cycle[i][k])

        buff = k+buff+1

        dic_data_cycle = {}
        dic_data_seq = {}
        dic_data_cycle["t_cycle"] = t_cycle
        dic_data_cycle["i_cycle"] = i_cycle
        dic_data_cycle["v_cycle"] = v_cycle
        dic_data_cycle["Q_c_cycle"] = Q_c_cycle
        dic_data_cycle["Q_d_cycle"] = Q_d_cycle
        dic_data_cycle["tempe_cycle"] = tempe_cycle
        dic_data_seq["T_d"] = T_d
        dic_data_seq["V_d"] = V_d
        dic_data_seq["I_d"] = I_d
        dic_data_seq["Q_d"] = Q_d
        dic_data_seq["tempe_d"] = tempe_d
        dic_data_seq["T_c"] = T_c
        dic_data_seq["V_c"] = V_c
        dic_data_seq["I_c"] = I_c
        dic_data_seq["Q_c"] = Q_c
        dic_data_seq["tempe_c"] = tempe_c

    return dic_data_cycle, dic_data_seq


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


def plotCurve1yAxis(x, y, xlabel, ylabel, color):
    """
    plotCurve2yAxis : Plot a curve from parameters x and one y axis

    Parameters :
        - x (list) and y (list) : Data to plot
        - title (str) : title of the graph
        - xlabel (str) and ylabel (str) : title of the axis
    """
    plt.xlabel(xlabel)
    plt.ylabel(ylabel, color=color)
    plt.plot(x, y, color=color)  # , marker='o')
    plt.tick_params(axis='y', labelcolor=color)

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

def plotCurves(x1, x2, y1, y2, labelx1, labely1, labelx2, labely2, title1, title2):
    """
    plotCurves : Plot curves on different figures (x1/y1 ; x2/y2)

    Parameters :
        - x & y (lists) : datas
        - labels (str) : title of the different axis
        - title (str) : title of the graph
    """

    plot1 = plt.figure(1)

    color = 'tab:red'
    plt.xlabel(labelx1)
    plt.ylabel(labely1, color=color)
    plt.plot(x1, y1, color=color, marker='o')
    plt.tick_params(axis='y', labelcolor=color)
    plt.title(title1)

    plot2 = plt.figure(2)

    color = 'tab:blue'
    plt.xlabel(labelx2)
    plt.ylabel(labely2, color=color)
    plt.plot(x2, y2, color=color, marker='o')
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


##################################################################################################
#                    CALCUL FUNCTIONS
##################################################################################################


def calculICA(voltage, capacity, charge, high_voltage, low_voltage):
    """CalculICA : Calcul the Incremental Capacity -> dQ/dV and create new list x and y to plot

    Parameters :    
        - voltage (list) : data dictionary of the cycles of the sequences
        - capacity (list) : string for the dictionary ; x-values
        - charge (list) : string for the dictionary ; y-values

    Returns :
        - ICA (list) : list of dQ/dV values (new y-values)
        - new_voltage (list) : list of the new x-values related to the y-values (dQ/dV)
    """

    ICA = []
    new_voltage = []
    if(len(voltage) == len(capacity)):
        for i in range(len(capacity)-1):
            if(i > 1):
                if ((voltage[i+1]-voltage[i-1]) != 0):
                    calcul = ((capacity[i+1]-capacity[i-1]) /
                              (voltage[i+1]-voltage[i-1]))
                    if charge == 0:
                        if (calcul > -200000000) and (calcul < 200) and voltage[i] < high_voltage and voltage[i] > low_voltage:
                            ICA.append(calcul)
                            new_voltage.append(voltage[i])
                    if charge == 1:
                        if (calcul > -2500) and (calcul < 10000000) and voltage[i] < high_voltage and voltage[i] > low_voltage:
                            ICA.append(calcul)
                            new_voltage.append(voltage[i])
    return ICA, new_voltage


#################################################

def capacityCalcul(time, current, n, charge):
    """
    capacityCalcul : create a list of capacity values from time and current values

    Parameters :    
        - time (list) : time values (s)
        - current (list) : current values (A)
        - n (int) : nomber of values
        - charge (bool) : either 1 or 0 (1 == charge values ; 0 == discharge values)
    """

    capacity = []

    for i in range(n):
        if i < 1:
            capacity.append(time[i])
        else:
            # if charge then capacity[n-1] "+" ; if discharge then capacity[n-1] "-"
            if charge == 1:
                capacity.append(capacity[i-1]+(time[i]*current[i]/3600))
            elif charge == 0:
                capacity.append(capacity[i-1]-(time[i]*current[i]/3600))
            else:
                print("Error in charge value, must be 1 or 0")

    return capacity


def percentageCapa(time, voltage, capa):
    """
    Compute the percentage of SoC when the CC is over and the CV begins

    Parameters :
        - time (list) : list of the time values (x-axis) of a charge sequence  
        - voltage (list) : list of voltage values of a charge sequence
        - capa (list) : list of capacity values of ac harge sequence
        """
    capa_cv = []

    for i in range(len(time)):
        if voltage[i] > CV_LOW and voltage[i] < CV_HIGH:
            capa_cv.append(capa[i])

    first_capa_cv_percent = capa_cv[0]*100/capa_cv[len(capa_cv)-1]
    print('Percentage of capacity (SoC) at first CV voltage value : ', first_capa_cv_percent)
    
    return capa_cv


##################################################################################################
#                    FILTER FUNCTIONS
##################################################################################################

#################################################


def capaFilter(x, y, param_smooth):
    """
    capaFilter : Apply a filter in order to smooth the curve (y-axis)

    Parameters :
        - x & y (list) : data
        - paramSmooth (float between 0 and 1) : percentage/100 for the smoothing
    """

    y_lowess = sm.nonparametric.lowess(
        y, x, frac=param_smooth)  # xx% lowess smoothing
    df = pd.DataFrame(y_lowess)
    # Get the first column (voltage) of the Dataframe as a serie and convert it into a list
    y_new = df.iloc[:, 1].tolist()
    x_new = df.iloc[:, 0].tolist()

    return x_new, y_new


#################################################


def ICAFilter(ICA, window, order):
    """
    ICAFilter : Apply a filter in order to smooth the curve (y-axis)

    Parameters : 
        - ICA (list) : ICA data
        - window (int) : lenght of the filter window, odd integer, usually 51 is good
        - order (int) : order of the polynomial used to fit the samples
    """

    y_sf = scipy.signal.savgol_filter(ICA, window, order)

    return y_sf


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
