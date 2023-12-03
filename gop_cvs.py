import os
import pandas as pd

folder_path = 'U:/THI/YSC_2023/25_10_2023/data_19_11'
dataframes = []


for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        dataframes.append(df)

merged_df = pd.concat(dataframes, ignore_index=True)
merged_df.to_csv('U:/THI/YSC_2023/25_10_2023/data_train/19_11_2023_lan_1.csv', index=False)
