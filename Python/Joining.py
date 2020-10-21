
import pandas as pd

df1 = pd.DataFrame({'Name' : ['TSM_Ent', 'Soul', 'OR', 'Fnatic', 'Force'],
        'Leader' : ['Ghatak', 'Mortal', 'Mavi', 'Scout', 'Judwaa'],
         'Follower' : [20000,70000,10000,90000,1000]},
          index = [0,1,2,3,4])

df2 = pd.DataFrame({'Names' : ['TSM_Ent', 'Soul', 'Megastars', 'Fnatic', 'Force'],
        'Leaders' : ['Ghatak', 'Mortal', 'Vexe', 'Scout', 'Judwaa'],
         'Followers' : [20000,70000,20000,90000,1000]},
          index = [0,1,5,3,4])

joined = df1.join(df2)

print(joined)

