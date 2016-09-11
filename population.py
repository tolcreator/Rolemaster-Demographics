import dice
import stats
import social

def GetAgeByDieOneThousandRoll(roll):
    if roll <= 280:
        """ Infant to 14 """
        return 0
    if roll <= 300: return 15
    if roll <= 320: return 16
    if roll <= 340: return 17
    if roll <= 360: return 18 
    if roll <= 380: return 19
    if roll <= 400: return 20
    if roll <= 420: return 21
    if roll <= 440: return 22 
    if roll <= 460: return 23
    if roll <= 480: return 24
    if roll <= 500: return 25
    if roll <= 520: return 26 
    if roll <= 540: return 27
    if roll <= 560: return 28
    if roll <= 580: return 29
    if roll <= 600: return 30 

    if roll <= 614: return 31
    if roll <= 628: return 32
    if roll <= 642: return 33 
    if roll <= 656: return 34
    if roll <= 670: return 35
    if roll <= 684: return 36 
    if roll <= 698: return 37
    if roll <= 712: return 38
    if roll <= 726: return 39 
    if roll <= 740: return 40

    if roll <= 752: return 41
    if roll <= 764: return 42
    if roll <= 776: return 43 
    if roll <= 788: return 44
    if roll <= 800: return 45
    if roll <= 812: return 46 
    if roll <= 824: return 47
    if roll <= 836: return 48
    if roll <= 848: return 49 
    if roll <= 860: return 50

    if roll <= 869: return 61
    if roll <= 878: return 62
    if roll <= 887: return 63 
    if roll <= 896: return 64
    if roll <= 905: return 65
    if roll <= 914: return 66 
    if roll <= 923: return 67
    if roll <= 932: return 68
    if roll <= 941: return 69 
    if roll <= 950: return 60

    if roll <= 955: return 71
    if roll <= 960: return 72
    if roll <= 965: return 73 
    if roll <= 970: return 74
    if roll <= 975: return 75
    if roll <= 980: return 76 
    if roll <= 985: return 77
    if roll <= 990: return 78
    if roll <= 995: return 79 
    return 80

def GetXpPerYear(determination, ambition):
    return 750 * ambition * (1 + (determination / 100))

def GetLevelFromXp(xp):
    if xp < 10000:  return 0
    if xp < 20000:  return 1
    if xp < 30000:  return 2
    if xp < 40000:  return 3
    if xp < 50000:  return 4
    if xp < 70000:  return 5
    if xp < 90000:  return 6
    if xp < 110000: return 7
    if xp < 130000: return 8
    if xp < 150000: return 9
    if xp < 180000: return 10
    if xp < 210000: return 11
    if xp < 240000: return 12
    if xp < 270000: return 13
    if xp < 300000: return 14
    if xp < 340000: return 15
    if xp < 380000: return 16
    if xp < 420000: return 17
    if xp < 460000: return 18
    if xp < 500000: return 19
    return 20

PrimeStatsTable =\
{\
    "Commoner":     [],\
    "Fighter":      ["ST", "CO"],\
    "Adventurer":   ["ST", "AG"],\
    "Thief":        ["QU", "AG"],\
    "Warrior Monk": ["QU", "SD"],\
    "Ranger":       ["IN", "CO"],\
    "Bard":         ["PR", "ME"],\
    "Monk":         ["EM", "SD"],\
    "Cleric":       ["IN", "ME"],\
    "Animist":      ["IN", "ME"],\
    "Healer":       ["IN", "ME"],\
    "Illusionist":  ["EM", "RE"],\
    "Magician":     ["EM", "RE"],\
    "Alchemist":    ["EM", "RE"],\
    "Mentalist":    ["PR", "SD"],\
    "Seer":         ["PR", "SD"],\
    "Lay Healer":   ["PR", "SD"],\
    "Sorcerer":     ["EM", "IN"],\
    "Mystic":       ["EM", "PR"],\
    "Astrologer":   ["PR", "IN"]\
}


SocialClassAmbitionTable =\
{\
    "Slave":        0,\
    "Serf":         0,\
    "Unguilded":    1,\
    "Guilded":      2,\
    "Noble":        4\
}

ProfessionAmbitionTable=\
{\
    "Commoner":     0,\
    "Fighter":      1,\
    "Adventurer":   1,\
    "Thief":        1,\
    "Warrior Monk": 2,\
    "Ranger":       2,\
    "Bard":         2,\
    "Monk":         3,\
    "Cleric":       3,\
    "Animist":      3,\
    "Healer":       3,\
    "Illusionist":  4,\
    "Magician":     4,\
    "Alchemist":    4,\
    "Mentalist":    4,\
    "Seer":         4,\
    "Lay Healer":   4,\
    "Sorcerer":     5,\
    "Mystic":       5,\
    "Astrologer":   5\
}

def GetAmbition(socialClass, profession):
    ambition = 0
    if socialClass in SocialClassAmbitionTable:
        ambition = ambition + SocialClassAmbitionTable[socialClass]
    if profession in ProfessionAmbitionTable:
        ambition = ambition + ProfessionAmbitionTable[profession]
    ambition = ambition + dice.explode(3)
    return min(ambition, 15)

OppressionTable =\
{\
    "Slave":        2,\
    "Serf":         2,\
    "Unguilded":    1,\
    "Guilded":      1,\
    "Noble":        0\
}

OpportunityTable =\
{\
    "Slave":        0,\
    "Serf":         0,\
    "Unguilded":    1,\
    "Guilded":      1,\
    "Noble":        2\
}

class Npc():
    def __init__(self):
        self.socialClass = social.GetSocialClass("Feudal", dice.roll(1, 100))
        self.oppression = OppressionTable[self.socialClass]
        self.opportunity = OpportunityTable[self.socialClass]
        self.occupation = social.GetOccupation("Feudal", self.socialClass, dice.roll(1, 100))
        self.profession = social.GetProfession(self.occupation, dice.roll(1, 100))
        self.ambition = GetAmbition(self.socialClass, self.profession)
        self.initialAmbition = self.ambition
        if self.ambition < 6:
            self.stats = stats.Stats("Mundane", PrimeStatsTable[self.profession])
        else:
            self.stats = stats.Stats("Elite", PrimeStatsTable[self.profession])
        roll = dice.roll(1, 1000)
        self.age = GetAgeByDieOneThousandRoll(roll)
        if self.age == 0:
            self.level = 0
            self.xp = 0
            self.profession = "Child"
            return
        else:
            self.level = 1
            self.xp = 10000
        for x in range(15, self.age+1):
            co = self.stats.GetBonus("CO")
            ag = self.stats.GetBonus("AG")
            me = self.stats.GetBonus("ME")
            re = self.stats.GetBonus("RE")
            
            tenacity = int((co + me)/2)
            cunning = int((ag + re)/2)
            determination = max(tenacity, cunning)

            self.xp = self.xp + GetXpPerYear(determination, self.ambition)
            level = GetLevelFromXp(self.xp)
            if level > self.level:
                ambitionDrop = False
                self.level = level
                self.stats.Gain()
                if x == 35:
                    self.stats.AgingCrisis("Middle")
                if x == 53:
                    self.stats.AgingCrisis("Old")
                if x == 75:
                    self.stats.AgingCrisis("Venerable")
           
            sd = self.stats.GetBonus("SD")
            roll = dice.openPercent() + sd - (self.age + self.ambition)

            """
            if roll < -50: self.ambition = self.ambition - 2
            elif roll < 0: self.ambition = self.ambition -1
            elif roll > 50: self.ambition = self.ambition + 1
            elif roll > 100: self.ambition = self.ambition + 2
            if self.ambition < 1:
                self.ambition = 1
            """

            if roll < -66 and self.GetOppression() >= 2: self.ambition = self.ambition -3
            elif roll < -33 and self.GetOppression() >= 1: self.ambition = self.ambition -2 
            elif roll < 0: self.ambition = self.ambition -1
            elif roll > 33: self.ambition = self.ambition + 1
            elif roll > 66 and self.GetOpportunity() >= 1: self.ambition = self.ambition + 2
            elif roll > 100 and self.GetOpportunity() >= 2: self.ambition = self.ambition + 3
            if self.ambition < 1:
                self.ambition = 1
                
    def GetLevel(self):
        return self.level

    def GetAge(self):
        return self.age    

    def GetAmbition(self):
        return self.ambition

    def GetInitialAmbition(self):
        return self.initialAmbition

    def GetSocialClass(self):
        return self.socialClass

    def GetOccupation(self):
        return self.occupation

    def GetProfession(self):
        return self.profession

    def GetOppression(self):
        return self.oppression

    def GetOpportunity(self):
        return self.opportunity

class Pop():
    def __init__(self, population):
        self.citizens = []
        marker = population / 100
        mark = 0
        for x in range(1, population+1):
            citizen = Npc()
            self.citizens.append(citizen)
            mark = mark + 1
            if mark > marker:
                print "%d" % x
                mark = 0
        self.citizens.sort(key=lambda x: x.GetLevel())
    
    def report(self):
        levels = []
        professions = {}
        occupations = {}
        for level in range(0, 21):
            levels.append(0)
        for citizen in self.citizens:
            print "Level: %d Age: %d Ambition Current: %d Initial: %d. Class: %s Occupation: %s Profession: %s"\
                % (citizen.GetLevel(), citizen.GetAge(), citizen.GetAmbition(), citizen.GetInitialAmbition(),\
                        citizen.GetSocialClass(), citizen.GetOccupation(), citizen.GetProfession())
            occupation = citizen.GetOccupation()
            if occupation in occupations:
                occupations[occupation] = occupations[occupation] + 1
            else:
                occupations[occupation] = 1
            profession = citizen.GetProfession()
            if profession in professions:
                professions[profession]["Count"] = professions[profession]["Count"] + 1
                if citizen.GetLevel() in professions[profession]:
                    professions[profession][citizen.GetLevel()] = professions[profession][citizen.GetLevel()] + 1
                else:
                    professions[profession][citizen.GetLevel()] = 1
            else:
                professions[profession] = {}
                professions[profession]["Count"] = 1
                professions[profession][citizen.GetLevel()] = 1
            levels[citizen.GetLevel()] = levels[citizen.GetLevel()] + 1
        print ""
        for x in range(0, 21):
            print "Level %d: %d" % (x, levels[x])
        print ""
        for occupation in occupations:
            print "%s: %d" % (occupation, occupations[occupation])
        print ""
        for profession in professions:
            print "%s: %d" % (profession, professions[profession]["Count"])
        print ""
        for profession in professions:
            print "%s: " % profession,
            for level in professions[profession]:
                print "%s: %d, " % (str(level), professions[profession][level]),
            print "" 

    def reportLevel(self, level):
        subset = []
        for citizen in self.citizens:
            if citizen.GetLevel() == level:
                subset.append(citizen)
        subset.sort(key=lambda x: x.GetAge())
        for citizen in subset:
            print "Level: %d Age: %d Ambition Current: %d Initial: %d Sd: %d" % (citizen.GetLevel(), citizen.GetAge(), citizen.GetAmbition(), citizen.GetInitialAmbition(), citizen.GetTempSd())
 
if __name__ == "__main__":
    p = Pop(300)
    p.report()
