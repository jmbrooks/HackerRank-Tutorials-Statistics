def weighted_mean(values: list, weights: list) -> float:
	sum_weighted_vals = 0
	sum_weights = 0
	for i in range(len(values)):
		value = values[i]
		weight = weights[i]
		sum_weighted_vals += value * weight
		sum_weights += weight
	result = sum_weighted_vals / sum_weights
	return result


n = int(input())
x = [int(token) for token in input().split()]
w = [int(token) for token in input().split()]
print(round(weighted_mean(x, w), 1))