from Bio import SeqIO
import os

fin = "../raw/Mammalia.fa"


for entry in SeqIO.parse(fin, 'fasta'):
    with open(f'../raw/separate_seqs/{entry.id}.fa', 'w') as fout:
        fout.write(f'>{entry.id}\n{entry.seq}')

for filename in os.listdir('../raw/separate_seqs/'):
    file = os.path.join('../raw/separate_seqs/', filename)
    print(file[21:])
    os.system(f'etandem -sequence {file} -maxrepeat 100 -minrepeat 2 -outfile {file[21:]}.out -rdirectory2 ../reSLUTS/tandem_repeats')