# Import libraries
import pandas as pd

# Read in the two datasets
nexus_downloads = pd.read_csv('K:/Thesis Data/Sample B/Nexus Mods/nexus_downloads.csv')
nexus_newfiles = pd.read_csv('K:/Thesis Data/Sample B/Nexus Mods/nexus_newfiles.csv')

# Print the number of observations in the first dataset
print("Number of observations in nexus_downloads: ", len(nexus_downloads))

# Print the number of observations in the second dataset
print("Number of observations in nexus_newfiles: ", len(nexus_newfiles))

# Merge the datasets on both 'nexus_id' and 'date', and keep all observations
merged_df = pd.merge(nexus_downloads, nexus_newfiles, on=['nexus_id', 'date'], how='outer')

# Print the number of observations in the merged dataset
print("Number of observations in merged_df: ", len(merged_df))

# Write the merged dataset to a new CSV file
merged_df.to_csv('K:/Thesis Data/Sample B/Nexus Mods/merged_data.csv', index=False)
