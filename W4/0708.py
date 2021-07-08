#! /usr/bin/env python
# # 1.1

# print("This is sequence file")

# # 1.2

# a = input("Enter a string: ")
# print(a)
# # 1.3
# a = int(input("Enter an integer: "))
# b = int(input("Enter another: "))
# print("Sum: ", a + b)

# # 1.4
# a = int(input("Enter an integer: "))
# b = int(input("Enter another: "))
# if a > b:
#     print(f"{a} is greater than {b}")
# elif a == b:
#     print(f"{a} is equal to {b}")
# else:
#     print(f"{a} is less than {b}")

# 2.1
# a = int(input("Which times table: "))
# i = 1
# if a > 9:
#     print("What?")
# else:
#     for i in range(1, 10):
#         print(f"{a}*{i} = ", a * i)

# # 2.2
# a = input("Enter a string: ")

# print("The string length is", len(a))

# # 2.3
# a = input("Enter a string: ")
# i = int(input("How many times to reapeat: "))

# print(a * i, end="")

# 2.4
# a = input("Enter a string: ")
# b = input("Enter another: ")

# if a == b:
#     print("The two strings are identical")
# else:
#     print(f"{a}{b}")

# 2.5
# s1 = input("Enter s1: ")
# s2 = input("Enter s2: ")

# if len(s1) % 2 == 1 and len(s1) < len(s2):
#     print(f"{s1}{s2}")
# else:
#     print(f"{s2}{s1}")

# 2.6
# a = input("Enter a string: ")
# b = a[::-1]
# print(b)

# 2.7
d_codon = dict()
i_codon = ""
# input("Enter three-base codon to build: ")
i_acid = ""
# input("Enter amino acid: ")
s_codon = ""
d_codon[i_codon] = i_acid

while i_codon != "XXX":
    d_codon[i_codon] = i_acid
    i_codon = input("Enter three-base codon to build: ")
    if i_codon == "XXX":
        print("Okay, I will switch.")
        break
    else:
        i_acid = input("Enter amino acid: ")
        d_codon[i_codon] = i_acid
while s_codon != "XXX":
    s_codon = input("Enter three-base codon to search: ")
    if s_codon == "XXX":
        print("Okay I will stop")
        break
    else:
        print(f"The amino acid for {s_codon} is", d_codon[s_codon])

# 2.7 answer
# codon_dic = dict()
# while True:
#         codon = input('Enter three-base codon to build')
#         codon = codon.upper()
#         if codon =='XXX':
#             print('Okay I will switch.')
#             break
#         aa = input('Enter amino acid: ')
#         aa = aa.upper()
#         codon_dic[codon]=aa

# while True:
#     codon = input ('Enter three-base codon to search: ')
#     codon = codon.upper()
#     if codon =='XXX':
#         print('Okay I will stop.')
#         break
#     if codon in codon_dic:
#         aa=codon_dic[codon]
#         print(f'Amino aicd for {codon} is {aa}')
#     else:
#         break
