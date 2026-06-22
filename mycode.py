import pandas as pd
import os

# Create a sample dataset
sample_data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Convert dictionary into a DataFrame
df = pd.DataFrame(sample_data)

# Add a new record for Version 2
v2_record = {
    'Name': 'GF1',
    'Age': 20,
    'City': 'City1'
}
df.loc[len(df)] = v2_record

# Add another record for Version 3
v3_record = {
    'Name': 'GF2',
    'Age': 30,
    'City': 'City2'
}
df.loc[len(df)] = v3_record

# Create the data directory if it does not already exist
output_dir = "data"
os.makedirs(output_dir, exist_ok=True)

# Specify the output file path
csv_file_path = os.path.join(output_dir, "sample_data.csv")

# Save the DataFrame as a CSV file
df.to_csv(csv_file_path, index=False)

print(f"Dataset successfully saved at: {csv_file_path}")