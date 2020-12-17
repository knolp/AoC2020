from itertools import permutations

def find():
    with open("input1.txt") as f:
        lista = [int(x) for x in f.readlines()]
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if lista[i] + lista[j] == 2020:
                print(lista[i] * lista[j])
                return


def find2():
    with open("input1.txt") as f:
       lista = [int(x) for x in f.readlines()]
    
    perms = list(permutations(lista, 3))
    sums = [x + y + z for x,y,z in perms]

    if 2020 in sums:
        nummer = sums.index(2020)
        print(perms[nummer][0] * perms[nummer][1] * perms[nummer][2])


if __name__ == "__main__":
    find2()
