import pandas as pd
import re
df = pd.read_csv('pokemon_data.csv')

# read headers
# df.columns

# read each column
# print(df[['Name', 'HP']])

# read each row
# print(df.iloc[1:4])
#for index, row in df.iterrows():
#    print(index, row['Name'])

# printing out specific type
# fire = df.loc[df['Type 1'] == "Fire"]
# print(fire)

# read specific row and column
# print(df.iloc[2,1])


# sorting by name ascending
# name_sort = df.sort_values('Name')
# print(name_sort)

# sorting by name descending
# name_sort = df.sort_values('Name', ascending=False)
# print(name_sort)

# 2 ways of adding different values to a new column
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
df['total'] = df.iloc[:, 4:10].sum(axis=1)
# print(df.head(5))

# rearranging columns
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
# print(df)

# saving new csv
df.to_csv('modified.csv', index=False)

# filtering data
# grass_poison = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2']  == 'Poison') & (df['HP'] > 70)]
# grass_poison.to_csv('filtered.csv')
# print(grass_poison)

#reset index
# grass_poison = grass_poison.reset_index()
# grass_poison.to_csv('filtered.csv')
# print(grass_poison)

# regex filtering (filter based on textual patterns)
# new_df = df.loc[df['Name'].str.contains('Mega')]
# new_df = df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)]
# new_df = df.loc[df['Name'].str.contains('^Pi[a-z]', regex=True)]

# conditional changes
# df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Fire'
# print(df)

# aggregate statistics (groupby)
