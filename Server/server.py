import socket, os
from questions import *

"""
  O que cada função das questões recebem como parametro e retornam)

  Questão 1: 
  Recebe um valor de origem(inteiro), base do valor de origem(bin, dec, hex) e qual base deve ser convertido.
  Retorna uma String.

  Questão 4:
  Recebe 1 valor decimal (float)
  Retorna 2 variaveis string, 

  Questão 5:
  Recebe 1 frase qualquer
  Retorna 2 variaveis string

  Questão 6:
  Recebe uma expressão logica
  Retorna o nome do arquivo ('circuito.jpg')

  Questão 7:
  Recebe 3 valores booleanos (True ou False) ou inteiros (1 ou 0)
  Retorna um valor booleano ou inteiro
"""

def start_server(host='localhost', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # socket Internet TCP
        s.bind((host, port))
        s.listen()
        print(f'Servidor escutando em {host}:{port}')
        
        while True:
            conn, addr = s.accept() # Função accept() retorna um socket representando a conexão (conn) e e o endereço do client (addr).
            with conn: # with utilizado por motivo de segurança, caso algo de errado o with encerra a conexão.
                print(f'Conectado por {addr}')

                # Receber qual questão cliente quer fazer
                question_data = conn.recv(1024)
                if not question_data:
                    break
                question = question_data.decode()
                question = int(question)

                print(f'Questão {question} selecionada. \n')

                # Receber os parametros da questão.
                data = conn.recv(1024)
                if not data: # Quando o servidor não enviar dados irá dar break.
                    break
                
                # Processamentos dos parametros

                # Questão 1
                if question == 1:
                    params = data.decode().split(',') # O servidor recebe a data em bytes e decodifica retornando a ser uma string.
                    if len(params) != 3:
                        result = "Entrada inválida. Esperado: valor,base_origem,base_destino\n"
                    else:
                        value, from_base, to_base = params
                        result = questao1_converter_bases(value, from_base, to_base)
                        
                
                # Questão 2
                elif question == 2:
                    params = data.decode().split(',')
                    if len(params) != 3:
                        result = "Entrada inválida. Esperado: valor1, valor2, operador\n"
                    else:
                        value1, value2, operator = params
                        result = str(questao2_operadores(value1, value2, operator))

                # Questão 4
                elif question == 4:
                    params = data.decode()
                    binary_representation, hex_representation = questão4_float_para_ieee754(float(params))
                    result = f'IEEE 754 é: {binary_representation}\nHexadecimal: {hex_representation}\n'

                # Questão 5
                elif question == 5:
                    params = data.decode()
                    representacao_hex, quantidade_bytes = questão5_utf8(params)
                    result = f'Hex: {representacao_hex}\nBytes: {quantidade_bytes}'
                
                # Questão 6
                elif question == 6:
                    params = data.decode()
                    namefile = questão6_desenhar_logica_bool(params)

                    with open(namefile, 'rb') as arquivo:
                        for data in arquivo.readlines():
                            conn.send(data) 
                    os.remove(namefile) # Exclui o arquivo do servidor

                    result = 'Desenho enviado com sucesso\n'
                
                elif question == 7:
                    params = data.decode().split(',')
                    if len(params) != 3:
                        result = "Entrada inválida. Esperado: A, B, C\n"
                    else:
                        A, B, C = params

                        a = 1 if A == 'True' else 0
                        b = 1 if B == 'True' else 0
                        c = 1 if C == 'True' else 0

                        and3 = (a and b and c)
                        and4 = questão7_and3_com_and4(a, b, c)

                        and3 = 'True' if and3 == 1 else 'False'
                        and4 = 'True' if and4 == 1 else 'False'

                        result = f'({A} and {B} and {C}) = {and3} equivalente ({A} and {B} and {C} and "1") = {and4}\n' 

                # Envio do processamento ao client
                conn.sendall(result.encode()) # Envia o resultado de volta ao cliente, codificando em bytes a string.

if __name__ == "__main__":
    start_server()