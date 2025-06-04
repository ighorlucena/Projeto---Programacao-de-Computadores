sala = [["0" for _ in range(15)] for _ in range(10)]

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
    coluna_idx = int(coluna) - 1

    if not coordenadas_validas(linha_idx, coluna_idx):
        print("Coordenadas fora dos limites da sala.")
        return
    
    estado = sala[linha_idx][coluna_idx]

    if estado == "0":
        sala[linha_idx][coluna_idx] = "X"
        print("Reserva realizada com sucesso.")
    elif estado == "X":
        print("A cadeira já está ocupada.")
    elif estado == "B":
        print("A cadeira está bloqueada e não pode ser reservada.")
        