

class Mapping:
    end = 0
    start = 0
    scope = 0

    def __init__(self,string):
        self.end,self.start,self.scope = [int(x) for x in string.split()]

    def __str__(self):
        return f"Map: {self.end},{self.start},{self.scope}"


class Rango:
    min = 0
    max = 0
    valid = True
    maping = None
    def __init__(self, min, max,map=None):
        self.maping = map
        if min > max:
            self.valid = False
        else:
            self.min = min
            self.max = max

    def set_maping(self,map):
        self.maping=map



def day5():
    ans = 0
    with open("../input/day5.txt") as file:
        content = file.read()
    listx = content.strip().split("\n\n")
    seedsNum = [int(seed) for seed in listx[0].split()[1:]]

    seeds = []
    for i in range(0, len(seedsNum), 2):
        seeds.append(Rango(seedsNum[i], seedsNum[i] + seedsNum[i + 1]))

    mappings = []
    for block in listx[1:]:
        newMapping = [Mapping(line) for line in block.splitlines()[1:]]
        mappings.append(newMapping)
    minLocation=None
    for seedRange in seeds:
        currentBlock = [seedRange]
        for i in range(7):
            nextBlock = []
            for map in mappings[i]:
                for rang in currentBlock:
                    nextBlock.append(Rango(min(rang.min,map.start),max(rang.max,map.start+map.scope),map))
                #Rellenar los que no hayan sido mapeados, quitar los invalidos, sacar el mínimo

    print(mappings)
    print(ans)


if __name__ == '__main__':
    day5()
