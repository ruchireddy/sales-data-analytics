import pandas as pd

df = pd.read_csv('data/sales.csv')
df.dropna(inplace=True)
df['Total'] = df['Quantity'] * df['Price']
df.to_csv('data/processed_sales.csv', index=False)
print("Processed data saved to data/processed_sales.csv")
