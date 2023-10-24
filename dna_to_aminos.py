from rna_to_amino_acid import translate_rna_triplet
from dna_to_rna import dna_to_rna, sequence_to_triplets
from file_utils import read_text


def main():
    dna = read_text("data/dna.txt")
    rna = dna_to_rna(dna)
    (triplets, _) = sequence_to_triplets(rna)
    
    amino_acids = []
    for triplet in triplets:
        amino_acids.append(translate_rna_triplet(triplet))
    
    print(", ".join(amino_acids))


if __name__ == "__main__":
    main()