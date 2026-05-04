def remove_odd_numbers(numbers):
    new_list = []
    for number in numbers:
        if number % 2 == 0:
            new_list.append(number)
    return new_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
cut_down_list = remove_odd_numbers(my_list)

print("Original list:", my_list)
print("Cut-down list:", cut_down_list)