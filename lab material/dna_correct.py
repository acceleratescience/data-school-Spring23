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

def get_dna_count_correct_attempt_C(dna_seq):
    A_count, C_count, G_count, T_count = 0,0,0,0

    if not (set(dna_seq).issubset( set(['A', 'C', 'G', 'T']))):
        return "Input DNA sequence is not valid."
    
    if len(dna_seq) > 1000:
        return "Input DNA sequence length is above allowed limit."
            
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
            

    

def get_dna_count_optimised(dna_seq):
    if not (set(dna_seq).issubset( set(['A', 'C', 'G', 'T']))):
        return "Input DNA sequence is not valid."
    
    if len(dna_seq) > 1000:
        return "Input DNA sequence length is above allowed limit."
        

    return dna_seq.count('A'), dna_seq.count('C'), dna_seq.count('G'), dna_seq.count('T')    
