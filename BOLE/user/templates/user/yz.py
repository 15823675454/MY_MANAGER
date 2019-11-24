from random import *


def verification():
    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    str_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    rand_verification = []
    for i in range(4):
        print(i)
        a = [str_list, num_list]
        unit = choice(a)
        val1 = unit[randint(0, len(unit)-1)]
        rand_verification.append(val1)
    return rand_verification

a = verification()
print()


# num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# str_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#                 'u', 'v', 'w', 'x', 'y', 'z']
#
# a = [str_list, num_list]
# unit = choice(a)
# print(unit[randint(0, len(unit)-1)], type(unit))

