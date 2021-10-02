from datetime import date
today = date.today()

def bthdycal(b_year,b_month,b_date,name):
    age = today.year - int(b_year)
    if (today.month == int(b_month) and today.day == int(b_date)):
        print(f"Happy Birthday {name}")
        print(f"its your {age} birthday")
    else:
        print(f"the coming birthday will be your {age + 1} birthday")


bthdycal(2003,6,5,"Vinaya")
