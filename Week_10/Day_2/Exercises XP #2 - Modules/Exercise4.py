import datetime as dt

def display_amount(day,month,year):
    current_date_time = dt.datetime.now()
    holiday = dt.datetime(year,month,day)
    
    result = holiday - current_date_time
    res = str(result)
    r = res.replace(", "," and ")
    print(r)
    print(f"Todays date is {current_date_time}\nThe next holiday is in {r} hours")



display_amount(15,5,2021)
