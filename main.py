import pet_analysis as pa
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# File path 
file_path = '/Users/cindyalvarado/Desktop/Proyect_1/pets.csv'

# Load data 
print("-- LOAD DATA --")
df = pa.load_data(file_path)
print(df)

# Check missing values 
print("-- CHECK FOR MISSING VALUES --")
missing_values = df.isnull().sum()
print(missing_values)

# Clean data - with respecting column name and with clean data 
print("-- EXECUTING CLEAN DATA --")
df = pa.clean_data(df)
print(df)

# Print average price for a given specie
specie = 'Reptile'
print(f"- Average price for {specie} Specie is: {pa.calculate_average_price(df, specie)}")

# Print animal names with a given feature
feature = 'walks'
print(f"- Animal names that {feature}: {pa.find_pets_with_feature(df, feature)}")

# print species statistics
print(f"- SPECIES STATISTICS: ")
print(pa.get_species_statistics(df))

# plot price distrirbution 
print(f"- Plotting price distribution: {pa.plot_price_distribution(df)}")

# plot average price by species
print(f"- Plotting Average Price by Species: {pa.plot_average_price_by_species(df)}")

 # plot price vs age
print(f"- Plotting Price vs Age: {pa.plot_price_vs_age(df)}")

 # plot age distribution by species 
print(f"- Plotting Age Distribution by Species: {pa.plot_age_distribution_by_species(df)}")
