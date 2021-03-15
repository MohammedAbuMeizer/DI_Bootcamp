import datetime as dt

def display_amount():
    current_date_time = dt.datetime.now()
    future_date_time = dt.datetime(int(current_date_time.year+1),1,1)
    re = future_date_time - current_date_time
    print(f"the 1st January is in {re.date} hours ")

display_amount()
