list_values = open('list-int-str.txt')

def divide_variables(values):
    ints = []
    strs = []
    for value in values:
        value_proc = value.replace('\n','')
        if value_proc[0] in str(list(range(10))):
            ints.append(int(value_proc))
        else:
            strs.append(value_proc)

    return ints,strs

print(divide_variables(list_values.readlines()))
list_values.close()
