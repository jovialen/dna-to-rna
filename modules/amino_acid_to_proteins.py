STOP_AMINO = "$"


def amino_acid_to_proteins(amino_acids):
    proteins = []
    build_protein = []

    for amino in amino_acids:
        if amino == STOP_AMINO:
            if len(build_protein) > 0:
                proteins.append(build_protein)
                build_protein = []
        else:
            build_protein.append(amino)

    if len(build_protein) > 0:
        proteins.append(build_protein)

    return proteins