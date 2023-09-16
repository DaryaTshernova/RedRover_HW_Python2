# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

a = 355
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
f = 3
def count_positives_sum_negatives(arr):
    arr_n = []
    arr_p = []
    for i in arr:
        if i < 0:
            arr_n.append(i)
        if i > 0:
            arr_p.append(i)
    return [len(arr_p), sum(arr_n)]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
