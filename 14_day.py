import re
import itertools

def combinations(text):
    ret = []
    amount = text.count("X")
    for item in itertools.product([1, 0], repeat=amount):
        temp = text
        for letter in item:
            temp = temp.replace("X", str(letter), 1)
        ret.append(temp)

    return ret
def apply_bitmask(mask, value):
    ret = []
    mask = mask[::-1]
    binstr = str(bin(value))[2:][::-1]
    for i in range(len(mask)):
        if i < len(binstr):
            if mask[i] == "X":
                ret.append("X")
            elif mask[i] == "0":
                ret.append(binstr[i])
            else:
                ret.append(mask[i])
        else:
            if mask[i] == "X":
                ret.append("X")
            else:
                ret.append(mask[i])

    combs = combinations("".join(ret[::-1]))
    return [int("".join(comb), 2) for comb in combs]



if __name__ == "__main__":
    with open("input14.txt") as f:
        lista = [x.rstrip() for x in f.readlines()]

    res = r"^mem\[(\d*)\].*"
    init = {}
    for item in lista:
        if item.startswith("mask"):
            mask = item.split(" = ")[1]

        if item.startswith("mem"):
            pos = int(re.findall(res, item)[0])
            value = int(item.split(" = ")[1])
            for item in apply_bitmask(mask, pos):
                init[item] = value

    print(sum(init.values()))
            