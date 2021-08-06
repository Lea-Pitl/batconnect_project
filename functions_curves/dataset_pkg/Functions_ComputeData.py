################     LAAS STAGE      ################
# Functions File to plot Curves from a csv file
# Author : Léa Pitault
# Date : 2021/07/12
#####################################################

from dataset_pkg import *
from .constants import *

##################################################################################################
#                    COMPUTATIONAL FUNCTIONS
##################################################################################################

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
    print('Percentage of capacity (SoC) at first CV voltage value : ',
          first_capa_cv_percent)

    return capa_cv
