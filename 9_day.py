from itertools import combinations

def find(preamble, num):
    if num in [sum(x) for x in combinations(preamble, 2)]:
        return True
    return False

def part_one():
    with open("input9.txt") as f:
        lista = [int(x) for x in f.readlines()]

    counter = 0
    while True:
        preamble = lista[counter:counter+25]
        if not find(preamble, lista[counter+25]):
            print(lista[counter+25])
            break
        counter += 1

def part_two(num):
    with open("input9.txt") as f:
        lista = [int(x) for x in f.readlines()]

    temp = 0
    for i in range(len(lista)):
        temp = lista[i]
        for j in range(1,len(lista[i:])):
            temp += lista[i+j]
            if temp == num:
                a = max(lista[i:i+j])
                b = min(lista[i:i+j])
                print(a + b)
                return
            if temp > num:
                break
            #print(i,j)



if __name__ == "__main__":
    #part_one()
    part_two(15353384)
    #part_two(127)