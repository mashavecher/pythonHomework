#!/usr/bin/env python

import argparse
import re
from Primerletters import IUB_TO_DEG_F, IUB_TO_DEG_R


def primer_to_trans(primer, primlet):
    p = []
    if primer == '':
        raise ValueError('input primers')
    else:
        for let in primer:
            if let in 'ATCGBDHKMNRSVWY':
                p.append(primlet[let])
            else:
                raise ValueError('wrong primer format')
        transl = ''.join(let)
    return transl


def transl_to_exp(primer1, primer2):
    transl_1_f = primer_to_trans(primer1, IUB_TO_DEG_F)
    transl_1_r = primer_to_trans(primer1, IUB_TO_DEG_R)
    transl_2_f = primer_to_trans(primer2, IUB_TO_DEG_R)
    transl_2_r = primer_to_trans(primer2, IUB_TO_DEG_F)
    exp_f = f'{transl_1_f}.*{transl_2_f}'
    exp_r = f'{transl_1_r}.*{transl_2_r}'
    return exp_f, exp_r


def ampl(file_name, expression):
    try:
        if file_name.endswith((".fasta", ".fna", ".fa")):
            with open(file_name, "r") as file:
                file_contents = file.read()
                amplicons = re.findall(expression, file_contents)
        else:
            print("Not a fasta file")
        return amplicons
    except FileNotFoundError:
        print('No such file')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='find amplicons for given degenerate primers')
    parser.add_argument("-p1", "--primer1", help="primer in IUBMB", type=str, required=True)
    parser.add_argument("-p2", "--primer2", help="primer in IUBMB", type=str, required=True)
    parser.add_argument("-f", "--file_name", help="file in fasta format", type=str, required=True)
    args = parser.parse_args()
    primer1 = args.primer1
    primer2 = args.primer2
    exp_f, exp_r = transl_to_exp(primer1, primer2)
    file_name = args.file_name
    amp1 = ampl(file_name, exp_f)
    amp2 = ampl(file_name, exp_r)
    amp_all = amp1, amp2
    with open('amplicons.txt', 'w') as w:
        w.writelines(str(amp_all))
