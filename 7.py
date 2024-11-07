# This scripts create a pie chart of homicides, broken down
# by neighbourhood, per year
# It's not answering the question exactly, but you should be
# able to get to the answer from studying the code below

import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('crime.csv')

years = df['YEAR'].sort_values().unique()
fig, axs = plt.subplots(len(years), 1, figsize=(100, 100))
print(axs)
for i, year in enumerate(years):
    print(year)
    data = df[
        (df['TYPE'] == 'Homicide') & (df['YEAR'] == year)
    ].groupby(
        ['YEAR','NEIGHBOURHOOD']
    ).count()['TYPE']
    print(data)
    axs[i].pie(data, labels=data.reset_index()['NEIGHBOURHOOD'])
    axs[i].set_title(year)

plt.tight_layout()
fig.savefig('homicide.png')
plt.close(fig)