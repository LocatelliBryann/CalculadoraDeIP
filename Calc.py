# CALCULADORA DE IP
# Desenvolvida por Bryann Locatelli - 3INFO1


classe = str(input('Digite a classe da rede (A, B, C): '))
mascara = int(input('Digite a máscara de rede (em bits): '))
ip = [int(i) for i in input('Digite o endereço de IPV4 (separe por pontos): ').split('.')]
print(ip)

if classe == 'A' or classe == 'a':
    bits_masc = ip[1:4]
    ip = [ip[0]]
    bits_ip = 8
elif classe == 'B' or classe == 'b':
    bits_masc = ip[2:4]
    ip = ip[0:2]
    bits_ip = 16
elif classe == 'C' or classe == 'c':
    bits_masc = [ip[-1]]
    ip = ip[0:3]
    bits_ip = 24
else:
    print('Classe inválida!')
bits_masc