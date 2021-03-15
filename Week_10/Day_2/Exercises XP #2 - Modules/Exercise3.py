import datetime as dt

def display_amount(day,month,year):
    birthday = dt.datetime(year,month,day)
    current_date_time = dt.datetime.now()
    res = current_date_time - birthday
    res = res.days
    res = res*24*60*60
    print(f"You lived {res} mins in your whole life")



display_amount(31,7,1995)
