import Seqletters as sql
from collections import Counter


class SeqIterator:
    def __init__(self, seq):
        self.seq = seq
        self.index = 0

    def __next__(self):
        if self.index >= len(self.seq):
            raise StopIteration()
        position = self.seq[self.index]
        self.index += 1
        return position


class Sequence:   # parent class
    def __init__(self, name, seq):
        self.name = name
        self.sequence = seq

    def __str__(self):
        return f'Seq = {self.sequence}'

    def get_name(self):     # returns name
        return self.name

    def sequence(self):  # returns sequence
        return self.sequence

    def __len__(self):  # returns sequence length
        return len(self.sequence)   # (magic method is used to find the length of the instance attributes)

    def len(self):
        return len(self)    # returns length

    def stats(self):
        stats = dict(Counter(self.sequence))
        return stats        # returns letter occurrence

    def __iter__(self):     # makes iterable
        return SeqIterator(self.sequence)

    def __getitem__(self, num):      # returns letter from sequence by index
        return self.sequence[num]

    def repl(self, func):
        seqout = ''
        for i in range(len(self.sequence)):
            letter = self.sequence[i]
            seqout += func(letter)
        return self.sequence.replace(self.sequence, seqout)

    def repltwo(self, func):
        seqout = ''
        for i in range(len(self.sequence)):
            prevletter = self.sequence[i - 1]
            letter = self.sequence[i]
            seqout += func(prevletter, letter)
        return self.sequence.replace(self.sequence, seqout)


def rule(letter):
    if letter not in list(sql.DNA_compl.values()) and letter not in list(sql.RNA_compl.values())\
            and letter not in list(set((sql.RNA_to_prot.values()))):
        return 'N'
    else:
        return letter


def ruletwo(prevletter, letter):
    if prevletter and letter not in list(sql.DNA_compl.values())\
            and prevletter and letter not in list(sql.RNA_compl.values())\
            and prevletter and letter not in list(set((sql.RNA_to_prot.values()))):
        return 'N'
    else:
        return letter


class DNA(Sequence):    # DNA class

    @property
    def letters(self):  # self alphabet as property (set)
        return list(sql.DNA_compl.values())

    def __str__(self):
        return f'DNA = {self.sequence}'

    def compl(self):
        compl = ''          # string
        for i in self.sequence:
            compl += sql.DNA_compl[i]
        return compl

    def transc(self):
        transc = ''     # string
        for i in self.sequence:
            transc += sql.DNA_to_RNA[i]
        return RNA(self.name, transc)   # how to address this new object

    def molwt(self):
        molwt = 79.0   # as referenced in seqletters
        for i in self.sequence:
            molwt += float(sql.dnucl_mass[i])
        return molwt


class RNA(Sequence):    # class RNA
    @property
    def letters(self):  # self alphabet as property
        return list(sql.RNA_compl.values())

    def __str__(self):
        return f'RNA = {self.sequence}'

    def compl(self):
        compl = ''          # string
        for i in self.sequence:
            compl += sql.RNA_compl[i]
        return compl

    def molwt(self):
        molwt = 159.0   # as referenced in seqletters
        for i in self.sequence:
            molwt += float(sql.rnucl_mass[i])
        return molwt

    def transl(self):
        prot = ''
        i, k = 0, 3
        while k < len(self.sequence):
            if sql.RNA_to_prot[self.sequence[i:k]] != 'STOP':   # taking dict, taking RNA seq, slice by 3
                prot += sql.RNA_to_prot[self.sequence[i:k]]
                i += 3
                k += 3
            else:
                break
        return Protein(self.name, prot)   # how to address this new object


class Protein(Sequence):    # class Protein
    @property
    def letters(self):  # self alphabet as property
        amino = list(set((sql.RNA_to_prot.values())))
        amino.remove('STOP')
        return amino

    def __str__(self):
        return f'Protein = {self.sequence}'

    def molwt(self):
        wtww = 0
        molwt = ''
        for i in self.sequence:
            wtww += float(sql.amac_mass[i])
            molwt = wtww - (18.02 * (len(self.sequence) - 1))
        return molwt





