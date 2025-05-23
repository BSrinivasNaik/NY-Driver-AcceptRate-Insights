import pandas as pd

# Determine which file to use
print("Analyzing time range for created_at column...")

# Try to load the IST version first, fall back to original if needed
try:
    print("Reading Chennai_22March_IST.csv...")
    df = pd.read_csv('Chennai_22March_IST.csv')
    file_used = "Chennai_22March_IST.csv (IST times)"
except FileNotFoundError:
    print("IST file not found, reading Chennai_22March.csv...")
    df = pd.read_csv('Chennai_22March.csv')
    file_used = "Chennai_22March.csv (original times)"

# Convert created_at to datetime
df['created_at'] = pd.to_datetime(df['created_at'])

# Get min and max timestamps
min_time = df['created_at'].min()
max_time = df['created_at'].max()

# Calculate time range
time_range = max_time - min_time
hours = time_range.total_seconds() / 3600

print(f"\nTime Range Analysis for {file_used}:")
print(f"Earliest created_at: {min_time}")
print(f"Latest created_at: {max_time}")
print(f"Total time span: {time_range}")
print(f"Total hours: {hours:.2f} hours") 