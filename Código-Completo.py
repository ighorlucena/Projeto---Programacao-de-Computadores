sala = [["O" for _ in range(15)] for _ in range(10)]

def linha_para_indice(letra):
    return ord(letra.upper()) - ord("A")

def coordenadas_validas(linha, coluna):
    return 0 <= linha < 10 and 0 <= coluna < 15

def mostrar_sala():
    print("\nMapa da Sala:")
    print("   " + " ".join([str(i+1).rjust(2) for i in range(15)]))
    for i, linha in enumerate(sala):
        letra = chr(ord("A") + i)
        print(letra + "  " + " ".join(linha))

def menu():
    print("\n1. Ver sala")
    print("2. Reservar assento")
    print("3. Sair")
    return input("Escolha: ")

def main():
    while True:
        opcao = menu()
        if opcao == "1":
            mostrar_sala()
        elif opcao == "2":
            mostrar_sala()
            l = input("Digite a letra da linha (A-J): ").strip().upper()
            c = input("Digite o número da coluna (1-15): ").strip()
            
            if not c.isdigit():
                print("Coluna inválida.")
                continue

            linha_idx = linha_para_indice(l)
            coluna_idx = int(c) - 1

            if coordenadas_validas(linha_idx, coluna_idx):
                if sala[linha_idx][coluna_idx] == "O":
                    sala[linha_idx][coluna_idx] = "X"
                    print("Assento reservado!")
                else:
                    print("Assento ocupado.")
            else:
                print("Coordenadas inválidas.")
        elif opcao == "3":
            print("Tchau!")
            break
        else:
            print("Opção inválida.")

main()

sala = [["O" for _ in range(15)] for _ in range(10)]

def linha_para_indice(letra):
    letra = letra.strip().upper()
    if letra in "ABCDEFGHIJ":
        return ord(letra) - ord("A")
    return -1

def coordenadas_validas(linha_idx, coluna_idx):
    return 0 <= linha_idx < 10 and 0 <= coluna_idx < 15

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