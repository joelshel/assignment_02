#!/usr/bin/env python3

from Bio import SeqIO
import sys

def converter(file, input_extension='fasta', output_extension='nexus'):
    """Funcion to convert nucleotide sequence files.

    Args:
        file (str): The name of the file you want to convert.
        input_extension (str, optional): The type of your original file. Defaults to 'fasta'.
        output_extension (str, optional): The type of your converted file. Defaults to 'nexus'.

    Returns:
        str: The filename of your converted file.
    """
    split_file = file.rsplit(".", 1)[0]
    try:
        sequences = SeqIO.convert(f"{file}", f"{input_extension}", f"{split_file}.{output_extension}", f"{output_extension}", "DNA")
    except FileNotFoundError:
        try:
            sequences = SeqIO.convert(f"{split_file}.{input_extension}", f"{input_extension}", f"{split_file}.{output_extension}", f"{output_extension}", "DNA")
        except FileNotFoundError:
            print("Error, file not found, verify if the file name is correct!")
    print("Conversion executed successfully!")
    return split_file + '.' + output_extension

if __name__ == '__main__':
    converter(sys.argv[1])
