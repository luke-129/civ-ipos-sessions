

# Exercise 1: manually create a 2D data structure
#        elem    0  1  2      row
twoDimensional = [
    [ 1,2,3],
    [4,5,6],
    [7,8,9]
]
print(twoDimensional[0])
print(twoDimensional[0][0])

# Exercise 2:
# sequential iteration over 2D

for item in twoDimensional:
    print(item)

# Exercise 3:
# Dynamically build a 2D data structure and initialise with values
def make_2d(a,b):
    structure = []
    for i in range(a,b):
        structure.append(i)
    return structure




# Exercise 3a:
# Refactor to list comprehension
def make_2d_cool(a,b):
    '''Same function as above implemented as a list comprehension
    '''
    # Example 1
    structure = [i for i in range(a,b)]
    return structure
    # Example 2 - add watch statements

    # Example 3

    # Example 4



print('#'*50)
print(make_2d_cool(3, 3))
print('#'*50)
print(make_2d(3, 3))
print(make_2d(3, 3))


# Numpy & Pandas examples - view in Pycharm
