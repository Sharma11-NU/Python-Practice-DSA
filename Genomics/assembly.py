from Read_Fasta_using_Hash_map import read_fasta

proteins = read_fasta("data/protein.faa")
seq_ids = list(proteins.keys())

seq1 = proteins[seq_ids[0]].replace(" ", "").replace("\n", "")
seq2 = proteins[seq_ids[5]].replace(" ", "").replace("\n", "")

def lcs(s1, s2):                      # Alighnment  # Fabonicci pattern
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]                # Dynamic Programming

if __name__ == "__main__":
    print(f"Comparing {seq_ids[0]} vs {seq_ids[1]}")
    print("SEQ1 length:", len(seq1))
    print("SEQ2 length:", len(seq2))
    print("LCS length:", lcs(seq1, seq2))









