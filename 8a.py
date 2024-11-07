# Code to create a pivot table manually
# Can you pick out the potential problems with this script?
import pandas

df = pandas.read_csv('crime.csv')
summary = df[ ['YEAR', 'NEIGHBOURHOOD', 'TYPE'] ].groupby( ['YEAR', 'NEIGHBOURHOOD'] )['TYPE'].count().reset_index()
#print(summary)

years = summary['YEAR'].unique()
neighbourhoods = summary['NEIGHBOURHOOD'].unique()
#print(neighbourhoods)

data = {}
for area in neighbourhoods:
	data[area] = summary[ summary['NEIGHBOURHOOD'] == area ]['TYPE'].to_list()

#print(data)

df = pandas.DataFrame(data, index=years)
print(df)