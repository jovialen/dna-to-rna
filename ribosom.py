import argparse, csv


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

def dna_base_to_rna_compliment(base: str) -> str:
    """Convert a DNA base to the matching RNA base

    Args:
        base (str): The DNA base

    Returns:
        str: The complimentary RNA base, or None if `base` is invalid
    """
    
    compliments = {
        "A": "U",
        "T": "A",
        "G": "C",
        "C": "G",
    }
    return compliments.get(base.upper())


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
    return (triplets, sequence[count*3:])

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

def amino_acid_to_proteins(amino_acids: list[str]) -> list[list[str]]:
    """Convert amino acids to proteins

    Args:
        amino_acids (list[str]): List of the amino acids

    Returns:
        list[list[str]]: List of the proteins produced
    """
    
    proteins = []
    build_protein = ""

    for amino in amino_acids:
        if amino == STOP_AMINO:
            if build_protein != "":
                proteins.append(build_protein)
                build_protein = ""
        else:
            build_protein += amino

    if build_protein != "":
        proteins.append(build_protein)

    return proteins

# MAIN

def main(args):
    dna = read_text(args.path)
    rna = dna_to_rna(dna)
    (triplets, remainder) = sequence_to_triplets(rna)
    amino_acids = triplets_to_amino_acids(triplets)
    proteins = amino_acid_to_proteins(amino_acids)
    
    if args.out:
        with open(args.out, "w") as f:
            f.write("Proteins:\n  ")
            f.write("\n  ".join(proteins))
            f.write(f"\nRemainder: {remainder}")
    else:
        print("Proteins:\n ", "\n  ".join(proteins))
        print(f"Remainder: {remainder}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Ribosom", description="Convert a DNA sequence to the proteins they code")
    parser.add_argument("path", type=str)
    parser.add_argument("--out", type=str)
    args = parser.parse_args()
    
    main(args)
