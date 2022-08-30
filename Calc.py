# CALCULADORA DE IP
# Desenvolvida por Bryann Locatelli - 3INFO1

v = 0
ip = ""
while v == 0:
    ip_classe = str(input("\033[1;32mInforme qual a classe da rede desejada \033[1;96m(A , B , C): "))

    if ip_classe == 'A' or ip_classe == 'a':
        bits_masc = ip[1:4]
        ip = [ip[0]]
        bits_ip = 8
        v = 1
    elif ip_classe == 'B' or ip_classe == 'b':
        bits_masc = ip[2:4]
        ip = ip[0:2]
        bits_ip = 16
        v = 1
    elif ip_classe == 'C' or ip_classe == 'c':
        bits_masc = [ip[-1]]
        ip = ip[0:3]
        bits_ip = 24
        v = 1
    else:
        print('	\033[1;31mip_classe inválida!\033[0;0m')

mascara = int(input("\033[1;32mInforme a máscara de rede em bits: \033[1;96mExemplo:\033[1;35m26  "))
ip = [int(i) for i in input('Digite o endereço de IPV4 (separe por pontos): ').split('.')]
print(ip)



print(bits_masc)

from math import ceil

bits_mascara = mascara - bits_ip
octetos = ceil(bits_mascara/8)
lista_mascara = [[] for i in range(octetos)]

c = bits_mascara
for i in range(0, octetos):
    for num in range(0, 8):
        if c > 0:
            lista_mascara[i].append(2**(7-num))
            c -= 1
        else:
            break

print(lista_mascara)

new_rede = []
for i in lista_mascara:
    new_rede.append(sum(i))
for i in range(4-len(lista_mascara)):
    new_rede.insert(0, 255)
new_rede = [str(i) for i in new_rede]    
new_rede = ".".join(new_rede)

novo_ip = ip
for item in lista_mascara:
    novo_ip.append(sum(item))
novo_ip = [str(i) for i in novo_ip]


print(f'Total de IPs: {2**bits_mascara}')
print(f'Total de Redes: {(2**bits_mascara)/min(lista_mascara[-1])}')
print(f'Hosts por rede: {min(lista_mascara[-1])-2}')
print(f'IPs por rede: {min(lista_mascara[-1])}')
print(f'Máscara de rede: {new_rede}')