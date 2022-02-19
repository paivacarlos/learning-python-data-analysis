import datetime
nows = datetime.datetime.now()
print(nows)

#construindo a minha data
myDate = datetime.time(15, 18, 22)
print(myDate)
print("hour: ", myDate.hour)
print("minute: ", myDate.minute)
print("second: ", myDate.second)

#trabalhando mais com o datatime
today = datetime.date.today()
print(today)
print("ctime:", today.ctime())
print("year:", today.year)
print("month:", today.month)
print("day:", today.day)

#orquestrando datas
d1 = today
d2 = d1.replace(year=2025)
print(d2)

#difernça entre datas
print(d2 - d1)

print(datetime.timedelta(366))