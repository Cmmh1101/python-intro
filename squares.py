# importing a single external function
import functions
from functions import square

for i in range(10):
    print(f'The Square of {i} is {square(i)}')

# importing a file and specifying the ones I want to use
for i in range(10):
    print(f'The Square of {i} is {function.square(i)}')
