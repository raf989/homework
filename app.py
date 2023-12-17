import copy

# Task 1
"""test_lst = [
    [1, 2, 3],
    [4, 5, 6],
    [None, 8, 9],
    [10, 11, 12],
    [13, None, 15],
    [16, 17, 18],
    [19, 20, 21],
    [22, 23, None],
]
lst = copy.deepcopy(test_lst)


def change(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == None:
                lst[i][j] = 0
    return lst


new_lst = change(lst)
print(test_lst)
print(new_lst)
"""
# Task 2

"""def replace_rain(text):
    return text.replace("дождь", "ДОЖДЬ")


with open("2.txt", "r", encoding='utf-8') as f:
    text = f.read()

with open("2_rain.txt", "w", encoding='utf-8') as f:
    f.write(replace_rain(text))

"""


# Task 3
"""def divide_to_stacks(product, sklad):
    lst = []
    product_per_sklad = product // sklad
    remainder = product % sklad

    for _ in range(remainder):
        lst.append(product_per_sklad + 1)

    for _ in range(sklad - remainder):
        lst.append(product_per_sklad)

    return lst

product = int(input())
sklad = int(input())
lst = divide_to_stacks(product, sklad)
print(*lst)"""