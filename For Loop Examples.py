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

#Sums, Averages
values=[ 14, 41, 56, 69, 74 ]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print ("Total Sum: " + str(sum) + " - Average: " + str(sum/length))