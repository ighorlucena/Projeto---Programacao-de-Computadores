import tkinter as tk
from tkinter import messagebox

# Configurações da sala
LINHAS = 10
COLUNAS = 15

class CinemaGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Reserva de Assentos - Cinema")

        self.modo = tk.StringVar(value="reservar")

        self.sala = [["O"] * COLUNAS for _ in range(LINHAS)]

        self.criar_interface()

    def criar_interface(self):
        # Título e botões de modo
        frame_top = tk.Frame(self.master)
        frame_top.pack(pady=10)

        tk.Label(frame_top, text="Modo atual:").pack(side=tk.LEFT)

        tk.Radiobutton(frame_top, text="Reservar", variable=self.modo, value="reservar").pack(side=tk.LEFT)
        tk.Radiobutton(frame_top, text="Bloquear", variable=self.modo, value="bloquear").pack(side=tk.LEFT)

        # Área dos assentos
        self.frame_sala = tk.Frame(self.master)
        self.frame_sala.pack()

        self.botoes = []
        for i in range(LINHAS):
            linha_botoes = []
            for j in range(COLUNAS):
                btn = tk.Button(self.frame_sala, text=f"{i},{j}", width=4, height=2,
                                command=lambda x=i, y=j: self.clique_assento(x, y))
                btn.grid(row=i, column=j, padx=1, pady=1)
                linha_botoes.append(btn)
            self.botoes.append(linha_botoes)

        self.atualizar_mapa()

    def clique_assento(self, i, j):
        estado = self.sala[i][j]

        if self.modo.get() == "reservar":
            if estado == "O":
                self.sala[i][j] = "X"
                messagebox.showinfo("Reserva", f"Assento {i},{j} reservado com sucesso!")
            elif estado == "X":
                messagebox.showwarning("Reservado", f"Assento {i},{j} já está reservado.")
            elif estado == "B":
                messagebox.showerror("Bloqueado", f"Assento {i},{j} está bloqueado e não pode ser reservado.")
        elif self.modo.get() == "bloquear":
            if estado == "O":
                self.sala[i][j] = "B"
                messagebox.showinfo("Bloqueado", f"Assento {i},{j} bloqueado.")
            elif estado == "X":
                messagebox.showwarning("Reservado", f"Assento {i},{j} já está reservado. Não pode ser bloqueado.")
            elif estado == "B":
                messagebox.showinfo("Bloqueado", f"Assento {i},{j} já está bloqueado.")

        self.atualizar_mapa()

    def atualizar_mapa(self):
        for i in range(LINHAS):
            for j in range(COLUNAS):
                estado = self.sala[i][j]
                btn = self.botoes[i][j]
                if estado == "O":
                    btn.config(bg="green", state=tk.NORMAL)
                elif estado == "X":
                    btn.config(bg="red", state=tk.DISABLED)
                elif estado == "B":
                    btn.config(bg="gray", state=tk.DISABLED)

# Execução
if __name__ == "__main__":
    root = tk.Tk()
    app = CinemaGUI(root)
    root.mainloop()

