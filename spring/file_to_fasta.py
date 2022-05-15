#!/usr/bin/env python

import argparse


def get_file_sequence(file_name):
    file = open(file_name)
    sequence = ''
    for line in file:
        if line == '\n':
            yield sequence
            sequence = ''
        else:
            sequence += line


def write_sequence(file_name):
    i = 1
    g = get_file_sequence(file_name)
    for x in g:
        with open(f'{i}.fasta', 'w') as f:
            f.write(str(x))
        i += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='multifasta to single fasta')
    parser.add_argument("-f", "--file_name", help="multifasta file",
                        type=str, required=True)
    args = parser.parse_args()
    file_name = args.file_name
    write_sequence(file_name)
