from datetime import datetime
time1 = raw_input()
time2 = raw_input()
frmt = '%H:%M:%S'
print datetime.strptime(time2,frmt) - datetime.strptime(time1,frmt)
