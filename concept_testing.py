from datetime import date, datetime

today = date.today()
tommorow = datetime.strptime("2022-11-20", '%Y-%m-%d').date()
diff = tommorow - today
print(type(diff.days))
