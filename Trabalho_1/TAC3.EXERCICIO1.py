from Bio.Seq import Seq
DNA = Seq(input("Digite uma sequencia de DNA:"))
mRNA = DNA.transcribe()
proteina = mRNA.translate()
print('mRNA:', mRNA, 'proteina:', proteina, sep='\n')
