import time

def find_last(lista, n):
    #print(lista[::-1])
    #print(f"Found {n} at pos {(len(lista) - lista[::-1].index(n))}")
    return len(lista) - lista[::-1].index(n)

def part_one(lista):
    counter = len(lista)
    try:
        while True:
            if lista.count(lista[-1]) == 1:
                lista.append(0)
            else:
                last_time = find_last(lista[:-1], lista[-1])
                lista.append(counter - last_time)

            counter += 1
            if counter == 30000000:
                print(lista[-1])
                break
    except KeyboardInterrupt:
        print(counter)
        return


def part_two(lista):
    _dict = {}
    for item in lista:
        _dict[item] = [lista.index(item) + 1, False]
    last = lista[-1]

    counter = len(lista)
    while True:
        temp = 0
        #print(f"last = {last} counter = {counter}")
        counter += 1

        #3 options:
        #   _dict = { N : [last, previous] }
        #   1: It is not in dict, so make it a part of the dict
        #   2: Only seen once, new number = 0
        #   3: Seen twice, new number = counter - last
        try:
            if last in _dict.keys():
                if _dict[last][1] == False:
                    last = 0
                    if last not in _dict.keys():
                        _dict[last] = [counter, False]
                    else:
                        _dict[last] = [counter, _dict[last][0]]
                else:
                    last = _dict[last][0] - _dict[last][1]
                    if last not in _dict.keys():
                        _dict[last] = [counter, False]
                    else:
                        _dict[last] = [counter, _dict[last][0]]
            if counter == 20000000:
                print("Soon there")
            if counter == 30000000:
                print(last)
                break
        except KeyboardInterrupt:
            print(counter)
            break

        
    



















if __name__ == "__main__":
    lista = [5,2,8,16,18,0,1]
    #lista = [0,3,6]
    part_two(lista)