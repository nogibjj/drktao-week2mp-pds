import pandas as pd
import seaborn as sns
import statistics

def denirostats(file):
    df=pd.read_csv(file)
    sumstats=pd.DataFrame({'Mean Score':df.iloc[:,1].mean(),
                           'Median Score':df.iloc[:,1].median(),
                           'Standard Deviation of Scores':statistics.stdev(df.iloc[:,1])},
                           index=[0])
    return sumstats

result=denirostats('deniro.csv')
print(result)