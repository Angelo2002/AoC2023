dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}
def checkForNumber(string):
    substring = string[0:]
    for i in range(len(string)):
        if(substring in dict):
            return dict[substring]
        else:
            substring = substring[1:]
    return 'a'
def day1():
    ans = ""
    with open("day1.txt") as file:
        content = file.read()
    listx = content.strip().split()
    ans = 0
    for calval in listx:
        start = 'a'
        end = 'a'
        possibleS = ""
        for char in calval:
            possibleS+=char
            if char.isdigit():
                if start == 'a':
                    start = char
                    end = char
                else:
                    end = char
            char = checkForNumber(possibleS)
            if (char!='a'):
                if start == 'a':
                    start = char
                    end = char
                else:
                    end = char

        ans += int(start + end)

    print(ans)


if __name__ == '__main__':
    day1()
