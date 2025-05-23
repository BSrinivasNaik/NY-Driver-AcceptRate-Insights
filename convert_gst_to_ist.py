import pandas as pd
import datetime

# Read the CSV file
print("Reading CSV file...")
df = pd.read_csv('Chennai_22March.csv')

# Identify date columns
date_columns = ['created_at', 'start_time', 'dq.created_at']

# Function to convert GST to IST
def convert_to_ist(date_str):
    if pd.isna(date_str) or date_str == '1970-01-01 00:00:00':
        return date_str
    
    try:
        # Parse the date string
        dt = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        
        # Add 5 hours and 30 minutes to convert from GST to IST
        ist_dt = dt + datetime.timedelta(hours=5, minutes=30)
        
        # Return the IST date string
        return ist_dt.strftime('%Y-%m-%d %H:%M:%S')
    except:
        return date_str

# Convert date columns from GST to IST
print("Converting dates from GST to IST...")
for col in date_columns:
    df[col] = df[col].apply(convert_to_ist)

# Write the updated data to a new CSV file
print("Writing to new CSV file...")
df.to_csv('Chennai_22March_IST.csv', index=False)

print("Conversion completed. New file created: Chennai_22March_IST.csv") 