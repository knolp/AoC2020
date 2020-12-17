lista = [
	"..##.......",
	"#...#...#..",
	".#....#..#.",
	"..#.#...#.#",
	".#...##..#.",
	"..#.##.....",
	".#.#.#....#",
	".#........#",
	"#.##...#...",
	"#...##....#",
	".#..#...#.#"
]

with open("input3.txt") as f:
	lista = f.readlines()

for i in range(len(lista)):
	lista[i] = list(lista[i].strip())



class Start():
	def __init__(self):
		self.x = 0
		self.y = 0
	def __repr__(self):
		return f"Y:{self.y} X:{self.x}"
start = Start()
counter = 0
while True:
	start.x += 2
	start.y += 1
	if start.x >= len(lista):
		print(counter)
		break
	if lista[start.x][start.y % len(lista[0])] == "#":
		counter += 1
	lista[start.x][start.y % len(lista[0])] = "@"

with open("answer.txt", "w") as f:
	for item in lista:
		f.write("".join(item))
		f.write("\n")



