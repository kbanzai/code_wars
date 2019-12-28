# https://www.codewars.com/kata/52742f58faf5485cae000b9a

def format_duration(seconds):
    if not seconds: return "now"
    minute = 60
    hour = 60 * minute
    day = 24 * hour
    year = 365 * day
    units = [(year, "year"), (day, "day"), (hour, "hour"), (minute, "minute"), (1, "second")]
    durations = []
    for unit in units:
        t_unit, seconds = divmod(seconds, unit[0])
        if t_unit == 1:
            durations.append("%s %s" % (t_unit, unit[1]))
        elif t_unit > 1:
            durations.append("%s %ss" % (t_unit, unit[1]))
    comma = ", " if len(durations) > 2 else ""
    return ", ".join(durations[:-2]) + comma + " and ".join(durations[-2:])