if maxTempData == {}:
        print("data not found")
    else:
        print(maxTempData["results"])
        dates = (maxTempData["results"])
        for day in dates:
            celsius_tenth = (day['value'])
            farenheit = ( celsius_tenth / 10 ) * ( 9 / 5 ) + 32
            print(farenheit)
            if day['value'] == 69:
                celsius_tenth = (day['value'])
                farenheit = ( celsius_tenth / 10 ) * ( 9 / 5) + 32
                print(farenheit)

    if minTempData == {}:
        print("data not found")
    else:
        print(minTempData["results"])
        dates = (minTempData["results"])
        for day in dates:
            celsius_tenth = (day['value'])
            farenheit = ( celsius_tenth / 10 ) * ( 9 / 5 ) + 32
            print(farenheit)
            if day['value'] == 69:
                celsius_tenth = (day['value'])
                farenheit = ( celsius_tenth / 10 ) * ( 9 / 5) + 32
                print(farenheit)

    if snowData == {}:
        print("data not found")
    else:
        print(snowData["results"])
        dates = (snowData["results"])
        for day in dates:
            millimeters = (day['value'])
            inches = ( millimeters / 10 ) / 2.54
            print(inches)
            if day['value'] > 0:
                print('snowed!')