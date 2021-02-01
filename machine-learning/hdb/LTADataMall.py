import numpy as np
import pandas as pd
import json
import requests

key = input('Input API Key: ')
filepath = input('Input Filepath: ')

for i in range(0,20):

    if i == 0:
        r = requests.get("http://datamall2.mytransport.sg/ltaodataservice/BusStops",
                         headers={'AccountKey':key, 'accept':'application/json'})
        results = json.loads(r.text)
        result_df = pd.DataFrame.from_dict(results['value'])

    else:
        try:
            r = requests.get("http://datamall2.mytransport.sg/ltaodataservice/BusStops?$skip={}".format(500*i),
                             headers={'AccountKey':key, 'accept':'application/json'})
            results = json.loads(r.text)
            temp_df = pd.DataFrame.from_dict(results['value'])
            result_df = pd.concat([result_df,temp_df], ignore_index=True)

        except:

result_df.to_csv('{}/bus_stops.csv'.format(filepath))

for i in range(0,20):

    if i == 0:
        r = requests.get("http://datamall2.mytransport.sg/ltaodataservice/TaxiStands",
                         headers={'AccountKey':key, 'accept':'application/json'})
        results = json.loads(r.text)
        result_df = pd.DataFrame.from_dict(results['value'])

    else:
        try:
            r = requests.get("http://datamall2.mytransport.sg/ltaodataservice/TaxiStands?$skip={}".format(500*i),
                             headers={'AccountKey':key, 'accept':'application/json'})
            results = json.loads(r.text)
            temp_df = pd.DataFrame.from_dict(results['value'])
            result_df = pd.concat([result_df,temp_df], ignore_index=True)

        except:
            pass

result_df.to_csv('{}/taxi_stands.csv'.format(filepath))
