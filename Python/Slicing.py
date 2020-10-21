#Head
import pandas as pd

College = {'Department' : ['Civil','Computer','Mechanical','E&Tc'],
            'HOD' : ['Vinit','Sumit','Rohit','Satish'],
             'No of Students' : [60,120,60,60]}

df = pd.DataFrame(College, columns = ['Department','HOD','No of Students'])

print(df.head(2))


#Tail

import pandas as pd

College = {'Department' : ['Civil','Computer','Mechanical','E&Tc'],
            'HOD' : ['Vinit','Sumit','Rohit','Satish'],
             'No of Students' : [60,120,60,60]}

df = pd.DataFrame(College, columns = ['Department','HOD','No of Students'])

print(df.tail(2))


