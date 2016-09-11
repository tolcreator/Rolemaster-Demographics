SocialClassTable =\
{\
    "Tribal":\
    {\
        "Slave":     [x for x in range(1, 11)],\
        "Serf":      [],\
        "Unguilded": [x for x in range(11, 100)],\
        "Guilded":   [],\
        "Noble":     [100]\
    },\
    "Viking":\
    {\
        "Slave":     [x for x in range(1, 16)],\
        "Serf":      [x for x in range(16, 81)],\
        "Unguilded": [x for x in range(81, 94)],\
        "Guilded":   [x for x in range(94, 99)],\
        "Noble":     [99, 100]\
    },\
    "Feudal":\
    {\
        "Slave":     [],\
        "Serf":      [x for x in range(1, 71)],\
        "Unguilded": [x for x in range(71, 94)],\
        "Guilded":   [x for x in range(94, 99)],\
        "Noble":     [99, 100]\
    },\
    "Imperial":\
    {\
        """ TODO """\
    },\
    "Elf":\
    {\
        "Slave":     [],\
        "Serf":      [],\
        "Unguilded": [x for x in range(1, 71)],\
        "Guilded":   [x for x in range(71, 100)],\
        "Noble":     [100]\
    },\
    "Dwarf":\
    {\
        "Slave":     [],\
        "Serf":      [],\
        "Unguilded": [x for x in range(1, 16)],\
        "Guilded":   [x for x in range(16, 99)],\
        "Noble":     [99, 100]\
    },\
    "Hobbit":\
    {\
        "Slave":     [],\
        "Serf":      [],\
        "Unguilded": [x for x in range(1, 71)],\
        "Guilded":   [x for x in range(71, 100)],\
        "Noble":     [100]\
    },\
    "Gnome":\
    {\
        "Slave":     [],\
        "Serf":      [],\
        "Unguilded": [x for x in range(1, 16)],\
        "Guilded":   [x for x in range(16, 99)],\
        "Noble":     [99, 100]\
    }\
}

""" This is accessed as [culture][socialClass][roll] """
""" This is slightly different than as presented in the book """
""" But makes adding or removing cultures much easier """
TribalOccupationTable =\
{\
    """ TODO """\
}

VikingOccupationTable =\
{\
   
    """ TODO """\
    "Slave":\
    {\
        "Farmer":                   [],\
        "Herder":                   [],\
        "Cook/Servant":             [],\
        "Gladiator":                []\
    },\
    "Serf":\
    {\
        "Farmer":                   [x for x in range(1, 81)],\
        "Herder":                   [x for x in range(81, 96)],\
        "Cook/Servant":             [x for x in range(96, 100)]\
    },\
    "Unguilded":\
    {\
        "Animal Trainer":           [],\
        "Beggar/Scavenger":         [],\
        "Cartographer/Artist":      [],\
        "Cleric/Shaman":            [],\
        "Cook/Servant":             [],\
        "Farmer":                   [],\
        "Fisherman":                [],\
        "Gladiator":                [],\
        "Hedge Wizard/Witch":       [],\
        "Herder":                   [],\
        "Hunter/Trapper":           [],\
        "Labourer":                 [],\
        "Prostitute/Pimp":          [],\
        "Ratter":                   [],\
        "Sage/Tutor":               [],\
        "Scribe":                   [],\
        "Soldier, Guardsman":       [],\
        "Soldier, Mercenary":       [],\
        "Soldier, Yeoman":          [],\
        "Teamster":                 [],\
        "Thatcher":                 [],\
        "Toymaker":                 []\
    },\
    "Guilded":\
    {\
        "Alchemist":                [],\
        "Apothecary":               [],\
        "Astrologer":               [],\
        "Chandler":                 [],\
        "Charcoaler":               [],\
        "Clothier":                 [],\
        "Courtesan":                [],\
        "Embalmer":                 [],\
        "Glassworker":              [],\
        "Harper/Skald":             [],\
        "Hideworker":               [],\
        "Innkeeper":                [],\
        "Jeweler":                  [],\
        "Lexigrapher":              [],\
        "Litigant":                 [],\
        "Locksmith":                [],\
        "Mage":                     [],\
        "Mason":                    [],\
        "Merchant":                 [],\
        "Metalsmith":               [],\
        "Miller":                   [],\
        "Miner":                    [],\
        "Ostler":                   [],\
        "Perfumer":                 [],\
        "Physician":                [],\
        "Pilot":                    [],\
        "Potter":                   [],\
        "Salter":                   [],\
        "Seaman":                   [],\
        "Shipwright":               [],\
        "Tentmaker":                [],\
        "Thespian":                 [],\
        "Thief":                    [],\
        "Timberwright":             [],\
        "Weaponcrafter":            [],\
        "Woodcrafter":              []\
    },\
    "Noble":\
    {\
        "Cleric":                   [],\
        "Court Wizard":             [],\
        "Herald":                   [],\
        "Bailiff":                  [],\
        "Chieftain":                [],\
        "Knight Batchelor":         [],\
        "Knight":                   []\
    }\
}

FeudalOccupationTable =\
{\
    "Slave":\
    {\
    },\
    "Serf":\
    {\
        "Farmer":                   [x for x in range(1, 81)],\
        "Herder":                   [x for x in range(81, 96)],\
        "Cook/Servant":             [x for x in range(96, 101)]\
    },\
    "Unguilded":\
    {\
        "Animal Trainer":           [1],\
        "Beggar/Scavenger":         [2, 3, 4, 5],\
        "Cartographer/Artist":      [6],\
        "Cleric/Shaman":            [7, 8],\
        "Cook/Servant":             [9, 10, 11, 12],\
        "Farmer":                   [x for x in range(13, 61)],\
        "Fisherman":                [61, 62, 63, 64, 65, 66],\
        "Gladiator":                [],\
        "Hedge Wizard/Witch":       [67],\
        "Herder":                   [68, 69, 70],\
        "Hunter/Trapper":           [71, 72, 73],\
        "Labourer":                 [74, 75, 76, 77, 78, 79, 80, 81],\
        "Prostitute/Pimp":          [82, 83],\
        "Ratter":                   [84, 85],\
        "Sage/Tutor":               [86],\
        "Scribe":                   [87],\
        "Soldier, Guardsman":       [88],\
        "Soldier, Mercenary":       [89, 90],\
        "Soldier, Yeoman":          [91, 92, 93, 94, 95, 96, 97],\
        "Teamster":                 [98],\
        "Thatcher":                 [99],\
        "Toymaker":                 [100]\
    },\
    "Guilded":\
    {\
        "Alchemist":                [1],\
        "Apothecary":               [2],\
        "Astrologer":               [3],\
        "Chandler":                 [4, 5],\
        "Charcoaler":               [6, 7],\
        "Clothier":                 [8, 9, 10, 11],\
        "Courtesan":                [12],\
        "Embalmer":                 [13, 14],\
        "Glassworker":              [15, 16],\
        "Harper/Skald":             [17, 18, 19],\
        "Hideworker":               [20, 21, 22, 23, 24, 25, 26],\
        "Innkeeper":                [27, 28, 29, 30, 31],\
        "Jeweler":                  [32, 33],\
        "Lexigrapher":              [34, 35],\
        "Litigant":                 [36],\
        "Locksmith":                [37],\
        "Mage":                     [38],\
        "Mason":                    [39, 40, 41],\
        "Merchant":                 [42, 43, 44, 45, 46, 47],\
        "Metalsmith":               [48, 49, 50, 51, 52, 53, 54, 55, 56],\
        "Miller":                   [57, 58, 59, 60, 61, 62, 63, 64],\
        "Miner":                    [65, 66, 67],\
        "Ostler":                   [68, 69],\
        "Perfumer":                 [70, 71],\
        "Physician":                [72],\
        "Pilot":                    [73],\
        "Potter":                   [74, 75, 76, 77],\
        "Salter":                   [78, 79],\
        "Seaman":                   [80, 81, 82],\
        "Shipwright":               [83],\
        "Tentmaker":                [84],\
        "Thespian":                 [85],\
        "Thief":                    [86, 87, 88],\
        "Timberwright":             [89, 90],\
        "Weaponcrafter":            [91, 92],\
        "Woodcrafter":              [93, 94, 95, 96, 97, 98, 99, 100]\
    },\
    "Noble":\
    {\
        "Cleric":                   [1, 2, 3, 4, 5],\
        "Court Wizard":             [6, 7],\
        "Herald":                   [8, 9, 10, 11, 12],\
        "Bailiff":                  [13, 14, 15, 16, 17],\
        "Chieftain":                [],\
        "Knight Batchelor":         [x for x in range(18, 86)],\
        "Knight":                   [x for x in range(86, 101)]\
    }\
}

ImperialOccupationTable =\
{\
    """ TODO """\
}

ElfOccupationTable =\
{\
    """ TODO """\
}

DwarfOccupationTable =\
{\
    """ TODO """\
}

HobbitOccupationTable =\
{\
    """ TODO """\
}

GnomeOccupationTable =\
{\
    """ TODO """\
}

OccupationTable =\
{\
    "Tribal": TribalOccupationTable,\
    "Viking": VikingOccupationTable,\
    "Feudal": FeudalOccupationTable,\
    "Imperial": ImperialOccupationTable,\
    "Elf": ElfOccupationTable,\
    "Dwarf": DwarfOccupationTable,\
    "Hobbit": HobbitOccupationTable,\
    "Gnome": GnomeOccupationTable\
}


StandardProfessionTable =\
{\
    "Commoner":             [x for x in range(1, 89)],\
    "Fighter":              [89, 90],\
    "Adventurer":           [91, 92, 93, 94],\
    "Thief":                [95, 96, 97, 98, 99, 100]\
}

GladiatorProfessionTable =\
{\
    "Commoner":             [x for x in range(1, 41)],\
    "Fighter":              [x for x in range(41, 61)],\
    "Adventurer":           [x for x in range(61, 81)],\
    "Thief":                [x for x in range(81, 101)]
}

HerderProfessionTable =\
{\
    "Commoner":             [x for x in range(1, 87)],\
    "Fighter":              [87, 88],\
    "Adventurer":           [89, 90, 91, 92],\
    "Thief":                [93, 94, 95, 96, 97, 98],\
    "Ranger":               [99, 100]\
}

BeggarProfessionTable =\
{\
    "Commoner":             [x for x in range(1, 70)],\
    "Fighter":              [70, 71],\
    "Adventurer":           [72, 73, 74, 75],\
    "Thief":                [x for x in range(76, 100)],\
    "Bard":                 [100]\
}

ArtistProfessionTable =\
{\
    "Commoner":             [x for x in range(1, 79)],\
    "Fighter":              [79, 80],\
    "Adventurer":           [81, 82, 83, 84],\
    "Thief":                [85, 86, 87, 88, 89, 90],\
    "Bard":                 [x for x in range(91, 101)],\
}

ShamanProfessionTable =\
{\
    "Ranger":               [x for x in range(1, 11)],\
    "Cleric":               [x for x in range(11, 36)],\
    "Animist":              [x for x in range(36, 66)],\
    "Healer":               [x for x in range(66, 96)],\
    "Seer":                 [96, 97],\
    "Sorcerer":             [98],\
    "Mystic":               [99],\
    "Astrologer":           [100]\
}

WitchProfessionTable =\
{\
    "Bard":                 [x for x in range(1, 26)],\
    "Illusionist":          [x for x in range(26, 46)],\
    "Magician":             [x for x in range(46, 61)],\
    "Alchemist":            [x for x in range(61, 76)],\
    "Mentalist":            [x for x in range(76, 85)],\
    "Seer":                 [85, 86, 87, 88, 89],\
    "Lay Healer":           [90, 91, 92],\
    "Sorcerer":             [93, 94],\
    "Mystic":               [95, 96, 97, 98, 99],\
    "Astrologer":           [100]\
}    

ProstituteProfessionTable =\
{\
    "Commoner":             [x for x in range(1, 71)],\
    "Fighter":              [71, 72],\
    "Adventurer":           [73, 74, 75, 76],\
    "Thief":                [x for x in range(77, 100)],\
    "Bard":                 [100]\
}

RatterProfessionTable =\
{\
    "Commoner":             [x for x in range(1, 71)],\
    "Fighter":              [71, 72],\
    "Adventurer":           [73, 74, 75, 76],\
    "Thief":                [x for x in range(77, 100)],\
    "Ranger":               [100]\
}

ScholarProfessionTable =\
{\
    "Commoner":             [x for x in range(1, 76)],\
    "Fighter":              [76, 77],\
    "Adventurer":           [78, 79],\
    "Thief":                [80, 81, 82, 83, 84, 85],\
    "Bard":                 [x for x in range(86, 101)]
}

SoldierProfessionTable =\
{\
    "Commoner":             [x for x in range(1, 36)],\
    "Fighter":              [x for x in range(36, 56)],\
    "Adventurer":           [x for x in range(56, 81)],\
    "Thief":                [x for x in range(81, 98)],\
    "Ranger":               [98, 99, 100]\
}

AlchemistProfessionTable =\
{\
    "Commoner":             [x for x in range(1, 51)],\
    "Fighter":              [51, 52],\
    "Adventurer":           [53, 54, 55, 56, 57, 58],\
    "Thief":                [59, 60, 61, 62],\
    "Ranger":               [63],\
    "Bard":                 [64, 65, 66, 67, 68, 69, 70],\
    "Illusionist":          [71, 72, 73, 74, 75],\
    "Magician":             [76, 77, 78, 79, 80],\
    "Alchemist":            [x for x in range(81, 96)],\
    "Lay Healer":           [96, 97, 98],\
    "Sorcerer":             [99],\
    "Mystic":               [100]\
}

ApothecaryProfessionTable =\
{\
    "Commoner":             [x for x in range(1, 80)],\
    "Fighter":              [80, 81],\
    "Adventurer":           [82, 83, 84, 85],\
    "Thief":                [86, 87, 88, 89, 90, 91],\
    "Ranger":               [92, 93],\
    "Cleric":               [94],\
    "Animist":              [95, 96],\
    "Healer":               [97, 98],\
    "Lay Healer":           [99, 100]\
}

AstrologerProfessionTable =\
{\
    "Commoner":             [x for x in range(1, 57)],\
    "Fighter":              [57, 58],\
    "Adventurer":           [59, 60, 61, 62],\
    "Thief":                [63, 64, 65, 66, 67, 68],\
    "Ranger":               [69, 70, 71],\
    "Bard":                 [x for x in range(72, 82)],\
    "Animist":              [82],\
    "Illusionist":          [83, 84],\
    "Magician":             [85],\
    "Mentalist":            [86],\
    "Seer":                 [87, 88, 89],\
    "Mystic":               [90],\
    "Astrologer":           [x for x in range(91, 101)]\
}

CourtesanProfessionTable =\
{\
    "Commoner":             [x for x in range(1, 60)],\
    "Fighter":              [60, 61],\
    "Adventurer":           [62, 63, 64, 65],\
    "Thief":                [x for x in range(66, 86)],\
    "Bard":                 [x for x in range(86, 100)],\
    "Mystic":               [100]\
}

EmablmerProfessionTable =\
{\
    "Commoner":             [x for x in range(1, 85)],\
    "Fighter":              [85, 86],\
    "Adventurer":           [87, 88, 89, 90],\
    "Thief":                [91, 92, 93, 94, 95, 96],\
    "Cleric":               [97],\
    "Animist":              [98],\
    "Healer":               [99],\
    "Lay Healer":           [100]\
}

TechnicalProfessionTable =\
{\
    "Commoner":             [x for x in range(1, 88)],\
    "Fighter":              [88, 89],\
    "Adventurer":           [90, 91, 92, 93],\
    "Thief":                [94, 95, 96, 97, 98, 99],\
    "Alchemist":            [100]\
}

HarperProfessionTable =\
{\
    "Commoner":             [x for x in range(1, 49)],\
    "Fighter":              [49, 50],\
    "Adventurer":           [51, 52, 53, 54],\
    "Thief":                [x for x in range(55, 70)],\
    "Bard":                 [x for x in range(70, 98)],\
    "Illusionist":          [98],\
    "Seer":                 [99],\
    "Mystic":               [100]\
}

MageProfessionTable =\
{\
    "Bard":                 [x for x in range(1, 11)],\
    "Illusionist":          [x for x in range(11, 36)],\
    "Magician":             [x for x in range(36, 56)],\
    "Alchemist":            [x for x in range(56, 76)],\
    "Mentalist":            [x for x in range(76, 91)],\
    "Seer":                 [91, 92, 93, 94, 95],\
    "Sorcerer":             [96, 97],\
    "Mystic":               [98, 99],\
    "Astrologer":           [100]\
}

MerchantProfessionTable =\
{\
    "Commoner":             [x for x in range(1, 84)],\
    "Fighter":              [84, 85],\
    "Adventurer":           [86, 87, 88, 89, 90],\
    "Thief":                [91, 92, 93, 94, 95, 96],\
    "Bard":                 [97, 98],\
    "Illusionist":          [99],\
    "Mentalist":            [100]\
}

PhysicianProfessionTable =\
{\
    "Commoner":             [x for x in range(1, 82)],\
    "Fighter":              [82, 83],\
    "Adventurer":           [84, 85, 86, 87],\
    "Thief":                [88, 89, 90, 91, 92, 93],\
    "Ranger":               [94, 95, 96],\
    "Animist":              [97],\
    "Healer":               [98],\
    "Lay Healer":           [99, 100]\
}

ThespianProfessionTable =\
{\
    "Commoner":             [x for x in range(1, 63)],\
    "Fighter":              [63, 64],\
    "Adventurer":           [65, 66, 67, 68],\
    "Thief":                [69, 70, 71, 72, 73, 74],\
    "Bard":                 [x for x in range(75, 99)],\
    "Illusionist":          [99],\
    "Mystic":               [100]\
}

ThiefProfessionTable =\
{\
    "Commoner":             [x for x in range(1, 51)],\
    "Fighter":              [51, 52],\
    "Adventurer":           [x for x in range(53, 68)],\
    "Thief":                [x for x in range(68, 98)],\
    "Ranger":               [98],\
    "Bard":                 [99, 100]\
}

ClericProfessionTable =\
{\
    "Ranger":               [x for x in range(1, 11)],\
    "Cleric":               [x for x in range(1, 71)],\
    "Animist":              [x for x in range(71, 81)],\
    "Healer":               [x for x in range(81, 96)],\
    "Seer":                 [96],\
    "Lay Healer":           [97, 98],\
    "Sorcerer":             [99],\
    "Astrologer":           [100]\
}

WizardProfessionTable =\
{\
    "Bard":                 [x for x in range(1, 11)],\
    "Illusionist":          [x for x in range(11, 41)],\
    "Magician":             [x for x in range(41, 61)],\
    "Alchemist":            [x for x in range(61, 81)],\
    "Mentalist":            [x for x in range(81, 91)],\
    "Seer":                 [91, 92, 93, 94, 95],\
    "Sorcerer":             [96, 97],\
    "Mystic":               [98, 99],\
    "Astrologer":           [100]\
}

HeraldProfessionTable =\
{\
    "Fighter":              [x for x in range(1, 31)],\
    "Adventurer":           [x for x in range(31, 61)],\
    "Thief":                [x for x in range(61, 86)],\
    "Ranger":               [86, 87, 88, 89, 90],\
    "Bard":                 [91, 92, 93, 94, 95],\
    "Illusionist":          [96, 97],\
    "Magician":             [98],\
    "Mentalist":            [99],\
    "Seer":                 [100]\
}

BailiffProfessionTable =\
{\
    "Fighter":              [x for x in range(1, 31)],\
    "Adventurer":           [x for x in range(31, 61)],\
    "Thief":                [x for x in range(61, 96)],\
    "Ranger":               [96, 97, 98, 99],\
    "Bard":                 [100]\
}

ChieftainProfessionTable =\
{\
    "Fighter":              [x for x in range(1, 41)],\
    "Adventurer":           [x for x in range(41, 76)],\
    "Thief":                [x for x in range(71, 81)],\
    "Ranger":               [x for x in range(81, 90)],\
    "Bard":                 [90, 91, 92, 93, 94],\
    "Animist":              [94, 95, 96, 97, 98],\
    "Seer":                 [99],\
    "Mystic":               [100]\
}

KnightProfessionTable =\
{\
    "Fighter":              [x for x in range(1, 61)],\
    "Adventurer":           [x for x in range(61, 91)],\
    "Thief":                [91, 92, 93, 94, 95],\
    "Ranger":               [96, 97, 98, 99],\
    "Cleric":               [100]\
}

ProfessionTable =\
{\
    "Farmer":               StandardProfessionTable,\
    "Herder":               HerderProfessionTable,\
    "Cook/Servant":         StandardProfessionTable,\
    "Gladiator":            GladiatorProfessionTable,\
    "Animal Trainer":       HerderProfessionTable,\
    "Beggar/Scavenger":     BeggarProfessionTable,\
    "Cartographer/Artist":  ArtistProfessionTable,\
    "Cleric/Shaman":        ShamanProfessionTable,\
    "Fisherman":            HerderProfessionTable,\
    "Hedge Wizard/Witch":   WitchProfessionTable,\
    "Hunter/Trapper":       HerderProfessionTable,\
    "Labourer":             StandardProfessionTable,\
    "Prostitute/Pimp":      ProstituteProfessionTable,\
    "Ratter":               RatterProfessionTable,\
    "Sage/Tutor":           ScholarProfessionTable,\
    "Scribe":               ScholarProfessionTable,\
    "Soldier, Guardsman":    SoldierProfessionTable,\
    "Soldier, Mercenary":    SoldierProfessionTable,\
    "Soldier, Yeoman":       SoldierProfessionTable,\
    "Teamster":             HerderProfessionTable,\
    "Thatcher":             StandardProfessionTable,\
    "Toymaker":             StandardProfessionTable,\
    "Alchemist":            AlchemistProfessionTable,\
    "Apothecary":           ApothecaryProfessionTable,\
    "Astrologer":           AstrologerProfessionTable,\
    "Chandler":             StandardProfessionTable,\
    "Charcoaler":           HerderProfessionTable,\
    "Clothier":             StandardProfessionTable,\
    "Courtesan":            CourtesanProfessionTable,\
    "Embalmer":             EmablmerProfessionTable,\
    "Glassworker":          TechnicalProfessionTable,\
    "Harper/Skald":         HarperProfessionTable,\
    "Hideworker":           StandardProfessionTable,\
    "Innkeeper":            StandardProfessionTable,\
    "Jeweler":              TechnicalProfessionTable,\
    "Lexigrapher":          ScholarProfessionTable,\
    "Litigant":             ScholarProfessionTable,\
    "Locksmith":            TechnicalProfessionTable,\
    "Mage":                 MageProfessionTable,\
    "Mason":                StandardProfessionTable,\
    "Merchant":             MerchantProfessionTable,\
    "Metalsmith":           TechnicalProfessionTable,\
    "Miller":               StandardProfessionTable,\
    "Miner":                StandardProfessionTable,\
    "Ostler":               HerderProfessionTable,\
    "Perfumer":             StandardProfessionTable,\
    "Physician":            PhysicianProfessionTable,\
    "Pilot":                StandardProfessionTable,\
    "Potter":               StandardProfessionTable,\
    "Salter":               StandardProfessionTable,\
    "Seaman":               StandardProfessionTable,\
    "Shipwright":           StandardProfessionTable,\
    "Tentmaker":            StandardProfessionTable,\
    "Thespian":             ThespianProfessionTable,\
    "Thief":                ThiefProfessionTable,\
    "Timberwright":         StandardProfessionTable,\
    "Weaponcrafter":        TechnicalProfessionTable,\
    "Woodcrafter":          StandardProfessionTable,\
    "Cleric":               ClericProfessionTable,\
    "Court Wizard":         WizardProfessionTable,\
    "Herald":               HeraldProfessionTable,\
    "Bailiff":              BailiffProfessionTable,\
    "Chieftain":            ChieftainProfessionTable,\
    "Knight Batchelor":     KnightProfessionTable,\
    "Knight":               KnightProfessionTable\
}

def GetSocialClass(culture, roll):
    if culture in SocialClassTable:
        for socialClass in SocialClassTable[culture]:
            if roll in SocialClassTable[culture][socialClass]:
                return socialClass
    print "Unknown %s Social Class: %d" % (culture, roll)
    return "Unknown"


def GetOccupation(culture, socialClass, roll):
    if culture in OccupationTable:
        if socialClass in OccupationTable[culture]:
            for occupation in OccupationTable[culture][socialClass]:
                if roll in OccupationTable[culture][socialClass][occupation]:
                    return occupation
    print "Unknown %s %s occupation: %d" % (culture, socialClass, roll)
    return "Unknown"

def GetProfession(occupation, roll):
    if occupation in ProfessionTable:
        for profession in ProfessionTable[occupation]:
            if roll in ProfessionTable[occupation][profession]:
                return profession
    print "Unknown %s profession %d" % (occupation, roll)
    return "Unknown"
