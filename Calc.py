# CALCULADORA DE IP
# Desenvolvida por Bryann Locatelli - 3INFO1

import emoji #Importando biblioteca de emojis
from math import ceil #Importando biblioteca de matemática para arredondamento
import time #Importando biblioteca de controle de tempo


barrinha = "\033[1;33m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[1;33m"

print(barrinha)                                                                                                                                              #
print("              \033[1;31mCALCULADORA \033[1;32mDE \033[1;94mIP\033[0;0m")                                                                              #Cabeçalho
print(emoji.emojize(":exploding_head:", language='alias'),"Desenvolvida por Bryann Locatelli - 3INFO1",emoji.emojize(":exploding_head:", language='alias'))  #
print(barrinha)                                                                                                                                              #

v = 0
ip = []
while v == 0:
    ip_classe = str(input("\033[1;32mInforme qual a classe da rede desejada \033[1;96m(\033[1;35mA , B , C\033[1;96m) \033[1;32m=>\033[0;0m"))
    print(f"Aguarde...")
    time.sleep(1.5)

    if ip_classe == "A" or ip_classe == "a" or ip_classe == "B" or ip_classe == "b" or ip_classe == "C" or ip_classe == "c":                                  #Verificação se a classe de IP informada é válida (A, B ou C)
        print(emoji.emojize(":check_mark_button:", language='alias'),"\033[1;32mCLASSE DE IP VÁLIDA\033[0;0m")

        mask = int(input("\033[1;32mInforme a máscara de rede em bits: \033[1;96mExemplo:\033[1;35m26 \033[1;32m=>\033[0;0m "))
        print(f"Aguarde...")
        time.sleep(1.5)

        if mask <= 32:                                                                                                                                      #Verificação se a máscara de IP informada é válida
            print(emoji.emojize(":check_mark_button:", language='alias'),"\033[1;32mMÁSCARA DE IP VÁLIDA\033[0;0m")

            ip = [int(i) for i in input('\033[1;32mInforme o endereço de IP \033[1;96m(\033[1;35mSeparado por pontos\033[1;96m) \033[1;32m=>\033[0;0m ').split('.')]    #Recebe o input e já separa o IP pelo "."

            if ip_classe == 'A' or ip_classe == 'a':
                mask_bits = ip[1:4]
                ip = [ip[0]]
                ip_bits = 8
                v = 1
            elif ip_classe == 'B' or ip_classe == 'b':
                mask_bits = ip[2:4]
                ip = ip[0:2]
                ip_bits = 16
                v = 1
            elif ip_classe == 'C' or ip_classe == 'c':
                mask_bits = [ip[-1]]
                ip = ip[0:3]
                ip_bits = 24
                v = 1 

        else:
            print(emoji.emojize(":cross_mark:", language='alias'),'\033[1;31mMÁSCARA INVÁLIDA\033[0;0m',emoji.emojize(":cross_mark:", language='alias'))       
    else:
        print(emoji.emojize(":cross_mark:", language='alias'),'\033[1;31mCLASSE DE IP INVÁLIDA\033[0;0m',emoji.emojize(":cross_mark:", language='alias'))


bits_mascara = mask - ip_bits
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
