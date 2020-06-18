def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return x - (x % 5) + 5

# x = 43
# print(x % 5)
# print(x - (x % 5) + 5)

