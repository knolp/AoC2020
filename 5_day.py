def get_row(inp):
    lista = [x for x in range(128)]
    for item in inp:
        if item == "F":
            lista = lista[:int(len(lista) /2)]
        else:
            lista = lista[int(len(lista) /2):]
    return lista[0]

def get_col(inp):
    lista = [0,1,2,3,4,5,6,7]
    for item in inp:
        if item == "L":
            lista = lista[:int(len(lista) / 2)]
        else:
            lista = lista[int(len(lista) / 2):]
    
    return lista[0]













if __name__ == "__main__":
    with open("input5.txt") as f:
        lista = f.readlines()

    highest = 0
    seats = []
    for idx, item in enumerate(lista):
        seat = get_row(item[0:7]) * 8 + get_col(item[7:])
        if seat > highest:
            highest = seat
        seats.append(seat)
    seats = sorted(seats)
    for i in range(6,950):
        if seats[i - 6] != i:
            print(seats[i-6])
            print(seats[i-7])
            break