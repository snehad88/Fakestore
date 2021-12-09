#import Libraries
import requests
import json
import pandas as pd
url = "https://fakestoreapi.com/products"

#Requesting server to get the details and storing response in result variable
response = requests.get(url)
data = response.json()
print(json.dumps(response.json(),indent=4))
df = pd.DataFrame(data) 

#Creating a CSV file 
Fakestore = df
Fakestore.to_csv('C:\\Users\Raghav\\Downloads\\Fakestore.csv') 
print('Fakestore')
