import ctypes

atributo_ocultar = 0x02

#Oculta um arquivo, pode-se criar uma variável com o nome:
retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', atributo_ocultar)

#Oculta uma pasta/diretório inteiro:
oculta_pasta = input('Digite o diretório a ser ocultado: ')
retorno_pasta = ctypes.windll.kernel32.SetFileAttributesW(oculta_pasta, atributo_ocultar)


if retorno:
    print(f'Arquivo ocultado.')
else:
    print(f'Não foi possível ocultar.')


if retorno_pasta:
    print(f'Diretório ocultado.')
else:
    print(f'Não foi possível ocultar o diretório.')