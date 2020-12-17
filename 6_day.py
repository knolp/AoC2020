
def part_one():
    with open("input6.txt") as f:
        return sum([len(set(x.replace("\n", ""))) for x in f.read().split("\n\n")])

def part_two():
    ret_list = []
    with open("input6.txt") as f:
        lista = f.read().split("\n\n")

        for item in lista:
            counter = 0
            people = item.count("\n") + 1
            chars = list(set(item.replace("\n", "")))
            for char in chars:
                if item.count(char) == people:
                    counter += 1

            ret_list.append(counter)

    return sum(ret_list)


if __name__ == "__main__":
    print(part_two())