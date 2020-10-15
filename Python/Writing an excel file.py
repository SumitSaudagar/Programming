
import pandas as pd

Clan = {'Name' : ['TSM_Ent', 'Soul', 'OR', 'Fnatic', 'Force'],
        'Leader' : ['Ghatak', 'Mortal', 'Mavi', 'Scout', 'Judwaa'],
         'Followers' : [20000,70000,10000,90000,1000]}
        
df = pd.DataFrame(Clan, columns = ['Name','Leader','Followers'])

df.to_excel ('C:/Users/saudagar/Desktop/Gaming.xlsx', index=False, header = True)

