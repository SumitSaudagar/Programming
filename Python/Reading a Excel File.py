
import pandas as pd

df=pd.read_excel("C:/Users/saudagar/Desktop/OfficeSupplies.xlsx")

print(df)



#
import pandas as pd

df=pd.read_excel("C:/Users/saudagar/Desktop/OfficeSupplies.xlsx", index_col=0)

print(df)



#
import pandas as pd

df=pd.read_excel("C:/Users/saudagar/Desktop/OfficeSupplies.xlsx", 
                 index_col=0, usecols="A:C")

print(df)

