# 1. LIS
def longest_increasing_subsequence(sequence):
    """
    Dynamic Programming Algorithm for
    counting the length of longest increasing subsequence
    type sequence: list[int]
    rtype: int
    """
    length = len(sequence)
    counts = [1 for _ in range(length)]
    for i in range(1, length):
        for j in range(0, i):
            if sequence[i] > sequence[j]:
                counts[i] = max(counts[i], counts[j] + 1)
                print(counts)
    return max(counts)

# 2. LCS
def longest_common_subsequence(s_1, s_2):
    """
    :param s1: string
    :param s2: string
    :return: int
    """
    m = len(s_1)
    n = len(s_2)

    mat = [[0] * (n + 1) for i in range(m + 1)]
    # mat[i][j] : contains length of LCS of s_1[0..i-1] and s_2[0..j-1]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                mat[i][j] = 0
            elif s_1[i - 1] == s_2[j - 1]:
                mat[i][j] = mat[i - 1][j - 1] + 1
            else:
                mat[i][j] = max(mat[i - 1][j], mat[i][j - 1])

    return mat[m][n]

# 3.Knapsack
class Item:

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def get_maximum_value(items, capacity):
    dp = [0] * (capacity + 1)
    for item in items:
        for cur_weight in reversed(range(item.weight, capacity+1)):
            dp[cur_weight] = max(dp[cur_weight], item.value + dp[cur_weight - item.weight])
    return dp[capacity]

# 4. Matrix Chain Multiplication
'''
Dynamic Programming
Implementation of matrix Chain Multiplication
Time Complexity: O(n^3)
Space Complexity: O(n^2)
'''
INF = float("inf")


def matrix_chain_order(array):
    """Finds optimal order to multiply matrices
    array -- int[]
    """
    n = len(array)
    matrix = [[0 for x in range(n)] for x in range(n)]
    sol = [[0 for x in range(n)] for x in range(n)]
    for chain_length in range(2, n):
        for a in range(1, n-chain_length+1):
            b = a+chain_length-1

            matrix[a][b] = INF
            for c in range(a, b):
                cost = matrix[a][c] + matrix[c+1][b] + array[a-1]*array[c]*array[b]
                if cost < matrix[a][b]:
                    matrix[a][b] = cost
                    sol[a][b] = c
    return matrix, sol
# Print order of matrix with Ai as matrix

def print_optimal_solution(optimal_solution,i,j):
    """Print the solution
    optimal_solution -- int[][]
    i -- int[]
    j -- int[]
    """
    if i==j:
        print("A" + str(i),end = " ")
    else:
        print("(", end=" ")
        print_optimal_solution(optimal_solution, i, optimal_solution[i][j])
        print_optimal_solution(optimal_solution, optimal_solution[i][j]+1, j)
        print(")", end=" ")