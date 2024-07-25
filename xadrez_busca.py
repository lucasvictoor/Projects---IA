import pygame
import sys
import random
from collections import deque

pygame.init()

# Cores do Tabuleiro
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHT_GRAY = (192, 192, 192)

# Dimensões
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Img Peças
KING_WHITE = pygame.image.load("img/king_white.png")
QUEEN_WHITE = pygame.image.load("img/queen_white.png")
BISHOP_WHITE = pygame.image.load("img/bishop_white.png")
KNIGHT_WHITE = pygame.image.load("img/knight_white.png")
KING_BLACK = pygame.image.load("img/king_black.png")
QUEEN_BLACK = pygame.image.load("img/queen_black.png")
BISHOP_BLACK = pygame.image.load("img/bishop_black.png")
KNIGHT_BLACK = pygame.image.load("img/knight_black.png")

KING_WHITE = pygame.transform.scale(KING_WHITE, (SQUARE_SIZE, SQUARE_SIZE))
QUEEN_WHITE = pygame.transform.scale(QUEEN_WHITE, (SQUARE_SIZE, SQUARE_SIZE))
BISHOP_WHITE = pygame.transform.scale(BISHOP_WHITE, (SQUARE_SIZE, SQUARE_SIZE))
KNIGHT_WHITE = pygame.transform.scale(KNIGHT_WHITE, (SQUARE_SIZE, SQUARE_SIZE))
KING_BLACK = pygame.transform.scale(KING_BLACK, (SQUARE_SIZE, SQUARE_SIZE))
QUEEN_BLACK = pygame.transform.scale(QUEEN_BLACK, (SQUARE_SIZE, SQUARE_SIZE))
BISHOP_BLACK = pygame.transform.scale(BISHOP_BLACK, (SQUARE_SIZE, SQUARE_SIZE))
KNIGHT_BLACK = pygame.transform.scale(KNIGHT_BLACK, (SQUARE_SIZE, SQUARE_SIZE))

# Inicializar
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Xadrez_busca")

# Tabuleiro inicial
tabuleiro = [
    [KING_BLACK, QUEEN_BLACK, BISHOP_BLACK, KNIGHT_BLACK, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [KING_WHITE, QUEEN_WHITE, BISHOP_WHITE, KNIGHT_WHITE, 0, 0, 0, 0]
]

turn = "white"

# Desenhar Tabuleiro
def desenhar_tabuleiro(win):
    for row in range(ROWS):
        for col in range(COLS):
            if (row + col) % 2 == 0:
                pygame.draw.rect(win, WHITE, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(win, LIGHT_GRAY, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Desenhar Peças
def desenhar_pecas(win, tabuleiro):
    for row in range(ROWS):
        for col in range(COLS):
            piece = tabuleiro[row][col]
            if piece != 0:
                win.blit(piece, (col*SQUARE_SIZE, row*SQUARE_SIZE))

def cor_peca(piece):
    if piece in [KING_WHITE, QUEEN_WHITE, BISHOP_WHITE, KNIGHT_WHITE]:
        return "white"
    elif piece in [KING_BLACK, QUEEN_BLACK, BISHOP_BLACK, KNIGHT_BLACK]:
        return "black"
    return None

# Movimentação Peças
def mover_peca(tabuleiro, pos_inicio, pos_fim):
    piece = tabuleiro[pos_inicio[0]][pos_inicio[1]]
    tabuleiro[pos_inicio[0]][pos_inicio[1]] = 0
    tabuleiro[pos_fim[0]][pos_fim[1]] = piece

# Movimentação Rei
def movimentos_rei(tabuleiro, pos_inicio):
    moves = []
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for direction in directions:
        new_pos = (pos_inicio[0] + direction[0], pos_inicio[1] + direction[1])
        if 0 <= new_pos[0] < ROWS and 0 <= new_pos[1] < COLS:
            moves.append(new_pos)
    return moves

# Movimentação Rainha
def movimentos_rainha(tabuleiro, pos_inicio):
    moves = []
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for direction in directions:
        new_pos = pos_inicio
        while True:
            new_pos = (new_pos[0] + direction[0], new_pos[1] + direction[1])
            if 0 <= new_pos[0] < ROWS and 0 <= new_pos[1] < COLS:
                moves.append(new_pos)
                if tabuleiro[new_pos[0]][new_pos[1]] != 0:
                    break
            else:
                break
    return moves

# Movimentação Bispo
def movimentos_bispo(tabuleiro, pos_inicio):
    moves = []
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for direction in directions:
        new_pos = pos_inicio
        while True:
            new_pos = (new_pos[0] + direction[0], new_pos[1] + direction[1])
            if 0 <= new_pos[0] < ROWS and 0 <= new_pos[1] < COLS:
                moves.append(new_pos)
                if tabuleiro[new_pos[0]][new_pos[1]] != 0:
                    break
            else:
                break
    return moves

# Movimentação Cavalo
def movimentos_cavalo(tabuleiro, pos_inicio):
    moves = []
    directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    for direction in directions:
        new_pos = (pos_inicio[0] + direction[0], pos_inicio[1] + direction[1])
        if 0 <= new_pos[0] < ROWS and 0 <= new_pos[1] < COLS:
            moves.append(new_pos)
    return moves

# Validação dos movimentos
def movimentos_validos(tabuleiro, pos_inicio):
    piece = tabuleiro[pos_inicio[0]][pos_inicio[1]]
    if piece == KING_WHITE or piece == KING_BLACK:
        return movimentos_rei(tabuleiro, pos_inicio)
    elif piece == QUEEN_WHITE or piece == QUEEN_BLACK:
        return movimentos_rainha(tabuleiro, pos_inicio)
    elif piece == BISHOP_WHITE or piece == BISHOP_BLACK:
        return movimentos_bispo(tabuleiro, pos_inicio)
    elif piece == KNIGHT_WHITE or piece == KNIGHT_BLACK:
        return movimentos_cavalo(tabuleiro, pos_inicio)
    return []

def movimento_valido(tabuleiro, pos_inicio, pos_fim):
    piece = tabuleiro[pos_inicio[0]][pos_inicio[1]]
    target = tabuleiro[pos_fim[0]][pos_fim[1]]
    if cor_peca(piece) == cor_peca(target):
        return False
    valid_moves = movimentos_validos(tabuleiro, pos_inicio)
    if pos_fim in valid_moves:
        return True
    return False

# Movimentação aleatória
def movimento_aleatorio(tabuleiro, cor):
    valid_moves = []

    # Percorre todas as linhas e colunas do tabuleiro
    for row in range(ROWS):
        for col in range(COLS):
            piece = tabuleiro[row][col]
            # Verifica se há uma peça na posição atual e se a cor da peça corresponde à cor dada
            if piece != 0 and cor_peca(piece) == cor:
                moves = movimentos_validos(tabuleiro, (row, col))
                for move in moves:
                    if movimento_valido(tabuleiro, (row, col), move):
                        valid_moves.append(((row, col), move))

    if valid_moves:
        # Escolhe um movimento aleatório da lista de movimentos válidos
        move = random.choice(valid_moves)
        mover_peca(tabuleiro, move[0], move[1])
        return True
    
    return False

# Função Busca em Largura
def busca_em_largura(tabuleiro, pos_inicio, pos_objetivo):
    queue = deque([pos_inicio])
    visited = set()
    parent = {pos_inicio: None}
    
    while queue:
        # Remove o primeiro nó da fila
        current = queue.popleft()
        
        # Verifica se o nó atual é o objetivo
        if current == pos_objetivo:
            path = []
            # Reconstrói o caminho do objetivo até a origem
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        if current in visited:
            continue

        visited.add(current)
        
        # Obtém todos os movimentos válidos a partir do nó atual
        valid_moves = movimentos_validos(tabuleiro, current)
        for move in valid_moves:
            if move not in visited and move not in queue:
                parent[move] = current
                queue.append(move)
    
    return None

# Função para desenhar o caminho no tabuleiro
def desenhar_caminho(win, path):
    for pos in path:
        pygame.draw.rect(win, RED, (pos[1]*SQUARE_SIZE, pos[0]*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def main():
    global turn
    clock = pygame.time.Clock()

    pos_inicio = (7, 0)  
    pos_objetivo = (0, 7)   

    path = busca_em_largura(tabuleiro, pos_inicio, pos_objetivo)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        desenhar_tabuleiro(WIN)
        desenhar_pecas(WIN, tabuleiro)
        
        if path:
            desenhar_caminho(WIN, path)
        else:
            if turn == "white":
                if movimento_aleatorio(tabuleiro, "white"):
                    turn = "black"
            else:
                if movimento_aleatorio(tabuleiro, "black"):
                    turn = "white"

        pygame.display.update()
        clock.tick(1) 

if __name__ == "__main__":
    main()