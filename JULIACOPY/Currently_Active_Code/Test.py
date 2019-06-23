import sys

print(sys.getsizeof(True))
print("\n")
print(sys.getsizeof(1))
print(sys.getsizeof(0))
x = 0
print(sys.getsizeof(x))
y = False
z = True
a = 0
print(sys.getsizeof(y))
print(sys.getsizeof(z))
print(sys.getsizeof(a))
b = 55
print(sys.getsizeof(b))
# Learned: 0 and True are 28 bytes in Python
# Literally any other value in Boolean or integer is 24 bytes