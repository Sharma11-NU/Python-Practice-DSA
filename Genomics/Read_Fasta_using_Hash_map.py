# pattern = HASH Map + Linear Scan
# Associate ID with value

from collections import Counter

def read_fasta(filepath):
    proteins = {}      # why { } inside read_fast function
    current_id = None  # why current id none, not 0

    with open (filepath) as file:
        for line in file:   # O(n)
            line = line.strip()

            if not line:
                continue
            if line.startswith(">"):
                current_id = line[1: ].split()[0] # line start with ">", splice > only keep [0], that is ID
                proteins[current_id]= " "   # remove > only keep "WP_012345678.1 hypothetical protein ABC"
                                                  # now, index [0] = wp_o12345678
            else:
                proteins[current_id] += line
    return proteins

if __name__ == "__main__":
    proteins = read_fasta("data/protein.faa")
    print("Number of proteins: ", len(proteins))
    lengths = [len(seq) for seq in proteins.values()]
    print("Longest protein:", max(lengths))
    print("shortest of protein: ", min(lengths))

    aa_counter = Counter()         # using HASH Map counter
    for seq in proteins.values():  # each element in protein = values
        aa_counter.update(seq)

    print("Top 5 amino acids:")
    for aa, count in aa_counter.most_common(5):
        print(aa, count)
        