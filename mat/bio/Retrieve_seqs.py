from pyfaidx import Fasta
import sys
import re
if len(sys.argv)>=2:
    gen = sys.argv[1]
    chr = sys.argv[2]
    pos = sys.argv[3]
    desc = sys.argv[4]
    f = open("Ugene.txt", "a")
    if gen.upper() == "GB":
        genome = Fasta("H:/data/Gb/GB.fa")
        p = pos.split(":")
        f.write(">")
        f.write("Gb " + desc + " " + chr + " " + pos)
        f.write("\n")
        sequences = genome[chr][int(p[0]) - 1:int(p[1])]
        if re.match(".*-", desc):
            sequences = sequences.complement
            sequences = sequences.reverse
        f.write(str(sequences))
        f.write("\n")
        f.close()
    elif gen.upper()  == "BGI":
        genome = Fasta("H:\\data\\Gh\\BGI.fa")
        p = pos.split(":")
        f.write(">")
        f.write("Gh_BGI " + desc + " " + chr + " " + pos)
        if re.match("scaffold", chr) or re.match(".*chr", chr):
            chr=chr
        else:
            chr = re.sub("0","",re.sub("(\d+)","t_chr\\1",chr))
        f.write("\n")
        sequences = genome[chr][int(p[0]) - 1:int(p[1])]
        if re.match(".*-", desc):
            sequences = sequences.complement
            sequences = sequences.reverse
        f.write(str(sequences))
        f.write("\n")
        f.close()
    elif gen.upper()   == "NBI":
        genome = Fasta("H:\\data\\Gh\\NBI.fa")
        p = pos.split(":")
        f.write(">")
        f.write("Gh_NBI " + desc + " " +chr + " " + pos)
        f.write("\n")
        sequences = genome[chr][int(p[0]) - 1:int(p[1])]
        if re.match(".*-", desc):
            sequences = sequences.complement
            sequences = sequences.reverse
        f.write(str(sequences))
        f.write("\n")
        f.close()
    elif gen.upper()  == "JGI":
        genome = Fasta("H:\\data\\Gh\\JGI.fa")
        p = pos.split(":")
        f.write(">")
        f.write("Gh_JGI " + desc + " " +chr + " " + pos)
        f.write("\n")
        sequences = genome[chr][int(p[0]) - 1:int(p[1])]
        if re.match(".*-", desc):
            sequences = sequences.complement
            sequences = sequences.reverse
        f.write(str(sequences))
        f.write("\n")
        f.close()
    else:
        print("Not Supported Species")
    sys.exit()