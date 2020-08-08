num_to_word = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth"
]

verse = [
    "twelve Drummers Drumming,",
    "eleven Pipers Piping,",
    "ten Lords-a-Leaping,",
    "nine Ladies Dancing,",
    "eight Maids-a-Milking,",
    "seven Swans-a-Swimming,",
    "six Geese-a-Laying,",
    "five Gold Rings,",
    "four Calling Birds,",
    "three French Hens,",
    "two Turtle Doves, and",
    "a Partridge in a Pear Tree.",
]

base_verse = "On the {} day of Christmas my true love gave to me: {}"

def recite(start_verse, end_verse):
    yield from (gen_verse(i) for i in range(start_verse, end_verse+1))

def gen_verse(index):
    return base_verse.format(num_to_word[index-1], " ".join(verse[12-index:]))
