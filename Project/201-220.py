#! /usr/bin/env python
# # 201
# def print_coin():
#     print("비트코인")


# # 202
# print_coin()

# # 203
# for r in range(1, 100):
#     print_coin()

# # 204
# def print_coins():
#     for i in range(1, 100):
#         print("비트코인")

# 215
def print_with_smile(a):
    print(a + ":D")


# 216
print_with_smile("안녕하세요")

# 217
def print_upper_price(i):
    print(i * 1.3)


# 218
def print_sum(a, b):
    print(a + b)


# 219
def print_arithmetic_operation(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)


# 220
def print_max(a, b, c):
    if a > b > c or a > c > b:
        print(a)
    elif b > c > a or b > a > c:
        print(b)
    else:
        print(c)


print_max(1, 200, 3)

