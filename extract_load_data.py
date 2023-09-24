import requests
import json
from sqlalchemy import create_engine
import pandas as pd

def extract_load_flood_data():
    
    # the API for accessing flood monitoring data (refer to https://developer.data.gov.my/realtime-api/flood-warning)
    # have other multiple params could be refer to, it is a real time api
    api_url = "http://api.data.gov.my/flood-warning"
    params = {"filter": "Klang@district"}
    
    # the uri for accessing ur postgresql database 
    # you might need to change accordingly prior running the script 
    DATABASE_URI = "postgresql://kang:kang@localhost:5432/flood"
    engine = create_engine(DATABASE_URI)
    table_name = 'flood_site'

    # get the responses of flood monitoring site around Klang
    response = requests.get(api_url,params=params)
    
    if response.status_code == 200:
        
        # extract the data
        info = json.loads(response.content.decode('utf-8'))
        
        # put it into dataframe
        df = pd.DataFrame(info)
        
        # drop unneccessary column
        df.drop(columns=['water_level_update_date','rainfall_update_date'],inplace=True)
        
        insertion = df.to_sql(table_name,
                              engine,
                              if_exists='append',  # Choose 'replace', 'append', or 'fail' as needed
                              index=False  # Set to True if you want to include the DataFrame index as a column
                             )
        
        print(f'There are {insertion} insertion in total!')
    else:
        print('Bad request, kindly check your api_url')
        
        