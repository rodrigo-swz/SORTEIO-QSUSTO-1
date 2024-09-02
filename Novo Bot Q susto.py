import random
import tkinter as tk
from tkinter import messagebox, simpledialog

# Lista de campeões
campeoes = ["Aatrox", "Ahri", "Akali", "Akshan", "Alistar",
            "Amumu", "Anivia", "Annie", "Aphelios", "Ashe",
            "Aurelion Sol", "Aurora", "Azir", "Bardo", "Bel’Veth", "Blitzcrank",
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
            "Zilean", "Zoe", "Zyra"]

def sortear_campeoes(nomes, campeoes, opcoes_campeoes):
    sorteio = {}
    campeoes_disponiveis = campeoes.copy()
    
    for nome in nomes:
        if len(campeoes_disponiveis) < opcoes_campeoes:
            messagebox.showinfo("Atenção", f"Não há campeões suficientes para sortear para {nome}")
            sorteio[nome] = random.sample(campeoes_disponiveis, len(campeoes_disponiveis))
            continue

        sorteio[nome] = random.sample(campeoes_disponiveis, opcoes_campeoes)
        for campeao in sorteio[nome]:
            campeoes_disponiveis.remove(campeao)
    
    return sorteio

def resultado(sorteio):
    time_a = "Time A:\n"
    time_b = "Time B:\n"
    
    for i, (nome, campeoes) in enumerate(sorteio.items()):
        if i < len(sorteio)//2:
            time_a += f"{nome}: {', '.join(campeoes)}\n"
        else:
            time_b += f"{nome}: {', '.join(campeoes)}\n"
    
    return f"{time_a}\n{time_b}"

def iniciar_sorteio():
    global sorteio, nomes, opcoes_campeoes
    nomes_input = simpledialog.askstring("Nomes", "Digite os nomes dos jogadores (separados por vírgula):")
    opcoes_campeoes = simpledialog.askinteger("Campeões", "Digite a quantidade de opções de campeões por jogador:")
    
    if nomes_input and opcoes_campeoes:
        nomes = [nome.strip() for nome in nomes_input.split(',')]
        random.shuffle(nomes)
        sorteio = sortear_campeoes(nomes, campeoes, opcoes_campeoes)
        exibir_resultado()

def exibir_resultado():
    global sorteio
    resultado_texto = resultado(sorteio)
    resultado_box.delete(1.0, tk.END)
    resultado_box.insert(tk.END, resultado_texto)

def refazer_sorteio_mesmos_times():
    global sorteio
    if 'nomes' in globals() and 'opcoes_campeoes' in globals():
        sorteio = sortear_campeoes(nomes, campeoes, opcoes_campeoes)
        exibir_resultado()
    else:
        messagebox.showinfo("Erro", "Por favor, inicie um sorteio primeiro.")

def refazer_sorteio_novos_times():
    global sorteio
    if 'nomes' in globals() and 'opcoes_campeoes' in globals():
        random.shuffle(nomes)
        sorteio = sortear_campeoes(nomes, campeoes, opcoes_campeoes)
        exibir_resultado()
    else:
        messagebox.showinfo("Erro", "Por favor, inicie um sorteio primeiro.")

def copiar_resultado():
    root.clipboard_clear()
    root.clipboard_append(resultado_box.get(1.0, tk.END))
    messagebox.showinfo("Copiado", "Resultado copiado para a área de transferência.")

# Configurar a interface gráfica
root = tk.Tk()
root.title("Sorteio de Campeões")
root.geometry("400x400")

btn_iniciar = tk.Button(root, text="Iniciar Sorteio", command=iniciar_sorteio)
btn_iniciar.pack(pady=10)

btn_refazer_mesmos_times = tk.Button(root, text="Refazer Sorteio (Mesmos Times)", command=refazer_sorteio_mesmos_times)
btn_refazer_mesmos_times.pack(pady=10)

btn_refazer_novos_times = tk.Button(root, text="Refazer Sorteio (Novos Times)", command=refazer_sorteio_novos_times)
btn_refazer_novos_times.pack(pady=10)

btn_copiar = tk.Button(root, text="Copiar Resultado", command=copiar_resultado)
btn_copiar.pack(pady=10)

resultado_box = tk.Text(root, wrap=tk.WORD, height=15)
resultado_box.pack(pady=10, padx=10)

root.mainloop()