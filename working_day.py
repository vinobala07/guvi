working_day = ('Monday','Tuesday','Wednesday','Thursday','Friday')
leave_day = ('Saturday','Sunday')
day = raw_input().title()
if day in working_day:
    print True
elif day in leave_day:
    print False
else:
    print 'Not Valid Day'

