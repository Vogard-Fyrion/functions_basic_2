# countdown

def countdown(x):
    arr = []
    while x >= 0:
        arr.append(x)
        x -= 1
    return arr
print(countdown(5))
print(countdown(10))
print(countdown(15))

# print and return

def print_and_return(x,y):
    print(x)
    return y

print(print_and_return(1,2))
print(print_and_return(5,10))

# first plus length

def first_plus_length(ls):
    return ls[0] + len(ls)

print(first_plus_length([1,2,3,4,5]))
print(first_plus_length([1,2,3,4,5,6,7,8,9,10]))

# values greater than second

def values_greater_than_second(ls):
    new_ls = []
    if len(ls) == 1:
        return "false"
    else:
        for x in range(0, len(ls)):
            if ls[x] > ls[1]:
                new_ls.append(ls[x])
    print(len(new_ls))
    return new_ls

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))
print(values_greater_than_second([6,4,2,1,8,9,3,10,11,4]))

# this length, that value

def length_and_value(a,b):
    ls = []
    for x in range(0, a):
        ls.append(b)
    return ls

print(length_and_value(4,7))
print(length_and_value(6,2))