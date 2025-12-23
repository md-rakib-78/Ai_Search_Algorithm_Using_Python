import math

def alpha_beta(depth, node_index, is_max, values, alpha, beta,treeDepth):
    if depth == treeDepth:
        return values[node_index]

    if is_max:
        best = -math.inf
        for i in range(0, 2):
            val = alpha_beta(depth + 1, node_index * 2 + i, False, values, alpha, beta,treeDepth)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                print(f"Pruning at depth {depth} (Max node)")
                break
        return best

    else:
        best = math.inf
        for i in range(0, 2):
            val = alpha_beta(depth + 1, node_index * 2 + i, True, values, alpha, beta,treeDepth)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                print(f"Pruning at depth {depth} (Min node)")
                break
        return best


scores = [3, 5, 6, 9, 1, 2, 0, -1]
treeDepth=math.log(len(scores),2)
print("Optimal Value:", alpha_beta(0, 0, True, scores, -math.inf, math.inf,treeDepth))
