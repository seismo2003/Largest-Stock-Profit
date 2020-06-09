### Stock price problem
def max_returns(prices):
    """
    Calculate maxiumum possible return

    Args:
       prices(array): array of prices
    Returns:
       int: The maximum profit possible
    """

    matrix = [[0 for _ in range(len(prices))] for _ in range(len(prices))]

    n_a = 0
    n_b = 1
    i = 1

    while i < len(prices):
        while n_b < len(prices):
            if prices[n_b] > prices[n_a]:
                matrix[n_a][n_b] = max(prices[n_b] - prices[n_a], matrix[n_a + 1][n_b])
            else:
                matrix[n_a][n_b] = matrix[n_a][n_b-1]
            n_a += 1
            n_b += 1
        i += 1
        n_a = 0
        n_b = n_a + i

    return matrix[0][-1]

def test_function(test_case):
    prices = test_case[0]
    solution = test_case[1]
    output = max_returns(prices)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

prices = [2, 2, 7, 9, 9, 12, 18, 23, 34, 37, 45, 54, 78]
solution = 76
test_case = [prices, solution]
test_function(test_case)
