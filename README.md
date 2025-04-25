# Data-Cleaning
This Python script performs data cleaning and basic visualization on the Ames Housing dataset from Kaggle. It prepares the dataset for analysis by handling missing values, formatting data, and visualizing sale prices by dwelling type.

## Key Steps:
### Import Libraries: Uses pandas, matplotlib, and seaborn for data manipulation and visualization.

### Column Name Fix: Standardizes the column name Lot Frontage to LotFrontage.

### Handle Missing Values:

Categorical features like Alley, Fence, etc. are filled with 'None'.

Numerical columns such as LotFrontage, Garage Yr Blt, and basement areas are imputed using group medians, overall medians, or means.

Mode imputation is applied to key categorical columns (Mas Vnr Type, Bsmt Qual, Electrical).

### Formatting:

Formats SalePrice and Lot Area for readability (adds $ and comma separators).

Converts MS SubClass to a string for categorical plotting.

### Visualization:

Generates a scatter plot showing the distribution of Sale Price across different MS SubClass categories.

### Output:
A clean and formatted dataframe.

A scatter plot: MS SubClass vs. Sale Price.
