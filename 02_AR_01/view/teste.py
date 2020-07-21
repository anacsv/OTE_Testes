frase = "   Meu nome é Dyego,\n é verdade este bilhete\n"
frase2 = "Maykon;Dyego;Granemann"
# print(frase)
# print(frase.strip())

vetor = frase2.split(';')
vetor.append(89)
print('*'*50, '\n'*2)

print(vetor)
primeiro_ultimo = " ".join((vetor[0],vetor[2]))

#teste = vetor[0].join(vetor[2])
print(primeiro_ultimo)
#print(teste)
print( '\n'*2,'*'*50)