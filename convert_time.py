# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# Example


# Return '12:01:00'.


# Return '00:01:00'.


time_to_convert = '12:00:00AM'
print(time_to_convert[:-2])
print(time_to_convert[-2:])
print(time_to_convert.split(":"))

# hour, min, sec = map(int, time_to_convert[:-2].split(":"))
# print(hour)


def convert_to_military_time(time):
    hour, minn, sec = map(int, time[:-2].split(":"))
    if time[-2:] == "PM" and hour != 12:
        hour += 12
    if time[-2:] == "AM" and hour == 12:
        hour = 0
    return f"{hour:02d}:{minn:02d}:{sec:02d}"
