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

def day4():
    ans = 0
    with open("../input/day4.txt") as file:
        content = file.read()
    cards = content.strip().split("\n")
    for card in cards:
        newCard = Card(card)
        ans+=newCard.cardValue
    print(ans)


if __name__ == '__main__':
    day4()
