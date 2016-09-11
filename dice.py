import random

def roll(numdice, sides):
    random.seed()
    total = 0
    for x in range(numdice):
        total += random.randint(1, sides)
    return total

def explode(sides):
    total = 0
    r = sides
    while r == sides:
        r = roll(1, sides)
        """ This is a 'Hackmaster' explode """
        if total > 0: total = total - 1
        total = total + r
    return total

def openPercent():
    total = roll(1, 100)
    r = 100
    if total < 6: 
        while r > 95:
            r = roll(1, 100)
            total = total - r
    if total > 95:
        while r > 95:
            r = roll(1, 100)
            total = total + r
    return total

class Dice:
    def __init__(self):
        random.seed()

    def roll(self, numdice, sides):
        total = 0
        for x in range(numdice):
            total += random.randint(1, sides)
        return total
