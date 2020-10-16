seq1 = (input('Digite sequencia 1:'))
seq2 = (input('Digite sequencia 2:'))
seq = seq1 + seq2
complemento_reverso = ""
for i in seq:
    if i.upper() == "A":
        complemento_reverso += "T"
    if i.upper() == "G":
        complemento_reverso += "C"
    if i.upper() == "T":
        complemento_reverso += "A"
    if i.upper() == "C":
        complemento_reverso += "G"
print(complemento_reverso)