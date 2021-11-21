from itertools import count
from numpy.core.fromnumeric import mean
import  pandas as pd
import plotly.figure_factory as ff
import csv
import statistics
import random

df=pd.read_csv("sample.csv")
data=df["temp"].tolist()

def randomSetOfMean(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataSet.append(value)
    mean2=statistics.mean(dataSet)
    return mean
def showFig(meanList):
    df=meanList
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()
def setup():
    meanlist=[]
    for i in range(0,1000):
        setOfmeans=randomSetOfMean(100)
        meanlist.append(setOfmeans)
    showFig(meanlist)
setup()