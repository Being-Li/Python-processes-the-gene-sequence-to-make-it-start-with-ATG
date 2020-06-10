# -*- coding:utf-8 -*-

from numpy.core.defchararray import upper
dna_long = 29000  # Gene length
f = open('G:\\before_5_31_human_fas\\gisaid.fasta', 'r')

sequences = {}
for line in f:
    if line.startswith(">"):
        name = line.rstrip('\n')
        sequences[name] = ''
    else:
        sequences[name] = sequences[name] + line.rstrip('\n')

f.close()

fw = open('G:\\To.fasta', 'w')

for k, v in sequences.items():
    dna_ATGC = ''
    w = v.upper()
    for i in range(len(w)):
        if w[i] in 'ATGC':
            dna_ATGC += w[i]
        else:
            dna_ATGC += "-"

    if dna_ATGC[0:3] == "ATG":
        fw.write(k + '\n' + dna_ATGC[0:dna_long] + '\n')
    else:
        try:
            d = dna_ATGC.split("ATG", 1)[1]
            fw.write(k + '\n' + "ATG" + d[0:(dna_long - 3)] + '\n')
        except:
            continue
fw.close()
