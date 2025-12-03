import pandas as pd
import glob

print("=" * 50)
print("DATA PROCESSING - NEW VERSION")
print("=" * 50)

# Find files
csv_files = sorted(glob.glob('data/daily_sales_data_*.csv'))
print(f"\n📁 Found {len(csv_files)} CSV files")

all_data = []

for file in csv_files:
    print(f"\n📊 {file}")
    
    # Read
    df = pd.read_csv(file)
    print(f"   Read {len(df)} rows")
    
    # Filter
    df = df[df['product'].str.lower() == 'pink morsel']
    print(f"   Pink morsels: {len(df)} rows")
    
    # **KEY FIX**: Clean price column
    print(f"   Before clean - sample price: {df['price'].iloc[0]}")
    df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)
    print(f"   After clean - sample price: {df['price'].iloc[0]}")
    
    # Calculate
    df['sales'] = df['price'] * df['quantity']
    print(f"   Sample sales calculation: {df['price'].iloc[0]} × {df['quantity'].iloc[0]} = {df['sales'].iloc[0]}")
    
    # Keep columns
    df = df[['sales', 'date', 'region']]
    all_data.append(df)

# Combine
final_df = pd.concat(all_data, ignore_index=True)

print(f"\n" + "=" * 50)
print(f"✅ FINAL RESULT")
print(f"=" * 50)
print(f"Total rows: {len(final_df)}")
print(f"\nFirst 10 rows:")
print(final_df.head(10))

# Save
final_df.to_csv('output.csv', index=False)
print(f"\n✅ Saved to output.csv")
