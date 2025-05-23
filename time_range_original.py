import pandas as pd

# Load the original file
print("Analyzing time range for created_at column in the original file...")
df = pd.read_csv('Chennai_22March.csv')

# Convert created_at to datetime
df['created_at'] = pd.to_datetime(df['created_at'])

# Get min and max timestamps
min_time = df['created_at'].min()
max_time = df['created_at'].max()

# Calculate time range
time_range = max_time - min_time
hours = time_range.total_seconds() / 3600

print(f"\nTime Range Analysis for Chennai_22March.csv (GST times):")
print(f"Earliest created_at: {min_time}")
print(f"Latest created_at: {max_time}")
print(f"Total time span: {time_range}")
print(f"Total hours: {hours:.2f} hours") 