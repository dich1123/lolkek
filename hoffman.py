import sys
text = list(input(''))
text_set = set(text)
if len(text_set) == 1:
    print(1, len(text))
    print(f'{text[0]}: 0')
    print(''.join(text).replace(text[0], '0'))
    sys.exit(0)
values = {}
for key in text_set:
    values[key] = text.count(key)


def priority_queue(values_dict):
    sorted_values_dict = {k: values_dict[k] for k in sorted(values_dict, key=values_dict.get)}
    sorted_list = list(sorted_values_dict)
    if len(sorted_list) == 1:
        return sorted_values_dict
    a = {(sorted_list[0], sorted_list[1]): values_dict[sorted_list[0]]+values_dict[sorted_list[1]]}
    return a


while len(values) > 1:
    b = priority_queue(values)
    b_v = tuple(b.keys())[0]
    values.pop(b_v[0])
    values.pop(b_v[1])
    values.update(b)
graph = list(values.keys())[0]

answ = {}


def open_graph(gg):
    if gg not in answ:
        answ[gg] = ''
    left = gg[0]
    right = gg[1]
    answ[left] = answ[gg] + '0'
    answ[right] = answ[gg] + '1'
    if isinstance(left, tuple) and isinstance(right, tuple):
        return open_graph(left), open_graph(right)
    if isinstance(left, tuple):
        return open_graph(left)
    if isinstance(right, tuple):
        return open_graph(right)


open_graph(graph)
answer = {}
for key, value in answ.items():
    if not isinstance(key, tuple):
        answer[key] = value

answer_text = ''
for i in text:
    answer_text += answer[i]

print(len(answer), len(answer_text))
for key, value in answer.items():
    print(f'{key}: {value}')
print(answer_text)
