import pandas
import sys

if len(sys.argv) < 2:
    print("Usage: python 8.py <NEIGHBOURHOOD>")
    print("Here are the available neighbourhoods:")
    df = pandas.read_csv('crime.csv')
    for neighbourhood in df['NEIGHBOURHOOD'].unique():
        print(neighbourhood)
    sys.exit(1)

neighbourhood = sys.argv[1]

df = pandas.read_csv('crime.csv')
df = df[ df['NEIGHBOURHOOD'] == neighbourhood ].groupby('YEAR')['TYPE'].count()

print(df)