import pandas
df = pandas.read_csv('crime.csv')
print(df['YEAR'].unique())