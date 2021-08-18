# README : BATCONNECT PROJECT
**Author :** Léa PITAULT

**Tutors :** COorinne Alonso, Élodie Chanthery, Pauline Ribot (LAAS-CNRS) & Jérémy Dulout (BATCONNECT Company)

**Internship starting date :** June 1st 2021

<hr>


## Table of contents :
1. [Project](#project)
2. [Data file format](#data_file_format)
3. [Files of the project](#files)
4. [Usage](#usage)
5. [To plot the ICA curves](#plot_ica_curves)
6. [Minimal main example](#mini_example)
7. [Example of result with ICA Curves](#ica_curve)

---

## Project : <a name="project"></a>
The goal of this projet is to study LiFePO4 batteries. The data are extracted from a testbench in the LAAS Laboratory or are given by the Batconnect company. The next section [Data file format](#data_file_format) presents the data format. 

The code allows to sort the data and plot several curves (such as ICA [^1] VS Voltage)

Type of batteries : LF105 3.2V 105Ah

The data come from two different type of dataset : 

1. The LAAS Testbench, the batteries are cycled under controlled conditions and the data are collected in a file.txt 
2. The BATCONNECT data, given in a file.csv

<br>

---

[^1]: Incremental Capacity Analysis

## Data file format : <a name="data_file_format"></a>

* ### LAAS Testbench File

file.txt with 8 columns

*Example :*
| Sequence number  | time (s) | cycle number | Voltage (V) | Current (mA) | Charge (m.Ah)  | Discharge (m.Ah) | Cell external temperature (°C) |
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0  | 3.30  | 0 | 3.2196 | -4999.7 | 0 |  416.64 | 25.061 |

The sequence number depends on the testbench used. A sequence can either corresponds to a CC Charge, a CV charge, a discharge or a rest.

* ### BATCONNECT File

<br>

---

## Files of the project : <a name="files"></a>
* ### BATCONNECT package

    - TO DO
    
    <br>
* ### TESTBENCH package

    - Functions_PlotCurves.py : contains all the useful functions to sort the data, plot curves, compute the ICA, filter the data and curves
    - Main_dataMargot : main file using Margot dataset and LiNMC battery cell
    - Main_dataLea : main file using Lea dataset and LiFePO4 battery cell

    - TO UPDATE

<br>

---

## Usage : <a name="usage"></a>

<br>

### To plot the ICA curves : <a name="plot_ica_curves"></a>
 - F_plot.readFile(fileTitle) : you get the whole dataset as lists with the data of the 8 columns. You als get the number of cycle and sequence
 - F_plot.sortData(dic_dataSet) : you get a dictionary with the values in function of cycle or in function of sequences and charge or discharge
 - F_plot.plotICASeq(dic_dataSeq) : you plot the ICA curves after filtering

ICA curves are plotted using the **charge** values

---
### Minimal main example : <a name="mini_example"></a>
```python
import Functions_PlotCurves as F_plot

file_title = '20210722_Cycle50A_LiFePO4_BATCONNECT_CA1.txt'

dic_dataSet, nbCycle, nbSeq = F_plot.readFile(file_title)
dic_dataCycle, dic_dataSeq = F_plot.sortData(dic_dataSet)
F_plot.plotICASeq(dic_dataSeq)
```

<hr>

### Example of result with ICA Curves : <a name="ica_curve"></a>

![](Figures/ICA_15Cycles50A_29-07-21.PNG)
