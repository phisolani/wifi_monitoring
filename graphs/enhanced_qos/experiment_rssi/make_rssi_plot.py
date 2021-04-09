from graphs.enhanced_qos.rssi_plot import *

# Sensors
fig_size = [11, 4]

make_scatter_rssi_shared_y(
    experiment_path='arp_only/rssi/',
    x_axis='Time',
    x_axis_label='Time (sec)',
    x_axis_min_max={'min': 0, 'max': 600},
    y_axes=['STA 1', 'STA 2', 'STA 3', 'STA 4', 'STA 5', 'STA 6'],
    y_axis_label='RSSI (dBm)',
    y_axis_min_max={'min': -100, 'max': 0},
    filenames=['ap_1_rssi', 'ap_2_rssi', 'ap_3_rssi'],
    fig_size=fig_size
)

make_scatter_rssi_shared_y(
    experiment_path='workload/experiment_2/gomez/rssi/',
    x_axis='Time',
    x_axis_label='Time (sec)',
    x_axis_min_max={'min': 0, 'max': 600},
    y_axes=['STA 1', 'STA 2', 'STA 3', 'STA 4', 'STA 5', 'STA 6'],
    y_axis_label='RSSI (dBm)',
    y_axis_min_max={'min': -100, 'max': 0},
    filenames=['ap_1_rssi', 'ap_2_rssi', 'ap_3_rssi'],
    fig_size=fig_size,
    events=True
)