def clockhands_angle(hour):
    """
    a function for solving the clock hands angle riddle from job interviews: "Wht is the angle between the clock hands
    at 2:10?" (any given hour in this function)
    :param hour:
    :type hour: str
    :return angle: the angle between the clockhands in the given hour
    :rtype angle: float
    """

    minute_angle = 360/60  # =6
    five_min_angle = minute_angle * 5  # =30

    hours = int(hour[:2])  # hours from 0 to 12 only, not a minute after 12!
    mins = int(hour[3:])

    in_hour = five_min_angle / 60 * mins  # = 0.5 * mins
    if hours == 12:
        in_hour = 0

    answer = abs((five_min_angle * hours + in_hour) - (minute_angle * mins))

    # print(answer)  #  if angles beyond 180 are fine

    if answer < 180:
        print(answer)
    else:
        print(360 - answer)


clockhands_angle("02:10")  # from 00:00 to 12:00 only
