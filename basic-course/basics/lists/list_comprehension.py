temps = [234,543,789]

temps_dev = [temp/10 for temp in temps if temp > 300]
temps_dev_else = [temp/10 if temp > 300 else 0 for temp in temps]

print(temps_dev,temps_dev_else)
