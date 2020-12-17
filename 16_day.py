import time

def check(valid, values):
    for item in values:
        if item not in valid:
            return False
    return True

def part_one(fields, nearby, mine):
    lista = []
    for k,v in fields.items():
        lista = lista + v
    lista = set(lista)
    new = [x for x in nearby if check(lista, x)]
    rotated = list(zip(*new[::-1]))
    #assert len(rotated) == 20
    valids = {}
    for k in fields.keys():
        valids[k] = []
    for k,v in fields.items():
        for i in range(len(rotated)):
            if check(v, rotated[i]):
                valids[k].append(i)

    done = []
    result = {}
    completed = False
    while not completed:
        to_pop = []
        #Check if one is len 1
        for k,v in valids.items():
            if len(v) == 1:
                done.append(v[0])
                to_pop.append(k)
                if k.startswith("departure"):
                    result[k] = v[0]
        #Remove all with that number
        for k,v in valids.items():
            for number in done:
                if number in v:
                    valids[k].remove(number)
        
        for item in to_pop:
            valids.pop(item)

        to_pop = []

        if not len(valids.keys()):
            completed = True

    print(result)

    summa = 1
    for k,v in result.items():
        summa *= mine[v]

    print(summa)



if __name__ == "__main__":
    #Parse
    with open("input16.txt") as f:
        fields, mine, nearby = [x for x in f.read().split("\n\n")]
        
    #Parse Fields
    fields_dict = {}
    fields = [x.rstrip() for x in fields.split("\n")]
    for item in fields:
        name, values = item.split(": ")
        first, second = values.split(" or ")
        first = list(range(int(first.split("-")[0]), int(first.split("-")[1]) + 1))
        second = list(range(int(second.split("-")[0]), int(second.split("-")[1]) + 1))
        
        fields_dict[name] = first + second

    #Parse Mine
    mine = [int(x) for x in mine.split("\n")[-1].split(",")]
    

    #Parse Nearby
    nearby = nearby.split("\n")[1:]
    nearby = [[int(x) for x in y.split(",")] for y in nearby]
    
    part_one(fields_dict, nearby, mine)
    
