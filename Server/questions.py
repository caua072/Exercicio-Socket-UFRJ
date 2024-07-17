import socket, struct, schemdraw, pyparsing
from schemdraw.parsing import logicparse


"""
QUESTÃO 1
"""

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

def questao2_operadores(value1, value2, operator):
    # Converter valores complemento a 2 para decimal
    def complemento_a_2(value):
        if value[0] == "1":
            # Inverto os bits por ser negativo
            inv_value = "".join("1" if i == "0" else "0" for i in value)
            # Adiciona 1 ao bit invertido convertido para decimal
            valor_decimal = int(inv_value, 2) + 1
            # Converte para negativo
            valor_decimal = -valor_decimal
        else:
            valor_decimal = int(value, 2)
        return valor_decimal

    # Conversão dos valores para decimal
    valor1 = complemento_a_2(value1)
    valor2 = complemento_a_2(value2)
    
    if operator == "+":
        result = valor1 + valor2
    elif operator == "-":
        result = valor1 - valor2
    elif operator == "*":
        result = valor1 * valor2
    elif operator == "/":
        if valor2 != 0:
            result = valor1 // valor2
        else:
            return "Divisão por zero"
    else:
        return "Erro: Operador inválido"
    
    return result

"""
QUESTÃO 4
"""

# Função recebe um decimal qualquer e converte o valor para a representação IEEE 754 32 bits e sua representação em digitos hex.

# A função utiliza o modulo struct

# Recebe float
# Retorna duas strings: binary_representation que é o formato IEEE 754 e hex_representation que é sua represetanção em digitos hexadecimais.

def questão4_float_para_ieee754(number):
    # Converte o número decimal para bytes usando o formato IEEE 754
    packed = struct.pack('!f', number)
    
    # Converte os bytes para um inteiro que representa a forma binária IEEE 754
    integer_representation = int.from_bytes(packed, byteorder='big')
    
    # Formata a representação binária de 32 bits
    binary_representation = f'{integer_representation:032b}'
    
    # Converte para hexadecimal
    hex_representation = f'{integer_representation:08X}'
    
    return binary_representation, hex_representation

"""
QUESTÃO 5
"""

# Função recebe um texto str e retorna sua representação em hexadecimal utf-8 e quantidade de bytes.

# Recebe string
# Retorna sua representação em hex e quantos bytes.

def questão5_utf8(texto):
    encoded = texto.encode('utf-8')
    representacao_hex = encoded.hex()
    count_bytes = len(encoded)

    return representacao_hex, str(count_bytes)

"""
QUESTÃO 6
"""
# Função recebe um literal como a expressão que deve ser desenhada pela função logicparse
# Retorna o nome do arquivo ('circuito.jpg').

def questão6_desenhar_logica_bool(expressao):
    arquivo = 'circuito.jpg'

    circuito = logicparse(expressao, outlabel='$S$')
    circuito.save(arquivo)

    return arquivo
