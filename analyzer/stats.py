import math

from parse import parse_seed_data

def variance(running_average, data_point, n):
    return ((running_average - data_point)**2)/(n + 1)


def seed_average(data_list):
    return sum(data_list)/len(data_list), len(data_list)

def main(data_point):
    data = parse_seed_data("aws_cpu_usage.json")
    average, n = seed_average(data)
    var = variance(average, 6, n)
    sigma = math.sqrt(var)
    print("sigma : ", sigma)
    print("average : ", average)
    if data_point > (3*sigma) + average:
        print("yes")
    elif data_point < average - (3*sigma):
        print("yes")
    else:
        print("no")


main(6.4)