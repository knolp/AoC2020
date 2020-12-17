import itertools
from datetime import datetime

def get_neighbours(cube, dim):
    neighbours = [p for p in itertools.product([-1,0,1], repeat=dim)]
    if dim == 4:
        w,z,x,y = cube
        neighbours = [(w + ww, z + zz, x + xx, y + yy) for ww,zz,xx,yy in neighbours]
    elif dim == 3:
        z,x,y = cube
        neighbours = [(z + zz, x + xx, y + yy) for zz,xx,yy in neighbours]
    return neighbours

def find(lista, dim):
    #create dict of lista
    cubes = {}
    for i in range(len(lista)):
        for j in range(len(lista[0])):
            if lista[i][j]:
                if dim == 4:
                    cubes[(0,0,i,j)] = True
                elif dim == 3:
                    cubes[(0,i,j)] = True

    for i in range(6):
        #Set current neighbours to empty
        neighbours = {}

        #For each active cube, get the neighbours and add it do dict, if is already in dict, +1
        for k in cubes.keys():
            for item in get_neighbours(k, dim):
                if item not in neighbours.keys():
                    neighbours[item] = 1
                else:
                    neighbours[item] += 1

        # For seen neighbours, we check how many times it was seen and disable / enable it accordingly
        for k,v in neighbours.items():
            if k in cubes.keys():
                if v not in [3,4]:
                    cubes.pop(k)
            else:
                if v == 3:
                    cubes[k] = True
    return len(cubes.keys())


if __name__ == "__main__":
    with open("input17.txt") as f:
        lista = [x.rstrip() for x in f.readlines()]
    d = {"#" : True,"." : False}
    lista = [[d[symbol] for symbol in row] for row in lista]
    start_time = datetime.now()
    print(f"Part 1: {find(lista,3)} in {datetime.now() - start_time}")
    start_time = datetime.now()
    print(f"Part 2: {find(lista,4)} in {datetime.now() - start_time}")
