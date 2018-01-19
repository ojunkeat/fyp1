import csv
import pandas as pd
import math

data = pd.read_csv('price.csv')
df = pd.DataFrame(data)
# df.to_csv('new_price.csv')

prices = []
for index, row in  df.iterrows(): 
    for i in range(6, len(row)):
        if not math.isnan(row[i]):                    
            prices.append(row[i])
    print(sum(prices)/len(prices))
    prices = []


    