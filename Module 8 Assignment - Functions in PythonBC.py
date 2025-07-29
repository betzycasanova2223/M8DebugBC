# Function to check if x is greater than y
def greater_than(x, y):
    if x > y:
        return True
    else:
        return False

# First test: a = 2, b = 3
a = 2
b = 3
result = greater_than(a, b)
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))

# Second test: a = 10, b = 6
a = 5
b = 1
result = greater_than(a, b)
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))
