# MyPetStore-Data-Analysis-Project

### pet_analysis.py:
This script contains functions for data loading, cleaning, analysis, and visualization related to pets. To run this script, ensure that you have the file pets.csv in the correct directory or provide the correct file path. After running the script, it will load the data, clean it, and perform various analyses and visualizations.

## Scripts and Functions

- **load_data(file_path):** Loads the pet data from a CSV file and returns a pandas DataFrame.

- **clean_data(df):** Cleans the loaded data, handling missing values and converting data types.

- **calculate_average_price(df, species):** Calculates the average price of pets belonging to a specific species.

- **find_pets_with_feature(df, feature):** Finds pets with a specific special feature.

- **get_species_statistics(df):** Calculates statistics (average price and age) for each species in the dataset.

- **plot_price_distribution(df):** Plots the distribution of pet prices.
  
- **plot_average_price_by_species(df):** Plots the average price of pets by species.
  
- **plot_price_vs_age(df):** Plots the relationship between pet age and price.
  
- **plot_age_distribution_by_species(df):** Plots the age distribution of pets by species.
  
### main.py:

This script demonstrates the usage of the functions defined in pet_analysis.py by loading data, cleaning it, and performing various analyses and visualizations.

### Visualization Output:

The visualizations will be saved as image files in the same directory where the script is executed.
