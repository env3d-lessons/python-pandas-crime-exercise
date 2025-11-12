import pandas
df = pandas.read_csv('crime.csv')
df = df[ df['TYPE'] == 'Homicide' ].groupby( ['YEAR', 'NEIGHBOURHOOD'] ).count()['TYPE'].sort_values(ascending=False).head(1)
print(df)