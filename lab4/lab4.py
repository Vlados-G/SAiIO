def main():
    weights = [3, 4, 5, 8, 9]
    prices = [1, 6, 4, 7, 6]

    count = len(weights)
    maxWeight = 13

    A = [[0 for _ in range(maxWeight + 1)] for _ in range(count + 1)]

    for k in range(count + 1):
        for s in range(maxWeight + 1):
            if k == 0 or s == 0:
                A[k][s] = 0
            else:
                if s >= weights[k - 1]:
                    A[k][s] = max(A[k - 1][s], A[k - 1][s - weights[k - 1]] + prices[k - 1])
                else:
                    A[k][s] = A[k - 1][s]

    result = trace_result(A, weights, count, maxWeight)

    print("\n\nOPT:")
    for integer in result:
        print(integer)


def trace_result(A, weights, k, s):
    if A[k][s] == 0:
        return []
    if A[k - 1][s] == A[k][s]:
        return trace_result(A, weights, k - 1, s)
    else:
        sub_result = trace_result(A, weights, k - 1, s - weights[k - 1])
        sub_result.append(k)
        return sub_result


if __name__ == "__main__":
    main()
