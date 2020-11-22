import dash
import dash_core_components as dcc
import dash_html_components as html
from   dash.dependencies import Input, Output, State

import requests
import json


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


application = app.server


app.layout = html.Div([
    html.H6("Emotional analysis test"),
    html.Div(["Input: ",
              dcc.Textarea(id='cus_input', value="I'm happy", style={'width': '100%'})]),
    html.Br(),
    html.Div(id='my-output'),
    html.Br(),
    html.Button('Analysis', id='button_1'),

])

BASE_URL = "http://23.22.92.236:5000"

def test_analysis_emotion(text):
    data = {
        'text': text,
    }

    try:
        header_dict = {"Content-Type": "application/json"}
        url = '{}/api/emotion'.format(BASE_URL)
        res = requests.post(url=url, data=json.dumps(data), headers=header_dict)

        if res.status_code != 200:
            return "Error occurs: {}".format(res.text)

        return json.loads(res.text)['result']
    except:
        return "Error occurs"


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id="button_1", component_property="n_clicks"),
    State(component_id='cus_input', component_property='value'),

    prevent_initial_call=True
)
def update_output_div(n_clicks, input):
    return 'Emotion: {}'.format(test_analysis_emotion(input))


if __name__ == '__main__':
    app.run_server(debug=False)

