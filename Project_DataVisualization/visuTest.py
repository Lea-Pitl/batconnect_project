import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Import data
title = "dataset_testbench_files/20210721_test.csv"
df = pd.read_csv("dataset_testbench_files/20210721_test.csv", encoding ='latin1', delimiter='/t')

#df = df.groupby(['Cycle'])[['Voltage']].mean()
#df.reset_index(inplace=True)
print(df[:3])

# -------------------------------------------------------------------------------------------------
# App layout

app.layout= html.Div([
    html.H1("WWeb application...", style={'text-align':'center'}),
    
    dcc.Dropdown(id="slct_cycle",
                 opitions=[{}])
    
    ])