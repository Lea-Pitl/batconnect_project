################     LAAS STAGE      ################
# Functions File to plot Curves from a csv file
# Author : Léa Pitault
# Date : 2021/07/12
#####################################################

from dataset_testbench_pkg import *
import statsmodels.api as sm
import scipy.signal
import pandas as pd

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