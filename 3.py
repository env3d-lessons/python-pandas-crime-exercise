fatality_df = df[ df['TYPE'] == 'Vehicle Collision or Pedestrian Struck (with Fatality)' ]
fatality_df.groupby('YEAR')['TYPE'].count()