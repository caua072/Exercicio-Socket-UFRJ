import socket
from questions import *

"""
  O que cada função das questões recebem como parametro e retornam)

  Questão 1: 
  Recebe um valor de origem(inteiro), base do valor de origem(bin, dec, hex) e qual base deve ser convertido.
  
  Retorna uma String.

  Questão 2:
  

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
                data = conn.recv(1024)
                print(type(data))
                if not data: # Quando o servidor não enviar dados irá dar break.
                    break
                params = data.decode().split(',') # O servidor recebe a data em bytes e decodifica retornando a ser uma string.
                if len(params) != 3:
                    result = "Entrada inválida. Esperado: valor,base_origem,base_destino"
                else:
                    value, from_base, to_base = params
                    result = questao1_converter_bases(value, from_base, to_base)
                conn.sendall(result.encode()) # Envia o resultado de volta ao cliente, codificando em bytes a string.

if __name__ == "__main__":
    start_server()