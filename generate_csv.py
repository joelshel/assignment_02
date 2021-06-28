#!/usr/bin/env python3

import sys


def read_lines(file):
    with open(file, "r") as file:
        return file.readlines()


def return_line(expression_to_search="", list_=[]):
    for line in list_:
        if expression_to_search in line:
            return line


def get_seq_names(lines=[]):
    seq_names = return_line("#CHROM", lines).strip() # get the line with the sequence names
    seq_names = list(filter(lambda name: name != "", seq_names.split("\t")))[9:] # get the sequence names
    return seq_names


def get_rad_ids(lines=[]):
    rad_id = list(filter(lambda name: not name.startswith("#"), lines)) # get the lines with the RAD ids    
    rad_id = [line.split("\t") for line in rad_id] # split the lines in the white spaces (or tabs)
    rad_id = [line[2] for line in rad_id] # get the id for each line
    return rad_id


def write_geno_file(file_name, ids=[], seq_names=[], geno_lines=[]):
    with open(file_name, "w") as new_geno:
        new_geno.write("ID Species")
        for word in ids:
            new_geno.write(" " + word)
        new_geno.write("\n")
        for c, name in enumerate(seq_names):
            new_geno.write(name)
            new_geno.write(" " + name.split("-")[0])
            for d in range(len(geno_lines)):
                new_geno.write(" " + geno_lines[d][c])
            new_geno.write("\n")


def main():
    geno_lines = read_lines(sys.argv[1])
    geno_lines = [line.strip() for line in geno_lines]
    vcf_lines = read_lines(sys.argv[2])
    seq_names = get_seq_names(vcf_lines)
    rad_id = get_rad_ids(vcf_lines)
    write_geno_file(sys.argv[3], rad_id, seq_names, geno_lines)
    # print(seq_names)
    # print(rad_id)
    # print(geno_lines)


if __name__ == "__main__":
    # usage:
    # python generator_csv.py <file.geno> <file.vcf> <output.csv> 
    main()
