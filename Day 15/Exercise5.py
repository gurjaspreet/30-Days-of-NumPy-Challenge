import numpy as np


with open('stocks.txt', 'r') as file:
    text = file.read()
    
lines = text.split('\n')
lines = [line.split('\t') for line in lines]

result = np.array(lines)
    
print(result)