import datetime

print(datetime.date.today())

#this will print the diffent between today and specified date bellow
now= datetime.datetime.today()
other= datetime.datetime(1993,4,5,17,54)
print(now-other)


then = datetime.datetime(1918,6,16,16,36)
now= datetime.datetime(2018,6,16,16,30)
print(now-then)


