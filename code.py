def add_time(start, duration, day=None):
    # Days of the week
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Split and parse start time
    time_part, period = start.split()
    start_hour, start_minute = map(int, time_part.split(':'))

    # Convert start time to 24-hour format
    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    # Parse duration
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Total minutes
    total_minutes = start_minute + duration_minute
    extra_hour = total_minutes // 60
    final_minutes = total_minutes % 60

    # Total hours
    total_hours = start_hour + duration_hour + extra_hour
    days_later = total_hours // 24
    final_hour_24 = total_hours % 24

    # Convert back to 12-hour format
    if final_hour_24 == 0:
        final_hour = 12
        final_period = "AM"
    elif final_hour_24 < 12:
        final_hour = final_hour_24
        final_period = "AM"
    elif final_hour_24 == 12:
        final_hour = 12
        final_period = "PM"
    else:
        final_hour = final_hour_24 - 12
        final_period = "PM"

    # Format minutes with leading zero
    final_minutes_str = f"{final_minutes:02d}"

    # Calculate new day if provided
    if day:
        start_day_index = days_of_week.index(day.capitalize())
        new_day_index = (start_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        day_string = f", {new_day}"
    else:
        day_string = ""

    # Add day count message
    if days_later == 1:
        later_string = " (next day)"
    elif days_later > 1:
        later_string = f" ({days_later} days later)"
    else:
        later_string = ""

    # Build final result
    result = f"{final_hour}:{final_minutes_str} {final_period}{day_string}{later_string}"
    return result

print(add_time('3:30 PM', '2:12'))
# Returns: 5:42 PM

print(add_time('11:55 AM', '3:12'))
# Returns: 3:07 PM

print(add_time('2:59 AM', '24:00'))
# Returns: 2:59 AM (next day)

print(add_time('11:59 PM', '24:05'))
# Returns: 12:04 AM (2 days later)

print(add_time('8:16 PM', '466:02'))
# Returns: 6:18 AM (20 days later)

print(add_time('3:30 PM', '2:12', 'Monday'))
# Returns: 5:42 PM, Monday

print(add_time('2:59 AM', '24:00', 'saturDay'))
# Returns: 2:59 AM, Sunday (next day)

print(add_time('11:59 PM', '24:05', 'Wednesday'))
# Returns: 12:04 AM, Friday (2 days later)

print(add_time('8:16 PM', '466:02', 'tuesday'))
# Returns: 6:18 AM, Monday (20 days later)

print(add_time('3:00 PM', '0:00'))
# Returns: 3:00 PM
