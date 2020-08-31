class Heap:  # in fact it's priority queue using heap

    def __init__(self):
        self.tree = []

    def insert(self, data):
        self.tree.append(data)
        self.sift_up()

    def sift_up(self):
        descendant_id = len(self.tree) - 1
        descendant = self.tree[descendant_id]
        ancestor_id = int((descendant_id - 1) / 2)
        ancestor = self.tree[ancestor_id]
        while True:
            if descendant > ancestor:
                self.tree[descendant_id], self.tree[ancestor_id] = self.tree[ancestor_id], self.tree[descendant_id]
                descendant_id = ancestor_id
                ancestor_id = int((descendant_id - 1) / 2)
                descendant = self.tree[descendant_id]
                ancestor = self.tree[ancestor_id]
            if descendant <= ancestor:
                break

    def extract_max(self):
        if not self.tree:
            return
        self.tree[0], self.tree[-1] = self.tree[-1], self.tree[0]
        max_value = self.tree.pop()
        self.sift_down()
        return max_value

    def sift_down(self):
        if not self.tree:
            return
        ancestor_id = 0
        ancestor = self.tree[ancestor_id]
        descendant, descendant_id = self._find_descendant(ancestor_id)
        while True:
            if descendant > ancestor:
                self.tree[descendant_id], self.tree[ancestor_id] = self.tree[ancestor_id], self.tree[descendant_id]
                ancestor_id = descendant_id
                descendant, descendant_id = self._find_descendant(ancestor_id)

            if descendant <= ancestor:
                break

    def _find_descendant(self, ancestor_id) -> tuple:
        descendant_id_left = ancestor_id * 2 + 1
        descendant_id_right = ancestor_id * 2 + 2
        if descendant_id_left >= len(self.tree):
            return self.tree[ancestor_id], ancestor_id
        if descendant_id_right >= len(self.tree):
            return self.tree[descendant_id_left], descendant_id_left
        if self.tree[descendant_id_left] >= self.tree[descendant_id_right]:
            descendant = self.tree[descendant_id_left]
            descendant_id = descendant_id_left
        else:
            descendant = self.tree[descendant_id_right]
            descendant_id = descendant_id_right
        return descendant, descendant_id


heap = Heap()
amount = int(input())
for _ in range(amount):
    in_data = input()
    if 'Insert' in in_data:
        value = int(in_data.split()[-1])
        heap.insert(value)
    else:
        print(heap.extract_max())


# heap = Heap()
# test_ins = [2, 3, 18, 15, 18, 12, 12, 2]
# test_out = 3
# for test in test_ins:
#     heap.insert(test)
#     print(heap.tree)
# for i in range(test_out):
#     print(heap.extract_max())
#     print(heap.tree)
