################     LAAS STAGE      ##############################################################
# FUNCTIONS FILE TO MAKE COMPUTATION BETWEEN THE DATA
# Author : Léa Pitault
# Date : 2021/07/12
###################################################################################################

from dataset_testbench_pkg import *
from .constants import *

###################################################################################################
#                    COMPUTATIONAL FUNCTIONS
###################################################################################################

#################################################

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

def getMaxCapa(dic_dataSeq, current_cycle):
    """
    getMaxCapa: return the value of the capacity max for one charge

    Parameters:    
        - dic_dataSeq (dict) : dictionnary of the values sorted by charge or discharge
        - current_cycle (int) : current cycle to study

    Return:
        - max_capa (int) : max value of the capacity
    """

    nb=0
    max_capa=0
    
    for i in range(len(dic_dataSeq["Q_c"][current_cycle])):
        nb+=1
        if dic_dataSeq["Q_c"][current_cycle][i]>max_capa:
            max_capa=dic_dataSeq["Q_c"][current_cycle][i]
            
    print(" ---------------\n"
          "The max capacity of the charge is : ", max_capa, "A.h")
    return max_capa

#################################################


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
    print(' ------------\n Percentage of capacity (SoC) at first CV voltage value : ',
          first_capa_cv_percent)

    return capa_cv
