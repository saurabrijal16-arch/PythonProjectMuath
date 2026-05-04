def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

my_list = [2, 5, 7, 1]
result = sum_list(my_list)
print("The sum is:", result)