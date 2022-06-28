
#Question Two
def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor = factor + 1 #Solution
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5

#Question 3:
def is_power_of_two(n):
    # Check if the number can be divided by two without a remainder
    while n % 2 == 0:
        if n <= 0: #Solution
            return False
        n = n / 2
    # If after dividing by two the number is 1, it's a power of two
    if n == 1:
        return True
    return False


print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False

#Question 4:
