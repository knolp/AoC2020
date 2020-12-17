import copy

def check(lista,x,y):
    ret = 0
    for a,b in [(1,1), (-1,-1), (1,0), (-1,0), (0,1), (0,-1), (-1, 1), (1, -1)]:
        for i in range(1,len(lista)):
            if not 0 <= x+(a*i) <= len(lista) - 1 or not 0 <= y+(b*i) <= len(lista[0]) - 1:
                break
            if lista[x+(a*i)][y+(b*i)] == "L":
                break
            if lista[x+(a*i)][y+(b*i)] == "#":
                ret += 1
                break
    return ret


def is_same(kopia, lista):
    kopia = "".join([item for sublist in kopia for item in sublist])
    lista = "".join([item for sublist in lista for item in sublist])
    return kopia == lista

def part_one(lista):
    while True:
        kopia = copy.deepcopy(lista)
        for x in range(len(lista)):
            for y in range(len(lista[0])):
                if lista[x][y] == "L":
                    count = check(lista, x, y)
                    if count == 0:
                        kopia[x][y] = "#"
                if lista[x][y] == "#":
                    count = check(lista, x, y)
                    if count >= 5:
                        kopia[x][y] = "L"
        if is_same(kopia, lista):
            break
        lista = copy.deepcopy(kopia)

    print("".join([item for sublist in lista for item in sublist]).count("#"))


















if __name__ == "__main__":
    with open("input11.txt") as f:
        lista = [list(x.rstrip()) for x in f.readlines()]

        part_one(lista)