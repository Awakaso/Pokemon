
# Solicita introdução de movimentos até ser fornecida informação por stdin
print("Onde N, S, E e O, correspondem respetivamente a Norte, Sul, Este, Oeste...")
movimentos_input = input("Indique os movimentos do Ash numa sequência de letras: ")

# Inicialização de varáveis
x = 0
y = 0
pokemons = 1  # pokemon = 1 -> pokemon da casa inicial apanhado
casas = [(0, 0)]  # casa visitada na posição inicial
visita = (x, y)  # posição da casa a visitar

# Validar direcção do movimento
for move in movimentos_input:
    visitado = False
    match move:
        case 'N':
            x += 1
            visita = (x, y)
        case 'S':
            x -= 1
            visita = (x, y)
        case 'E':
            y += 1
            visita = (x, y)
        case 'O':
            y -= 1
            visita = (x, y)
        case _:
            # Introdução de qualquer outro caracter que não seja N, S, E, O fecha o programa
            print("Movimento incorrecto")
            exit()

    # Validar se a nova casa já foi visitada
    for valor in casas:
        if visita == valor:
            visitado = True

    # Se ainda não foi visitada, adiciona ao array e incrementa o número de pokemons apanhados
    if not visitado:
        casas.append(visita)
        pokemons += 1

# print(*saco, sep='\n')
print("Ash apanhou " + str(pokemons) + " pokemon(s) na sua viagem.")
