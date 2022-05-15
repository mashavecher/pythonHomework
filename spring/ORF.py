#!/usr/bin/env python

import argparse
import re


def find_orf(file_name):
    try:
        expression = 'ATC.{50,}(?:TAA|TAG|TGA)'
        if file_name.endswith((".fasta", ".fna", ".fa")):
            with open(file_name, "r") as file:
                file_contents = file.read()
                orf = re.findall(expression, file_contents)
        else:
            print("Not a fasta file")
        return orf
    except FileNotFoundError:
        print('No such file')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='find orf with length more than 50')
    parser.add_argument("-f", "--file_name", help="file in fasta format", type=str, required=True)
    args = parser.parse_args()
    file_name = args.file_name
    with open('orf.txt', 'w') as w:
        w.writelines(str(find_orf(file_name)))
