import random

def ler_entrada(caminho_arquivo):
    pessoas = []
    with open(caminho_arquivo, 'r') as f:
        for linha in f:
            nome, turnos = linha.split(',')
            pessoas.append((nome.strip(), int(turnos.strip())))
    return pessoas

def alocacao_valida(alocacao, pessoa, equipe, dia, pessoas_alocadas_no_dia):
    return (pessoa not in pessoas_alocadas_no_dia[dia] and 
            len(alocacao[equipe][dia]) < 2)

def alocar_backtracking(pessoas, equipes, alocacao, pessoas_alocadas_no_dia, index):
    if index == len(pessoas):
        return True
    
    nome, turnos = pessoas[index]
    turnos_alocados = sum(nome in dia for equipe in alocacao.values() for dia in equipe)
    
    if turnos_alocados == turnos:
        return alocar_backtracking(pessoas, equipes, alocacao, pessoas_alocadas_no_dia, index + 1)
    
    for equipe in equipes:
        for dia in range(7):
            if alocacao_valida(alocacao, nome, equipe, dia, pessoas_alocadas_no_dia):
                alocacao[equipe][dia].append(nome)
                pessoas_alocadas_no_dia[dia].add(nome)
                
                if alocar_backtracking(pessoas, equipes, alocacao, pessoas_alocadas_no_dia, index):
                    return True
                
                alocacao[equipe][dia].remove(nome)
                pessoas_alocadas_no_dia[dia].remove(nome)
    
    return False

# Utilizando o backtracking
def alocar_pessoas(pessoas, equipes):
    alocacao = {equipe: [[] for _ in range(7)] for equipe in equipes}
    pessoas_alocadas_no_dia = {dia: set() for dia in range(7)}
    
    if alocar_backtracking(pessoas, equipes, alocacao, pessoas_alocadas_no_dia, 0):
        return alocacao
    else:
        print("Não foi possível encontrar uma alocação válida.")
        return None

def salvar_alocacao(alocacao, caminho_arquivo):
    with open(caminho_arquivo, 'w') as f:
        for equipe, dias in alocacao.items():
            f.write(f'{equipe}\n')
            f.write('DOM______SEG______TER______QUA______QUI______SEX______SAB______\n')
            for turno in zip(*dias):
                f.write('_'.join([pessoa.ljust(10) for pessoa in turno]) + '\n')
            f.write('\n')

arquivo_entrada = 'C:/Users/Lucas/Desktop/Faculdade/Atividades e Livros/Inteligencia Artificial/bombeiros/entradas/entrada_37.txt'
arquivo_saida = 'C:/Users/Lucas/Desktop/Faculdade/Atividades e Livros/Inteligencia Artificial/bombeiros/entradas/saida_teste_37.txt'

equipes = ['Incêndio', 'Socorro', 'Telefone']
pessoas = ler_entrada(arquivo_entrada)
alocacao = alocar_pessoas(pessoas, equipes)

if alocacao:
    salvar_alocacao(alocacao, arquivo_saida)
    print("Alocação concluída e salva no arquivo de saída.")
else:
    print("Não foi possível gerar uma alocação válida.")