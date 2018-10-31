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



CATEGORY_FUNCS = {
    YACHT: score_yacht
}

def score(dice, category):
    return CATEGORY_FUNCS.get(category, lambda: -1)(dice)
