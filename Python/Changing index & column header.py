# changing index
import pandas as pd

df = pd.DataFrame({'No' : [1,2,3,4,5], 'Name' : ['TSM_Ent', 'Soul', 'OR', 'Fnatic', 'Force'],
        'Leader' : ['Ghatak', 'Mortal', 'Mavi', 'Scout', 'Judwaa'],
         'Followers' : [20000,70000,10000,90000,1000]})

df.set_index('No', inplace=True)

print(df)



#changing column header

import pandas as pd

df = pd.DataFrame({'Name' : ['TSM_Ent', 'Soul', 'OR', 'Fnatic', 'Force'],
        'Leader' : ['Ghatak', 'Mortal', 'Mavi', 'Scout', 'Judwaa'],
         'Followers' : [20000,70000,10000,90000,1000]})

df = df.rename(columns={'Name':'Clan Name'})

print(df)







