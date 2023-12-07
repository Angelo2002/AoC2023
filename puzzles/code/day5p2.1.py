
class Mapping:
    end = 0
    start = 0
    scope = 0

    def __init__(self ,string):
        self.end ,self.start ,self.scope = [int(x) for x in string.split()]

    def __str__(self):
        return f"Map: {self.end},{self.start},{self.scope}"


class Rango:
    min = 0
    max = 0
    valid = True
    maping = None
    def __init__(self, min, max ,map=None):
        self.maping = map
        if min > max:
            self.valid = False
        else:
            self.min = min
            self.max = max

    def set_maping(self ,map):
        self.maping =map

    def doMap(self):
        offset = self.maping.end - self.maping.start
        self.min += offset
        self.max += offset


def day5():
    ans = 0
    with open("../input/day5.txt") as file:
        content = file.read()
    listx = content.strip().split("\n\n")
    seedsNum = [int(seed) for seed in listx[0].split()[1:]]

    seeds = []
    for i in range(0, len(seedsNum), 2):
        seeds.append(Rango(seedsNum[i], seedsNum[i] + seedsNum[i + 1] - 1))

    mappings = []
    for block in listx[1:]:
        newMapping = [Mapping(line) for line in block.splitlines()[1:]]
        mappings.append(newMapping)
    minLocation =None
    for seedRange in seeds:
        currentBlock = [seedRange]
        for i in range(7):
            nextBlock = []
            for map in mappings[i]:
                for rang in currentBlock:
                    new_range = Rango(max(rang.min ,map.start) ,min(rang.max ,map.start + map.scope - 1) , map)
                    if new_range.valid:
                        nextBlock.append(new_range)
                # Rellenar los que no hayan sido mapeados, quitar los invalidos, sacar el mínimo
            nextBlock.sort(key=lambda x: x.min)
            prevVal = seedRange.min
            currentBlock=[]
            for curr_range in nextBlock:
                new_range = Rango(prevVal,curr_range.min-1)
                currentBlock.append(new_range)
                prevVal = curr_range.max+1
                curr_range.doMap()
            currentBlock.append(Rango(prevVal,seedRange.max))
            nextBlock+=currentBlock
            currentBlock = [x for x in nextBlock if x.valid]
        currentMin = min([m.min for m in currentBlock])
        minLocation = currentMin if minLocation is None else min(minLocation,currentMin)
    ans = minLocation
    print(ans)


if __name__ == '__main__':
    day5()
