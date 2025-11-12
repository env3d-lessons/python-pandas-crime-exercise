# python-pandas-crime-exercise

Crime data exercise

For the questions below, use the file `crime.csv`, which is a version of the
 actual vancouver crime dataset from https://geodash.vpd.ca/opendata/ and contains data on all crime types per year and per neighborhood.

Just use the file `crime.csv` to answer the questions.  DO NOT re-download.

Each question is a python script that sends the final output to stdout.  Empty files are provided, you just need to fill them in.

  1. Extract all unique years from this dataset.

  2. Extract all unique crime types from this dataset.

  3. Create an output of, per YEAR number of 'Vehicle Collision or Pedestrian Struck (with Fatality)' since the beginning of the dataset.

  4. Which year and neighborhood has the highest number of homicide

  5. Which neighborhood has the most recent homicide

  6. Which neighborhood has the most number of overall crime

  7. Output in csv format that for each year, count the number of crimes per neighbourhood.  This output can potentially be used in a race chart.  The following is the output:
  ```bash
  $ python 7.py
YEAR,Arbutus Ridge,Central Business District,Dunbar-Southlands,Fairview,Grandview-Woodland,Hastings-Sunrise,Kensington-Cedar Cottage,Kerrisdale,Killarney,Kitsilano,Marpole,Mount Pleasant,Musqueam,Oakridge,Renfrew-Collingwood,Riley Park,Shaughnessy,South Cambie,Stanley Park,Strathcona,Sunset,Victoria-Fraserview,West End,West Point Grey
2003,724,12865,835,4299,3969,2148,2652,722,1044,3469,1392,2881,72,800,2715,1300,560,651,510,3441,2156,1258,6133,646
2004,739,11933,1034,3795,3486,2205,3047,917,1313,3206,1516,3308,98,857,3106,1344,576,556,467,3348,2066,1413,5398,758
2005,684,11049,777,3833,3136,1783,2572,906,1228,2974,1568,3013,70,810,2735,1307,568,530,432,3216,1899,1297,4588,712
2006,529,11592,608,3238,2797,1796,2532,721,1116,2775,1188,2701,73,715,2785,1208,375,426,405,2719,1912,1077,4639,558
2007,438,11285,493,2973,2778,1509,2141,538,958,2164,1159,2393,40,552,2190,908,379,361,284,2489,1703,859,4243,448
...
  ```

  8. Create a script such that given a neighbourhood as argument, it'll return a dataframe describing crime per year.  As follows:

```bash
$ python 8.py 
Usage: python 8.py <NEIGHBOURHOOD>
Here are the available neighbourhoods:
Oakridge
Fairview
West End
Shaughnessy
...
@anon91825 ➜ /workspaces/python-pandas-crime-exercise (main) $ python 7.py Sunset
YEAR
2003    2156
2004    2066
2005    1899
2006    1912
2007    1703
2008    1406
2009    1293
...
```