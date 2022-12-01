# %%
import heapq
import copy

input_n = int(input())

input_list = [0]*input_n
value_list = [0]*input_n

for i in range(input_n):
    input_list[i] = int(input())

value_list = copy.deepcopy(input_list)
heapq.heapify(value_list)
value_list = ['x'] + value_list


print(input_list)
print(value_list)

# %%
class Huff_node():    
    def __init__(self, freq, left_node=None, right_node=None):
        self.freq = freq
        self.left_node = left_node
        self.right_node = right_node
        self.zero_one = ''
        self.final_code = ''
        
    def __lt__(self, other):
        return self.freq < other.freq

    def __gt__(self, other):
        return self.freq > other.freq

# %%
class Min_heap():
    def __init__(self, array):
        self.arr = array
        self.heap_size = len(self.arr) -1

    def build_min_heap(self):
        for i in range(1, (self.heap_size//2)+1)[::-1]:
            self.min_heapify(i)
        return self
    
    def min_heapify(self, i):
        smallest = i
        l = (2 * i)
        r = (2 * i) + 1
        
        if l < self.heap_size and self.arr[l].freq < self.arr[i].freq:
            smallest = l
        
        if r <= self.heap_size and self.arr[r].freq < self.arr[smallest].freq:
            smallest = r
        
        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i] ## swapping
            self.min_heapify(smallest)
            



            
class Min_priority_que(Min_heap):
    
    def return_minimum_value(self):
        print('node:', self.arr[1], 'freq:', self.arr[1].freq)
        return self.arr[1]
    
    def return_min_heap_extract(self):       
        print('------------extract----------')
        self.show_node_values()
        # print(self.arr)
        self.arr[1:] = sorted(self.arr[1:], key = lambda x: x.freq)
        min_node = self.arr[1]
        self.arr[1] = self.arr[self.heap_size] ## 맨 위 노드와 맨 아래 노드 바꾸기
        # min_node = min(self.arr[1:])
        print(min_node.freq)
        print('-----------------------------')
        
        
        self.heap_size -= 1
        self.arr = self.arr[1:]
        self.min_heapify(1)
        return min_node
    
    def min_heap_decrease_key(self, i, new_node): ## i는 value를 증가시킬 target의 index
        
        if new_node.freq > self.arr[i].freq:
            print("Current value is already smaller than new value")
            return None
        
        self.arr[i] = new_node
        
        while i > 1 and self.arr[i // 2].freq > self.arr[i].freq:
            self.arr[i], self.arr[i // 2] = self.arr[i // 2], self.arr[i]
            i = i // 2
       
        self.arr[1:] = sorted(self.arr[1:], key = lambda x: x.freq)

            
    
    def min_heap_insert(self, key):
        self.heap_size += 1
        self.arr += [Huff_node(float("inf"))]
        self.min_heap_decrease_key(self.heap_size, key)
        

    def show_node_values(self):
        for node in self.arr[1:]:
            print('-', node, ':', node.freq)
            try: 
                print('---', node.left_node, ':', node.left_node.freq)
                print('---', node.right_node, ':', node.right_node.freq)
            except:
                pass
            


# %%
node_list = ['x'] + [0] * (len(value_list)-1)
for i in range(1, len(value_list)):  ## 1~6
    node_list[i] = Huff_node(value_list[i])
    
node_que = Min_priority_que(node_list).build_min_heap()
print(node_que.arr)
node_que.show_node_values()

# %%
print(value_list)

for i in range(len(node_que.arr) - 2):
    left_node = node_que.return_min_heap_extract()
    left_node.zero_one = 0
    
    right_node = node_que.return_min_heap_extract()
    right_node.zero_one = 1
    new_node = Huff_node(left_node.freq + right_node.freq, left_node, right_node)
    print('*** whole freq:', new_node.freq)
    print('*** left freq:', new_node.left_node.freq)
    print('*** right freq:', new_node.right_node.freq)
    
    node_que.min_heap_insert(new_node)
    
    node_que.show_node_values()
    
    


# %%
final_code_list = []
def make_final_code(node, code = ''):
    new_code = code + str(node.zero_one)
    
    if node.left_node:
        make_final_code(node.left_node, new_code)
        
    if node.right_node:
        make_final_code(node.right_node, new_code)
    
    if (not node.left_node) and (not node.right_node):
        node.final_code = new_code
        final_code_list.append((node.freq, node.final_code))
        print(new_code)

print(node_que.arr)       
root_node = max(node_que.arr)

make_final_code(root_node)
print(final_code_list)
for original_value in input_list:
    for value, code in final_code_list:
        if original_value == value:
            print(code)


