# Given a real number n, find the square root of n.
# For example, given n = 9, return 3.

def square_root(real):
    for i in range(0, real):
        if i * i == real:
            return i
    return 0

print(square_root(16))
