# Exercise 7: Filter Foods
#
# Assign to a variable named foods_with_an_a the result of list comprehension that filters the foods tuple to only include food strings that contain the letter 'a'.
# For example, if foods is a tuple of ('Taco', 'Burrito', 'Sandwich'), foods_with_an_a would be a list equal to ['Taco', 'Sandwich']

def filter_foods_with_a():
    # your code here
    foods = ('hot dog', 'bacon', 'arrabbiata pasta')
    filter_foods_with_a = [food for food in foods if 'a' in food]
    return filter_foods_with_a

# Call the function and print the result
print('Exercise 7:', filter_foods_with_a())
