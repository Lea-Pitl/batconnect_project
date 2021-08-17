################     LAAS STAGE      ################
# Functions File to plot Curves from a csv file
# Author : Léa Pitault
# Date : 2021/08/16
#####################################################

from dataset_batconnect_pkg import *
import csv
from .bat_constants import *
from datetime import datetime
import numpy as np


def readBatFile(file_title):
    """
    """

    id = []
    time = []
    date = []
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
            elif line_count > BAT_LINE_BEGIN and line_count < BAT_LINE_END:
                if (row[BAT_VOLTAGE] != '') and (row[BAT_TEMPE_MIN] != '') and (row[BAT_LATITUDE] != '') and (row[BAT_CHARGE] != '') and (row[BAT_CURRENT] != ''):
                    id.append(float(row[BAT_ID]))
                    time.append(float(row[BAT_TIME]))
                    # date.append(float(row[BAT_DATE]))
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
    # dic_bat_dataset["date"] = date
    dic_bat_dataset["status"] = status
    dic_bat_dataset["latitude"] = lat
    dic_bat_dataset["longitude"] = long
    dic_bat_dataset["voltage"] = voltage
    dic_bat_dataset["charge"] = charge
    dic_bat_dataset["current"] = current
    dic_bat_dataset["tempe_min"] = tempe_min
    dic_bat_dataset["tempe_max"] = tempe_max

    return dic_bat_dataset, line_count, nb_data_line


def sortBatData(dic_bat_dataset, nb_line):
    """
    """

    date = []
    y_data = []
    timestamp = []
    nb_line_ID1 = 0
    nb_status_not_OK = 0

    id_unique = np.unique(dic_bat_dataset["id"])

    for i in range(nb_line):
        if dic_bat_dataset["id"][i] != ID_BAT1:
            print("timestamp bad id ", dic_bat_dataset["time"][i])
        else:
            timestamp.append(dic_bat_dataset["time"][i])
            date.append(datetime.fromtimestamp(dic_bat_dataset["time"][i]))
            y_data.append(dic_bat_dataset["voltage"][i])
            nb_line_ID1 += 1

            if dic_bat_dataset["status"][i] != 0:
                print("date :", dic_bat_dataset["time"][i], "  ;  status :", dic_bat_dataset["status"][i],
                      "  ;  voltage :", dic_bat_dataset["voltage"][i], "  ;  id :", dic_bat_dataset["id"][i])
                nb_status_not_OK += 1

    return date, y_data  # , nb_line_ID1, nb_status_not_OK
