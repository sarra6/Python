# 1
def number_of_food_groups():
    return 5

print(number_of_food_groups())

# 2
def number_of_military_branches():
    return 5

print(number_of_military_branches())

# 3
def number_of_books_on_hold():
    return 5

print(number_of_books_on_hold())

# 4
def number_of_fingers():
    return 5

print(number_of_fingers())

# 5
def number_of_great_lakes():
    return 5

x = number_of_great_lakes()
print(x)

# 6
def add(b, c):
    return b + c

result = add(1, 2) + add(2, 3)
print(result)

# 7
def concatenate(b, c):
    return str(b) + str(c)

print(concatenate(2, 5))

# 8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10

print(number_of_oceans_or_fingers_or_continents())

# 9
def number_of_days_in_a_week_silicon_or_triangle_sides(b, c):
    if b < c:
        return 7
    else:
        return 14

result1 = number_of_days_in_a_week_silicon_or_triangle_sides(2, 3)
result2 = number_of_days_in_a_week_silicon_or_triangle_sides(5, 3)
result3 = result1 + result2
print(result1)
print(result2)
print(result3)

# 10
def addition(b, c):
    return b + c

result = addition(3, 5)
print(result)

# 11
b = 500
print(b)

def foobar():
    b = 300
    print(b)

print(b)
foobar()
print(b)

# 12
b = 500
print(b)

def foobar():
    b = 300
    print(b)
    return b

print(b)
foobar()
print(b)

# 13
b = 500
print(b)

def foobar():
    b = 300
    print(b)
    return b

print(b)
b = foobar()
print(b)

# 14
def foo():
    print(1)
    bar()
    print(2)

def bar():
    print(3)

foo()
