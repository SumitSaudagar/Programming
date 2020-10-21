
import pandas as pd


OfficeSupplies = pd.read_excel('C:/Users/saudagar/Desktop/OfficeSupplies.xlsx', index_col=0)

OfficeSupplies.to_html('C:/Users/saudagar/Desktop/OS.html', index=False, header = True)
                       
                       
