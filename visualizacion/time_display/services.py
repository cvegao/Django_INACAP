import requests
import substring as substring


def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()


def get_datetime(params={}):
    response = generate_request("http://worldtimeapi.org/api/timezone/America/Santiago", params=params)

    day = ""
    month = ""
    year = ""
    hours = ""
    minutes = ""
    seconds = ""
    p = ""
    timezone = ""

    if response:
        datetime = response.get("datetime")
        year = datetime[0:4]
        month = datetime[5:7]
        day = datetime[8:10]
        hours = datetime[11:13]
        minutes = datetime[14:16]
        seconds = datetime[17:19]
        timezone = response.get("timezone")

        if int(hours) < 12:
            p = "AM"
        elif int(hours) == 12:
            p = "PM"
        else:
            p = "PM"
            hours = str(int(hours) - 12)

    return '{}/{}/{} {}:{}:{} {} \n {}'.format(day, month, year, hours, minutes, seconds, p, timezone)
