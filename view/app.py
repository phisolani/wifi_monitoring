import dash
from dash.dependencies import Input, Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import json

from configs.wtp_settings import *


# TODO: read list of WTPs statistics
wtps_stats_files = ['../stats/wtp1_aggregated_stats.json']

app = dash.Dash(__name__)

app.layout = html.Div(
    html.Div([
        html.H4('SDW Manager'),
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*2000  # in milliseconds
        )
    ]), id='div_layout'
)


# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-update-graph', 'figure'),
              events=[Event('interval-component', 'interval')])
def update_graph_live():
    for wtp_stats in wtps_stats_files:
        with open(wtp_stats) as f:
            wtp_aggregated_stats = json.load(f)

        data = {'TIME': [],
                'MANAGEMENT': [],
                'CONTROL': [],
                'DATA': [],
                'OTHER': []}

        for packets in wtp_aggregated_stats['MEASUREMENTS']['PACKETS']:
            if packets is not None:
                data['MANAGEMENT'].append(packets['MANAGEMENT'])
                data['CONTROL'].append(packets['CONTROL'])
                data['DATA'].append(packets['DATA'])
                data['OTHER'].append(packets['OTHER'])
                data['TIME'].append(packets['TIME'])

        # Create the graph with subplots
        fig = plotly.tools.make_subplots(rows=2, cols=1, vertical_spacing=0.2)
        fig['layout']['margin'] = {
            'l': 30, 'r': 10, 'b': 30, 't': 10
        }
        fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

        fig.append_trace({
            'x': data['TIME'],
            'y': data['MANAGEMENT'],
            'name': 'Management Packets',
            'mode': 'lines+markers',
            'type': 'scatter'
        }, 1, 1)
        fig.append_trace({
            'x': data['TIME'],
            'y': data['CONTROL'],
            'name': 'Control Packets',
            'mode': 'lines+markers',
            'type': 'scatter'
        }, 1, 1)
        fig.append_trace({
            'x': data['TIME'],
            'y': data['DATA'],
            'name': 'Data Packets',
            'mode': 'lines+markers',
            'type': 'scatter'
        }, 1, 1)
        fig.append_trace({
            'x': data['TIME'],
            'y': data['OTHER'],
            'name': 'Other Packets',
            'mode': 'lines+markers',
            'type': 'scatter'
        }, 1, 1)
        # fig.append_trace({
        #     'x': data['MANAGEMENT'],
        #     'y': data['CONTROL'],
        #     'text': data['TIME'],
        #     'name': 'Management vs Control',
        #     'mode': 'lines+markers',
        #     'type': 'scatter'
        # }, 2, 1)

    return fig


if __name__ == '__main__':
    # TODO read the output from WTP list to create the list of stations that have to be monitored...
    app.run_server(debug=True)