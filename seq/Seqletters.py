DNA_to_RNA = {
    'A': 'U',
    'T': 'A',
    'G': 'C',
    'C': 'G',
}

RNA_to_DNA = {
    'U': 'A',
    'A': 'T',
    'C': 'G',
    'G': 'C',
}

DNA_compl = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C',
}

RNA_compl = {
    'A': 'U',
    'U': 'A',
    'C': 'G',
    'G': 'C',
}

'''Exact M.W. of ssDNA (e.g., Oligonucleotides):
M.W. = (An x 313.2) + (Tn x 304.2) + (Cn x 289.2) + (Gn x 329.2) + 79.0ª
An, Tn, Cn, and Gn are the number of each respective nucleotide within the polynucleotide.
ªAddition of "79.0" to the M.W. takes into account the 5' monophosphate left
by most restriction enzymes. No phosphate is present at the 5' end of strands made by primer extension.'''

dnucl_mass = {
    'A': '313.2',
    'T': '304.2',
    'G': '329.2',
    'C': '289.2',
}


'''Exact M.W. of ssRNA (e.g., RNA Transcript):
M.W. = (An x 329.2) + (Un x 306.2) + (Cn x 305.2) + (Gn x 345.2) + 159ª
An, Un, Cn, and Gn are the number of each respective nucleotide within the polynucleotide.
M.W. calculated is valid at physiological pH.
ªAddition of "159" to the M.W. takes into account the M.W. of a 5' triphosphate.'''

rnucl_mass = {
    'A': '329.2',
    'U': '306.2',
    'G': '345.2',
    'C': '305.2',
}

RNA_to_prot = {
    'AUG': 'M',     # START
    'GCU': 'A',
    'GCC': 'A',
    'GCA': 'A',
    'GCG': 'A',
    'CGU': 'R',
    'CGA': 'R',
    'AGA': 'R',
    'CGC': 'R',
    'CGG': 'R',
    'AGG': 'R',
    'AAU': 'N',
    'AAC': 'N',
    'GAU': 'D',
    'GAC': 'D',
    'UGU': 'C',
    'UGC': 'C',
    'CAA': 'Q',
    'CAG': 'Q',
    'GAA': 'E',
    'GAG': 'E',
    'GGU': 'G',
    'GGC': 'G',
    'GGA': 'G',
    'GGG': 'G',
    'CAU': 'H',
    'CAC': 'H',
    'AUU': 'I',
    'AUC': 'I',
    'AUA': 'I',
    'CUU': 'L',
    'CUC': 'L',
    'CUA': 'L',
    'CUG': 'L',
    'UUA': 'L',
    'UUG': 'L',
    'AAA': 'K',
    'AAG': 'K',
    'UUU': 'F',
    'UUC': 'F',
    'CCU': 'P',
    'CCC': 'P',
    'CCA': 'P',
    'CCG': 'P',
    'UCU': 'S',
    'UCC': 'S',
    'UCA': 'S',
    'UCG': 'S',
    'AGU': 'S',
    'AGC': 'S',
    'ACU': 'T',
    'ACC': 'T',
    'ACA': 'T',
    'ACG': 'T',
    'UGG': 'W',
    'UAU': 'Y',
    'UAC': 'Y',
    'GUU': 'V',
    'GUC': 'V',
    'GUA': 'V',
    'GUG': 'V',
    'UAA': 'STOP',
    'UGA': 'STOP',
    'UAG': 'STOP',
}

'''Protein MW = Aminoacid MW.1 +... Aminoacid MW.n -(18.0153 * (n-1)) 
that is with minus water per bond'''

amac_mass = {
    'M': '149.21',
    'A': '89.10',
    'R': '174.20',
    'N': '132.12',
    'D': '133.11',
    'C': '121.16',
    'E': '147.13',
    'Q': '146.15',
    'G': '75.07',
    'H': '155.16',
    'I': '131.18',
    'L': '131.18',
    'K': '146.19',
    'F': '165.19',
    'P': '115.13',
    'S': '105.09',
    'T': '119.12',
    'W': '204.23',
    'Y': '181.19',
    'V': '117.15',
}






# from collections import Counter
# rna = 'ACAGUCGUUUCAUAU'
#
# def get_stats(rna):
#     stats = dict(Counter(rna)) # dict leaves only dictionary
#     return stats
# print(get_stats(rna))

#rna = 'ACAGUCGUUUCAUAU'
# def transl(rna):
#     prot = ''
#     i, k = 0, 3
#     while k < len(rna):
#         if RNA_to_prot[rna[i:k]] != 'STOP':  # taking dict, taking RNA seq, slice by 3
#             prot += RNA_to_prot[rna[i:k]]
#             i += 3
#             k += 3
#         else:
#             break
#     return prot
# print(transl(rna))

# prot = 'KMFPSTWN'
# def amacmolwt(prot):
#     wtww = 0
#     molwt = ''
#     for i in prot:
#         wtww += float(amac_mass[i])
#         molwt = wtww - (18.02 * (len(prot)-1))
#     return molwt
# print(amacmolwt(prot))


# def gmolwt(rna):
#     molwt = 159.0  # as referenced in seqletters
#     for i in rna:
#         molwt += float(rnucl_mass[i])
#     return molwt
# print(gmolwt(rna))