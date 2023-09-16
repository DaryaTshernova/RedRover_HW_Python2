def count_positives_sum_negatives(arr):
    arr_n = []
    arr_p = []
    for i in arr:
        if i < 0:
            arr_n.append(i)
        if i > 0:
            arr_p.append(i)
    return [len(arr_p), sum(arr_n)]

