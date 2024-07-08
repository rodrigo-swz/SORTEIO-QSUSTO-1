import random

# Lista de campeões
campeoes = ["Aatrox", "Ahri", "Akali", "Akshan", "Alistar",
            "Amumu", "Anivia", "Annie", "Aphelios", "Ashe",
            "Aurelion Sol", "Azir", "Bardo", "Bel’Veth", "Blitzcrank",
            "Brand", "Braum", "Briar", "Caitlyn", "Camille", "Cassiopeia",
            "Cho’Gath", "Corki", "Darius", "Diana", "Draven",
            "Dr. Mundo", "Ekko", "Elise", "Evelynn", "Ezreal",
            "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank",
            "Garen", "Gnar", "Gragas", "Graves", "Gwen",
            "Hecarim", "Heimerdinger", "Hwei", "Illaoi", "Irelia", "Ivern",
            "Janna", "Jarvan IV", "Jax", "Jayce", "Jhin",
            "Jinx", "Kai’Sa", "Kalista", "Karma", "Karthus",
            "Kassadin", "K’sante", "Katarina", "Kayle", "Kayn",
            "Kennen", "Kha’Zix", "Kindred", "Kled", "Kog’Maw",
            "LeBlanc", "Lee Sin", "Leona", "Lillia", "Lissandra",
            "Lucian", "Lulu", "Lux", "Malphite", "Malzahar",
            "Maokai", "Master Yi", "Milio", "Miss Fortune", "Mordekaiser",
            "Morgana", "Naafiri", "Nami", "Nasus", "Nautilus", "Neeko",
            "Nidalee", "Nilah", "Nocturne", "Nunu e Willump", "Olaf",
            "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke",
            "Qiyana", "Quinn", "Rakan", "Rammus", "Rek’Sai",
            "Rell", "Renata Glasc", "Renekton", "Rengar", "Riven",
            "Rumble", "Ryze", "Samira", "Sejuani", "Senna",
            "Seraphine", "Sett", "Shaco", "Shen", "Shyvana",
            "Singed", "Sion", "Sivir", "Skaner", "Smolder", "Sona",
            "Soraka", "Swain", "Sylas", "Syndra", "Tahm Kench",
            "Taliyah", "Talon", "Taric", "Teemo", "Thresh",
            "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch",
            "Udyr", "Urgot", "Varus", "Vayne", "Veigar",
            "Vel’Koz", "Vex", "Vi", "Viego", "Viktor",
            "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah",
            "Xerath", "Xin Zhao", "Yasuo", "Yone", "Yorick",
            "Yuumi", "Zac", "Zed", "Zeri", "Ziggs",
            "Zilean", "Zoe", "Zyra",
]

# Solicitar entrada do usuário para a quantidade de jogadores e opções de campeões por jogador
def ler_nomes():
    entrada = input("Digite os nomes dos jogadores: ")
    opcoes_campeoes = int(input("Digite a quantidade de opções de campeões por jogador: "))
    nomes = [nome.strip() for nome in entrada.replace(',', ' ',).split()]
    num_jogadores = len(nomes)

    return nomes, num_jogadores, opcoes_campeoes

# Sortear os campeões para cada jogador
def sortear_campeoes(nomes, campeoes, opcoes_campeoes):
    sorteio = {}
    # cria cópia da lista de campeões para não remover em definitivo
    campeoes_disponiveis = campeoes.copy()
    
    for nome in nomes:
        # Verificar se há campeões suficientes para sortear
        if len(campeoes_disponiveis) < opcoes_campeoes:
            print(f"Atenção: Não há campeões suficientes para sortear para {nome}")
            sorteio[nome] = random.sample(campeoes_disponiveis, len(campeoes_disponiveis))
            continue

        # Sortear campeoes
        sorteio[nome] = random.sample(campeoes_disponiveis, opcoes_campeoes)
        
        # Remover os campeoes sorteados da lista de campeões
        for campeao in sorteio[nome]:
            campeoes_disponiveis.remove(campeao)
    return sorteio

# Mostrar o resultado
def resultado(sorteio):
    print(f"Time A:")
    for i, (nome, campeoes) in enumerate(sorteio.items()):
        if i < len(sorteio)//2:
            print(f"{nome}: {campeoes}")

    print(f"Time B:")
    for i, (nome, campeoes) in enumerate(sorteio.items()):
        if i >= len(sorteio)//2:
            print(f"{nome}: {campeoes}")


# Chamada da função de ler nomes
nomes, num_jogadores, opcoes_campeoes = ler_nomes()

# Embaralha os nomes para definição dos times
random.shuffle(nomes)

# Chamada da função de sortear os campeões para cada jogador
sorteio = sortear_campeoes(nomes, campeoes, opcoes_campeoes)

# Chamada da função para exibição do resultado
resultado(sorteio)


# Solicitar ao usuário se deseja realizar um novo sorteio das opções de campeões
novo_sorteio = input("\nDeseja realizar um novo sorteio das opções de campeões? (s/n): ")

# Loop para sortear até o usuário digitar não
while(novo_sorteio.lower() != 'n'):

    # Realizar um novo sorteio das opções de campeões
    sorteio = sortear_campeoes(nomes, campeoes, opcoes_campeoes)

    # Imprimir os resultados do segundo sorteio
    resultado(sorteio)
    novo_sorteio = input("\nDeseja realizar um novo sorteio das opções de campeões? (s/n): ")

# Fim do sorteio
print(f"Fim de jogo! Proibido tilt!")

















