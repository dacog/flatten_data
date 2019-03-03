import pandas as pd
from pandas.io.json import json_normalize

def venues_explore(client,lat,lng, limit=100, verbose=0, sort='popular', radius=2000, offset=1, day='any',query=''):
    '''funtion to get n-places using explore in foursquare, where n is the limit when calling the function.
    This returns a pandas dataframe with name, city ,country, lat, long, address and main category as columns
    Arguments: *client, *lat, *long, limit (defaults to 100), radius (defaults to 2000), verbose (defaults to 0), offset (defaults to 1), day (defaults to any)'''
    # create a dataframe
    df_a = pd.DataFrame(columns=['Name', 
    'City', 
    'Latitude',
    'Longitude',
    'Category',
    'Address'])
    ll=lat+','+lng
    if offset<=50:
        for i_offset in range(0,offset):
            #get venues using client https://github.com/mLewisLogic/foursquare
            venues = client.venues.explore(params={'ll':ll,
            'limit':limit, 
            'intent' : 'browse',
            'sort':sort, 
            'radius':radius, 
            'offset':i_offset,
            'day':day,
            'query':query
            })
            venues=venues['groups'][0]['items']
            df_venues = pd.DataFrame.from_dict(venues)
            df_venues['venue'][0]
            #print('limit', limit, 'sort', sort, 'radius', radius)
            for i, value in df_venues['venue'].items():
                if verbose==1:
                    print('i', i, 'name', value['name'])
                venueName=value['name']
                try:
                    venueCity=value['location']['city']
                except:
                    venueCity=''
                venueCountry=value['location']['country']
                venueLat=value['location']['lat']
                venueLng=value['location']['lng']
                venueCountry=value['location']['country']
                try:
                    venueAddress=value['location']['address']
                except:
                    venueAddress=''
                venueCategory=value['categories'][0]['name']
                df_a=df_a.append([{'Name':venueName, 
                                   'City':venueCity,
                                   'Country':venueCountry,
                                   'Latitude':venueLat,
                                   'Longitude':venueLng,
                                   'Category':venueCategory,
                                   'Address':venueAddress
                                  }])
    else:
        print('ERROR: offset value per Foursquare API is up to 50. Please use a lower value.')
    return df_a.reset_index()

def venues_explore_near(client,near, limit=100, verbose=0, sort='popular', radius=100000, offset=1, day='any',query=''):
    '''funtion to get n-places using explore in foursquare, where n is the limit when calling the function.
    This returns a pandas dataframe with name, city ,country, near, address and main category as columns.
    "near" argument searches within the bounds of the geocode for a string naming a place in the world.
    Arguments: *client, *near, limit (defaults to 100), radius (defaults to 100000, max according to api docs), verbose (defaults to 0), offset (defaults to 1), day (defaults to any)'''
    # create a dataframe
    df_a = pd.DataFrame(columns=['Name', 
    'City', 
    'Latitude',
    'Longitude',
    'Category',
    'Address'])
    if offset<=50:
        for i_offset in range(0,offset):
            #get venues using client https://github.com/mLewisLogic/foursquare
            venues = client.venues.explore(params={'near':near,
            'limit':limit, 
            'intent' : 'browse',
            'sort':sort, 
            'radius':radius, 
            'offset':i_offset,
            'day':day,
            'query':query
            })
            venues=venues['groups'][0]['items']
            df_venues = pd.DataFrame.from_dict(venues)
            df_venues['venue'][0]
            #print('limit', limit, 'sort', sort, 'radius', radius)
            for i, value in df_venues['venue'].items():
                if verbose==1:
                    print('i', i, 'name', value['name'])
                venueName=value['name']
                try:
                    venueCity=value['location']['city']
                except:
                    venueCity=''
                venueCountry=value['location']['country']
                venueLat=value['location']['lat']
                venueLng=value['location']['lng']
                venueCountry=value['location']['country']
                try:
                    venueAddress=value['location']['address']
                except:
                    venueAddress=''
                venueCategory=value['categories'][0]['name']
                df_a=df_a.append([{'Name':venueName, 
                                   'City':venueCity,
                                   'Country':venueCountry,
                                   'Latitude':venueLat,
                                   'Longitude':venueLng,
                                   'Category':venueCategory,
                                   'Address':venueAddress
                                  }])
    else:
        print('ERROR: offset value according to Foursquare API is up to 50. Please use a lower value.')
    return df_a.reset_index()

def get_categories():
    '''Function to get a Pandas DataFrame of all categories in Foursquare as listed in https://developer.foursquare.com/docs/resources/categories
    It uses json_normalize to get nested information and return a DataFrame with main, sub and sub-sub categories name and ID'''
    df1 = pd.read_json('https://api.foursquare.com/v2/venues/categories?v=20170211&oauth_token=QEJ4AQPTMMNB413HGNZ5YDMJSHTOHZHMLZCAQCCLXIX41OMP&includeSupportedCC=true')
    df1=df1.iloc[0,1]
    df1 = json_normalize(df1)

    #json_normalize(df1.iloc[0,0])
    i=0
    df_size=df1.shape[0]
    df_cat=pd.DataFrame()


    for i in range(i,df_size):
        #print('print',df1.iloc[i,0])
        
        #normalize subcategories
        new_cats=json_normalize(df1.iloc[i,0])
        #get new df size
        new_size=new_cats.shape[0]
        #print('new_size',new_size)
        #new vars
        i_sub=0
        new_sub_cat=pd.DataFrame() #new df for sub sub cats
        #iterate to get sub sub categories
        for i_sub in range(i_sub,new_size):
            sub_cats=json_normalize(new_cats.iloc[i_sub,0]) #normalize sub sub categories
            sub_cats['Sub-Main Category Name']=new_cats.iloc[i_sub, new_cats.columns.get_loc('name')] #for sub sub categories assign parent name
            sub_cats['Sub-Main Category ID']=new_cats.iloc[i_sub, new_cats.columns.get_loc('id')] #for sub sub categories assign parent ID
            #print('sub sub head', sub_cats.head())
            new_sub_cat=new_sub_cat.append(sub_cats)
            #print('new sub cats shape', new_sub_cat.shape)
        #print(type(new_cats))
        new_sub_cat['Main Category Name']=df1.iloc[i, df1.columns.get_loc('name')]
        new_sub_cat['Main Category ID']=df1.iloc[i, df1.columns.get_loc('id')]
        df_cat=df_cat.append(new_sub_cat)

    df_cat.drop(['categories','countryCodes', 'icon.mapPrefix', 'icon.prefix', 'icon.suffix'], axis=1, inplace=True)

    print('There are %i Main Categories, %i sub-categories and %i sub-sub categories'% (df_cat['Main Category Name'].unique().size, df_cat['Sub-Main Category Name'].unique().size, df_cat['name'].unique().size))
    return df_cat
    
    
    
    
    
    