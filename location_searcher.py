import pandas as pd
import numpy as np

# import from csv file
tweets = pd.DataFrame.from_csv('data/postgres_output.csv')
count = len(tweets.index)
# prevent duplicated tweets
tweets = tweets[~tweets.index.duplicated()]

indexgeo = tweets[tweets['geolocationlongitude'] != 0].

# search in geotags for geotags located in Amsterdam
for index in indexgeo:
    if (tweets.loc[index, 'geolocationlongitude'] > 4.687368) & (
            tweets.loc[index, 'geolocationlongitude'] < 4.996374) & (
            tweets.loc[index, 'geolocationlatitude'] > 52.290620) & (
            tweets.loc[index, 'geolocationlatitude'] < 52.452090):
        tweets.loc[index, 'wijk'] = 'geo'
    else:
        tweets.drop(index, axis=0)
indexgeofound = tweets[tweets['wijk'] == 'geo'].index

# search in 'name' for neighhourhoods in Amsterdam

wijknamen = pd.DataFrame.from_csv('data/neighbourhood names.csv')
searchindex = tweets[tweets['name'] != 0].index
for wijk in wijknamen.columns:
    for naam in wijknamen[wijk].dropna().values:
        found = tweets.loc[searchindex, 'name'].str.contains(naam, case=False)
        found = found.fillna(value=False)
        tweets.loc[found, 'wijk'] = wijk

# search in 'screen_name' for neighhourhoods in Amsterdam
searchindex = tweets[tweets['screen_name'] != 0].index
for wijk in wijknamen.columns:
    for naam in wijknamen[wijk].dropna().values:
        found = tweets['screen_name'].str.contains(naam, case=False)
        found = found.fillna(value=False)
        tweets.loc[found, 'wijk'] = wijk

# search in 'location' for neighhourhoods in Amsterdam
searchindex = tweets[tweets['location'] != 0].index
for wijk in wijknamen.columns:
    for naam in wijknamen[wijk].dropna().values:
        found = tweets['location'].str.contains(naam, case=False)
        found = found.fillna(value=False)
        tweets.loc[found, 'wijk'] = wijk

# search in 'description' for neighhourhoods in Amsterdam
searchindex = tweets[tweets['description'] != 0].index
for wijk in wijknamen.columns:
    for naam in wijknamen[wijk].dropna().values:
        found = tweets['description'].str.contains(naam, case=False)
        found = found.fillna(value=False)
        tweets.loc[found, 'wijk'] = wijk

# search in 'text' for neighhourhoods in Amsterdam
searchindex = tweets[tweets['text'] != 0].index
for wijk in wijknamen.columns:
    for naam in wijknamen[wijk].dropna().values:
        found = tweets['text'].str.contains(naam, case=False)
        found = found.fillna(value=False)
        tweets.loc[found, 'wijk'] = wijk

## Remove all tweets that don't have a location
gefilterd = tweets['wijk'].dropna().index
tweets_met_wijk = tweets.loc[gefilterd]






print('Total tweets entered: ' + str(count))
print('Total tweets with geolocation in Amsterdam: ' + str(len(tweets[tweets['wijk'] == 'geo'].index)))
print('Total tweets found by area name search: ' + str(len(tweets_met_wijk[tweets_met_wijk['wijk'] != 'geo'].index)))

tweets_met_wijk.to_csv('data/results.csv')