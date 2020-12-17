def find():
    with open("input2.txt") as f:
        lista = f.readlines()

    counter = 0
    for item in lista:
        policy, password = item.split(": ")
        nums, letter = policy.split(" ")
        lower, higher = [int(x) for x in nums.split("-")]
        
        if lower <= password.count(letter) <= higher:
            counter += 1
    
    print(counter)


def find2():
    with open("input2.txt") as f:
        lista = f.readlines()

    counter = 0
    for item in lista:
        policy, password = item.split(": ")
        nums, letter = policy.split(" ")
        lower, higher = [int(x) for x in nums.split("-")]
        
        if password[lower-1] == letter and password[higher-1] == letter:
            continue
        if password[lower-1] == letter and password[higher-1] != letter:
            counter += 1
        if password[lower-1] != letter and password[higher-1] == letter:
            counter += 1
    
    print(counter)



if __name__ == "__main__":
    find2()