import argparse
import csv
import random


def read_text(path: str) -> str:
    """Read a file to a text string

    Args:
        path (str): Path to the file

    Returns:
        str: The contents of the file
    """
    
    with open(path, "r") as f:
        return f.read().replace("\n", "")

# DNA TO RNA

COMPLIMENTS = {
    "A": "U",
    "T": "A",
    "G": "C",
    "C": "G",
}

def dna_base_to_rna_compliment(base: str) -> str:
    """Convert a DNA base to the matching RNA base

    Args:
        base (str): The DNA base

    Returns:
        str: The complimentary RNA base, or None if `base` is invalid
    """
    
    return COMPLIMENTS.get(base.upper())


def dna_to_rna(dna: str) -> str:
    """Convert a DNA string into the matching RNA string

    Args:
        dna (str): The string containing the DNA sequence

    Returns:
        str: The complimentary RNA string
    """
    
    rna = ""
    for char in dna:
        base = dna_base_to_rna_compliment(char)
        if base == None:
            print(f"FAILED: {char} is not a dna base")
            continue
        rna += base
    return rna

# SPLIT INTO TRIPLETS

def sequence_to_triplets(sequence: str) -> tuple[list[str], str]:
    """Split a DNA/RNA sequence into triplets

    Args:
        sequence (str): The sequence to split

    Returns:
        tuple[list[str], str]: List of the triplets of the sequence and the remainder of the sequence
    """
    
    count = len(sequence) // 3
    triplets = []
    for i in range(count):
        triplets.append(sequence[3 * i:3 * i + 3])
    remainder = sequence[count * 3:]
    return (triplets, remainder)

# TRIPLETS TO AMINO ACIDS

def load_mapping(filename):
    mapping = {}
    with open(filename, 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        for row in reader:
            triplet = row['TRIPLET']
            amino_acid = row['AMINO']
            if triplet and amino_acid:
                mapping[triplet] = amino_acid
    return mapping


MAPPING = load_mapping('data/dna-to-amino-acid.csv')
STOP_AMINO = "$"


def translate_rna_triplet(rna_triplet):
    return MAPPING.get(rna_triplet, 'Unknown')


def triplets_to_amino_acids(triplets: list[str]):
    amino_acids = []
    for triplet in triplets:
        amino_acids.append(translate_rna_triplet(triplet))
    return amino_acids

# AMINO ACIDS TO PROTEINS

def amino_acid_to_proteins(amino_acids: list[str]) -> list[str]:
    """Convert amino acids to proteins

    Args:
        amino_acids (list[str]): List of the amino acids

    Returns:
        list[str]: List of the proteins produced
    """
    
    return filter(lambda protein: protein != "", "".join(amino_acids).split(STOP_AMINO))

# MUTATION

def mutate_rna(rna: str) -> str:
    """Mutate a RNA string

    Args:
        rna (str): The RNA to mutate

    Returns:
        str: The mutated RNA string
    """

    mutation = random.randint(0, 2)
    at = random.randint(0, len(rna))
    base = random.choice(list(COMPLIMENTS.values()))
    
    if mutation == 0:
        print("Replacing base")
        return rna[:at] + base + rna[at + 1:]
    elif mutation == 1:
        print("Inserting base")
        return rna[:at] + base + rna[at:]
    else:
        print("Removing base")
        return rna[:at] + rna[at + 1:]

# MAIN

def dna_to_proteins(dna: str, mutate: bool = False) -> (list[str], str):
    rna = dna_to_rna(dna)
    
    if mutate:
        rna = mutate_rna(rna)

    (triplets, remainder) = sequence_to_triplets(rna)
    amino_acids = triplets_to_amino_acids(triplets)
    proteins = amino_acid_to_proteins(amino_acids)
    return (proteins, remainder)


def main(args):
    dna = read_text(args.path)
    (proteins, remainder) = dna_to_proteins(dna)
    proteins = "\n  ".join(proteins)

    print("Proteins:\n ", proteins)
    print(f"Remainder: {remainder}")
    
    if args.mutate:
        (mutated_protein, mutated_remainder) = dna_to_proteins(dna, mutate=True)
        mutated_protein = "\n  ".join(mutated_protein)
        
        count = sum(1 for a, b in zip(proteins, mutated_protein) if a != b)

        print("Mutated proteins:\n ", mutated_protein)
        print(f"Mutated remainder: {mutated_remainder}")
        print(f"Different amino acids from original: {count} ({count / len(proteins) * 100:,.1f}%)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Ribosom", description="Convert a DNA sequence to the proteins they code")
    parser.add_argument("path", type=str)
    parser.add_argument("--mutate", action='store_true')
    args = parser.parse_args()

    main(args)
