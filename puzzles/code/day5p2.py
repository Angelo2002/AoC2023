def getDict(destination, source, nrange):
    newDict = {}
    for n in range(nrange):
        newDict[source + n] = destination + n
    return newDict


def getDicts(string):
    newDict = []
    values = string.split(":\n")[1].split("\n")
    for stringline in values:
        line = stringline.split()
        newDict.append([int(line[1]), int(line[0]), int(line[2])])
    return newDict


def day5():
    ans = 0
    with open("../input/day5.txt") as file:
        content = file.read()
    listx = content.strip().split("\n\n")
    seedsNum = [int(seed) for seed in listx[0].split()[1:]]

    seeds = []
    for i in range(0, len(seedsNum), 2):
        seeds.append(range(seedsNum[i], seedsNum[i] + seedsNum[i + 1] - 1))

    dictList = []
    for block in listx[1:]:
        dictList.append(getDicts(block))
    tutorial = []
    for seed in seeds:
        tuto = [[seed]]
        for i in range(7):
            newEntry = []
            preMap = []
            for dicti in dictList[i]:
                dictMin = dicti[0]
                dictMax = dicti[0] + dicti[2]
                offset = - dictMin + dicti[1]
                for rangus in tuto[i]:
                    mapped_range = range(max(min(rangus), dictMin),
                                         min(max(rangus) + 1, dictMax))
                    if len(mapped_range) != 0:
                        preMap += [mapped_range]
                        newEntry+=[range(min(mapped_range)+offset,max(mapped_range)+1+offset)]
            preMap.sort(key=lambda x:min(x))
            newEntry+=[range(min())]
            for element in preMap:
                newEntry+=[range()]
            tuto.append(newEntry)

        tutorial.append(tuto)
    print(tutorial)
    ans = [min(x) for y in tutorial for x in y[7]]
    print(ans)
    print(min(ans))


if __name__ == '__main__':
    day5()
