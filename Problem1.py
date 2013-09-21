
import numpy as np

# Find upper bounds for powers of 3 and 5
three_max = 1000/3
five_max = 1000/5

summ = 0

three_mults = [3*i for i in range(1,three_max+1)]
five_mults = [5*i for i in range(1,five_max+1)]

print sum(three_mults) + sum(five_mults)






