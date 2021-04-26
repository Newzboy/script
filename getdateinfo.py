#Get Current Date
import datetime
leapyears=[2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096]
year=int(datetime.date.today().strftime('%Y'))
daysintoyear=int(datetime.date.today().strftime('%j'))

if year in leapyears:
    dl = 366 - daysintoyear
else:
    dl = 365 - daysintoyear
    
date=datetime.date.today().strftime(f'Current date: %m/%d/%Y|Days into year: {daysintoyear}|Days left in year: {dl}')
print(date)
