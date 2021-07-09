#! /usr/bin/env python

# 4.4
# from Bio.Seq import Seq

# fasta = open("sequence.nucleotide.fasta")
# gb = open("sequence.nucleotide.gb")

# print(
#     "1) Read a FASTA format DNA sequence file and make a reverse sequence file."
# )
# print(
#     "2) Read a FASTA format DNA sequence file and make a reverse complement sequence file."
# )
# print("3) Convert GenBank format file to FASTA format file.")
# l_seq = []
# option = input("Select an option: ")
# for lines in fasta:
#     line = lines.strip()
#     if line.startswith(">"):
#         title = line
#     elif line.isalpha():
#         l_seq.append(line)
#     s_seq = "\n".join(l_seq)
# if option == "1":
#     rev_seq = open("reverse.sequence.nucleotide.fasta", "w")
#     rev_seq.write(title + " Reverse: \n")
#     rev_seq.write(s_seq[::-1])
#     rev_seq.close()
# if option == "2":
#     revcomp_seq = open("reverse.complement.sequence.nucleotide.fasta", "w")
#     revcomp_seq.write(title + " Reverse.Complement: \n")
#     rs_seq = Seq(s_seq)
#     revcomp_seq.write(str(rs_seq))
#     revcomp_seq.close()
# if option == "3":
#     a = False
#     gbseq = list()
#     title = gb.readline()
#     for line in gb:
#         line = line.strip()
#         if line.startswith("ORIGIN"):
#             a = True
#         if a:
#             gbseq.append(line)
#     gbseq = "\n".join(gbseq)
#     newgbfasta = open("new.sequence.nucleotide.fasta", "w")
#     newgbfasta.write(title)
#     newgbfasta.write(gbseq)
#     newgbfasta.close()

# fasta.close()
# gb.close()
# 4.5
# a = False
# aT = list()
# for line in gb:
#     lines = line.strip()
#     if lines.startswith("JOURNAL"):
#         a = False
#     if lines.startswith("TITLE"):
#         a = True
#     if a:
#         aT.append(line)

# gb.close()
# aT = "\n".join(aT)
# print(aT)

# 5.1
codon_dic = {
    "TTT": "F",
    "TTC": "F",
    "TTA": "L",
    "TTG": "L",
    "TCT": "S",
    "TCC": "S",
    "TCA": "S",
    "TCG": "S",
    "TAT": "Y",
    "TAC": "Y",
    "TAA": "*",
    "TAG": "*",
    "TGT": "C",
    "TGC": "C",
    "TGA": "*",
    "TGG": "W",
    "CTT": "L",
    "CTC": "L",
    "CTA": "L",
    "CTG": "L",
    "CCT": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "CAT": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "CGT": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "ATT": "I",
    "ATC": "I",
    "ATA": "I",
    "ATG": "M",
    "ACT": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "AAT": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "AGT": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GTT": "V",
    "GTC": "V",
    "GTA": "V",
    "GTG": "V",
    "GCT": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "GAT": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "GGT": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
}
l_seq = list()
l_codon = list()
fr = open("sequence.nucleotide.fasta")
for lines in fr:
    line = lines.strip()
    if line.startswith(">"):
        title = line
    elif line.isalpha():
        l_seq.append(line)
    s_seq = "".join(l_seq)

# for i in range(0, len(s_seq) - 2, 3):
# print(s_seq[i : i + 3])

# 5.2
for i in range(0, len(s_seq) - 2, 3):
    l_codon.append(s_seq[i : i + 3])

for i in range(len(l_codon)):
    # print(l_codon[i] + "   " + codon_dic[l_codon[i]])
    # print(l_codon[i], end="")
    print(codon_dic[l_codon[i]], end="  ")

