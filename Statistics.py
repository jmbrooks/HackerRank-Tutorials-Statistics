import statistics as stat

example_list = [5, 1, 4, 3, 2, 6, 7, 9, 10, 11, 15, 0, -5, 2]

mean = stat.mean(example_list)
print(mean)

median = stat.median(example_list)
print(median)

mode = stat.mode(example_list)
print(mode)

stddev = stat.stdev(example_list)
print(stddev)

variance = stat.variance(example_list)
print(variance)
