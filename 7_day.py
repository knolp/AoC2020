def search(_dict, name):
    #print(f"Searching  {name}")
    while True:
        v = _dict[name]
        if v == "no other":
            return False
        if "shiny gold" in v.keys():
            return True

        
        for item in v.keys():
            if search(_dict, item):
                return True
        
        return False

def part_one():
    _dict = {}
    with open("input7.txt") as f:
        rules = [x.replace(".", "") for x in f.read().split("\n")]

    for i in range(len(rules)):
        rules[i] = rules[i].replace(" bags", "")
        rules[i] = rules[i].replace(" bag", "")
        rules[i] = rules[i].split(" contain ")

    for i in range(len(rules)):
        outer, inner = rules[i]
        inner_list = inner.split(", ")
        if outer not in _dict.keys():
            _dict[outer] = {}
            if len(inner_list) == 1 and inner_list[0] == "no other":
                _dict[outer] = "no other"
            else:
                for j in range(len(inner_list)):
                    number, name = inner_list[j][0], inner_list[j][2:]
                    _dict[outer][name] = number

    counter = 0
    for k in _dict.keys():
        if search(_dict, k):
            counter += 1
    return counter







def search_two(_dict, name):
    print(f"Searching  {name}")
    v = _dict[name]
    print(f"v = {v}")
    if v == "no other":
        return 1
    
    summa = 1
    for key,val in v.items():
        print(f"Next up: {key}, {val}")
        count = search_two(_dict, key)
        summa += count * int(val)

    return summa


def part_two():
    _dict = {}
    with open("input7.txt") as f:
        rules = [x.replace(".", "") for x in f.read().split("\n")]

    for i in range(len(rules)):
        rules[i] = rules[i].replace(" bags", "")
        rules[i] = rules[i].replace(" bag", "")
        rules[i] = rules[i].split(" contain ")

    for i in range(len(rules)):
        outer, inner = rules[i]
        inner_list = inner.split(", ")
        if outer not in _dict.keys():
            _dict[outer] = {}
            if len(inner_list) == 1 and inner_list[0] == "no other":
                _dict[outer] = "no other"
            else:
                for j in range(len(inner_list)):
                    number, name = inner_list[j][0], inner_list[j][2:]
                    _dict[outer][name] = number

    return search_two(_dict, "shiny gold")

if __name__ == "__main__":
    #print(part_one())
    print(part_two() - 1)