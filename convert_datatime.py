# Import libraries
import csv
import datetime

# Open the input and output CSV files
with open(r'K:\Thesis Data\Sample B\Nexus Mods\site-stats.csv', 'r') as infile, \
     open(r'K:\Thesis Data\Sample B\Nexus Mods\site-stats-datetime.csv', 'w', newline='') as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write the header row to the output file
    header = next(reader)
    writer.writerow(header + ['datetime'])

    # Loop over the rows in the input file
    for row in reader:
        # Convert epoch time to datetime
        epoch_time = int(row[0])
        dt = datetime.datetime.fromtimestamp(epoch_time)

        # Write the row to the output file, including the datetime value
        writer.writerow(row + [dt])
