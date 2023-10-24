from dna_to_rna import dna_to_rna, sequence_to_triplets
from file_utils import read_json


def dna_test(dna, correct_rna, correct_triplets, correct_remainder):
    rna = dna_to_rna(dna)
    if rna != correct_rna:
        print(f"FAIL: {dna} should be {correct_rna}, got {rna}")
        return False
    (triplets, remainder) = sequence_to_triplets(rna)
    if triplets != correct_triplets:
        print(f"FAIL: {dna} should have {correct_triplets}, got {triplets}")
        return False
    if remainder != correct_remainder:
        print(f"FAIL: {dna} should have {correct_remainder}, got {remainder}")
        return False
    return True


def dna_test_file(file_path):
    tests = read_json(file_path)
    for test in tests:
        if not dna_test(test["dna"], test["rna"], test["triplets"], test["remainder"]):
            print("TESTS FAILED")
            return
    print("ALL TESTS PASSED")


if __name__ == "__main__":
    dna_test_file("data/dna_tests.json")