# Very simple perf-o-meter
def perfometer_check_mk_as400_users(row, check_command, perf_data):
    left = float(perf_data[0][1])
    warn = float(perf_data[0][3])
    crit = float(perf_data[0][4])

    red    = "#ff0000"
    yellow = "#ffff00"
    green  = "#00ff00"

    if left >= crit:
        color = red

    elif left >= warn:
        color = yellow

    else:
        color = green

    return "%d" % left, perfometer_linear(left, color)

perfometers["check_mk-snmp_as400_users"] = perfometer_check_mk_as400_users

