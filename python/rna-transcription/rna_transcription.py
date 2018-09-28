RNA_TRANSLATE_LOOKUP = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U",
}

def to_rna(dna_strand):
    return str.join("", [RNA_TRANSLATE_LOOKUP[c] for c in dna_strand])
