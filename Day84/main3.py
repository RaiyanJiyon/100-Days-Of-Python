#time.strftime()

'''The time.strftime() function formats a time value as a string, based on a specified format. This function is particularly useful for formatting dates and times in a human-readable format, such as for display in a GUI, a log file, or a report. Here's an example:'''

import time

t = time.localtime()
formated_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formated_time)

'''As you can see, the function time.strftime() formats the current time (obtained using time.localtime()) as a string, using a specified format. The format string contains codes that represent different parts of the time value, such as the year, the month, the day, the hour, the minute, and the second.'''
