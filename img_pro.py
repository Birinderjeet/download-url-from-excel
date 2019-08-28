#import lib
import requests
import pandas as pd

#get excel file from storage
file_errors_location = 'C:/Users/Birinderjeet/Desktop/image downlaoder/excel file/url.xlsx'
df = pd.read_excel(file_errors_location)

for i in range(0,len(df['url'])):
    print(i)
    #set name of images
    p = 'images/'+str(df['name'][i])+'.jpg'

    #downloading file from url
    r = requests.get(df['url'][i], stream=True)
    with open(p, 'wb') as f:
        for chunk in r:
            f.write(chunk)
            
        
    




            
        
    
                
            

        
