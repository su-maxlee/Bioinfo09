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
# d_codon = dict()
# i_codon = ""
# # input("Enter three-base codon to build: ")
# i_acid = ""
# # input("Enter amino acid: ")
# s_codon = ""
# d_codon[i_codon] = i_acid

# while i_codon != "XXX":
#     d_codon[i_codon] = i_acid
#     i_codon = input("Enter three-base codon to build: ")
#     if i_codon == "XXX":
#         print("Okay, I will switch.")
#         break
#     else:
#         i_acid = input("Enter amino acid: ")
#         d_codon[i_codon] = i_acid
# while s_codon != "XXX":
#     s_codon = input("Enter three-base codon to search: ")
#     if s_codon == "XXX":
#         print("Okay I will stop")
#         break
#     else:
#         print(f"The amino acid for {s_codon} is", d_codon[s_codon])

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

# 3.1
# a = open("title.txt", "a")
# a.write("This is a sequence file")
# a.close

# 3.2
# with open("title.txt", "r") as handle:
#     print(handle.readlines(1))

# 3.2 answer
# fr=open('title.txt')
# for line in fr:
#     line.strip()
#     break
# fr.close()
# print(fr.readline())

# 3.3
# with open("sequence.fasta") as handle:
#     for lines in handle:
#         print(lines.strip())

# 3.4
# handle = open("sequence.fasta")
# handle2 = open("sequence2.fasta", "w")
# l = handle.readlines()
# i = 0
# while i < len(l[:]):
#     handle2.write(l[i])
#     i += 1
# handle.close
# handle2.close

# # 3.5
# with open("sequence.fasta") as handle:
#     l = handle.readlines()
#     print(l[1])

# 3.6
# seq = []
# with open("sequence2.fasta") as handle:
#     for lines in handle:
#         line = lines.strip()
#         if line.startswith(">"):
#             title = line
#         else:
#             seq =

# print("title:", title)
# print("seq:", seq)

# 3.6 answer
# fr = open("sequence2.fasta")
# lines = fr.readlines()
# title = ""
# seq_list = list()
# for line in lines:
#     line = line.strip()
#     if line == "":
#         continue
#     if line[0] != ">":
#         seq_list.append(line)
#     else:
#         title = line
# fr.close()
# seq = "".join(seq_list)
# print("title: ", title)
# print("seq: ", seq)

# 3.7
# while True:
#     i = input("Position: ")
#     if i == "XXX":
#         print("Okay I will stop.")
#         break
#     else:
#         a = int(i)
#     print(f"Three amino acids: ", seq[a : a + 3])

# find = list()
# c = 0
# while True:
#     b = input("Searching for: ")
#     if b == "XXX":
#         print("Okay I will stop")
#         break
#     else:
#         for c in range(len(seq)):
#             if seq[c] == b:
#                 find.append(c + 1)
#     print(find)
#     find = list()

# # 4.1
seq = list()
a = False
with open("sequence.gp") as handle:
    title = handle.readline()
    print("Title: ", title)
    for line in handle:
        line = line.strip()
        if line.startswith("ORIGIN"):
            a = True
        if a:
            seq.append(line)
        if line.startswith("//"):
            break
seq = "\n".join(seq)
# print(seq)
# 4.2
l_tmp = list()
tmp = seq.split()
i = 1

for i in range(len(tmp)):
    if tmp[i].isdigit():
        pass
    elif tmp[i] == "ORIGIN":
        pass
    elif tmp[i] == "//":
        pass
    else:
        l_tmp.append(tmp[i])
    i += 1
# l_tmp = "".join(l_tmp)
# print("seq: ", l_tmp)

# 4.3
a_tmp = l_tmp[:7:1]
a_tmp = "".join(a_tmp)
print(a_tmp)
print(len(a_tmp))
