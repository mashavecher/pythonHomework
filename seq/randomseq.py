import random
import Seqletters as sql

DNA = list(sql.DNA_compl.values())
RNA = list(sql.RNA_compl.values())
amino = list(set((sql.RNA_to_prot.values())))
amino.remove('STOP')


def create_nucl(type_seq):
    return random.choice(type_seq)


def randdeoxy():
    return create_nucl(DNA)


def randribo():
    return create_nucl(RNA)


def randamino():
    return create_nucl(amino)


def create_seq_any(type_seq):
    return ''.join(random.choices(type_seq, k=random.randint(10, 1000)))


def create_dna_any():
    return create_seq_any(DNA)


def create_rna_any():
    return create_seq_any(RNA)


def create_prot_any():
    return create_seq_any(amino)


def create_sequence(type_seq, length):
    return ''.join([create_nucl(type_seq) for i in range(0, length)])


def create_dna_fixed(length):
    return create_sequence(DNA, length)


def create_rna_fixed(length):
    return create_sequence(RNA, length)


def create_prot_fixed(length):
    return create_sequence(amino, length)


