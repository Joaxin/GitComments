def findcomplement(text):
    complement = []
    for i in range(len(text)):
        if text[i] == "A":
            complement.append("T")
        elif text[i] == "T":
            complement.append("A")
        elif text[i] == "G":
            complement.append("C")
        else :
            complement.append("G")
    return complement

text = "AAGACGGGCACCGTGTCCTTCGCGACGTACTCCGACCAGTTGTACACGTTCAGGTTGGTGTCGCCGGCAT"
print(''.join(findcomplement(text)))
print('reverse:')
print(''.join(findcomplement(text)[::-1]))

poolA =  ['AAG', 'TAC', 'CGG', 'GAT', 'TTG', 'GTG', 'CAT', 'GGC', 'ATT', 'TCT']
complements = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}

def matching_codons(complements, poolA):
    answer = []
    for i in poolA:
        codon = ''     # inside of for, codon reset in each iteration
        for a in i:
            codon+= complements[a]
        answer.append(codon)  # outside of secondary for, codon have three leters to end iterations
    return answer

print(matching_codons(complements, poolA))


# from Bio.Seq import Seq
# from Bio.Alphabet import IUPAC
#
# [str(Seq(seq, IUPAC.unambiguous_dna).complement()) for seq in poolA]