import random

def ler_dados(arquivo):
    """Lê os dados do arquivo de entrada e retorna um dicionário."""
    pessoas = {}
    with open(arquivo, 'r') as f:
        for linha in f:
            nome, turnos = linha.strip().split()
            pessoas[nome] = int(turnos)
    return pessoas

def alocar_turnos(pessoas):
    """Aloca as pessoas nos turnos, evitando conflitos."""
    alocacoes = {}
    for nome, num_turnos in pessoas.items():
        alocacoes[nome] = []
        for _ in range(num_turnos):
            turno = random.choice(['manhã', 'noite'])
            equipe = random.choice(['incêndio', 'socorro', 'telefone'])
            while (nome, turno, equipe) in alocacoes[nome]:  # Verifica conflito
                turno = random.choice(['manhã', 'noite'])
                equipe = random.choice(['incêndio', 'socorro', 'telefone'])
            alocacoes[nome].append((turno, equipe))
    return alocacoes

def salvar_alocacoes(alocacoes, arquivo):
    """Salva as alocacoes em um arquivo com a estrutura especificada."""
    with open(arquivo, 'w') as f:
        for equipe in ['Incêndio', 'Socorro', 'Telefone']:
            f.write(f"{equipe}\n")
            f.write("DOM  SEG  TER  QUA  QUI  SEX  SAB\n")

            # Cria um dicionário para agrupar as alocações por dia e equipe
            alocacoes_por_dia = {}
            for nome, turnos in alocacoes.items():
                for turno, equipe_atual in turnos:
                    if equipe_atual == equipe:
                        alocacoes_por_dia.setdefault(turno, []).append(nome)
                print(f"Alocações por dia para {nome}: {alocacoes_por_dia}")

            # Escreve as alocações por dia, garantindo que todos os dias sejam exibidos
            for dia in ['DOM', 'SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB']:
                nomes = alocacoes_por_dia.get(dia, [])
                # Junta os nomes com espaços e alinha à direita para melhor visualização
                linha = ' '.join(nomes).rjust(49)
                f.write(linha + '\n')

if __name__ == "__main__":
    arquivo_entrada = "entrada_1.txt"
    arquivo_saida = "saida1.txt"

    pessoas = ler_dados(arquivo_entrada)
    alocacoes = alocar_turnos(pessoas)
    salvar_alocacoes(alocacoes, arquivo_saida)