from rna_to_amino_acid import translate_rna_triplet
from dna_to_rna import dna_to_rna, sequence_to_triplets
from amino_acid_to_proteins import amino_acid_to_proteins
from file_utils import read_text


def main():
    dna = read_text("data/dna.txt")
    rna = dna_to_rna(dna)
    (triplets, remainder) = sequence_to_triplets(rna)
    
    amino_acids = []
    for triplet in triplets:
        amino_acids.append(translate_rna_triplet(triplet))
    
    proteins = amino_acid_to_proteins(amino_acids)
    
    print("Proteins:")
    print("\n".join(["".join(protein) for protein in proteins]))
    print(f"Remaining RNA: {remainder}")


if __name__ == "__main__":
    main()