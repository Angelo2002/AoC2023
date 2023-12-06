

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
    seeds = [int(seed) for seed in listx[0].split()[1:]]
    dictList = []
    for block in listx[1:]:
        dictList.append(getDicts(block))
    tutorial = []
    for seed in seeds:
        tuto = [seed]
        for i in range(7):
            for dicti in dictList[i]:
                offset = dicti[0]+ dicti[2]
                if dicti[0] <= tuto[i] < offset:
                    tuto.append(dicti[1] + (tuto[i] - dicti[0]))
                    break
            else:
                tuto.append(tuto[i])
        tutorial.append(tuto)

    ans = min([x[7] for x in tutorial])
    print(ans)


if __name__ == '__main__':
    day5()
