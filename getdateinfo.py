import datetime
year=int(datetime.date.today().strftime('%Y'))
daysintoyear=int(datetime.date.today().strftime('%j'))

if year % 4:
    dl = 366 - daysintoyear
else:
    dl = 365 - daysintoyear
    
date=datetime.date.today().strftime(f'%m/%d/%Y Days into year: %j Days left in year: {dl}')
print(date)
