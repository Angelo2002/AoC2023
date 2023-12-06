class enginePiece:
    number = 0
    symbol=""
    isSymbol = False
    selected = False
    x = 0
    y = 0
    width = 0

    def __init__(self, num, x, y):
        self.x = x
        self.y = y
        if num.isdigit():
            self.width = len(num) - 1
            self.number = int(num)
            self.isSymbol = False
            self.selected = False
        else:
            self.symbol=num
            self.width = 1
            self.isSymbol = True

    def getVal(self, symbol):
        if self.selected:
            return False

        x1 = symbol.x - 1
        x2 = symbol.x + 1
        y1 = symbol.y - 1
        y2 = symbol.y + 1
        if (x1 <= self.x <= x2) or (x1 <= self.x + self.width <= x2):
            if (y1 <= self.y <= y2):
                return True
        return False


def day3():
    ans = 0
    with open("../input/day3.txt") as file:
        content = file.read()
    listx = content.strip().split("\n")
    y = 0
    numx = 0
    numberlist = []
    symbolList = []
    for line in listx:
        x = 0
        temp = ""
        for char in line:
            if char.isdigit():
                if (temp == ""):
                    numx = x
                temp += char

            elif temp != "":
                newPiece = enginePiece(temp, numx, y)
                numberlist.append(newPiece)
                temp = ""

            if (not char.isdigit()) and char == "*":
                newSymbol = enginePiece(char, x, y)
                symbolList.append(newSymbol)

            x += 1
        if temp != "":
                newPiece = enginePiece(temp, numx, y)
                numberlist.append(newPiece)
        y += 1

    for sym in symbolList:
        count=0
        num=1
        for number in numberlist:
            if number.getVal(sym):
                num*=number.number
                count+=1
            if(count>2):
                break
        if(count==2):
            ans+=num

    print(ans)


if __name__ == '__main__':
    day3()
