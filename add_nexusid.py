# Import libraries
import os
import pandas as pd

# Set the filepath
folder_path = r'K:\Thesis Data\Sample B\Nexus Mods\newfiles

# Loop through all files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)
        
        # Remove ".csv" from file name
        nexus_id = file_name[:-4] 

        # Read the dataframe
        df = pd.read_csv(file_path)
        
        # Rename existing columns
        df.columns = ['date', 'new_files', 'new_images', 'new_videos'] 
        
        # Insert "nexus_id" column at the beginning of the DataFrame
        df.insert(0, 'nexus_id', nexus_id) 
        
        # Reorder columns
        df = df[['nexus_id', 'date', 'new_files']] 
        
        # Overwrite the original file with the modified DataFrame
        df.to_csv(file_path, index=False) #
