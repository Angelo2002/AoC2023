from codeUtils import *

class Card:
    cardNumber = 0
    winningNumbers = []
    numbers = []
    cardValue = 0
    winnings = 0
    def __init__(self,string):
        name,data = string.split(":")
        self.cardNumber = int(name[5:])
        win,have = data.split("|")
        self.winningNumbers = [int(x) for x in win.split()]
        self.numbers = [int(x) for x in have.split()]
        self.cardValue=0
        self.winnings = 0
        for number in self.numbers:
            if number in self.winningNumbers:
                self.cardValue = 1 if self.cardValue==0 else self.cardValue*2
                self.winnings+=1

    def makeCopies(self,nextCards):
        copies = []
        for card in nextCards:
            new_card = Card(card)
            new_card.cardNumber = self.cardNumber
            copies.append(new_card)
        return copies

def checkForCard(cardC, ogList):
    if cardC.winnings == 0:
        return 1
    total=1
    cuttedList = ogList[cardC.cardNumber:cardC.cardNumber+cardC.winnings]
    for card in cuttedList:
        total+=checkForCard(card,ogList)
    return total


def day4():
    ans = 0
    with open("../input/day4.txt") as file:
        content = file.read()
    cards = content.strip().split("\n")
    cardList = []
    for card in cards:
        newCard = Card(card)
        cardList.append(newCard)
    for card in cardList:
        ans+=checkForCard(card,cardList)


    print(ans)



if __name__ == '__main__':
    day4()
