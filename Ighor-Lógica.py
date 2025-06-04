sala = [["0" for _ in range(15)] for _ in range(10)]

def linha_para_indice(letra):
    letra = letra.upper()
    if letra in "ABCDEFGHIJ":
        return ord(letra) - ord("A")
    else:
        return -1
    
def reservar_cadeira():
    linha = input("Digite a letra da Linha (A-J): ").upper()
    coluna = input("Digite o número da coluna (1-15): ")

    if not coluna.isdigit():
        print("Coluna inválida")
        return
    
    linha_idx = linha_para_indice(linha)
    coluna_idx = int(coluna) - 1

    if linha_idx == -1 or not (0 <= coluna_idx < 15):
        print("Coordenadas fora dos limites.")
        return 
    
    if sala[linha_idx][coluna_idx] == "0":
        sala[linha_idx][coluna_idx] = "X"
        print("Reserva realizada com sucesso.")
    elif sala[linha_idx][coluna_idx] == "X":
        print("Cadeira já está ocupada.")
    elif sala[linha_idx][coluna_idx] == "B":
        print("Cadeira está bloqueada.")
 
