#! /usr/bin/env python
# # 221
# def print_reverse(s):
#     print(s[::-1])


# print_reverse("python")

# # 222
# def print_score(score_list):
#     print(sum(score_list) / len(score_list))


# print_score([1, 2, 3])

# # 223


# def print_even(even_list):
#     for i in even_list:
#         if i % 2 == 0:
#             print(i)


# print_even([1, 2, 3, 10, 11, 12, 17, 16])

# # 224


# def print_keys(my_dict):
#     for i in my_dict.keys():
#         print(i)


# print_keys({"이름": "김말똥", "나이": 30, "성별": 0})

# # 225
# my_dict = {"10/26": [100, 130, 100, 100], "10/27": [10, 12, 10, 11]}


# def print_value_by_key(dic, a):
#     print(dic[a])


# print_value_by_key(my_dict, "10/26")

# TODO 226
def print_5xn(a):
    s = int(len(a) / 5)
    for i in range(s + 1):
        print(a[i * 5 : i * 5 + 5])


print_5xn("아이엠어보이유알어걸")

# 227


def print_mxn(a, i):
    s = int(len(a) / i)
    for x in range(s + 1):
        print(a[x * i : x * i + i])


print_mxn("아이엠어보이유알어걸", 3)

# 228


def calc_salary(a):
    i = a / 12
    print(int(i))


calc_salary(12000000)

