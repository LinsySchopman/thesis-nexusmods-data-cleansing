import os
import pandas as pd

folder_path = r'K:\Thesis Data\Sample B\Nexus Mods\Sample B Nexus files added'
output_file_path = os.path.join(folder_path, 'nexus_new_files.csv')

# initialize an empty DataFrame to store the combined data
combined_df = pd.DataFrame()

# loop through all files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_csv(file_path)
        combined_df = pd.concat([combined_df, df], ignore_index=True) # concatenate the data to the combined DataFrame

# write the combined data to a new CSV file
combined_df.to_csv(output_file_path, index=False)

print(f"Combined data written to {output_file_path}")
