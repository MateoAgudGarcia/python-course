
with open('../list-int-str.txt') as file:
    list_values = file.readlines()
    ints = []
    strs = []
    for value in list_values:
        value_proc = value.replace('\n','')
        if value_proc[0] in str(list(range(10))):
            ints.append(int(value_proc))
        else:
            strs.append(value_proc)
    print(ints,strs)