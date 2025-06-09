sala = [["O" for _ in range(15)] for _ in range(10)]

def linha_para_indice(letra):
    letra = letra.strip().upper()
    if letra in "ABCDEFGHIJ":
        return ord(letra) - ord("A")
    return -1

def coordenadas_validas(linha_idx, coluna_idx):
    return 0 <= linha_idx < 10 and 0 <= coluna_idx < 15
1
def mostrar_sala():
    print("\n Mapa da Sala de Cinema\n")
    print("Legenda: O = Livre, X = Ocupada, B = Bloqueada\n")

    print("    " + " ".join(f"{i:02}" for i in range(1, 16)))

    for i, linha in enumerate(sala):
        letra_linha = chr(ord("A") + i)
        print(f"{letra_linha} | " + " ".join(linha))
        
    print("")

def menu():
    print("\n--- MENU ---")
    print("1. Ver sala")
    print("2. Reservar assento")
    print("3. Cancelar reserva")
    print("4. Bloquear assento")
    print("5. Desbloquear assento")
    print("6. Ver ocupação")
    print("7. Sair")
    return input("Escolha: ")

def reservar_cadeira():
    linha = input("Digite a letra da Linha (A-J): ").strip().upper()
    coluna = input("Digite o número da coluna (1-15): ").strip()

    if not coluna.isdigit():
        print("Coluna inválida. Digite apenas números de 1 a 15.")
        return
    
    linha_idx = linha_para_indice(linha)
    if linha_idx == -1:
        print("Linha inválida. Digite uma letra de A a J.")
        return
    coluna_idx = int(coluna) - 1

    if not coordenadas_validas(linha_idx, coluna_idx):
        print("Coordenadas fora dos limites da sala.")
        return
    
    estado = sala[linha_idx][coluna_idx]

    if estado == "O":
        sala[linha_idx][coluna_idx] = "X"
        print("Reserva realizada com sucesso.")
    elif estado == "X":
        print("A cadeira já está ocupada.")
    elif estado == "B":
        print("A cadeira está bloqueada e não pode ser reservada.")

def cancelar_reserva():
    linha = input("Digite a letra da linha (A-J): ").strip().upper()
    coluna = input("Digite o número da coluna (1-15): ").strip()

    if not coluna.isdigit():
        print("Coluna inválida. Digite apenas números de 1 a 15.")
        return
    
    linha_idx = linha_para_indice(linha)
    if linha_idx == -1:
        print("Linha inválida. Digite uma letra de A a J.")
        return
    coluna_idx = int(coluna) - 1

    if not coordenadas_validas(linha_idx, coluna_idx):
        print("Coordenadas fora dos limites da sala.")
        return
    
    estado = sala[linha_idx][coluna_idx]

    if estado == "X":
        sala[linha_idx][coluna_idx] = "O"
        print("Reserva cancelada com sucesso.")
    elif estado == "O":
        print("A cadeira já está livre")
    elif estado == "B":
        print("A cadeira está bloqueada e não pode ser alterada.")

def ver_ocupacao():
    livres = 0
    ocupadas = 0
    bloqueadas = 0 

    for linha in sala: 
        for cadeira in linha:
            if cadeira == "O":
                livres += 1
            elif cadeira == "X":
                ocupadas += 1
            elif cadeira == "B":
                bloqueadas += 1

    total = livres + ocupadas + bloqueadas 

    print("\n status atual da sala:")
    print(f"Total de Cadeiras:   {total}")
    print(f" - Livres:           {livres}")
    print(f" - Ocupadas:         {ocupadas}")
    print(f" - Bloqueadas:       {bloqueadas}\n")

def bloquear_cadeira():
    linha = input("Digite a letra da linha (A-J): ").strip().upper()
    coluna = input("Digite o número da coluna (1-15): ").strip()

    if not coluna.isdigit():
        print("Coluna inválida. Digite apenas números de 1 a 15.")
        return
    
    linha_idx = linha_para_indice(linha)
    if linha_idx == -1:
        print("Linha inválida. Digite uma letra de A a J.")
        return
    coluna_idx = int(coluna) - 1

    if not coordenadas_validas(linha_idx, coluna_idx):
        print("Coordenadas fora dos limites da sala.")
        return
    
    estado = sala[linha_idx][coluna_idx]

    if estado == "O":
        sala[linha_idx][coluna_idx] = "B"
        print("Cadeira Bloqueada com Sucesso.")
    elif estado == "X":
        print("A cadeira está ocupada. Cancele antes de bloquear.")
    elif estado == "B":
        print("A cadeira já está bloqueada.")

def desbloquear_cadeira():
    linha = input("Digite a letra da linha (A-J): ").strip().upper()
    coluna = input("Digite o número da coluna (1-15): ").strip()
    
    if not coluna.isdigit():
        print("Coluna inválida. Digite apenas números de 1 a 15")
        return
    
    linha_idx = linha_para_indice(linha)
    if linha_idx == -1:
        print("Linha inválida. Digite uma letra de A a J.")
        return
    coluna_idx = int(coluna) - 1

    if not coordenadas_validas(linha_idx, coluna_idx):
        print("Coordenadas fora dos limites da sala.")
        return
    
    estado = sala[linha_idx][coluna_idx]
    
    if estado == "B":
        sala[linha_idx][coluna_idx] = "O"
        print("Cadeira desbloqueada com sucesso.")
    elif estado == "O":
        print("A cadeira já está livre.")
    elif estado == "X":
        print("A cadeira está ocupada e não está bloqueada.")

def main():
    while True:
        opcao = menu()
        if opcao == "1":
            mostrar_sala()
        elif opcao == "2":
            reservar_cadeira()
        elif opcao == "3":
            cancelar_reserva()
        elif opcao == "4":
            bloquear_cadeira()
        elif opcao == "5":
            desbloquear_cadeira()
        elif opcao == "6":
            ver_ocupacao()
        elif opcao == "7":
            print("Tchau!")
            break
        else:
            print("Opção inválida.")

import tkinter as tk
from tkinter import messagebox

LINHAS = 10
COLUNAS = 15

class CinemaGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Reserva de Assentos - Cinema")

        self.modo = tk.StringVar(value="reservar")

        self.criar_interface()

    def criar_interface(self):
        frame_top = tk.Frame(self.master)
        frame_top.pack(pady=10)

        tk.Label(frame_top, text="Modo atual:").pack(side=tk.LEFT, padx=5)

        modos = [("Reservar", "reservar"), ("Cancelar Reserva", "cancelar"),
                 ("Bloquear", "bloquear"), ("Desbloquear", "desbloquear")]

        for texto, valor in modos:
            tk.Radiobutton(frame_top, text=texto, variable=self.modo, value=valor).pack(side=tk.LEFT, padx=5)

        self.frame_sala = tk.Frame(self.master)
        self.frame_sala.pack()

        self.botoes = []
        for i in range(LINHAS):
            linha_botoes = []
            for j in range(COLUNAS):
                label = f"{chr(ord('A') + i)}{j+1}"
                btn = tk.Button(self.frame_sala, text=label, width=4, height=2,
                                font=("Arial", 10),
                                command=lambda x=i, y=j: self.clique_assento(x, y))
                btn.grid(row=i, column=j, padx=1, pady=1)
                linha_botoes.append(btn)
            self.botoes.append(linha_botoes)

        frame_legenda = tk.Frame(self.master)
        frame_legenda.pack(pady=10)

        tk.Label(frame_legenda, text="Legenda:").pack()
        tk.Label(
            frame_legenda,
            text="Verde = Livre   Vermelho = Ocupado   Cinza = Bloqueado",
            font=("Arial", 10)
        ).pack()

        self.atualizar_mapa()

    def clique_assento(self, i, j):
        estado = sala[i][j]
        posicao = f"{chr(ord('A') + i)}{j+1}"
        modo = self.modo.get()

        if modo == "reservar":
            if estado == "O":
                sala[i][j] = "X"
                messagebox.showinfo("Reserva", f"Assento {posicao} reservado com sucesso!")
            elif estado == "X":
                messagebox.showwarning("Reservado", f"Assento {posicao} já está reservado.")
            elif estado == "B":
                messagebox.showerror("Bloqueado", f"Assento {posicao} está bloqueado e não pode ser reservado.")

        elif modo == "cancelar":
            if estado == "X":
                sala[i][j] = "O"
                messagebox.showinfo("Cancelado", f"Reserva do assento {posicao} cancelada.")
            elif estado == "O":
                messagebox.showwarning("Livre", f"Assento {posicao} já está livre.")
            elif estado == "B":
                messagebox.showerror("Bloqueado", f"Assento {posicao} está bloqueado e não pode ser alterado.")

        elif modo == "bloquear":
            if estado == "O":
                sala[i][j] = "B"
                messagebox.showinfo("Bloqueado", f"Assento {posicao} bloqueado com sucesso.")
            elif estado == "X":
                messagebox.showwarning("Reservado", f"Assento {posicao} está ocupado. Cancele antes de bloquear.")
            elif estado == "B":
                messagebox.showinfo("Bloqueado", f"Assento {posicao} já está bloqueado.")

        elif modo == "desbloquear":
            if estado == "B":
                sala[i][j] = "O"
                messagebox.showinfo("Desbloqueado", f"Assento {posicao} desbloqueado com sucesso.")
            elif estado == "O":
                messagebox.showinfo("Livre", f"Assento {posicao} já está livre.")
            elif estado == "X":
                messagebox.showwarning("Ocupado", f"Assento {posicao} está ocupado e não pode ser desbloqueado.")

        self.atualizar_mapa()

    def atualizar_mapa(self):
        for i in range(LINHAS):
            for j in range(COLUNAS):
                estado = sala[i][j]
                btn = self.botoes[i][j]
                if estado == "O":
                    btn.config(bg="green", state=tk.NORMAL)
                elif estado == "X":
                    btn.config(bg="red", state=tk.NORMAL)
                elif estado == "B":
                    btn.config(bg="gray", state=tk.NORMAL)

if __name__ == "__main__":
    modo = input("Escolha o modo (1 = Terminal, 2 = Interface): ").strip()
    if modo == "1":
        main()
    else:
        root = tk.Tk()
        app = CinemaGUI(root)
        root.mainloop()