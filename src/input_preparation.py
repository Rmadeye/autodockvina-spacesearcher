from Bio import SeqIO
from Bio.Blast import NCBIWWW

def test():
    my_query = SeqIO.read("test.fasta", format="fasta")
    print(my_query)
    result_handle = NCBIWWW.qblast("blastp", "refseq_protein", my_query.seq)
    blast_result = open("my_blast.xml", "w")
    blast_result.write(result_handle.read())
    blast_result.close()
    result_handle.close()

if __name__ == '__main__':
    test()