# Convert .json to .csv, header columns and nexus_id column
import json
import csv
import os

# Set the path to the directory containing the JSON files
json_dir = r"K:\Thesis Data\Sample B\Nexus Mods\Sample B - Nexus downloads - 518"

# Create a CSV file to store the data
csv_file = open("nexusmods_downloads.csv", "w", newline="")
csv_writer = csv.writer(csv_file)

# Write the header row
csv_writer.writerow(["nexus_id", "date", "downloads", "page_views", "unique_downloads"])

# Loop through each JSON file in the directory
for json_file in os.listdir(json_dir):
    if json_file.endswith(".json"):
        # Extract the nexus_id from the file name
        nexus_id = os.path.splitext(json_file)[0]

        # Load the JSON data
        with open(os.path.join(json_dir, json_file)) as f:
            data = json.load(f)

        # Loop through each date in the "downloads" object
        for date, downloads in data["downloads"].items():
            # Get the corresponding values for "page_views" and "unique_downloads"
            page_views = data["page_views"].get(date, 0)
            unique_downloads = data["unique_downloads"].get(date, 0)

            # Write a row to the CSV file
            csv_writer.writerow([nexus_id, date, downloads, page_views, unique_downloads])
            print(f"Processing file {json_file}")

# Close the CSV file
csv_file.close()

