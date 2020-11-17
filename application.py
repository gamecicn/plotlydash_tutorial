import dash
import plotly.express as px

import numpy as np
import pandas as pd

import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input


# Data Exploration
#----------------------------------------
df = pd.read_csv("./data/MPVDataset.csv")

df["Victim's age"] = pd.to_numeric(df["Victim's age"], errors='coerce').fillna(0).astype(np.int64)
df.rename(columns={'Fleeing (Source: WaPo)' : 'Fleeing'}, inplace=True )


df = df[df["State"].isin(['NY', 'CA', 'TX'])]
df = df[df["Victim's race"].isin(["White", "Black", "Hispanic", "Asian"])]

fig = px.sunburst(
    data_frame=df,
    path=["Unarmed", "State", "Victim's race"],
    color="Unarmed",
    color_discrete_sequence=px.colors.qualitative.Pastel,
    # maxdepth=-1,                        # set the sectors rendered. -1 will render all levels in the hierarchy
    # color="Victim's age",
    # color_continuous_scale=px.colors.sequential.BuGn,
    # range_color=[10,100],

    # branchvalues="total",               # or 'remainder'
    # hover_name="Unarmed",
    # # hover_data={'Unarmed': False},    # remove column name from tooltip  (Plotly version >= 4.8.0)
    # title="7-year Breakdown of Deaths by Police",
    # template='ggplot2',               # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
    #                                   # 'plotly_white', 'plotly_dark', 'presentation',
    #                                   # 'xgridoff', 'ygridoff', 'gridon', 'none'
)

fig.update_traces(textinfo='label+percent entry')
fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

fig.show()




'''
########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
application = app.server
app.title='Interactive Excel Dashboard'



########### Set up the layout
'''

########### Run the app
#if __name__ == '__main__':
#    application.run(debug=True, port=8080)

