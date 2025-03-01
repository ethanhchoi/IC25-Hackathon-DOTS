# Python algorithim for getting the collisions. I was thinking this could be used to make a descion tree, once the dates are known to be an issue you can then use that to then determine what is valid from there.
#Im going to work on this part anyways so dont worry about it

import numpy as np
import pandas as pd
from datetime import datetime

# loads the dataset, specially just for the special events one
def loadData():
        df = pd.read_excel("dates.xlsx", engine='openpyxl')
        return df.to_numpy()

# converts a time stamp in an interger array denotes each of the date info
def conv(time):
    timestamp = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    return [timestamp.year, timestamp.month, timestamp.day, timestamp.hour, timestamp.minute, timestamp.second]

# insert a date, and check if it colides with any event, returns collision if it does
def dateColision(date):
    #
    data = loadData()
    comp = conv(date)
    for i in range(0,len(data)):
        bef = conv(data[i][1].strftime('%Y-%m-%d %H:%M:%S'))
        af = conv(data[i][2].strftime('%Y-%m-%d %H:%M:%S'))
        if (bef[0]<=comp[0] and bef[1]<=comp[1] and bef[2]<=comp[2] and af[0]>=comp[0] and af[1]>=comp[1] and af[2]>=comp[2]):
            return "collision"


    
    # day, month, year = date_str.split('/')
    # return [int(year), int(month), int(day)]

    # lots = []

    # return lots

print(dateColision("20-03-07 00:00:00"))
