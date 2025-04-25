import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('AmesHousing.csv')
df.columns = df.columns.str.replace('Lot Frontage', 'LotFrontage')

cat_cols_none = ['Alley', 'Pool QC', 'Fence', 'Misc Feature', 'Fireplace Qu',
                 'Garage Type', 'Garage Finish', 'Garage Qual', 'Garage Cond',
                 'Bsmt Cond', 'Bsmt Exposure', 'BsmtFin Type 1', 'BsmtFin Type 2']
for col in cat_cols_none:
    df[col] = df[col].fillna('None')

df['LotFrontage'] = df.groupby('Neighborhood')['LotFrontage'].transform(
    lambda x: x.fillna(x.median())
)
overall_median = df['LotFrontage'].median()
df['LotFrontage'] = df['LotFrontage'].fillna(overall_median)
df['Mas Vnr Area'] = df['Mas Vnr Area'].fillna(df['Mas Vnr Area'].median())
df['Garage Yr Blt'] = df['Garage Yr Blt'].fillna(df['Garage Yr Blt'].median())
df['BsmtFin SF 1'] = df['BsmtFin SF 1'].fillna(df['BsmtFin SF 1'].mean())
df['BsmtFin SF 2'] = df['BsmtFin SF 2'].fillna(df['BsmtFin SF 2'].mean())
df['Bsmt Unf SF'] = df['Bsmt Unf SF'].fillna(df['Bsmt Unf SF'].mean())
df['Total Bsmt SF'] = df['Total Bsmt SF'].fillna(df['Total Bsmt SF'].mean())
df['Garage Area'] = df['Garage Area'].fillna(df['Garage Area'].mean())
df['Bsmt Full Bath'] = df['Bsmt Full Bath'].fillna(df['Bsmt Full Bath'].median())
df['Bsmt Half Bath'] = df['Bsmt Half Bath'].fillna(df['Bsmt Half Bath'].median())
df['Garage Cars'] = df['Garage Cars'].fillna(df['Garage Cars'].median())


df['Mas Vnr Type'] = df['Mas Vnr Type'].fillna(df['Mas Vnr Type'].mode()[0])
df['Bsmt Qual'] = df['Bsmt Qual'].fillna(df['Bsmt Qual'].mode()[0])
df['Electrical'] = df['Electrical'].fillna(df['Electrical'].mode()[0])

df['SalePrice'] = df['SalePrice'].apply(lambda x: f"${x:,.0f}")
df['Lot Area'] = df['Lot Area'].apply(lambda x: f"{x:,.0f}")

print(df.duplicated().sum())
print(df)

df['SalePriceNum'] = df['SalePrice'].str.replace('$', '').str.replace(',', '').astype(float)
df['MS SubClass'] = df['MS SubClass'].astype(str)

plt.figure(figsize=(12, 6))
sns.scatterplot(x='MS SubClass', y='SalePriceNum', data=df)
plt.title('SalePrice Distribution')
plt.xlabel('MS SubClass (Dwelling Type)')
plt.ylabel('Sale Price ($)')
plt.xticks(rotation=45)
plt.show()