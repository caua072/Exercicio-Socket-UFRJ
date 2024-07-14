import socket

# Função de conversão das bases
# A função recebe o valor de origem, de qual base é o valor de origem (bin, dec, hex) e qual base o valor deve ser convertido.

# A logica dessa função é converter qualquer que for o valor de origem para a base decimal(utlizando a função int() do python) e 
# depois converter da base decimal para a base solicitada utilizando 

# Retorna uma string.

def questao1_converter_bases(value, from_base, to_base):
    # Converte o valor para decimal
    if from_base == 'bin':
        decimal_value = int(value, 2) 
    elif from_base == 'hex':
        decimal_value = int(value, 16)
    elif from_base == 'dec':
        decimal_value = int(value)
    else:
        return "Base de origem inválida"

    # Converte de decimal para a base de destino
    if to_base == 'bin':
        return bin(decimal_value)[2:]  # [2:] remove o prefixo '0b' da string
    elif to_base == 'hex':
        return hex(decimal_value)[2:]  # [2:] remove o prefixo '0x' da string
    elif to_base == 'dec':
        return str(decimal_value) # já que o valor já está em decimal é só transformar o inteiro em string com o str()
    else:
        return "Base de destino inválida"
    