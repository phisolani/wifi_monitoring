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

" Python script for parsing some Grafana results"
# TODO: this script needs refactoring..."

filename = 'experiment_2/gomez_rssi/rssi/ap_3_rssi.csv'
col_time = 'Time'
col_datetime = 'Datetime'
begin_datetime = dateutil.parser.parse('2021-01-06T12:35:20+01:00')
end_datetime = dateutil.parser.parse('2021-01-06T12:45:20+01:00')

# open csv file to be parsed
df = pd.read_csv(filename, sep=';')

if col_time in df.columns:
    df = df.drop(columns=col_time, axis=1)

# index column
index_time = 1

# open a new csv for the parsed values
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')

    # writing the header
    header = [col_time] + list(df)
    writer.writerow(header)
    print(header)

    flag_begin = False
    flag_end = False
    prev_datetime = None
    crr_datetime = None
    prev_datetime = None

    # writing the values
    for index, row in df.iterrows():
        add_null_row = False
        crr_datetime = dateutil.parser.parse(row[col_datetime])

        # if begin is null
        if crr_datetime > begin_datetime and not flag_begin:
            add_null_row = True
            while add_null_row:
                aux_datetime = begin_datetime + datetime.timedelta(0, index_time)  # days, seconds, then other fields.
                values = [index_time]
                for col in list(df):
                    if col == col_datetime:
                        values.append(aux_datetime.isoformat())
                    else:
                        values.append('null')
                writer.writerow(values)
                print(values)
                index_time += 1
                gap_time = crr_datetime - aux_datetime
                prev_datetime = aux_datetime
                if gap_time.total_seconds() == 1:
                    add_null_row = False
                    flag_begin = True

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
                for col in list(df):
                    if col == col_datetime:
                        values.append(aux_datetime.isoformat())
                    else:
                        values.append('null')
                writer.writerow(values)
                index_time += 1
                gap_time = crr_datetime - aux_datetime
                prev_datetime = aux_datetime
                if gap_time.total_seconds() == 1:
                    add_null_row = False

            values = [index_time]
            for col in list(df):
                if pd.isna(row[col]):
                    values.append('null')
                else:
                    values.append(row[col])
            print(values)
            writer.writerow(values)
            index_time += 1

            if crr_datetime == end_datetime:
                break

            prev_datetime = crr_datetime
    if crr_datetime is not None and prev_datetime is not None:
        if crr_datetime <= end_datetime:
            add_null_row = True
            while add_null_row:
                aux_datetime = begin_datetime + datetime.timedelta(0, index_time)  # days, seconds, then other fields.
                values = [index_time]
                for col in list(df):
                    if col == col_datetime:
                        values.append(aux_datetime.isoformat())
                    else:
                        values.append('null')
                writer.writerow(values)
                print(values)
                index_time += 1
                if aux_datetime >= end_datetime:
                    add_null_row = False