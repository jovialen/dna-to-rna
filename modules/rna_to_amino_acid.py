import csv


def load_mapping(filename):
    mapping = {}
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            triplet = row['TRIPLET']
            amino_acid = row['AMINO']
            if triplet and amino_acid:
                mapping[triplet] = amino_acid
    return mapping


mapping = load_mapping('data/dna-to-amino-acid.csv')


def translate_rna_triplet(rna_triplet):
    return mapping.get(rna_triplet, 'Unknown')


if __name__ == "__main__":
    while True:
        rna_triplet = input("Enter an RNA triplet (or 'exit' to quit): ").strip().upper()
        
        if rna_triplet == 'EXIT':
            break
        
        amino_acid = translate_rna_triplet(rna_triplet)
        
        if amino_acid == 'Unknown':
            print("Invalid RNA triplet. Please enter a valid RNA triplet.")
        else:
            print(f"The amino acid for {rna_triplet} is {amino_acid}")