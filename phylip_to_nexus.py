#!/usr/bin/env python3

# to understand better the program see 
# https://github.com/joelshel/homework2_ASB/blob/master/bio_converter.py
# and [link]

from bio_formats_converter import converter
import sys


def phylip_nexus():
    nexus_filename = converter(sys.argv[1], input_extension='phylip', output_extension='nexus')
    try:
        if "-mb" == sys.argv[2]:
            print("Adding MB block")
            mb_file = nexus_filename.rsplit('.')[0]
            with open(nexus_filename, "a") as nexus:
                nexus.write(f"""begin mrbayes;
    set autoclose=yes;
    outgroup {sys.argv[3]};
    mcmcp ngen={sys.argv[4]} printfreq=1000 samplefreq=100 diagnfreq=1000 nchains=4 savebrlens=yes filename={mb_file};
    mcmc;
    sumt filename={mb_file};
    end;
    """)
            print("MB block added successfully")
    except IndexError:
        pass

if __name__ == '__main__':
    phylip_nexus()