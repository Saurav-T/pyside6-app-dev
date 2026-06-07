def alpha_beta(depth, index, is_max, values, alpha, beta):

    if depth == 0:
        return values[index]

    if is_max:
        best = float('-inf')

        for i in range(2):
            val = alpha_beta(depth-1, index*2 + i, False, values, alpha, beta)
            best = max(best, val)

            alpha = max(alpha, best)

            if alpha >= beta:
                break  # PRUNE

        return best

    else:
        best = float('inf')

        for i in range(2):
            val = alpha_beta(depth-1, index*2 + i, True, values, alpha, beta)
            best = min(best, val)

            beta = min(beta, best)

            if alpha >= beta:
                break  # PRUNE

        return best


values = [3, 5, 2, 9]
print(alpha_beta(2, 0, True, values, float('-inf'), float('inf')))