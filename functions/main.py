# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line


# 1.
def greet(name):
    return f'Hello, {name}!'


print(greet('Bob'))


# 2.

def add(n1, n2, n3):
    return n1 + n2 + n3


print(add(5, 3, 2))

# or

# def add(n1, n2, n3):
#     added = n1 + n2 +n3
#     return added

# print(add(5, 3, 2))


# 3.

def positive(number):
    if number > 0:
        return True
    else:
        return False


print(positive(50))
print(positive(-50))
print(positive(0))


# 4. Negative

def negative(number):
    if number < 0:
        return True
    else:
        return False


print(negative(50))
print(negative(-50))
print(negative(0))
