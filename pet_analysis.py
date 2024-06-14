import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# Load Data
def load_data(file_path):
    # Read the CSV file 
    df = pd.read_csv("pets.csv")
    return df


# Clean data 
def clean_data(df):
     # Create column names 
    column_names = ["Name", "Birthdate", "Price", "Species", "SpecialFeature", "Unnamed"]
    # Assign column names to the DataFrame
    df.columns = column_names
    # Delete the empty column
    df.drop(columns=["Unnamed"], inplace=True)
    # Removing the last row
    df = df[:-1]    
    # Convert 'Birthdate' to datetime
    df['Birthdate'] = pd.to_datetime(df['Birthdate'])
    # Convert 'Price' to float
    df['Price'] = df['Price'].astype(float)
    return df # Display the cleaned DataFrame


## TASK 2: Decision Making and Loops
# Calculate average price
def calculate_average_price(df, species):
    for price in df['Species']:
        species_df = df[df['Species'] == species]
        avg_price = round(species_df['Price'].mean(), 1)
    # species_df = df[df['Species'] == species]
   #  avg_price = species_df['Price'].mean()
   
    return avg_price

# Find pets with feature 
def find_pets_with_feature(df, feature):
    feature_df = df[df['SpecialFeature'] == feature]
    list_fetaure_df = feature_df['Name'].tolist()
    return list_fetaure_df


# calculate age 
def calculate_age_in_years(birthdate):
    # Get the current date
    current_date = datetime.now()

    # Calculate the difference between the current date and the birthdate
    age_difference = current_date - birthdate

    # Calculate the age in years
    age_in_years = round(age_difference.days / 365.25, 1)  # Assuming a year has 365.25 days on average

    return age_in_years

## TASK 3: Functions and Modules
# get stats 
def get_species_statistics(df):
    # Add 'Age' column
    df['Age'] = df['Birthdate'].apply(calculate_age_in_years)
    
    # Group by species and calculate average price and average age
    species_stats = round(df.groupby('Species').agg({'Price': 'mean', 'Age': 'mean'}).reset_index(),1)
    
    # Create the dictionary with the desired format
    stats_dict = {row['Species']: {'Average Price': row['Price'], 'Average Age': row['Age']} for index, row in species_stats.iterrows()}
    return stats_dict
## TASK 4: Data visualization with Mathplotlib
def plot_price_distribution(df):
    plt.figure(figsize=(12, 6),facecolor='beige')
    plt.hist(df['Price'], bins=30, edgecolor='k', alpha=0.7,facecolor='lightblue')
    plt.title('Price Distribution of Pets', fontsize=18, fontweight='bold', color='black', family='Times New Roman',
              bbox=dict(facecolor='pink', alpha=0.4))
    plt.xlabel('Price', fontsize=14, fontweight='bold', color='black', family='Times New Roman')
    plt.ylabel('Frequency', fontsize=14, fontweight='bold', color='black', family='Times New Roman')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig('price_distribution.png')
    plt.close()
    plt.show()
    
# plot average price by species
def plot_average_price_by_species(df):
    plt.figure(figsize=(12, 8), facecolor='beige')
    avg_prices = df.groupby('Species')['Price'].mean().sort_values()
    avg_prices.plot(kind='bar', color='lightgreen')
    
    plt.title('Average Price by Species', fontsize=18, fontweight='bold', color='darkgreen', family='Times New Roman',
              bbox=dict(facecolor='lightblue', alpha=0.4))
    plt.xlabel('Species', fontsize=14, fontweight='bold', color='darkgreen', family='Times New Roman')
    plt.ylabel('Average Price', fontsize=14, fontweight='bold', color='darkgreen', family='Times New Roman')
    
    plt.xticks(rotation=45, fontsize=12, color='darkgreen', family='Times New Roman')
    plt.yticks(fontsize=12, color='darkgreen', family='Times New Roman')
    
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.savefig('average_price_by_species.png')
    plt.close()
    plt.show()
    
## TASK 5: Data Visualization with Seaborn and Plotly
# plo price vs age
def plot_price_vs_age(df):
    plt.figure(figsize=(12, 6), facecolor='beige')
    sns.scatterplot(x='Age', y='Price', data=df, color='black', alpha=0.7)
    
    plt.title('Price vs Age of Pets', fontsize=18, fontweight='bold', color='purple', family='Times New Roman',
              bbox=dict(facecolor='pink', alpha=0.4))
    plt.xlabel('Age (years)', fontsize=14, fontweight='bold', color='purple', family='Times New Roman')
    plt.ylabel('Price', fontsize=14, fontweight='bold', color='purple', family='Times New Roman')
    
    plt.xticks(fontsize=12, color='black', family='Times New Roman')
    plt.yticks(fontsize=12, color='black', family='Times New Roman')
    
    plt.grid(axis='both', linestyle='--', alpha=0.7)
    
    plt.savefig('price_vs_age.png')
    plt.close()
    plt.show()
# plot age distribution by species
def plot_age_distribution_by_species(df):
    fig = px.box(df, x='Species', y='Age', color='Species', title='Age Distribution by Species',  template='plotly_white')
    
    fig.update_layout(
        title={'text': 'Age Distribution by Species',
               'font': {'size': 18, 'family': 'Times New Roman', 'color': 'black'},
               'xanchor': 'center', 'x': 0.5,
               'yanchor': 'top', 'y': 0.9, # Adjust the position vertically
              },
        xaxis_title={'font': {'size': 14, 'family': 'Times New Roman', 'color': 'black'}},
        yaxis_title={'font': {'size': 14, 'family': 'Times New Roman', 'color': 'black'}},
        font=dict(family="Times New Roman", size=12, color="black"),
        xaxis={'tickfont': {'size': 12, 'family': 'Times New Roman', 'color': 'black'}},
        yaxis={'tickfont': {'size': 12, 'family': 'Times New Roman', 'color': 'black'}},
    )
    fig.update_layout(
        plot_bgcolor='beige',  # Set plot background color to beige
        paper_bgcolor='lightblue',  # Set general background color to beige
       
    )

    fig.write_image('age_distribution_by_species.png')
