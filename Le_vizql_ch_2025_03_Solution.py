"""
DataDevQuest - DDQ2025-03
Challenged By: Cristian Saavedra Desmoineaux
Level: Beginner
Created By: Le Luu

Objective: Familiarize yourself with VizQL Data Service, and connect and execute a query to a published data source.
Description: 
Use the filter by Category to keep only Furniture and Technology.
"""


import requests
import json
import pandas as pd

#Declare a function to get token
#Requires the URL, Personal Access Token (Name and Key) and Site ID
def get_token(url, PAT_NAME, PAT_SECRET, SITE_ID):
    
    payload = json.dumps({
      # Define the credentials data
      "credentials": {
        "personalAccessTokenName": PAT_NAME,
        "personalAccessTokenSecret": PAT_SECRET,
        "site": {
          "contentUrl": SITE_ID
        }
      }
    })
    
    headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    }

    #Send POST request to get the response
    response = requests.request("POST", url, headers=headers, data=payload)
    #Store the response in data variable
    data=response.json()
    #Only get the token value from the response
    token = data['credentials']['token']

    return token


#Define the query_data function to pull the data from the published data source
#Requires the retrieved token, URL and LUID from the data source
def query_data(token, url, LUID):
    payload = {
        #input the LUID from the published data source
        "datasource": {
            "datasourceLuid": LUID
        },
        "options": {
            "debug": True
        },
        #send the query to server with fields, and filters
        "query": {
            "fields": [
                {
                    "fieldCaption": "Region"
                },
                #I add this field to check if the Category only returns Furniture and Technology
                {
                    "fieldCaption": "Category"
                },
                {
                    "fieldCaption": "Sales",
                    "function": "SUM"
                }
            ],
            #The challenge requests the Category by keeping only Furniture and Technology
            #So use the SET filter Type and set exclude to False (it means keep that values)
            "filters": [
                {
                    "field": {
                        "fieldCaption": "Category"
                    },
                    "filterType": "SET",
                    "values": ["Furniture", "Technology"],
                    "exclude": False
                }
            ]
        }
    }

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'x-tableau-auth': token
    }

    #Send the POST request to server and get the response
    response = requests.post(url, headers=headers, json=payload)
    
    #Parse the JSON data from the response and store it in a pandas data frame
    data = response.json()
    df = pd.DataFrame(data['data'])

    return df

#Declare the main function to set the credentials info and also print the result to the screen
def main():
    url = "https://10ax.online.tableau.com/api/3.24/auth/signin"
    PAT_NAME = "test"
    PAT_SECRET = "Your_PAT_Secret"
    SITE_ID = "Your_Site_ID"

    QUERY_URL = "https://10ax.online.tableau.com/api/v1/vizql-data-service/query-datasource"
    LUID = "Your_Datasource_LUID"
    
    #Call the get_token function to retrieve the token
    token = get_token(url, PAT_NAME, PAT_SECRET, SITE_ID)

    #Call the query_data function to retrieve data from the query
    my_data = query_data(token,QUERY_URL,LUID)

    #Print out the screen
    print("Result of DataDev Quest 2025-03 VDS:")
    print(my_data)

if __name__ == "__main__":
    main()