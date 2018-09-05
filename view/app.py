import dash
from dash.dependencies import Input, Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import json
import glob

# TODO: read list of WTPs statistics
wtps_stats_files = glob.glob("../stats/*.aggr.json")

app = dash.Dash(__name__)

# WTPs information
wtps_options = []
for wtp_stats in wtps_stats_files:
    with open(wtp_stats) as f:
        wtp_aggregated_stats = json.load(f)
    wtps_options.append({'name': wtp_aggregated_stats['NAME'], 'filename': wtp_stats})

# Creating an array of Divs
all_divs = []

div_header = html.Div(id='header',
                      children=[
    html.H4('WiFi Monitoring Framework'),
    dcc.Interval(
        id='graph-update',
        interval=1*5000  # in milliseconds
    )
])
all_divs.append(div_header)

dcc_wpts_selecter = dcc.Dropdown(
    id='wtps-dropdown',
    options=[{'label': i['name'], 'value': i['filename']} for i in wtps_options],
    value=[]
)
all_divs.append(dcc_wpts_selecter)

dcc_another_graph_packets = dcc_graph_packets = dcc.Graph(id='another-live-update-graph')
all_divs.append(dcc_another_graph_packets)

app.layout = html.Div(id='content', children=all_divs)


# Multiple components can update everytime interval gets fired.

@app.callback(
    dash.dependencies.Output('another-live-update-graph','figure'),
    [dash.dependencies.Input('wtps-dropdown', 'value')],
    events=[dash.dependencies.Event('graph-update', 'interval')]
    )
def update_mcdm_graph(wtp_file):
    if wtp_file:
        with open(wtp_file) as f:
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
        fig = plotly.tools.make_subplots(rows=2, cols=1, vertical_spacing=0.2, print_grid=False)
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
        return fig

external_css = ["https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"]
for css in external_css:
    app.css.append_css({"external_url": css})

#external_js = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js']
#for js in external_js:
#    app.scripts.append_script({'external_url': js})

if __name__ == '__main__':
    # TODO read the output from WTP list to create the list of stations that have to be monitored...
    app.run_server(debug=True)