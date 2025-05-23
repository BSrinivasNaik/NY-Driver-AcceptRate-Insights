import pandas as pd
import json
import os
import numpy as np

def convert_csv_to_json():
    # Check which file to use (preferring the IST version)
    if os.path.exists('Chennai_22March_IST.csv'):
        file_path = 'Chennai_22March_IST.csv'
        print("Using IST converted file...")
    elif os.path.exists('Chennai_22March.csv'):
        file_path = 'Chennai_22March.csv'
        print("Using original file...")
    else:
        print("Error: No data file found.")
        return
    
    # Read the CSV file
    print(f"Reading data from {file_path}...")
    df = pd.read_csv(file_path)
    
    # Convert dates to datetime objects for proper handling
    for col in ['created_at', 'start_time', 'dq.created_at']:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    
    # Convert numeric columns and clean data
    numeric_columns = ['distance', 'distance_to_pickup', 'base_fare', 'driver_rating']
    for col in numeric_columns:
        # Replace non-numeric values with NaN
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Extract hour from created_at
    df['hour'] = df['created_at'].dt.hour
    
    # Generate hourly summary data
    print("Generating hourly analytics...")
    hourly_data = []
    
    for hour in range(24):
        hour_df = df[df['hour'] == hour]
        
        if len(hour_df) == 0:
            continue
            
        total_searches = len(hour_df)
        quotes_received = hour_df['dq.id'].notna().sum()
        conversion_rate = quotes_received / total_searches * 100 if total_searches > 0 else 0
        
        # Calculate average metrics for each hour - convert to Python primitives to avoid circular references
        avg_distance = float(hour_df['distance'].dropna().mean() / 1000) if not hour_df['distance'].dropna().empty else 0.0
        avg_base_fare = float(hour_df['base_fare'].dropna().mean()) if not hour_df['base_fare'].dropna().empty else 0.0
        avg_pickup_distance = float(hour_df['distance_to_pickup'].dropna().mean()) if not hour_df['distance_to_pickup'].dropna().empty else 0.0
        
        # Count status distribution
        completed = len(hour_df[hour_df['status'] == 'COMPLETED'])
        cancelled = len(hour_df[hour_df['status'] == 'CANCELLED'])
        active = len(hour_df[hour_df['status'] == 'ACTIVE'])
        
        hourly_data.append({
            'hour': int(hour),
            'totalSearches': int(total_searches),
            'quotesReceived': int(quotes_received),
            'conversionRate': float(conversion_rate),
            'avgDistance': float(avg_distance),
            'avgBaseFare': float(avg_base_fare),
            'avgPickupDistance': float(avg_pickup_distance),
            'completed': int(completed),
            'cancelled': int(cancelled),
            'active': int(active)
        })
    
    # Generate distance-based summary
    print("Generating distance-based analytics...")
    
    # Create distance bins
    df['distance_km'] = df['distance'] / 1000
    distance_bins = [0, 5, 10, 15, 20, 25, 30, float('inf')]
    bin_labels = ['0-5', '5-10', '10-15', '15-20', '20-25', '25-30', '30+']
    
    # Create a copy to avoid SettingWithCopyWarning
    distance_df = df.copy()
    distance_df['distance_range'] = pd.cut(distance_df['distance_km'].fillna(-1), bins=distance_bins, labels=bin_labels, right=False)
    
    distance_data = []
    
    for distance_range in bin_labels:
        range_df = distance_df[distance_df['distance_range'] == distance_range]
        
        if len(range_df) == 0:
            continue
            
        total_searches = len(range_df)
        quotes_received = range_df['dq.id'].notna().sum()
        conversion_rate = quotes_received / total_searches * 100 if total_searches > 0 else 0
        
        avg_base_fare = float(range_df['base_fare'].dropna().mean()) if not range_df['base_fare'].dropna().empty else 0.0
        
        distance_data.append({
            'distanceRange': str(distance_range),
            'totalSearches': int(total_searches),
            'quotesReceived': int(quotes_received),
            'conversionRate': float(conversion_rate),
            'avgBaseFare': float(avg_base_fare)
        })
    
    # Generate fare-based summary
    print("Generating fare-based analytics...")
    
    # Create fare bins
    fare_bins = [0, 50, 100, 150, 200, 250, 300, 350, 400, float('inf')]
    fare_labels = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400+']
    
    # Create a copy to avoid SettingWithCopyWarning
    fare_df = df.copy()
    # Only include rows with valid fare values
    fare_df = fare_df[fare_df['base_fare'].notna()]
    fare_df['fare_range'] = pd.cut(fare_df['base_fare'], bins=fare_bins, labels=fare_labels, right=False)
    
    fare_data = []
    
    for fare_range in fare_labels:
        range_df = fare_df[fare_df['fare_range'] == fare_range]
        
        if len(range_df) == 0:
            continue
            
        total_searches = len(range_df)
        quotes_received = range_df['dq.id'].notna().sum()
        conversion_rate = quotes_received / total_searches * 100 if total_searches > 0 else 0
        
        fare_data.append({
            'fareRange': str(fare_range),
            'totalSearches': int(total_searches),
            'quotesReceived': int(quotes_received),
            'conversionRate': float(conversion_rate)
        })
    
    # Generate pickup distance summary
    print("Generating pickup distance analytics...")
    
    # Create pickup distance bins (meters)
    pickup_bins = [0, 500, 1000, 1500, 2000, 2500, 3000, float('inf')]
    pickup_labels = ['0-500', '500-1000', '1000-1500', '1500-2000', '2000-2500', '2500-3000', '3000+']
    
    # Create a copy to avoid SettingWithCopyWarning
    pickup_df = df.copy()
    # Only include rows with valid pickup distance values
    pickup_df = pickup_df[pickup_df['distance_to_pickup'].notna()]
    pickup_df['pickup_range'] = pd.cut(pickup_df['distance_to_pickup'], bins=pickup_bins, labels=pickup_labels, right=False)
    
    pickup_data = []
    
    for pickup_range in pickup_labels:
        range_df = pickup_df[pickup_df['pickup_range'] == pickup_range]
        
        if len(range_df) == 0:
            continue
            
        total_searches = len(range_df)
        quotes_received = range_df['dq.id'].notna().sum()
        conversion_rate = quotes_received / total_searches * 100 if total_searches > 0 else 0
        
        pickup_data.append({
            'pickupRange': str(pickup_range),
            'totalSearches': int(total_searches),
            'quotesReceived': int(quotes_received),
            'conversionRate': float(conversion_rate)
        })
    
    # Make sure the output directory exists
    os.makedirs('chennai-rickshaw-analytics/public', exist_ok=True)
    
    # Combine all data - ensure all values are basic Python types
    output_data = {
        'summary': {
            'totalRecords': int(len(df)),
            'totalSearches': int(len(df)),
            'totalQuotes': int(df['dq.id'].notna().sum()),
            'overallConversionRate': float(df['dq.id'].notna().sum() / len(df) * 100 if len(df) > 0 else 0),
            'completed': int(len(df[df['status'] == 'COMPLETED'])),
            'cancelled': int(len(df[df['status'] == 'CANCELLED'])),
            'active': int(len(df[df['status'] == 'ACTIVE'])),
        },
        'hourlyData': hourly_data,
        'distanceData': distance_data,
        'fareData': fare_data,
        'pickupDistanceData': pickup_data
    }
    
    # Write to JSON file
    output_path = 'chennai-rickshaw-analytics/public/data.json'
    
    print(f"Writing data to {output_path}...")
    with open(output_path, 'w') as f:
        # Use a simpler approach to handle serialization issues
        json.dump(output_data, f, indent=2)
    
    print("Conversion completed!")
    
    return output_path

if __name__ == "__main__":
    convert_csv_to_json() 