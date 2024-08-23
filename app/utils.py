import pandas as pd
import numpy as np
from scipy import stats

def process_data(df):
    df.dropna(inplace=True)

    if 'Comments' in df.columns:
        df.drop(columns=['Comments'], inplace=True)

    if all(col in df.columns for col in ['GHI', 'DNI', 'DHI']):
        df[['GHI', 'DNI', 'DHI']] = df[['GHI', 'DNI', 'DHI']].apply(pd.to_numeric, errors='coerce')

        z_scores = stats.zscore(df[['GHI', 'DNI', 'DHI']])
        abs_z_scores = np.abs(z_scores)
        filtered_entries = (abs_z_scores < 3).all(axis=1)  # Keeping entries where all z-scores are less than 3
        df = df[filtered_entries]
    else:
        print("Columns for Z-score calculation are missing or non-numeric.")
    
    # Drop duplicate rows
    df.drop_duplicates(inplace=True)

    # Replace negative values with NaN
    df[df < 0] = np.nan

    # Convert the 'Timestamp' column to datetime format if it exists
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

        # Drop rows where conversion failed (if any)
        df.dropna(subset=['Timestamp'], inplace=True)

        # Set 'Timestamp' as the index
        df.set_index('Timestamp', inplace=True)
    else:
        print("Timestamp column is missing.")

    return df
