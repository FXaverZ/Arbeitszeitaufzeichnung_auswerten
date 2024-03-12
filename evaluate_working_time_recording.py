import pandas as pd
import numpy as np
from datetime import datetime

# Clear variables
path = "./"
name = 'Arbeitszeitaufzeichnung.xlsx'
out_name = 'Auswertung.xlsx'
sheet = 'Arbeitszeit Siemens'
sheet_out_1 = 'Output Analyse'

output_depth = 2
project = 'CLUE'
project_eval = 1

time_start = None  # '22.11.2018'
time_end = None  # '20.02.2019'

# Read Excel file
df = pd.read_excel(path + name, sheet_name=sheet)

# Filter rows based on time_start and time_end
dates = pd.to_datetime(df['Datum'], format='%d.%m.%Y')
df = df[(dates >= time_start) & (dates <= time_end)]

# Extract exercises
exercises = df['Tätigkeit'].dropna().values

# Create DataFrames to store results
unique_exe_columns = ['Haupttätigkeit', 'Dauer [h]', 'Anzahl', 'Orte']
unique_exe = pd.DataFrame(columns=unique_exe_columns)
unique_exe_idx_columns = ['Haupttätigkeit', 'Anzahl', 'Orte']
unique_exe_idx = pd.DataFrame(columns=unique_exe_idx_columns)

# Iterate through exercises to extract main activities
for i in range(len(exercises)):
    # Split exercise string
    parts = str(exercises[i]).split(' - ')
    main_name = parts[0]

    # Check if the main activity already exists
    idx = unique_exe[unique_exe['Haupttätigkeit'] == main_name].index.tolist()
    if not idx:
        # If not, add a new row
        unique_exe = unique_exe.append({'Haupttätigkeit': main_name,
                                        'Dauer [h]': df.iloc[i, df.columns.get_loc('h')],
                                        'Anzahl': 1,
                                        'Orte': [i]}, ignore_index=True)
        # Add to unique_exe_idx
        unique_exe_idx = unique_exe_idx.append({'Haupttätigkeit': main_name,
                                                'Anzahl': 1,
                                                'Orte': [i]}, ignore_index=True)
    else:
        # If exists, update existing row
        idx = idx[0]
        unique_exe.at[idx, 'Anzahl'] += 1
        unique_exe.at[idx, 'Orte'].append(i)

        unique_exe_idx.at[idx, 'Anzahl'] += 1
        unique_exe_idx.at[idx, 'Orte'].append(i)

# Sort unique_exe based on the 'Anzahl' column
unique_exe = unique_exe.sort_values(by='Anzahl', ascending=False)

# Output the result
print(unique_exe)
