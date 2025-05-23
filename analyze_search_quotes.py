import pandas as pd
import numpy as np

# Load the IST converted file
print("Analyzing search tries and driver quotes...")
df = pd.read_csv('Chennai_22March_IST.csv')

# Basic dataset stats
total_records = len(df)
print(f"\nTotal records in dataset: {total_records}")

# Analyze search tries
search_repeat_counts = df['search_repeat_counter'].value_counts().sort_index()
search_repeat_types = df['search_repeat_type'].value_counts()

# Analyze driver quotes
driver_quotes_present = df['dq.id'].notna().sum()
driver_quotes_absent = df['dq.id'].isna().sum()

# Analyze completed vs cancelled rides
completed_rides = df[df['status'] == 'COMPLETED']
cancelled_rides = df[df['status'] == 'CANCELLED']
active_rides = df[df['status'] == 'ACTIVE']

# Analyze driver data
drivers_with_ratings = df['driver_rating'].notna().sum()
avg_driver_rating = df['driver_rating'].mean()

# Analyze fare and distance data
avg_base_fare = df['base_fare'].mean()
avg_distance = df[df['distance'].notna()]['distance'].mean() / 1000  # Convert to kilometers

# Print results
print("\n=== SEARCH TRY ANALYSIS ===")
print(f"Search repeat counter distribution:\n{search_repeat_counts}")
print(f"\nSearch repeat type distribution:\n{search_repeat_types}")

print("\n=== DRIVER QUOTE ANALYSIS ===")
print(f"Records with driver quotes: {driver_quotes_present} ({driver_quotes_present/total_records*100:.2f}%)")
print(f"Records without driver quotes: {driver_quotes_absent} ({driver_quotes_absent/total_records*100:.2f}%)")

print("\n=== RIDE STATUS ANALYSIS ===")
print(f"Completed rides: {len(completed_rides)} ({len(completed_rides)/total_records*100:.2f}%)")
print(f"Cancelled rides: {len(cancelled_rides)} ({len(cancelled_rides)/total_records*100:.2f}%)")
print(f"Active rides: {len(active_rides)} ({len(active_rides)/total_records*100:.2f}%)")

print("\n=== DRIVER ANALYSIS ===")
print(f"Drivers with ratings: {drivers_with_ratings} ({drivers_with_ratings/total_records*100:.2f}%)")
print(f"Average driver rating: {avg_driver_rating:.2f}")

print("\n=== FARE AND DISTANCE ANALYSIS ===")
print(f"Average base fare: ₹{avg_base_fare:.2f}")
print(f"Average distance: {avg_distance:.2f} km")

# Analyze relationship between search tries and driver quotes
print("\n=== RELATIONSHIP BETWEEN SEARCH TRIES AND DRIVER QUOTES ===")
# Group by search_repeat_type and calculate the percentage of records with driver quotes
quote_by_search_type = df.groupby('search_repeat_type')['dq.id'].notna().agg(['count', 'sum'])
quote_by_search_type['percentage'] = (quote_by_search_type['sum'] / quote_by_search_type['count']) * 100
print(quote_by_search_type)

# Time distribution of search tries
df['hour'] = pd.to_datetime(df['created_at']).dt.hour
hourly_searches = df.groupby('hour').size()
print("\n=== TIME DISTRIBUTION OF SEARCH TRIES ===")
print(hourly_searches) 