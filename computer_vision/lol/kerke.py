'''def input_values():
    input_data = input().split()
    input_data = list(map(int, input_data))
    elem_number, full_volume = input_data
    segments = []
    for i in range(elem_number):
        segment = input().split()
        segment = list(map(int, segment))
        segments.append(segment)

    return full_volume, segments


def find_max_cost(volume, segments):
    segments.sort(key=lambda x: x[0]/x[1], reverse=True)
    print(segments)
    added_volume = 0
    total_cost = 0
    for price, volume_s in segments:
        if added_volume + volume_s <= volume:
            added_volume += volume_s
            total_cost += volume_s * price
        elif added_volume + volume_s > volume:
            add_volume = volume - added_volume
            added_volume += add_volume
            total_cost += round(price/volume_s*add_volume, 3)

        if added_volume >= volume:
            return total_cost
    return total_cost


volume, segments = input_values()
a = find_max_cost(25, [[30, 10], [16, 10], [123, 3]])



def answer(data):
    print(len(data))
    data = list(map(str, data))
    print(' '.join(data))
'''

data = input()


def give_data_dict():
    data_set = set(list(data))
    data_dict = {}
    for i in data_set:
        data_dict[i] = data.count(i)
    # data_sorted = list(data_set)
    # data_sorted.sort(key=lambda x: data_dict[x])
    return data_dict


def find_two(data_dict):
    data_sorted = list(data_dict.keys())
    data_sorted.sort(key=lambda x: data_dict[x])
    return data_sorted[:2]


data_dict = give_data_dict()
print(data_dict)
tree_values = []
ch = 0
while len(data_dict) > 1:
    two = find_two(data_dict)
    data_dict[two[0]+two[1]] = data_dict[two[0]] + data_dict[two[1]]
    data_dict.pop(two[0])
    data_dict.pop(two[1])
    tree_values.append(())
    print(data_dict)


class BinaryTree:
    def __init__(self):
        self._storage = []

    def put_left(self):
        pass

'''
data_keys = {}
translated_word = ''
for i in data:
    translated_word += data_keys[i]

print(translated_word)
for key, value in data_keys.items():
    print(f'{key}: {value}')
'''


