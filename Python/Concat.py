
import pandas as pd

df1 = pd.DataFrame({'Name' : ['TSM_Ent', 'Soul', 'OR', 'Fnatic', 'Force'],
        'Leader' : ['Ghatak', 'Mortal', 'Mavi', 'Scout', 'Judwaa'],
         'Followers' : [20000,70000,10000,90000,1000]}, 
                   index = [1,2,3,4,5])


df2 = pd.DataFrame({'Name' : ['TSM_Ent', 'Soul', 'OR', 'Fnatic', 'Force'],
        'Leader' : ['Jony', 'Viper', 'Vexe', 'Pro', 'Agent'],
         'Followers' : [50000,90000,20000,70000,31000]}, 
                   index = [6,7,8,9,10])

Concat = pd.concat([df1,df2])

print(Concat)

