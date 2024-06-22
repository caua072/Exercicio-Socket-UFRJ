import socket

# Função de conversão das bases
# A função recebe o valor de origem, de qual base é o valor de origem (bin, dec, hex) e qual base o valor deve ser convertido.

# A logica dessa função é converter qualquer que for o valor de origem para a base decimal(utlizando a função int() do python) e 
# depois converter da base decimal para a base solicitada utilizando 

# Retorna uma string.

def convert_base(value, from_base, to_base):
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
                    result = convert_base(value, from_base, to_base)
                conn.sendall(result.encode()) # Envia o resultado de volta ao cliente, codificando em bytes a string.

if __name__ == "__main__":
    start_server()
