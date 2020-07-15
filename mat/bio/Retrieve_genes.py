from pyfaidx import Fasta
f=open("gggene.txt","a")

genelist=["Gbscaffold1061.4.0","Gbscaffold11358.2.0","Gbscaffold11669.25.0","Gbscaffold11669.27.0","Gbscaffold11670.10.0","Gbscaffold11670.9.0","Gbscaffold12844.12.0","Gbscaffold12844.13.0","Gbscaffold12844.14.0","Gbscaffold13861.30.0","Gbscaffold13861.31.0","Gbscaffold13861.32.0","Gbscaffold14774.10.0","Gbscaffold15128.6.0","Gbscaffold15751.7.0","Gbscaffold15818.6.0","Gbscaffold1632.13.0","Gbscaffold16951.3.0","Gbscaffold17766.23.0","Gbscaffold18431.1.0","Gbscaffold18653.11.0","Gbscaffold20579.11.0","Gbscaffold2145.2.0","Gbscaffold2145.3.0","Gbscaffold2145.4.0","Gbscaffold2295.17.0","Gbscaffold22993.1.0","Gbscaffold2334.6.0","Gbscaffold24029.11.0","Gbscaffold24029.12.0","Gbscaffold27352.1.0","Gbscaffold27352.1.0","Gbscaffold2783.8.0","Gbscaffold3298.6.0","Gbscaffold34790.3.0","Gbscaffold3599.17.0","Gbscaffold37570.8.0","Gbscaffold3794.2.0","Gbscaffold3794.3.0","Gbscaffold38732.1.0","Gbscaffold4.6.0","Gbscaffold4081.3.0","Gbscaffold4478.7.0","Gbscaffold515.3.0","Gbscaffold5770.1.0","Gbscaffold5770.2.0","Gbscaffold6297.1.0","Gbscaffold6321.12.0","Gbscaffold6754.5.0","Gbscaffold7585.16.0","Gbscaffold803.15.0","Gbscaffold8622.26.0","Gbscaffold8630.2.0","Gbscaffold8630.3.0","Gbscaffold8741.1.0","Gbscaffold9680.39.0"]

# genelist=["Gh_A10G1051","Gh_A03G2174","Gh_D02G2148","Gh_D01G1810","Gh_A11G0075","Gh_D11G0080","Gh_A01G1495","Gh_D01G1732","Gh_A05G3069","Gh_D04G0574","Gh_A09G0423","Gh_Sca062728G01","Gh_A09G1935","Gh_D09G2145","Gh_A12G1044","Gh_D12G1163","Gh_A01G2000","Gh_D01G0046","Gh_A12G0290","Gh_D12G0375","Gh_D10G2150","Gh_A08G2130","Gh_D08G2500","Gh_A08G1089","Gh_D08G1373","Gh_A01G0005","Gh_D01G0003","Gh_D10G2187","Gh_D10G2188","Gh_A05G0127","Gh_D05G0189","Gh_A05G1657","Gh_D05G1846","Gh_D01G0004","Gh_A10G1904","Gh_A10G1905","Gh_A10G1906","Gh_D10G2189","Gh_A01G0045","Gh_D01G0045","Gh_A06G0501","Gh_D06G0558","Gh_Sca032732G01","Gh_A07G1227","Gh_D07G1331","Gh_A03G1286","Gh_D02G1726","Gh_A03G0701","Gh_D02G0946","Gh_A06G1558","Gh_D06G2376","Gh_Sca144453G01","Gh_D05G3896","Gh_A07G0864","Gh_Sca018269G01","Gh_Sca047531G01"]

Gbgenes=Fasta("H:\\Roo\\Cottondata\\Gb\\Gb.final.all.CDS.fa")
# Ghgenes=Fasta("H:\\Roo\\Cottondata\\Gh\\NBI_Gossypium_hirsutum_v1.1.cds.fa")

for i in genelist:
    f.write(">")
    f.write(str(i))
    f.write("\n")
    f.write(str((Gbgenes[i][:])))
    f.write("\n")
f.close()

# print(Gh["D01"][11687:14745])
