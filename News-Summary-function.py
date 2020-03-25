import requests
import json
import pandas as pd



def nsf(nTitle,nText):
    n = len(nTitle)
    
    for _ in range(n):
        flag = False
        sentences = list(nText[_].strip().split('.'))
        for sentence in sentences:                                # it will print title of news once and senteces if keyword matches
            for word in sentence:
                if str(word) in keyWords:
                    if not flag:
                        print(nTitle[_])
                        flag = True
                    print(sentence)
    
    
def getNews():
    api_key = "your_api_key"                              #Need key to call Api
    ApiUrl = "Website_api_url" + "&api_key=" + api_key              #Url for Api call

    response = requests.get(url)
    data = json.loads(response.text)
    df = pd.DataFrame(data)                         # News stored in table with title, summary, full-news and url in different columns  
    
    return df

if __name__ == "__main__":
    news = getNews()
    
    keyWords = ['surge','acquisitions','IPO', """ .....other keywords..... """]
    kw = list(input().strip().split(" "))
    for word in kw:                            # take keywords as input string with words seperated with space and store in keyWords
        keyWords.append(word)
 
    nTitle = news['title'].tolist()             # title are stored in list
    nText = news['full-news'].tolist()          # news text are stored in another list 
    
    nsf(nTitle,nText)
   
                
    
    
  
