import socket

# Pega os parametros da questão 1 para envio ao servidor. 
def get_question_parameters():
    value = input('Digite o valor a ser convertido: ')
    from_base = input('Digite a base de origem (bin/dec/hex): ')
    to_base = input('Digite a base de destino (bin/dec/hex): ')
    return f"{value},{from_base},{to_base}"

def start_client(host='localhost', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        params = get_question_parameters()
        s.sendall(params.encode())
        data = s.recv(1024)
        print(f'Resposta do servidor: {data.decode()}')

if __name__ == "__main__":
    start_client()
