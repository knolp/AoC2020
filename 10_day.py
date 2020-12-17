def part_one(lista):
    lista = sorted(lista)
    _dict = {
        1 : 0,
        2 : 0,
        3 : 0
    }
    lista.insert(0, 0)
    lista.append(lista[-1] + 3)

    for i in range(len(lista) - 1):
        _dict[lista[i+1] - lista[i]] += 1

    print(_dict)
    print(_dict[1] * _dict[3])




def find_3_jumps(lista):
    ret_lista = []
    for i in range(len(lista) - 1):
        if lista[i+1] - lista[i] == 3:
            ret_lista.append(lista[i+1])

    return ret_lista


def part_two(lista):
    lista.insert(0, 0)
    lista.append(lista[-1] + 3)
    permanent = find_3_jumps(lista)
    print(permanent)
    new = []
    for i in range(len(permanent)):
        if i == 0:
            new.append(lista[0:lista.index(permanent[i])])
        else:
            new.append(lista[lista.index(permanent[i-1]):lista.index(permanent[i])])
    _dict = {
        1 : 1,
        2 : 2,
        3 : 4,
        4 : 7,
        5 : 13
    }
    prod = 1
    for item in new:
        if len(item) == 1:
            continue
        prod *= _dict[len(item) - 1]
    print(prod)





if __name__ == "__main__":
    with open("input10.txt") as f:
        lista = sorted([int(x) for x in f.readlines()])

    #part_one(lista)
    part_two(lista)


