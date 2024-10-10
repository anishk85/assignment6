
import math

def trig_function(angle):
    def nested_function(x):
        return math.sin(x + angle)
    return nested_function

# Create cos(x) function
cos = trig_function(math.pi/2)

# Create sin(x) function
sin = trig_function(math.pi)

# Test the functions
print(f"cos(0) = {cos(0):.6f}")
print(f"cos(pi/2) = {cos(math.pi/2):.6f}")
print(f"sin(0) = {sin(0):.6f}")
print(f"sin(pi/2) = {sin(math.pi/2):.6f}")