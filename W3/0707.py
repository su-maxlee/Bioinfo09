#! /usr/bin/env python

# json import file read
# import json

# with open("data.json", "r") as handle:
#     data = json.load(handle)

# for elem in data:
#     print(f"{elem['id']}\t{elem['sequence']}\t{elem['species']}")


# k-mer 만들기

# Fasta AGCT 읽기

# f_59 = "059.fasta"
# d_count = dict()
# with open(f_59, "r") as handle:
#     for line in handle:
#         if line.startswith(">"):
#             continue
#         for base in line.strip():
#             if base not in d_count:
#                 d_count[base] = 0
#             d_count[base] += 1
# print(d_count)

# FastQ 만들기 165
# cnt = 0
# data = dict()
# with open("061.fastq", "r") as handle:
#     for line in handle:
#         if cnt % 4 == 0:  # header
#             pass
#         elif cnt % 4 == 1:  # base
#             for base in line.strip():
#                 if base not in data:
#                     data[base] = 0
#                 data[base] += 1
#         elif cnt % 4 == 2:  # delimiter
#             pass
#         elif cnt % 4 == 3:  # qual
#             pass
#         cnt += 1
# print(cnt / 4)
# print(data)

# bed file 77

# result=0
# with open("077.bed", "r") as handle:
#     for line in handle:
#         data=line.strip().split('\t')
#         #int(data[2])-int(data[1])
#         chrom,start,end=data
#         length=int(end)-int(start)
#         result+=length
# print(result)

# VCF 70
"""
cnt = 0
with open("070.vcf", "r") as handle:
    for line in handle:
        if line.startswith("#"):
            continue
        else:
            cnt += 1
print(cnt)
cnt2 = 0
with open("070.vcf", "r") as handle:
    for line in handle:
        if line.startswith("#"):
            continue
        elif line.__contains__("PASS"):
            cnt2 += 1

print(cnt2)

cnt_all = 0
cnt_pass = 0
with open("070.vcf", "r") as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        elif line.startswith("#"):
            header = line.strip().split("\t")
            filter_idx = header.index("FILTER")
            continue
        data = line.strip().split("\t")
        cnt_all += 1
        # if data[6]== "PASS":
        if data[filter_idx] == "PASS":
            cnt_pass += 1
print(cnt_all, cnt_pass, cnt_pass / cnt_all)
"""
# 재귀함수
# 재귀함수의 기본 - 피보나치 수열

# import sys

# n = int(input("input number: "))


# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# print(fib(n))

# k mer
import sys


def rec(l1, l2, n):
    if n < 2:
        return l2
    else:
        ltmp = []
        for s1 in l1:
            for s2 in l2:
                ltmp.append(s1 + s2)
        return rec(l1, ltmp, n - 1)


l1 = ["A", "C", "G", "T"]
l2 = ["A", "C", "G", "T"]
n = int(sys.argv[1])
l = rec(l1, l2, n)
print(l)
