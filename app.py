from crypt import methods
from flask import Flask, render_template, url_for, request
app = Flask(__name__)
import requests
import json
import numpy as np

Token = #input Token/environment variable
station_id = 'GHCND:USW00014734'
station_id_2 = 'GHCND:USW00023129'

def getMinTemp(selectedDate, selectedNumber, selectedOperator):
    for year in range(2020, 1970, -1):
        year = str(year)
        print('working on year '+year)

        minTempDataReq = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=TMIN&limit=1000&stationid='+station_id+'&startdate='+year+'-01-01&enddate='+year+'-12-31', headers={'token':Token})
        minTempData = json.loads(minTempDataReq.text)

        if minTempData == {}:
            print("data not found")
        elif selectedOperator == "<=":
            testDay = selectedDate + 'T'
            testTemp = float(selectedNumber)
            dates = (minTempData["results"])
            for day in dates:
                yearAndDay = day['date']
                if yearAndDay[5:11] == testDay and ((day['value'] / 10 ) * ( 9 / 5 ) + 32) <= testTemp:
                    return yearAndDay[0:4]
        else:
            testDay = selectedDate + 'T'
            testTemp = float(selectedNumber)
            dates = (minTempData["results"])
            for day in dates:
                yearAndDay = day['date']
                if yearAndDay[5:11] == testDay and ((day['value'] / 10 ) * ( 9 / 5 ) + 32) >= testTemp:
                    return yearAndDay[0:4]

def getMaxTemp(selectedDate, selectedNumber, selectedOperator):
    for year in range(2020, 1970, -1):
        year = str(year)
        print('working on year '+year)

        maxTempDataReq = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=TMAX&limit=1000&stationid='+station_id+'&startdate='+year+'-01-01&enddate='+year+'-12-31', headers={'token':Token})
        maxTempData = json.loads(maxTempDataReq.text)

        if maxTempData == {}:
            print("data not found")
        elif selectedOperator == "<=":
            testDay = selectedDate + 'T'
            testTemp = float(selectedNumber)
            dates = (maxTempData["results"])
            for day in dates:
                yearAndDay = day['date']
                if yearAndDay[5:11] == testDay and ((day['value'] / 10 ) * ( 9 / 5 ) + 32) <= testTemp:
                    print(yearAndDay)
                    return yearAndDay[0:4]
        else:
            testDay = selectedDate + 'T'
            testTemp = float(selectedNumber)
            dates = (maxTempData["results"])
            for day in dates:
                yearAndDay = day['date']
                if yearAndDay[5:11] == testDay and ((day['value'] / 10 ) * ( 9 / 5 ) + 32) >= testTemp:
                    print(yearAndDay)
                    return yearAndDay[0:4]

def getSnowData(selectedDate, selectedNumber, selectedOperator):
    for year in range(2020, 1970, -1):
        year = str(year)
        print('working on year'+year)

        snowDataReq = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=SNOW&limit=1000&stationid='+station_id+'&startdate='+year+'-01-01&enddate='+year+'-12-31', headers={'token':Token})
        snowData = json.loads(snowDataReq.text)

        if snowData == {}:
            print("data not found")
        elif selectedOperator == "<=":
            testDay = selectedDate + 'T'
            testTemp = float(selectedNumber)
            dates = (snowData["results"])
            for day in dates:
                yearAndDay = day['date']
                if yearAndDay[5:11] == testDay and ((day['value'] / 10) / 2.54) <= testTemp:
                    return yearAndDay[0:4]
        else:
            testDay = selectedDate + 'T'
            testTemp = float(selectedNumber)
            dates = (snowData["results"])
            for day in dates:
                yearAndDay = day['date']
                if yearAndDay[5:11] == testDay and ((day['value'] / 10) / 2.54) >= testTemp:
                    return yearAndDay[0:4]


@app.route('/', methods=["GET","POST"])
def index():
    if request.form.get("user_number") != None:
        selectedDate = ""
        selectedField = request.form.get("field")
        selectedOperator = request.form.get("operator")
        selectedNumber = request.form.get("user_number")
        selectedLocation = request.form.get("location")
        selectedParty = request.form.get("party")
        selectedParty = selectedParty[5:10]
        selectedDate = selectedParty

        print(selectedDate)
        print(selectedField)
        print(selectedOperator)
        print(selectedNumber)
        print(selectedLocation)
        print(selectedParty)


        if selectedLocation == "Newark Liberty":
            global station_id 
            station_id = 'GHCND:USW00014734'
        elif selectedLocation == "Long Beach":
            station_id = 'GHCND:USW00023129'
        elif selectedLocation == "Dallas":
            station_id = 'GHCND:USW00013960'
        elif selectedLocation == "Philadelphia":
            station_id = 'GHCND:USW00013739'
        elif selectedLocation == "Miami Beach":
            station_id = 'GHCND:USW00092811'
        else:
            station_id = 'GHCND:USW00014734'

        if selectedField == "snow":
            x = (getSnowData(selectedDate, selectedNumber, selectedOperator))
            message = "The last year where " + selectedDate + " in " + selectedLocation + " had snowfall that was " + selectedOperator + " " + selectedNumber + " was " + x
            return render_template('index.html', year=message) 
        elif selectedField == "maxTemp":
            x = (getMaxTemp(selectedDate, selectedNumber, selectedOperator))
            message = "The last year where " + selectedDate + " in " + selectedLocation + " had a daily maximum temperature that was " + selectedOperator + " " + selectedNumber + " was " + x
            return render_template('index.html', year=message)
        else:
            x = (getMinTemp(selectedDate, selectedNumber, selectedOperator))
            message = "The last year where " + selectedDate + " in " + selectedLocation + " had a daily minimum temperature that was " + selectedOperator + " " + selectedNumber + " was " + x
            return render_template('index.html', year=message) 
    else:
        return render_template('index.html', year="")

if __name__ == "__main__":
    app.run(debug=True)
