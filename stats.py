import dice

def GetMundaneStats():
    stats = []
    for x in range(0, 10):
        temp = dice.roll(1, 100)
        stats.append(temp)
    return stats

def GetEliteStats():
    temps = []
    stats = []
    for x in range(0, 10):
        roll = 0
        while(roll < 20):
           roll = dice.roll(1, 100)
        stats.append(roll)
    return stats

def GetPotential(temp):
    sides = 10
    num = 1
    if temp < 25:
        num = 8
        add = 20
    elif temp < 35:
        num = 7
        add = 30
    elif temp < 45:
        num = 6
        add = 40
    elif temp < 55:
        num = 5
        add = 50
    elif temp < 65:
        num = 4
        add = 60
    elif temp < 75:
        num = 3
        add = 70
    elif temp < 85:
        num = 2
        add = 80
    elif temp < 92:
        add = 90
    elif temp == 92:
        sides = 9
        add = 91
    elif temp == 93:
        sides = 8
        add = 92
    elif temp == 94:
        sides = 7
        add = 93
    elif temp == 95:
        sides = 6
        add = 94
    elif temp == 96:
        sides = 5
        add = 95
    elif temp == 97:
        sides = 4
        add = 96
    elif temp == 98:
        sides = 3
        add = 97
    elif temp == 99:
        sides = 2
        add = 98
    else:
        sides = 2
        add = 99

    pot = dice.roll(num, sides) + add
    pot = max(temp, pot)
    if(pot > 101):
        errstr = "pot %d temp %d num %d sides %d add %d" % (pot, temp, num, sides, add)
        raise NameError(errstr)
    return pot

def GetBonus(stat):
    if stat < 12:   return -10
    if stat < 16:   return -9
    if stat < 19:   return -8
    if stat < 22:   return -7
    if stat < 25:   return -6
    if stat < 28:   return -5
    if stat < 31:   return -4
    if stat < 34:   return -3
    if stat < 37:   return -2
    if stat < 41:   return -1
    if stat < 60:   return 0
    if stat < 64:   return 1
    if stat < 68:   return 2
    if stat < 72:   return 3
    if stat < 75:   return 4
    if stat < 78:   return 5
    if stat < 81:   return 6
    if stat < 84:   return 7
    if stat < 87:   return 8
    if stat < 90:   return 9
    if stat < 91:   return 10
    if stat < 92:   return 11
    if stat < 93:   return 12
    if stat < 94:   return 13
    if stat < 95:   return 14
    if stat < 96:   return 15
    if stat < 97:   return 17
    if stat < 98:   return 19
    if stat < 99:   return 21
    if stat < 100:  return 23
    if stat < 101:  return 25
    return 30

def GetNewTemp(temp, pot):
    first = dice.roll(1, 10)
    second = dice.roll(1, 10)
    inc = 0
    if first == second:
        if first < 6:
            return temp - (first * 2)
        else:
            inc = first * 2
    elif (pot - temp) > 20:
        inc = first + second
    elif (pot - temp) > 10:
        inc = max(first, second)
    else:
        inc = min(first, second)
    newtemp = temp + inc
    temp = max(temp, newtemp)
    temp = min(temp, pot)
    if(temp > 101):
        errstr = "temp %d pot %d, first %d second %d inc %d" % (temp, pot, first, second, inc)
        raise NameError(errstr)
    return temp



class Stats():
    def __init__(self, rank, primes):
        tofill = ["CO", "AG", "SD", "ME", "RE", "ST", "QU", "EM", "IN", "PR"]
        if rank == "Mundane":
            table = GetMundaneStats()
        else:
            table = GetEliteStats()
        
        table.sort(reverse=True)
        self.stats = {}
        remaining = 10
        for prime in primes:
            self.stats[prime] = {}
            if table[0] < 90:
                self.stats[prime]["Temp"] = 90
            else:
                self.stats[prime]["Temp"] = table[0]
            table.remove(table[0])
            tofill.remove(prime)
            remaining = remaining - 1
        for stat in tofill:
            self.stats[stat] = {}
            roll = dice.roll(1, remaining) - 1
            self.stats[stat]["Temp"] = table[roll]
            table.remove(table[roll])
            remaining = remaining - 1
            
        for stat in self.stats:
            self.stats[stat]["Pot"] = GetPotential(self.stats[stat]["Temp"]) 

    def Report(self):
        for stat in self.stats:
            print "%s: %03d %03d %d" % (stat, self.stats[stat]["Temp"], self.stats[stat]["Pot"], GetBonus(self.stats[stat]["Temp"]))

    def Gain(self):
        for stat in self.stats:
            self.stats[stat]["Temp"] = GetNewTemp(self.stats[stat]["Temp"], self.stats[stat]["Pot"])

    def GetBonus(self, stat):
        return GetBonus(self.stats[stat]["Temp"])

    def AgingCrisis(self, crisis):
        if crisis == "Middle":
            num = 1
        elif crisis == "Old":
            num = 2
        elif crisis == "Venerable":
            num = 3
        for stat in ["CO", "AG", "ST", "QU"]:
            self.stats[stat]["Pot"] = self.stats[stat]["Pot"] - dice.roll(num, 10)
            if self.stats[stat]["Temp"] > self.stats[stat]["Pot"]:
                self.stats[stat]["Temp"] = self.stats[stat]["Pot"]
        for stat in ["SD", "ME", "RE", "EM", "IN", "PR"]:
            self.stats[stat]["Temp"] = GetNewTemp(self.stats[stat]["Temp"], self.stats[stat]["Pot"])


