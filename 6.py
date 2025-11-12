import pandas
df = pandas.read_csv('crime.csv')
df = df.groupby('NEIGHBOURHOOD').count()['TYPE'].sort_values(ascending=False).head(1).reset_index()['NEIGHBOURHOOD']
print(df)