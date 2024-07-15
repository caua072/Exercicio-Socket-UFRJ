import socket

# Armazenar questão desejada (Retorna um int)
def get_question():
    while True:
        question = int(input('Digite a questão a ser realizada: '))
        if question >= 1 and question <= 7:
            return question
        print(f'{question} não é uma questão valida.\nTente novamente.\n')


# Armazenar parametros das questões determinadas pelo client (Retornam Strings)

# Questão 1
def get_question1_parameters():
    value = input('Digite o valor a ser convertido: ')
    from_base = input('Digite a base de origem (bin/dec/hex): ')
    to_base = input('Digite a base de destino (bin/dec/hex): ')
    return f"{value},{from_base},{to_base}"

# Questão 4
def get_question4_parameters():
    number = input('Digite o valor decimal qualquer: ')
    return number

def start_client(host='localhost', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        question = get_question()
        print(f'Você selecionou a questão {question}.\n')
        s.sendall(str(question).encode()) # Primeiro envia a questão para o servidor Str --> bytes

        if question == 1:
            params = get_question1_parameters()
        elif question == 4:
            params = get_question4_parameters()

        
        s.sendall(params.encode()) # Envia os parametros em bytes. (String --> bytes)
        data = s.recv(1024) # Recebe os dados do servidor em bytes e decodifica para string 
        print(f'Resposta do servidor: {data.decode()}')

if __name__ == "__main__":
    start_client()
