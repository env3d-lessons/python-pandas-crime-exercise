import pandas
df = pandas.read_csv('crime.csv')
race = df.groupby(['YEAR', 'NEIGHBOURHOOD']).count().reset_index().pivot( index='YEAR', columns = 'NEIGHBOURHOOD', values='TYPE')
print(race.to_csv())