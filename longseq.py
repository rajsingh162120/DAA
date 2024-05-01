def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)
    
    # Initialize table to store lengths of LCS
    lcs = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Bottom-up approach: compute lengths of LCS iteratively
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
    
    # Reconstruct the LCS
    lcs_str = ""
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str = X[i - 1] + lcs_str
            i -= 1
            j -= 1
        elif lcs[i - 1][j] > lcs[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    if len(lcs_str) == 0:
        return "No common subsequence found."
    else:
        return lcs_str

# Taking string inputs from the user
X = input("Enter the first string: ")
Y = input("Enter the second string: ")

print("Longest Common Subsequence: ", longest_common_subsequence(X, Y))
