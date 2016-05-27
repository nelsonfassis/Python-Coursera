import re
arquivo = open("regex_sum_233694.txt","r")
texto = ""
for linha in arquivo:
    texto = texto + linha
numeros = re.findall('[0-9]+', texto)
print texto
print numeros
soma = 0
for value in numeros:
    soma = soma + int(value)
print soma

# import re
# print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )