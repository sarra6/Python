# Countdown
def countdown(n):
    return list(range(n, -1, -1))

# Print and Return
def print_and_return(lst):
    print(lst[0])
    return lst[1]

# First Plus Length
def first_plus_length(lst):
    return lst[0] + len(lst)

# Values Greater than Second
def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    new_list = [value for value in lst if value > lst[1]]
    print(len(new_list))
    return new_list

# This Length, That Value
def length_and_value(size, value):
    return [value] * size

# Example usages
print(countdown(5))  # [5, 4, 3, 2, 1, 0]
print(print_and_return([1, 2]))  # Prints 1 and returns 2
print(first_plus_length([1, 2, 3, 4, 5]))  # 6
print(values_greater_than_second([5, 2, 3, 2, 1, 4]))  # Prints 3 and returns [5, 3, 4]
print(values_greater_than_second([3]))  # False
print(length_and_value(4, 7))  # [7, 7, 7, 7]
print(length_and_value(6, 2))  # [2, 2, 2, 2, 2, 2]
