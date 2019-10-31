# Score categories
# Change the values as you see fit
YACHT = 'YACHT'
ONES = 'ONES'
TWOS = 'TWOS'
THREES = 'THREES'
FOURS = 'FOURS'
FIVES = 'FIVES'
SIXES = 'SIXES'
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'


def score_yacht(dice):
    return 50 if all(d == dice[0] for d in dice) else 0


def filter_number(dice, number):
    return [d for d in dice if d == number]


def score_number(dice, number):
    return sum(filter_number(dice, number))


def score_full_house(dice):
    unique_dice = list(set(dice))
    if len(unique_dice) != 2:
        return 0

    groups = [filter_number(dice, d) for d in unique_dice]
    lengths = list(map(len, groups))
    if not (2 in lengths and 3 in lengths):
        return 0

    return sum(sum(g) for g in groups)





CATEGORY_FUNCS = {
    YACHT: score_yacht,
    ONES: lambda d: score_number(d, 1),
    TWOS: lambda d: score_number(d, 2),
    THREES: lambda d: score_number(d, 3),
    FOURS: lambda d: score_number(d, 4),
    FIVES: lambda d: score_number(d, 5),
    SIXES: lambda d: score_number(d, 6),
    FULL_HOUSE: score_full_house,
}

def score(dice, category):
    return CATEGORY_FUNCS.get(category, lambda: -1)(dice)
