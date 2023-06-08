# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random
from os import system, name

# Função para limpar a tela a cada execução:
def limpa_tela():
    # Windows
    if name == "nt":
        _ = system('cls')
    # Mac ou Linux
    else:
        _ = system('clear')


# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:
    # Método Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_escolhidas = []

    # Método para adivinhar a letra
    def guess(self, letra):
        if letra in self.palavra and letra not in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    def hang_over(self):
        return self.hang_manwon() or (len(self.letras_erradas) == 6)

    # Método para verificar se o jogador venceu
    def hang_manwon(self):
        if '_' not in self.hide_palavra():
            return True
        return False

    # Método para não mostrar a letra no board
    def hide_palavra(self):
        rtn = ''
        
        for letra in self.palavra:
            if letra not in self.letras_escolhidas:
                rtn += "_"
            else:
                rtn += letra
            return rtn

# Função para escolher uma palavra aleatoriamente
def rand_palavra():
    # Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    # Escolhe uma palavra aleatoriamente
    palavra = random.choice(palavras)
    return palavra

# Método main - inicia o programa
def main():
    limpa_tela()
    # Cria o objeto e seleciona uma palavra aleatoriamente
    palavra_aleatoria = rand_palavra()
    game = Hangman(palavra_aleatoria)

    # Enquanto o jogo não estiver terminado, imprime o status e solicita uma letra para adivinhar
    while not game.hang_over():
        # Imprime o status do jogo
        game.hide_palavra()
        print(board[len(game.letras_erradas)])
        print('\nLetras erradas: ', end='')
        for letra in game.letras_erradas:
            print(letra, end=' ')
        print()
        print('Letras corretas: ', end='')
        for letra in game.letras_escolhidas:
            print(letra, end=' ')
        print()

        # Recebe a entrada do usuário
        user_input = input('\nDigite uma letra: ')

        # Verifica se a letra digitada faz parte da palavra
        game.guess(user_input)

    # Verifica o resultado do jogo
    if game.hang_manwon():
        print('\nParabéns! Você venceu!')
    else:
        print('\nGame Over! Você perdeu!')
        print('A palavra era: ' + game.palavra)

    print('\nFoi bom jogar com você! Agora, vá estudar!\n')

# Executa o programa
if __name__ == "__main__":
    main()

