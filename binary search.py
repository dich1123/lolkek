data = input().split()
data_list = [int(i) for i in data[1:]]
data2 = input().split()
keys_list = [int(i) for i in data2[1:]]


def binary_search(values, key):
    left = 0
    right = len(values)
    mid = int((left+right)/2)
    while True:
        if values[mid] == key:
            return mid + 1
        if right - left == 1:
            return -1
        if key > values[mid]:
            left = mid
            mid = int((left + right) / 2)
            continue
        if key < values[mid]:
            right = mid
            mid = int((left + right) / 2)


answer = [binary_search(data_list, i) for i in keys_list]
print(' '.join([str(i) for i in answer]))




