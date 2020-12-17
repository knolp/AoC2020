DEB = True


def check_reqs(_dict):
    if not 1920 <= int(_dict["byr"]) <= 2002:
        return False
    if not 2010 <= int(_dict["iyr"]) <= 2020:
        return False 
    if not 2020 <= int(_dict["eyr"]) <= 2030:
        return False
    if _dict["hgt"].endswith("cm") or _dict["hgt"].endswith("in"):
        if _dict["hgt"].endswith("cm"):
            if not 150 <= int(_dict["hgt"].replace("cm", "")) <= 193:
                return False
        if _dict["hgt"].endswith("in"):
            if not 59 <= int(_dict["hgt"].replace("in", "")) <= 76:
                return False
    else:
        return False
    if len(_dict["ecl"]) == 3:
        if _dict["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
    else:
        return False

    if _dict["hcl"].startswith("#"):
        if len(_dict["hcl"].replace("#", "")) == 6:
            for item in _dict["hcl"].replace("#", ""):
                if item not in ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]:
                    return False
        else:
            return False
    else:
        return False

    if len(_dict["pid"]) == 9:
        if not _dict["pid"].isdigit():
            return False
    else:
        return False

    return True


def check_valid(text):
    _base_dict = {
        "byr" : False,
        "iyr" : False,
        "eyr" : False,
        "hgt" : False,
        "hcl" : False,
        "ecl" : False,
        "pid" : False,
        "cid" : False
    }
    lista = text.split(" ")
    for i in range(len(lista)):
        k,v = lista[i].split(":")
        _base_dict[k] = v

    if [v for k, v in _base_dict.items()].count(False) == 1:
        if _base_dict["cid"] == False:
            if check_reqs(_base_dict):
                return True
            else:
                return False
        else:
            return False
    
    if [v for k, v in _base_dict.items()].count(False) == 0:
        if check_reqs(_base_dict):
            return True
        else:
            return False

    if [v for k, v in _base_dict.items()].count(False) > 1:
        return False



if __name__ == "__main__":
    with open("input4.txt") as f:
        lista = [x.replace("\n", " ") for x in f.read().split("\n\n")]

    counter = 0
    for item in lista:
        if check_valid(item):
            counter += 1
    print(counter)