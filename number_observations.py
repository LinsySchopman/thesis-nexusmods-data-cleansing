# Import libraries
import pandas as pd

# Set the file path
filepath = r'K:\Thesis Data\Sample B\Nexus Mods\-nexus_mods_merged.csv'

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(filepath)

# Get the number of observations (rows) in the DataFrame
num_observations = len(df.index)

# Print the number of observations
print("Number of observations in the file:", num_observations)

# Get the number of unique 'nexus_id' values in the DataFrame
num_unique_nexus_id = df['nexus_id'].nunique()

# Print the number of unique 'nexus_id' values
print("Number of unique 'nexus_id' values in the file:", num_unique_nexus_id)
