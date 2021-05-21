import pandas as pd
df = pd.read_excel('hotel.xlsx','data')
print(df['source link'].values.tolist())