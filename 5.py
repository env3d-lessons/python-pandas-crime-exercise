import pandas
df = pandas.read_csv('crime.csv')
df = df[ df['TYPE'] == 'Homicide' ].sort_values( ['YEAR','MONTH','DAY' ], ascending=False ).head(1)['NEIGHBOURHOOD']
print(df)
