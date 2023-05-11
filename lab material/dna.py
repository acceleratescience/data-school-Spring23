################################################################################################
# From Rosalind list of bioinformatics problems: https://rosalind.info/problems/list-view/
# Problem: Counting DNA Nucleotides https://rosalind.info/problems/dna/
# Problem description:

# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
# 
# Given: A DNA string s
# of length at most 1000 nt.

# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
# Sample Dataset
# AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
# Sample Output
# 20 12 17 21
################################################################################################

# Approach 1:
def get_dna_count_first_attempt(dna_seq):
    A_count, C_count, G_count, T_count = 0,0,0,0

    for n in dna_seq:
        if n == 'A':
            A_count = A_count + 1
        elif n == 'C':
            C_count = C_count + 1
        elif n == 'G':
            G_count = G_count + 1
        else:
            T_count = T_count + 1

    return A_count, C_count, G_count, T_count



    


