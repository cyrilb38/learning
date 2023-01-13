# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    bag_values = []
    bag_weight = []
    
    values_per_weight = [v/w for v,w in zip(values, weights)]
    weights = [w for _,w in sorted(zip(values_per_weight,weights))]
    values_per_weight = sorted(values_per_weight)
    
    # write your code here
    while (sum(bag_weight) < capacity) and (len(weights) > 0):
        capacity_left = capacity - sum(bag_weight)
        # last slot available
        if weights[-1] > capacity_left:
            bag_values.append(values_per_weight[-1] * capacity_left)
            bag_weight.append(capacity_left)

        else :
            value_f_w = values_per_weight.pop()
            w = weights.pop()
            bag_values.append(value_f_w * w)
            bag_weight.append(w)
    return sum(bag_values)


# print(get_optimal_value(50, [20, 50, 30], [60, 100, 120]))

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
