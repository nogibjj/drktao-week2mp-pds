import pandas as pd
import matplotlib.pyplot as plt
import statistics

def denirostats(file):
    df=pd.read_csv(file)
    sumstats=pd.DataFrame({'Mean Score':round(df.iloc[:,1].mean(),2),
                           'Median Score':round(df.iloc[:,1].median(),2),
                           'Standard Deviation of Scores':round(statistics.stdev(df.iloc[:,1]),2)},
                           index=[0])
    return sumstats

def denirohist(file):
    df=pd.read_csv(file)
    plt.hist(df.iloc[:,1])
    plt.show()

result=denirostats('deniro.csv')
print(result)
denirohist('deniro.csv')