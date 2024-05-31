from time import sleep
from requests import get
from plyer import notification
from datetime import date

while True:
    try:
        country = str(input('Type the name of the country: '))
        covidData = get(f"https://corona-rest-api.herokuapp.com/Api/{country}")
        if "error" in covidData:
            raise ValueError
        else:
            break
    except:
        print("ERROR! Invalid country, try again.")

data = covidData.json()["Success"]

while True:
    notification.notify(
        title = f"Covid-19 Stats on {date.today()}",
        message = f"Total cases: {data['cases']}\nTotal deaths: {data['deaths']}\nRecovered: {data['recovered']}",
        timeout = 50
    )

    sleep(30)