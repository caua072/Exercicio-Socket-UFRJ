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

  Questão 6:
  Recebe uma expressão logica
  Retorna o nome do arquivo ('circuito.jpg')

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
                
                # Questão 4
                elif question == 4:
                    params = data.decode()
                    binary_representation, hex_representation = questão4_float_para_ieee754(float(params))
                    result = f'IEEE 754 é: {binary_representation}\nHexadecimal: {hex_representation}\n'
                
                # Questão 6
                elif question == 6:
                    params = data.decode()
                    namefile = questão6_desenhar_logica_bool(params)

                    with open(namefile, 'rb') as arquivo:
                        for data in arquivo.readlines():
                            conn.send(data) 
                    os.remove(namefile) # Exclui o arquivo do servidor

                    result = 'Desenho enviado com sucesso\n'

                # Envio do processamento ao client
                conn.sendall(result.encode()) # Envia o resultado de volta ao cliente, codificando em bytes a string.

if __name__ == "__main__":
    start_server()