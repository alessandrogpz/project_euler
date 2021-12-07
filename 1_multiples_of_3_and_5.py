# https://projecteuler.net/problem=1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_multiples_3_and_5(initial_value, final_value):

    total_sum = 0

    for current_number in range(initial_value, final_value):
        if current_number % 3 == 0 or current_number % 5 == 0:
            total_sum += current_number
    return total_sum

solution = sum_multiples_3_and_5(0,1000)
print(solution)