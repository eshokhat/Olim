import pandas as pd
import matplotlib.pyplot as plt

combined_table_path = '/Users/eshochat/Downloads/Olim/combined_table.csv'

def aliya_by_settlement(yeshuv_klita):
    try:
        # Load data from the CSV file
        df = pd.read_csv(combined_table_path)
        
        # Filter data for the specified year
        year_data = df[df['yeshuv_klita'] == yeshuv_klita]
        
        # Group by year and count number of olims
        grouped_data = year_data.groupby('year_aliya').size().reset_index(name='olims')
        
        # Extracting data into separate lists for plotting
        years = grouped_data['year_aliya'].tolist()
        olims = grouped_data['olims'].tolist()
        
        if not years:
            print(f"No data found for {yeshuv_klita}")
            return
        
        # Create a line plot using matplotlib
        plt.figure(figsize=(12, 6))
        plt.plot(years, olims, marker='o', linestyle='-', color='blue', label=f'Olims per Year in the {yeshuv_klita}')
        
        # Adding labels and title
        plt.xlabel(f'{yeshuv_klita}')
        plt.ylabel('Olims')
        plt.title(f'Olims Distribution for {yeshuv_klita} by Year')
        plt.xticks(years)
        plt.legend()
        
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print(f"File '{combined_table_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")