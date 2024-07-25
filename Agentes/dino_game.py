import pygame
import random

# Inicializando o Pygame
pygame.init()

# Dimensões da tela
screen_width = 800
screen_height = 400

# Configurando a tela
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Jogo do Dinossauro')

# Cores
white = (255, 255, 255)
black = (0, 0, 0)

# Carregando imagens
dino_image = pygame.image.load('dino.png')
cactus_image = pygame.image.load('cactus.png')

# Redimensionando imagens
dino_image = pygame.transform.scale(dino_image, (60, 80))
cactus_image = pygame.transform.scale(cactus_image, (20, 60))

# Variáveis do dinossauro
dino_width = 60
dino_height = 80
dino_x = 50
dino_y = screen_height - dino_height
dino_y_velocity = 0
jump_height = -15

# Variáveis dos cactos
cactus_width = 20
cactus_height = 60
cactus_x = screen_width
cactus_y = screen_height - cactus_height
cactus_speed = 10

# Relógio do jogo
clock = pygame.time.Clock()
fps = 30

# Pontuação
score = 0

# Fonte
font = pygame.font.Font(None, 36)

# Funções dos agentes
def reactive_agent_simple(dino_x, dino_y, cactus_x):
    if cactus_x - dino_x < 150:
        return True  # Pular
    return False

def reactive_agent_model_based(dino_x, dino_y, cactus_x, state):
    if state["cactus_close"]:
        return True  # Pular
    if cactus_x - dino_x < 150:
        state["cactus_close"] = True
    else:
        state["cactus_close"] = False
    return False

def game_loop(agent_type):
    global dino_y, dino_y_velocity, cactus_x, score

    game_exit = False
    game_over = False
    state = {"cactus_close": False}

    while not game_exit:
        while game_over:
            screen.fill(white)
            game_over_text = font.render(f'Game Over! Score: {score}', True, black)
            screen.blit(game_over_text, [screen_width // 4, screen_height // 2])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_loop(agent_type)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        # Atualizando a posição do dinossauro
        if agent_type == "simple":
            if reactive_agent_simple(dino_x, dino_y, cactus_x):
                dino_y_velocity = jump_height
        elif agent_type == "model":
            if reactive_agent_model_based(dino_x, dino_y, cactus_x, state):
                dino_y_velocity = jump_height

        dino_y += dino_y_velocity
        if dino_y < screen_height - dino_height:
            dino_y_velocity += 1
        else:
            dino_y = screen_height - dino_height
            dino_y_velocity = 0

        # Atualizando a posição do cacto
        cactus_x -= cactus_speed
        if cactus_x < -cactus_width:
            cactus_x = screen_width
            score += 1

        # Verificando colisão
        if dino_x + dino_width > cactus_x and dino_x < cactus_x + cactus_width:
            if dino_y + dino_height > cactus_y:
                game_over = True

        # Desenhando na tela
        screen.fill(white)
        screen.blit(dino_image, (dino_x, dino_y))
        screen.blit(cactus_image, (cactus_x, cactus_y))

        # Desenhando a pontuação
        score_text = font.render(f'Score: {score}', True, black)
        screen.blit(score_text, [10, 10])

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()

# Escolha o tipo de agente aqui ("simple" para agente reativo simples, "model" para agente reativo baseado em modelos)
game_loop(agent_type="simple")
# game_loop(agent_type="model")