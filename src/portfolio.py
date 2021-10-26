from app import df

from getChartData import getChartData


def generateResponse():
    resp = getChartData(df)
    return resp
