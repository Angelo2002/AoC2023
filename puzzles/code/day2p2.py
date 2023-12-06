MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


class Game:
    red = 0
    green = 0
    blue = 0
    imposible=False
    gameval = 0
    power = 0
    def __init__(self,string):
        gameVal,games = string.split(":")
        self.gameval = int(gameVal[5:])
        games = games.split(";")
        for game in games:
            values = game.split(",")
            for info in values:
                amm,color = info.split()
                amm = int(amm)
                if "red" == color:
                    self.red=amm if amm > self.red else self.red
                elif ("green" == color):
                    self.green = amm if amm > self.green else self.green
                elif "blue" == color:
                    self.blue = amm if amm > self.blue else self.blue
        self.calculatePower()

    def check_imp(self):
        self.imposible = self.red>MAX_RED or self.green>MAX_GREEN or self.blue>MAX_BLUE

    def calculatePower(self):
        self.power = self.red*self.green*self.blue
def day2():
    ans = ""
    with open("../input/day2.txt") as file:
        content = file.read()
    listx = content.strip().split("\n")
    ans=0
    for value in listx:
        print(value)
        game = Game(value)
        ans+=game.power
    print(ans)


if __name__ == '__main__':
    day2()
