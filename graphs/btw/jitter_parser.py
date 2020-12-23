#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__copyright__ = "Copyright 2020, QoS-aware WiFi Slicing"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"

import pandas as pd
import csv
import datetime
import dateutil.parser

" Python script for parsing Grafana results"

filename = 'experiment_mcs/apps_e2e_latency.csv'
col_time = 'Time'
col_datetime = 'Datetime'
begin_datetime = dateutil.parser.parse('2020-10-09T12:31:22+02:00')
end_datetime = dateutil.parser.parse('2020-10-09T12:43:00+02:00')

# open csv file to be parsed
df = pd.read_csv(filename, sep=';')

if col_time in df.columns:
    df = df.drop(columns=col_time, axis=1)

# index column
index_time = 1

moving_dict = {
    'APP 1': [],
    'APP 2': [],
    'APP 3': [],
    'APP 4': []
}

# open a new csv for the parsed values
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    with open('experiment_mcs/apps_e2e_jitter.csv', 'w', newline='') as csvfilejitter:
        writer_jitter = csv.writer(csvfilejitter, delimiter=';')

        # writing the header
        header = [col_time] + list(df)
        writer.writerow(header)
        writer_jitter.writerow(header)
        print(header)

        flag_begin = False
        flag_end = False
        prev_datetime = None
        # writing the values
        for index, row in df.iterrows():
            add_null_row = False
            crr_datetime = dateutil.parser.parse(row[col_datetime])

            # if begin has been found
            if crr_datetime == begin_datetime:
                # print(crr_datetime, begin_datetime)
                flag_begin = True

            if flag_begin:
                if prev_datetime is not None:
                    elapsed_time = crr_datetime - prev_datetime
                    if elapsed_time.total_seconds() > 1:
                        add_null_row = True

                while add_null_row:
                    aux_datetime = prev_datetime + datetime.timedelta(0, 1)  # days, seconds, then other fields.
                    values = [index_time]
                    values_jitter = [index_time]
                    for col in list(df):
                        if col == col_datetime:
                            values.append(aux_datetime.isoformat())
                            values_jitter.append(aux_datetime.isoformat())
                        else:
                            values.append('null')
                            values_jitter.append('null')
                    writer.writerow(values)
                    writer_jitter.writerow(values_jitter)
                    index_time += 1
                    gap_time = crr_datetime - aux_datetime
                    prev_datetime = aux_datetime
                    if gap_time.total_seconds() == 1:
                        add_null_row = False

                values = [index_time]
                values_jitter = [index_time]
                for col in list(df):
                    if pd.isna(row[col]):
                        values.append('null')
                        values_jitter.append('null')
                    else:
                        values.append(row[col])
                        if col.startswith('APP'):
                            moving_dict[col].append(row[col])
                            if len(moving_dict[col]) > 10:
                                sum_of_latencies_diff = 0
                                for i in range(0, 10):
                                    sum_of_latencies_diff += abs(moving_dict[col][i] - moving_dict[col][i + 1])

                                jitter = sum_of_latencies_diff / (len(moving_dict[col]) - 1)
                                print("moving", moving_dict[col], "sum", sum_of_latencies_diff, "jitter", jitter)
                                moving_dict[col].pop(0)
                                values_jitter.append(jitter)
                            else:
                                values_jitter.append('null')
                        else:
                            values_jitter.append(row[col])
                print(values)
                print(values_jitter)
                writer.writerow(values)
                writer_jitter.writerow(values_jitter)
                index_time += 1

                if crr_datetime == end_datetime:
                    break

                prev_datetime = crr_datetime