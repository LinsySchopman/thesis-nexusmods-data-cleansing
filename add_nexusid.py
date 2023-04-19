import os
import pandas as pd

folder_path = r'K:\Thesis Data\Sample B\Nexus Mods\new_files

# loop through all files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)
        nexus_id = file_name[:-4] # remove ".csv" from file name
        df = pd.read_csv(file_path)
        df.columns = ['date', 'new_files', 'new_images', 'new_videos'] # rename existing columns
        df.insert(0, 'nexus_id', nexus_id) # insert "nexus_id" column at the beginning of the DataFrame
        df = df[['nexus_id', 'date', 'new_files']] # reorder columns
        df.to_csv(file_path, index=False) # overwrite the original file with the modified DataFrame
