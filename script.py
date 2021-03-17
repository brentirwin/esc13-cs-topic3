# ESC13 - CS Topic 3
# Brent Irwin

# Get input integers
print("Enter one integer: ")
val1 = input()
print("Enter another integer: ")
val2 = input()

# Sort integers
if val1 > val2:
    tmp = val1
    val1 = val2
    val2 = tmp

# FIXME: Get random value between val1 and val2
val3 = "FIXME"

# Output
print("A random integer between %s and %s is %s."%(val1, val2, val3))
