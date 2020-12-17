import sys
import math

def find_bus(earliest, buses):
    orig = earliest
    while True:
        for item in buses:
            if earliest % item == 0:
                print(item)
                print(earliest - orig)
                return
        earliest += 1


def find_time(buses):
    testcase = "a = sum([(t+idx) % item for idx, item in enumerate(buses) if item != \"x\"])"
    t = 0
    buses = [(idx, bus) for idx, bus in enumerate(buses) if bus != "x"]
    print(buses)
    eq = []
    try:
        while True:
            #print(f"t = {t}")
            for idx, item in buses:
                if item == "x":
                    continue
                #print(f"{t} + {idx} % {item} = {(t+idx) % item}")
                if (t+idx) % item != 0:
                    break
                if (t+idx) % item == 0 and item not in eq:
                    eq.append(item)
            else:
                print(t)
                return
            if eq:
                prod = 1
                for item in eq:
                    prod *= item
                t += prod
            else:
                t += buses[0][1]
    except KeyboardInterrupt:
        print(f"\n{t}")
        sys.exit()
    print(t) 












if __name__ == "__main__":
    with open("input13.txt") as f:
        lista = [x.rstrip() for x in f.readlines()]
        earliest = int(lista[0])
        buses = [int(x) if x.isdigit() else x for x in lista[1].split(",")]


    #find_bus(earliest, buses)
    find_time(buses)