import numpy as np
import plotly.express as px
import csv

'''
#plot the data
with open("project_106(2).csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x = "Days Present", y = "Marks In Percentage")
    fig.show()
'''

#find the correlation between the data
def getDataScores(data_path):
    daysPresent = []
    marksinPercentage = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            daysPresent.append(float(row["Coffee in ml"]))
            marksinPercentage.append(float(row["sleep in hours"]))

    return {"x":daysPresent, "y":marksinPercentage}

def findCorr(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print(correlation[0, 1])

def setup():
    data_path = "project_106(2).csv"
    data_source = getDataScores(data_path)
    findCorr(data_source)

setup()