import os
import pandas as pd


csv_folder = os.getcwd() 

# Output file
output_file = 'combined_output.csv'


dfs = []


for filename in os.listdir(csv_folder):
    if filename.endswith('.csv'):
        file_path = os.path.join(csv_folder, filename)
        try:
            df = pd.read_csv(file_path)
            if not df.empty:
                dfs.append(df)
            else:
                print(f'Skipping empty file: {filename}')
        except Exception as e:
            print(f'Error reading {filename}: {e}')


if dfs:
    combined_df = pd.concat(dfs, ignore_index=True)
    combined_df.to_csv(output_file, index=False)
    print(f'All CSV files have been combined into {output_file}')
else:
    print('No valid CSV files found to combine.')

