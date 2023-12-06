class Race:
    duration = 0
    record = 0
    margin = 0

    def __init__(self,duration,record):
        self.duration = duration
        self.record = record
        self.margin = 0
        for i in range(duration+1):
            if (i*(duration-i)>record):
                self.margin+=1

def day6():
    with open("../input/day6.txt") as file:
        content = file.read()
    listx = content.strip().splitlines()
    ms = int(listx[0].split(":")[1].replace(" ",""))
    records = int(listx[1].split(":")[1].replace(" ",""))
    newRace = Race(ms,records)
    ans=newRace.margin
    print(ans)



if __name__ == '__main__':
    day6()
