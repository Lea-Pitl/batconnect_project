################     LAAS STAGE      ################
# Functions File to plot Curves from a csv file
# Author : Léa Pitault
# Date : 2021/07/12
#####################################################

from dataset_pkg import *
import copy
import numpy as np
import csv
from .constants import *

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
