def temperature(value):
    if value > 25:
        return 'Hot'
    elif value <= 25 and value >= 15:
        return 'Warm'
    else:
        return 'Cold'
weather = temperature(int(input('Enter degrees to define a weather: ')))
print('Your weather is %s' % weather)
print(f'Your weather is {weather}')
