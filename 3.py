import pandas
df = pandas.read_csv('crime.csv')
fatality_df = df[ df['TYPE'] == 'Vehicle Collision or Pedestrian Struck (with Fatality)' ]
fatality_df = fatality_df.groupby('YEAR')['TYPE'].count()
print(fatality_df)