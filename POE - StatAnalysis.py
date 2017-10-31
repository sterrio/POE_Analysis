#Path of Exile statistic analysis - Oct 31st - Stephen Terrio
#Data up to the date of August 7th - 2017
import math
import pandas as pd
import numpy as np

# importing the required file
data = pd.read_csv('poe_stats.csv')

#Path of exile is seperated by :
#One league - Harbinger & 4 different divisions
print(data['ladder'].value_counts()) #prints divison info
print (data['class'].value_counts()) #prints class info

# finding if being a streamer means being a better player.

print(data.dropna()['level'])
