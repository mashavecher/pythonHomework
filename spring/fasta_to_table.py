#!/usr/bin/env python

import argparse
import sys
import subprocess
import pkg_resources

required = {'prettytable'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)


from file_to_fasta import get_file_sequence
from collections import Counter
from prettytable import PrettyTable as pt


tb = pt()
tb.field_names = ["Name", "length", "A", "C", "G", "T"]


def write_data(file_name):
    seq = get_file_sequence(file_name)
    for x in seq:
        rows = x.splitlines()
        name_row, x = rows[0], rows[1:]
        name = name_row.replace(', partial sequence', '')
        x = ''.join(x)
        letters = Counter(x)
        tb.add_row([f'{name}', len(x), letters["A"], letters["C"], letters["G"], letters["T"]])


def write_table(file_name):
    write_data(file_name)
    with open('table.txt', 'w') as w:
        w.write(str(tb))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='multifasta to table with name, length and character count')
    parser.add_argument("-f", "--file_name", help="multifasta file",
                        type=str, required=True)
    args = parser.parse_args()
    file_name = args.file_name
    write_table(file_name)
