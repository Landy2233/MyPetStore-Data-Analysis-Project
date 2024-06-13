import pet_analysis as pa
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# File path 
file_path = '/Users/landyjimenez/Desktop/Project 1/pets.csv'

# Load data 
df = pa.load_data(file_path)
print(df)

# Clean data
print("- Executing clean_data")
df = pa.clean_data(df)
print(df)

# Print average price for a given specie
specie = 'Rabbit'
print(f"- Average price for {specie} Specie is: {pa.calculate_average_price(df, specie)}")

# Print animal names with a given feature
feature = 'flies'
print(f"- Animal names that {feature}: {pa.find_pets_with_feature(df, feature)}")

# print species statistics
print(f"- Species Statistics: ")
print(pa.get_species_statistics(df))
print(f"- Price: \n {df['Price']}")
print(f"- Age: \n {df['Age'].tolist()}")
print(f"- Birthdate: \n {df['Birthdate'].dt.strftime('%Y-%m-%d').tolist()}")
print(f"- data: \n {df}")
# plot price distrirbution 
print(f"- Plotting price distribution: {pa.plot_price_distribution(df)}")

# plot average price by species
print(f"- Plotting Average Price by Species: {pa.plot_average_price_by_species(df)}")

 # plot price vs age
print(f"- Plotting Price vs Age: {pa.plot_price_vs_age(df)}")

 # plot age distribution by species 
print(f"- Plotting Age Distribution by Species: {pa.plot_age_distribution_by_species(df)}")
