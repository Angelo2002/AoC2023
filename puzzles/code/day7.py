dict = {'A':'m', 'K':'l', 'Q':'k', 'J':'j', 'T': 'i', '9':'h', '8':'g', '7':'f', '6':'e', '5':'d', '4':'c', '3':'b', '2':'a'}

class Hand:
    string=""
    bid=0
    value=0
    rank = 0
    def __init__(self,string):
        self.string,bid = string.split()
        self.bid = int(bid)

    def getNumber(self):
        stringval=""
        custDict =  {'A':0, 'K':0, 'Q':0, 'J':0, 'T': 0, '9':0, '8':0, '7':0, '6':0, '5':0, '4':0, '3':0, '2':0}
        for char in self.string:
            stringval+=dict[char]
            custDict[char]+=1
        doubles=0
        triple=False
        four = False
        five = False
        for element in custDict:

            val = custDict[element]

            if val==2:
                doubles+=1
            elif val==3:
                triple=True
            elif val == 4:
                four = True
            elif val == 5:
                five = True




        if five:
            value = 7
        elif four:
            value = 6
        elif triple and doubles==1:
            value= 5
        elif triple:
            value = 4
        elif doubles == 2:
            value = 3
        elif doubles == 1:
            value = 2
        else:
            value=1


        self.value=(value,stringval)
        return (value,stringval)
def day7():
    ans = 0
    with open("../input/day7.txt") as file:
        content = file.read()
    listx = content.strip().splitlines()
    handlist= []
    for item in listx:
        handlist.append(Hand(item))
    handlist.sort(key=lambda x:x.getNumber())

    for element in range(len(handlist)):
        ans+=handlist[element].bid*(element+1)

    print(ans)


if __name__ == '__main__':
    day7()
