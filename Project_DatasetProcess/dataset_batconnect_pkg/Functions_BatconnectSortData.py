################     LAAS STAGE      ##############################################################
# FUNCITON FILE TO READ THE BATCONNECT CSV FILE  AND TO SORT THE DATAS INTO DICTIONNARIES
# Author : Léa Pitault
# Date : 2021/08/16
###################################################################################################

from dataset_batconnect_pkg import *
import csv
from .bat_constants import *
from datetime import datetime
import numpy as np

###################################################################################################



#################################################

def read_sortBatFile(file_title, line_begin, line_end):
    """
    read_sortBatFile :  Read a csv file and create lists from the different columns
    Those lists go in a dictionnary with two keys : the id the battery and the wanted values (voltage, current, ...)

    Parameters :
        - file_title (str) : Title of the csv file to read
        - line_begin (int) : lower line interval limit
        - line_end (int) : upper line interval limit

    Return : 
        - dic_bat_dataset (dict) : dictionary with the values from the csv file
        - line_count (int) : total number of line in the file
        - nb_data_line (int) : total number of line that are treated and stored in the dictionnary \n  
        All the line are not stored, we specify the interval to be processed

    """

    dic_bat_dataset = {}

    with open(file_title, mode='r') as csvfile:
        file = csv.reader(csvfile, delimiter=';')
        line_count = 0
        for row in file:
            columns = len(row)
            for i in range(columns):
                row[i] = row[i].replace(',', '.')
            if line_count == 0:
                print(f'Columns headers are {", ".join(row)}')
            elif line_count > line_begin and line_count < line_end:
                if (row[BAT_VOLTAGE] != '') and (row[BAT_TEMPE_MIN] != '') and (row[BAT_LATITUDE] != '') and (row[BAT_CHARGE] != '') and (row[BAT_CURRENT] != ''):

                    if not(row[BAT_ID] in dic_bat_dataset):
                        dic_bat_dataset[row[BAT_ID]] = {}
                        
                        dic_bat_dataset[row[BAT_ID]]["time"] = []
                        dic_bat_dataset[row[BAT_ID]]["date"] = []
                        dic_bat_dataset[row[BAT_ID]]["status"] = []
                        dic_bat_dataset[row[BAT_ID]]["latitude"] = []
                        dic_bat_dataset[row[BAT_ID]]["longitude"] = []
                        dic_bat_dataset[row[BAT_ID]]["voltage"] = []
                        dic_bat_dataset[row[BAT_ID]]["charge"] = []
                        dic_bat_dataset[row[BAT_ID]]["current"] = []
                        dic_bat_dataset[row[BAT_ID]]["tempe_min"] = []
                        dic_bat_dataset[row[BAT_ID]]["tempe_max"] = []


                    dic_bat_dataset[row[BAT_ID]]["time"].append(float(row[BAT_TIME]))
                    dic_bat_dataset[row[BAT_ID]]["date"].append(datetime.fromtimestamp(float(row[BAT_TIME])))
                    dic_bat_dataset[row[BAT_ID]]["status"].append(float(row[BAT_STATUS]))
                    dic_bat_dataset[row[BAT_ID]]["latitude"].append(float(row[BAT_LATITUDE]))
                    dic_bat_dataset[row[BAT_ID]]["longitude"].append(float(row[BAT_LONGITUDE]))
                    dic_bat_dataset[row[BAT_ID]]["voltage"].append(float(row[BAT_VOLTAGE]))
                    dic_bat_dataset[row[BAT_ID]]["charge"].append(float(row[BAT_CHARGE]))
                    dic_bat_dataset[row[BAT_ID]]["current"].append(float(row[BAT_CURRENT]))
                    dic_bat_dataset[row[BAT_ID]]["tempe_min"].append(float(row[BAT_TEMPE_MIN]))
                    dic_bat_dataset[row[BAT_ID]]["tempe_max"].append(float(row[BAT_TEMPE_MAX]))

            line_count += 1

    return dic_bat_dataset

#################################################

def getIDBatteriesFromDict(dic_dataset_sort_id):
    IDs = list(dic_dataset_sort_id.keys())
    return IDs

#################################################

def getNumberOfIDsFromDict(dic_dataset_sort_id):
    nb=len(list(dic_dataset_sort_id))
    return nb

#################################################

    
#def readBatFile(file_title, line_begin, line_end):
    """
    readBatFile :  Read a csv file and create lists from the different columns
    Those lists go in a dictionnary

    Parameters :
        - file_title (str) : Title of the csv file to read
        - line_begin (int) : lower line interval limit
        - line_end (int) : upper line interval limit

    Return : 
        - dic_bat_dataset (dict) : dictionary with the values from the csv file
        - line_count (int) : total number of line in the file
        - nb_data_line (int) : total number of line that are treated and stored in the dictionnary \n  
        All the line are not stored, we specify the interval to be processed

    """

    id = []
    time = []
    status = []
    lat = []
    long = []
    voltage = []
    charge = []
    current = []
    tempe_min = []
    tempe_max = []
    nb_data_line = 0

    with open(file_title, mode='r') as csvfile:
        file = csv.reader(csvfile, delimiter=';')
        line_count = 0
        for row in file:
            columns = len(row)
            for i in range(columns):
                row[i] = row[i].replace(',', '.')
            if line_count == 0:
                print(f'Columns headers are {", ".join(row)}')
            elif line_count > line_begin and line_count < line_end:
                if (row[BAT_VOLTAGE] != '') and (row[BAT_TEMPE_MIN] != '') and (row[BAT_LATITUDE] != '') and (row[BAT_CHARGE] != '') and (row[BAT_CURRENT] != ''):
                    id.append(float(row[BAT_ID]))
                    time.append(float(row[BAT_TIME]))
                    status.append(float(row[BAT_STATUS]))
                    lat.append(float(row[BAT_LATITUDE]))
                    long.append(float(row[BAT_LONGITUDE]))
                    voltage.append(float(row[BAT_VOLTAGE]))
                    charge.append(float(row[BAT_CHARGE]))
                    current.append(float(row[BAT_CURRENT]))
                    tempe_min.append(float(row[BAT_TEMPE_MIN]))
                    tempe_max.append(float(row[BAT_TEMPE_MAX]))
                    nb_data_line += 1

            line_count += 1

    dic_bat_dataset = {}

    dic_bat_dataset["id"] = id
    dic_bat_dataset["time"] = time
    dic_bat_dataset["status"] = status
    dic_bat_dataset["latitude"] = lat
    dic_bat_dataset["longitude"] = long
    dic_bat_dataset["voltage"] = voltage
    dic_bat_dataset["charge"] = charge
    dic_bat_dataset["current"] = current
    dic_bat_dataset["tempe_min"] = tempe_min
    dic_bat_dataset["tempe_max"] = tempe_max

    return dic_bat_dataset, line_count, nb_data_line


#def sortBatDataByValues(dic_bat_dataset, nb_line):
    """
    sortBatData : sort the batconnect dataset values in a dictionnary

    Parameters : 
        - dic_bat_dataset (dict) : dictionnary with all the useful values given by readBatFile(file_title)
        The values in the dic are the columns values of the initial dataset file
        - nb_line : number of line of the dictionnary, there are the same number of values (==lines) for all the given keys

    Return : 
        - dic_dataset_id (dict) : dictionnary with all the values but sorted by id

        You can get the voltage, the current, the state of charge (%), 
        the timestamp, the date, and the id of the batteries

        By specifying the id, (0, 1, ...) like that : dic_dataset_id["date"][0],
        you get the date values for the battery 0
    """

    date = []
    voltage = []
    charge = []
    current = []
    timestamp = []

    timestamp_diff = []
    voltage_diff = []
    charge_diff = []
    current_diff = []
    latitude_diff = []
    longitude_diff = []

    nb_status_not_OK = 0

    id_unique = getIDBatteries(dic_bat_dataset)

    #print("type id_unique : ", type(id_unique))
    for k in range(len(id_unique)):

        dic_dataset_id = {}

        date.append([])
        timestamp.append([])
        voltage.append([])
        charge.append([])
        current.append([])

        dic_bat_status_not_OK = {}

        timestamp_diff.append([])
        voltage_diff.append([])
        charge_diff.append([])
        current_diff.append([])
        latitude_diff.append([])
        longitude_diff.append([])

        # print(id_unique[k])

        for i in range(nb_line):

            if dic_bat_dataset["id"][i] == id_unique[k]:
                timestamp[k].append(dic_bat_dataset["time"][i])
                date[k].append(datetime.fromtimestamp(
                    dic_bat_dataset["time"][i]))
                voltage[k].append(dic_bat_dataset["voltage"][i])
                charge[k].append(dic_bat_dataset["charge"][i])
                current[k].append(dic_bat_dataset["current"][i])

                if dic_bat_dataset["status"][i] != 0:

                    timestamp_diff[k].append(dic_bat_dataset["time"][i])
                    voltage_diff[k].append(dic_bat_dataset["voltage"][i])
                    charge_diff[k].append(dic_bat_dataset["charge"][i])
                    current_diff[k].append(dic_bat_dataset["current"][i])
                    latitude_diff[k].append(dic_bat_dataset["latitude"][i])
                    longitude_diff[k].append(dic_bat_dataset["longitude"][i])
                    nb_status_not_OK += 1

    dic_dataset_id["voltage"] = voltage
    dic_dataset_id["current"] = current
    dic_dataset_id["charge"] = charge
    dic_dataset_id["timestamp"] = timestamp
    dic_dataset_id["date"] = date
    dic_dataset_id["id_unique"] = id_unique

    dic_bat_status_not_OK["voltage"] = voltage_diff
    dic_bat_status_not_OK["current"] = current_diff
    dic_bat_status_not_OK["charge"] = charge_diff
    dic_bat_status_not_OK["timestamp"] = timestamp_diff
    dic_bat_status_not_OK["latitude"] = latitude_diff
    dic_bat_status_not_OK["longitude"] = longitude_diff

    return dic_dataset_id, dic_bat_status_not_OK
