import requests
import json
import datetime
import time
import numpy as np
import pandas as pd
from stockstats import StockDataFrame

def getData(val):
    api_key = "your_api_key"                              #Need key to call Api
    ApiUrl = "Website_api_url" + "&api_key=" + api_key              #Url for Api call

    response = requests.get(url)
    data = json.loads(response.text)
    dataC = pd.DataFrame(data)
    
    return dataC[[val]]

def alert(a):
    date_time = datetime.datetime.now().strftime("%A %d %B %Y %H:%M:%S:%f")             
    msg = str(a) + "On " + str(date_time) + " has %Chg more than 2"
    print(msg)                                                          # Alerting company's name when %Chg difference is more than 2 
    
  
if __name__ == "__main__":
    df = getData('Company Name')
    
    ZerosList = np.array(list(0 for _ in range(len(dataC))))
    
    df['open'] = ZerosList
    df['second'] = ZerosList            # 4 columns with initial value 0 in every cell
    df['third'] = ZerosList
    df['close'] = ZerosList
    
    n=1
    while n<40:                # n=40 means 20 minutes(1200 seconds) completed 
        value = getData('%Chg')
        val = value.rename(columns={'%Chg': 'close'})
        
        df.open = df.second
        df.second = df.third             # continuos flow of data into 4 columns
        df.third = df.close
        df.update(val)
        
        if n>3:                                     #not calculate till we have complete data of 2 minutes i.e. 120 seconds(n=4)
            ls = df[['open']].tolist()
            lss = df[['close']].tolist()
            cn = df[['Company Name']].tolist()
            
            for _ in range(len(df)):
                diff = abs(ls[_]-lss[_])                  
                if diff >= 2:
                    alert(cn[_])                      # Alerting with company's name
                else:
                    pass
        else:
            pass
        
        time.sleep(30)      # refreshing time of 30 seconds
