import dash
import plotly.express as px
import pandas as pd

import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input


# Data Exploration
#----------------------------------------
df = pd.read_csv("./data/vgsales.csv")

#  print(df[:5])
#  print(df.Genre.nunique())
#  print(df.Genre.unique())

#fig_pie = px.pie(data_frame=df, names="Genre", values="Japan Sales")
#fig_pie.show()

#fig_bar = px.bar(data_frame=df, x="Genre", y="Japan Sales")
#fig_bar.show()

# fig_hist = px.histogram(data_frame=df, x="Year", y="Japan Sales")
# fig_hist.show()

# Interactive Graphing with Dash
app = dash.Dash(__name__)
application = app.server

app.layout = html.Div([

    html.H1("Graph Analysis with Charming Data"),

    dcc.Dropdown(id='genre-choice',
                 options=[{'label': x, 'value': x}
                          for x in sorted(df.Genre.unique())],
                 value='Sports'),

    dcc.Graph(id="my-graph", figure=px.histogram(data_frame=df,
                                                 x='Year',
                                                 y='Japan Sales'))

])

@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='genre-choice', component_property='value')
)
def interactive_graphing(value_genre):
    print(value_genre)
    dff = df[df.Genre == value_genre]
    fig = px.bar(data_frame=dff, x="Year", y="Japan Sales")
    return fig


'''
########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
application = app.server
app.title='Interactive Excel Dashboard'



########### Set up the layout
'''

########### Run the app
if __name__ == '__main__':
    application.run(debug=True, port=8080)

