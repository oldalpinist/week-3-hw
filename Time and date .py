import datetime
import time

now = datetime.datetime.now()
print(now.strftime("%m/%d/%Y" ' сегодня'))
dayago = datetime.timedelta(days=1)
y = now - dayago
print(y.strftime("%m/%d/%Y"' день назад'))
monthago = datetime.timedelta(days=31)
m = now - monthago
print(m.strftime("%m/%d/%Y" ' месяц назад'))

date_time_str = "01/01/25 12:10:03.234567"
date_time_obj = datetime.datetime.strptime(date_time_str, '%y/%m/%d %H:%M:%S.%f')

print('Дата и время:', date_time_obj)
#Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
#Превратите строку "01/01/25 12:10:03.234567" в объект datetime