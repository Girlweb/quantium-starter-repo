import pandas as pd
import glob

# Step 1: Find all CSV files in the data folder
csv_files = glob.glob('data/daily_sales_data_*.csv')
print(f"Found {len(csv_files)} CSV files: {csv_files}")

# Step 2: Read and process each CSV file
all_data = []

for file in csv_files:
    print(f"\nProcessing {file}...")
    
    # Read the CSV file
    df = pd.read_csv(file)
    print(f"  Original rows: {len(df)}")
    
    # Filter for only Pink Morsels
    df = df[df['product'] == 'pink morsel']
    print(f"  After filtering for Pink Morsels: {len(df)}")
    
    # Calculate sales (quantity × price)
    df['sales'] = df['quantity'] * df['price']
    
    # Keep only the columns we need
    df = df[['sales', 'date', 'region']]
    
    # Add to our list
    all_data.append(df)

# Step 3: Combine all dataframes into one
final_df = pd.concat(all_data, ignore_index=True)
print(f"\n✅ Total rows in final dataset: {len(final_df)}")

# Step 4: Save to output file
final_df.to_csv('output.csv', index=False)
print("✅ Saved to output.csv")

# Show first few rows
print("\nFirst 5 rows of output:")
print(final_df.head())