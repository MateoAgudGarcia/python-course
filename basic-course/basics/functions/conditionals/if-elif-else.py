def temperature(value):
    if value > 25:
        return 'Hot'
    elif value <= 25 and value >= 15:
        return 'Warm'
    else:
        return 'Cold'

print(temperature(33))
print(temperature(22))
print(temperature(11))
