# 1. TASK: print "Hello World"
Test = "Hello World"
print(type(Test))
# 2. print "Hello Noelle!" with the name in a variable
Greeting = "Hello"
name = "Noelle"
print(Greeting, name)  # with a comma
print(Greeting + name)  # with a +

# 3. print "Hello 42!" with the number in a variable
name = 42
print(Greeting, name)  # with a comma
# The next line should give an error because you can't concatenate a string and an integer without converting the integer to a string.
# print(Greeting + name)

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2))  # with .format()
print(f"I love to eat {fave_food2} and {fave_food1}.")  # with an f-string
