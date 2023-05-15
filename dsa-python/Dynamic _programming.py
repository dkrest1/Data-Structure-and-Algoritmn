# longest common subsequence

def lcs(seq1: str, seq2: str):
    memo = {}

    def recursive(seq1, seq2, idx1, idx2):
        key = (idx1, idx2)
        if key in memo:
            return memo[key]
        elif idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0

        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recursive(seq1, seq2, idx1+1, idx2+1)
        else:
            option1 = recursive(seq1, seq2, idx1+1, idx2)
            option2 = recursive(seq1, seq2, idx1, idx2+2)
            memo[key] = max(option1, option2)


a = [[]]
for i in range(len(a)):
    print("Ik" + i)
