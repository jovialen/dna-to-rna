from file_utils import read_csv_to_dict


AMINO_ACIDS = read_csv_to_dict("data/dna-to-amino-acid.csv")


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
