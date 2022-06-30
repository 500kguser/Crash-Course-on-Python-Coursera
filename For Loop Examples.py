#Numbers are always one less than expected
for x in range(5):
    print(x)

#For Loops Intro
def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285