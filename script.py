# ESC13 - CS Topic 3
# Brent Irwin

import random

# Get input integers
print("Enter one integer: ")
val1 = int(input())
print("Enter another integer: ")
val2 = int(input())

# Sort integers
if val1 > val2:
    tmp = val1
    val1 = val2
    val2 = tmp

# Get random value between val1 and val2
val3 = random.randint(val1, val2)

# Output
print("A random integer between %s and %s is %s."%(val1, val2, val3))
