import requests
import pandas as pd
file_errors_location = 'C:/Users/Birinderjeet/Desktop/image downlaoder/excel file/url.xlsx'
df = pd.read_excel(file_errors_location)

for i in range(0,len(df['url'])):
    print(i)
    p = 'images/'+str(df['name'][i])+'.jpg'
    r = requests.get(df['url'][i], stream=True)
    with open(p, 'wb') as f:
        for chunk in r:
            f.write(chunk)
            
        
    




            
        
    
                
            

        
