#pip install pandas
#pip install pandas-profiling

from asyncore import read
import profile
import pandas as pd
from pandas_profiling import ProfileReport

df= pd.read_csv('loan_train.csv') # input your csv name here
print(df)

#To generate a report
profile= ProfileReport(df)
profile.to_file(output_file="loan.html")