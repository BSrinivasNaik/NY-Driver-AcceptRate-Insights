import pandas as pd
import numpy as np
import datetime
import os
import sys
import matplotlib.pyplot as plt

class ChennaiDataAnalyzer:
    def __init__(self):
        self.original_file = 'Chennai_22March.csv'
        self.ist_file = 'Chennai_22March_IST.csv'
        self.df_original = None
        self.df_ist = None
        
    def check_files(self):
        """Check if the required files exist"""
        if not os.path.exists(self.original_file):
            print(f"Error: Original file '{self.original_file}' not found.")
            return False
            
        print(f"Original file '{self.original_file}' found.")
        return True
    
    def load_data(self, file_type='original'):
        """Load the specified data file"""
        try:
            if file_type == 'original':
                print(f"Loading original data from {self.original_file}...")
                self.df_original = pd.read_csv(self.original_file)
                return self.df_original
            elif file_type == 'ist':
                if os.path.exists(self.ist_file):
                    print(f"Loading IST data from {self.ist_file}...")
                    self.df_ist = pd.read_csv(self.ist_file)
                    return self.df_ist
                else:
                    print(f"IST file '{self.ist_file}' not found. Please convert to IST first.")
                    return None
            else:
                print("Invalid file type specified.")
                return None
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
    
    def convert_to_ist(self):
        """Convert dates from GST to IST in the original file"""
        if self.df_original is None:
            self.load_data('original')
            
        if self.df_original is None:
            return
            
        print("Converting dates from GST to IST...")
        
        # Create a copy of the dataframe to avoid modifying the original
        df = self.df_original.copy()
        
        # Identify date columns
        date_columns = ['created_at', 'start_time', 'dq.created_at']
        
        # Function to convert GST to IST
        def convert_date(date_str):
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
        for col in date_columns:
            df[col] = df[col].apply(convert_date)
        
        # Write the updated data to a new CSV file
        print(f"Writing IST data to {self.ist_file}...")
        df.to_csv(self.ist_file, index=False)
        
        # Update the IST dataframe
        self.df_ist = df
        
        print(f"Conversion completed. New file created: {self.ist_file}")
    
    def analyze_time_range(self, file_type='ist'):
        """Analyze the time range in the specified file"""
        # Load the appropriate dataframe
        df = None
        file_name = ""
        
        if file_type == 'original':
            if self.df_original is None:
                self.load_data('original')
            df = self.df_original
            file_name = self.original_file + " (GST times)"
        elif file_type == 'ist':
            if self.df_ist is None:
                self.load_data('ist')
            df = self.df_ist
            file_name = self.ist_file + " (IST times)"
        
        if df is None:
            return
        
        # Convert created_at to datetime
        df['created_at'] = pd.to_datetime(df['created_at'])
        
        # Get min and max timestamps
        min_time = df['created_at'].min()
        max_time = df['created_at'].max()
        
        # Calculate time range
        time_range = max_time - min_time
        hours = time_range.total_seconds() / 3600
        
        print(f"\n=== TIME RANGE ANALYSIS for {file_name} ===")
        print(f"Earliest created_at: {min_time}")
        print(f"Latest created_at: {max_time}")
        print(f"Total time span: {time_range}")
        print(f"Total hours: {hours:.2f} hours")
    
    def analyze_search_quotes(self):
        """Analyze search tries and driver quotes in the dataset"""
        # Use IST file if available, otherwise use original
        df = None
        file_name = ""
        
        if os.path.exists(self.ist_file):
            if self.df_ist is None:
                self.load_data('ist')
            df = self.df_ist
            file_name = self.ist_file
        else:
            if self.df_original is None:
                self.load_data('original')
            df = self.df_original
            file_name = self.original_file
        
        if df is None:
            return
            
        print(f"\nAnalyzing search tries and driver quotes in {file_name}...")
        
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
        
        # Analyze driver data - Clean driver ratings first
        df['driver_rating'] = pd.to_numeric(df['driver_rating'], errors='coerce')
        # Clean distance and base_fare columns as well
        df['distance'] = pd.to_numeric(df['distance'], errors='coerce')
        df['base_fare'] = pd.to_numeric(df['base_fare'], errors='coerce')
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
        # Create a boolean column for whether a driver quote is present
        df['has_driver_quote'] = df['dq.id'].notna()
        # Group by search_repeat_type and calculate the percentage of records with driver quotes
        quote_by_search_type = df.groupby('search_repeat_type')['has_driver_quote'].agg(['count', 'sum'])
        quote_by_search_type['percentage'] = (quote_by_search_type['sum'] / quote_by_search_type['count']) * 100
        print(quote_by_search_type)
        
        # Time distribution of search tries
        df['hour'] = pd.to_datetime(df['created_at']).dt.hour
        hourly_searches = df.groupby('hour').size()
        print("\n=== TIME DISTRIBUTION OF SEARCH TRIES ===")
        print(hourly_searches)

    def show_menu(self):
        """Display the main menu and handle user choices"""
        while True:
            print("\n" + "="*50)
            print("CHENNAI AUTO RICKSHAW DATA ANALYZER")
            print("="*50)
            print("1. Convert dates from GST to IST")
            print("2. Analyze time range (GST)")
            print("3. Analyze time range (IST)")
            print("4. Analyze search tries and driver quotes")
            print("5. Visualize data")
            print("6. Exit")
            print("-"*50)
            
            choice = input("Enter your choice (1-6): ")
            
            if choice == '1':
                self.convert_to_ist()
            elif choice == '2':
                self.analyze_time_range('original')
            elif choice == '3':
                self.analyze_time_range('ist')
            elif choice == '4':
                self.analyze_search_quotes()
            elif choice == '5':
                self.visualize_data()
            elif choice == '6':
                print("Exiting program. Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")
            
            input("\nPress Enter to continue...")

    def visualize_data(self):
        """Visualize the data using matplotlib"""
        # Use IST file if available, otherwise use original
        df = None
        if os.path.exists(self.ist_file):
            if self.df_ist is None:
                self.load_data('ist')
            df = self.df_ist
        else:
            if self.df_original is None:
                self.load_data('original')
            df = self.df_original
        
        if df is None:
            return
        
        # Create a figure with two subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
        
        # Plot 1: Time distribution of search tries
        df['hour'] = pd.to_datetime(df['created_at']).dt.hour
        hourly_searches = df.groupby('hour').size()
        ax1.bar(hourly_searches.index, hourly_searches.values)
        ax1.set_xlabel('Hour of Day')
        ax1.set_ylabel('Number of Searches')
        ax1.set_title('Time Distribution of Search Tries')
        
        # Plot 2: Relationship between search tries and driver quotes
        df['has_driver_quote'] = df['dq.id'].notna()
        quote_by_search_type = df.groupby('search_repeat_type')['has_driver_quote'].agg(['count', 'sum'])
        quote_by_search_type['percentage'] = (quote_by_search_type['sum'] / quote_by_search_type['count']) * 100
        quote_by_search_type['percentage'].plot(kind='bar', ax=ax2)
        ax2.set_xlabel('Search Repeat Type')
        ax2.set_ylabel('Percentage of Records with Driver Quotes')
        ax2.set_title('Relationship Between Search Tries and Driver Quotes')
        
        plt.tight_layout()
        plt.show()

# Create an instance of the analyzer and run it
if __name__ == "__main__":
    analyzer = ChennaiDataAnalyzer()
    if analyzer.check_files():
        analyzer.show_menu()
    else:
        print("Exiting due to missing files.") 