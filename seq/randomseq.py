import random
import Seqletters as sql

DNA = list(sql.DNA_compl.values())
RNA = list(sql.RNA_compl.values())
amino = list(set((sql.RNA_to_prot.values())))
amino.remove('STOP')

type = input('which nucleotide, amino acid? ')


def randdeoxy(type):
    return random.choice(DNA)


def randribo(type):
    return random.choice(RNA)


def randamino(type):
    return random.choice(amino)


def create_dna_any(type):
    return ''.join(random.choices(DNA, k=random.randint(10, 1000)))


def create_rna_any(type):
    return ''.join(random.choices(RNA, k=random.randint(10, 1000)))


def create_prot_any(type):
    return ''.join(random.choices(amino, k=random.randint(10, 1000)))


length = int(input('What length? '))


def create_dna_fixed(type, length):
    return ''.join([randdeoxy(type) for i in range(0, length)])


def create_rna_fixed(type, length):
    return ''.join([randribo(type) for i in range(0, length)])


def create_prot_fixed(type, length):
    return ''.join([randamino(type) for i in range(0, length)])




