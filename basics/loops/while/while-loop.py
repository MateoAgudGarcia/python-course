list_numbers = list(range(2,40,3))
i = 0
while i < 10:
    print(list_numbers[i])
    i+=1

while True:
    if (input('Don\'t enter "this":\n')) == 'this':
        break