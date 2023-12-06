MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


class Game:
    red = 0
    green = 0
    blue = 0
    imposible=False
    gameval = 0

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
                    self.red=amm
                elif ("green" == color):
                    self.green = amm
                elif "blue" == color:
                    self.blue = amm
            self.check_imp()
            if(self.imposible):
                break

    def check_imp(self):
        self.imposible = self.red>MAX_RED or self.green>MAX_GREEN or self.blue>MAX_BLUE

def day2():
    ans = ""
    with open("../input/day2.txt") as file:
        content = file.read()
    listx = content.strip().split("\n")
    ans=0
    for value in listx:
        print(value)
        game = Game(value)

        if(not game.imposible):
            ans+=game.gameval
    print(ans)


if __name__ == '__main__':
    day2()
