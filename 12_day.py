class Waypoint():
    def __init__(self):
        #x = S/N
        #y = W/E
        self.x = 1
        self.y = 10
    
    def rotate(self, directions, arg):
        degrees = arg // 90
        for i in range(degrees):
            if directions == "R":
                self.x, self.y = -self.y, self.x
            elif directions == "L":
                self.x, self.y = self.y, -self.x

    def update(self, direction, arg):
        if direction == "E":
            self.y += arg
        elif direction == "W":
            self.y -= arg
        elif direction == "N":
            self.x += arg
        elif direction == "S":
            self.x -= arg

    def pos(self):
        print(self.x, self.y)
        print(abs(self.x) + abs(self.y))

class Ship():
    def __init__(self):
        self.x = 0
        self.y = 0

    def forward(self, arg, waypoint):
        self.x += waypoint.x * arg
        self.y += waypoint.y * arg

    def pos(self):
        print(self.x, self.y)
        print(abs(self.x) + abs(self.y))


def part_one(lista):
    ship = Ship()
    way = Waypoint()
    for item in lista:
        command, argument = item[0], int(item[1:])
        if command in ["N", "S", "W", "E"]:
            way.update(command, argument)
        elif command in ["L", "R"]:
            way.rotate(command, argument)
        elif command == "F":
            ship.forward(argument, way)
    
    print(ship.pos())



if __name__ == "__main__":
    with open("input12.txt") as f:
        lista = [x.rstrip() for x in f.readlines()]
    
    part_one(lista)