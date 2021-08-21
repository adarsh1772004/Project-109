import statistics
import random
import plotly.figure_factory as pf
import pandas as pd
import csv
df=pd.read_csv("StudentsPerformance.csv")
marks=df["math score"].tolist()
##graph=pf.create_distplot([dice],["reasult"],show_hist=False)
##graph.show()
mean=sum(marks)/len(marks)
median=statistics.median(marks)
mode=statistics.mode(marks)
stdv=statistics.stdev(marks)
fstd_start=mean-stdv
fstd_end=mean+stdv
fstd=[]
for d in marks:
    if(d>fstd_start and d<fstd_end):
        fstd.append(d)
p=len(fstd)*100/len(marks)
print (p)