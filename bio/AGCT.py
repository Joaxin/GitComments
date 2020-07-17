
map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"*", "UAG":"*",
    "UGU":"C", "UGC":"C", "UGA":"*", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

imap={"UUU":"Phe", "UUC":"Phe", "UUA":"Leu", "UUG":"Leu",
    "UCU":"Ser", "UCC":"Ser", "UCA":"Ser", "UCG":"Ser",
    "UAU":"Tyr", "UAC":"Tyr", "UAA":"***", "UAG":"***",
    "UGU":"Cys", "UGC":"Cys", "UGA":"***", "UGG":"Trp",
    "CUU":"Leu", "CUC":"Leu", "CUA":"Leu", "CUG":"Leu",
    "CCU":"Pro", "CCC":"Pro", "CCA":"Pro", "CCG":"Pro",
    "CAU":"His", "CAC":"His", "CAA":"Gln", "CAG":"Gln",
    "CGU":"Arg", "CGC":"Arg", "CGA":"Arg", "CGG":"Arg",
    "AUU":"Ile", "AUC":"Ile", "AUA":"Ile", "AUG":"Met",
    "ACU":"Thr", "ACC":"Thr", "ACA":"Thr", "ACG":"Thr",
    "AAU":"Asn", "AAC":"Asn", "AAA":"Lys", "AAG":"Lys",
    "AGU":"Ser", "AGC":"Ser", "AGA":"Arg", "AGG":"Arg",
    "GUU":"Val", "GUC":"Val", "GUA":"Val", "GUG":"Val",
    "GCU":"Ala", "GCC":"Ala", "GCA":"Ala", "GCG":"Ala",
    "GAU":"Asp", "GAC":"Asp", "GAA":"Glu", "GAG":"Glu",
    "GGU":"Gly", "GGC":"Gly", "GGA":"Gly", "GGG":"Gly",}

def Triplets(RNA,n):
    AA=[]
    for i in range(n,len(RNA),3):
        if i>len(RNA)-3:
            break
        condon=RNA[i:i+3]
        AA.append(map[condon])
    return AA

def iTriplets(RNA,n):
    AA=[]
    for i in range(n,len(RNA),3):
        if i>len(RNA)-3:
            break
        condon=RNA[i:i+3]
        AA.append(imap[condon])
    return AA

DNA = "ATGGAAGTCCCCTTTTTCCCAACCCTTTTCTCCTGTATCAAAGGCTTGGTGGTGCAACAAGCCTTGTTCTCAACCTTGGAGGATTGGCTAG"

# text=input("Please input the sequences\n")

# BP={"A":"U","T":"A","C":"G","G":"C"}
BP = {"A":"A","T":"U","C":"C","G":"G"}
RNA = ("".join((BP[i]) for i in DNA))
print(RNA,len(RNA))

for i in range(3):
    iAmmino="".join(iTriplets(RNA,i))
    if i==0:
        print(iAmmino)
    else:
        print(" "*(i-1),iAmmino)

for i in range(3):
    Ammino="".join(Triplets(RNA,i))
    print(Ammino)
