#! /usr/bin/env python
# cnt = dict()
# with open("059.fasta", "r") as handle:
#     for line in handle:
#         if line.startswith(">"):
#             continue
#         else:
#             for base in line.strip():
#                 if base not in cnt:
#                     cnt[base] = 0
#                 cnt[base] += 1

# print(cnt)

# from Bio import SeqIO

# record = SeqIO.read("059.fasta", "fasta")

# A = record.seq.count("A")
# C = record.seq.count("C")
# G = record.seq.count("G")
# T = record.seq.count("T")

# print(f"A: {A}  C:{C}  G:{G}  T:{T}")
# cnt = 0
# with open("061.fastq", "r") as handle:
#     for line in handle:
#         if line.startswith("@"):
#             cnt += 1
# print(cnt)

# n = 0
# d_count = dict()
# with open("061.fastq", "r") as handle:
#     for line in handle:
#         if n % 4 == 0:
#             pass
#         elif n % 4 == 1:
#             for base in line.strip():
#                 if base not in d_count:
#                     d_count[base] = 0
#                 d_count[base] += 1
#         elif n % 4 == 2:
#             pass
#         else:
#             pass
#         n += 1
# print(n/4)
# print(d_count)

# bed 길이 의 합 구하기
# l_data = list()
# length = 0
# with open("077.bed", "r") as handle:
#     for line in handle:
#         data = line.strip().split("\t")
#         result = int(data[2]) - int(data[1])
#         length += result

# print(length)

# with open("077.bed", "r") as handle:
#     for line in handle:
#         data = line.strip().split("\t")
#         chrome, start, end = data
#         length = int(end) - int(start)
#         print(chrome, length)


data = dict()
idx = 1
with open("077.bed") as handle:
    for line in handle:
        chrom, start, end = line.strip().split("\t")
        length = int(end) - int(start)
        if chrom not in data:
            data[chrom] = dict()
        data[chrom][str(idx)] = length
        idx += 1
print(data)
print(data["chr21"]["10"])
