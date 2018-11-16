import os
import pandas as pd

path = os.getcwd()
fN = (path + './data/fn.txt')
cleveland = (path + "./data/c.csv")
switzerland = (path + "./data/s.csv")
hungarian = (path + "./data/h.csv")
va = (path + "./data/lb.csv")
m_Data = (path + "./data/Merged_Data.csv")

headers = pd.read_csv(fN, sep='\n', header=None)



cleveland_df = pd.read_csv(cleveland, sep=',', names = headers.values.T.tolist()[0] , na_values =["?"])
switzerland_df = pd.read_csv(switzerland, sep=',', names = headers.values.T.tolist()[0] , na_values =["?"])
va_df = pd.read_csv(va, sep=',',  names = headers.values.T.tolist()[0] , na_values =["?"])
hungarian_df = pd.read_csv(hungarian, sep=',',  names = headers.values.T.tolist()[0] , na_values =["?"])

# append the four files into a single dataframe
temp = cleveland_df.append(switzerland_df).append(va_df).append(hungarian_df)
print(temp.head())
print()
print(temp.info())
print()


# Save the merged data as a csv
temp.to_csv(m_Data)
print('The heart disease data has been merged')









