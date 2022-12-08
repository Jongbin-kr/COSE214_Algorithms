## graph node with distance and predecessor
class Graph_node():
    
    def __init__(self, vertex_name):
        self.vertex_name = vertex_name
        self.edge_dict = {} ## dest: dist
        self.pred = '' ## predecessor vertex name for min_distance
        self.min_dist = 0


## min-priority que 

class Min_heap():
    def __init__(self, graph_node_list):
        self.arr = graph_node_list
        self.heap_size = len(self.arr) -1 ## -1 because index 0 in node list is 'X'. we don't use the zero-index value.

    def return_build_min_heap(self):
        for i in range(1, (self.heap_size//2)+1)[::-1]:
            self.min_heapify(i)
        return self
    
    def min_heapify(self, i):
        smallest = i
        l = (2 * i)
        r = (2 * i) + 1
        
        if l < self.heap_size and self.arr[l].min_dist < self.arr[i].min_dist:
            smallest = l
        
        if r <= self.heap_size and self.arr[r].min_dist < self.arr[smallest].min_dist:
            smallest = r
        
        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i] ## swapping
            self.min_heapify(smallest)
            
                  
class Min_priority_que(Min_heap):

    def return_min_heap_extract(self):       
        min_node = self.arr[1]
        self.arr[1] = self.arr[self.heap_size] ## input the largest node into first index to min heapify
        self.heap_size -= 1
        self.min_heapify(1)
        return min_node
        
        
#####################################
## main code
#####################################

## input graph nodes' name, create graph nodes and append them into graph node list
input_vertex_name_list = input().split(',')
graph_node_list = ['X'] ## we don't use index number 0.
for vertex_name in input_vertex_name_list:
    new_node = Graph_node(vertex_name)
    graph_node_list.append(new_node)

## input how many edges, update edge info to the source graph node
input_how_many_edges = int(input())
for i in range(input_how_many_edges):
    src, dest, dist = input().split(',')
    
    for i in range(1, len(graph_node_list)):
        if src == graph_node_list[i].vertex_name:
            graph_node_list[i].edge_dict[dest] = int(dist)
    


## initialize
for graph_node in graph_node_list[1:]:
    graph_node.min_dist = float("inf")
    graph_node.pred = 'NIL'
graph_node_list[1].min_dist = 0 ## we just follow the vertex name input order. Therefore, source node is the first node.


s = set() ## set for the processed graph node

## let's build min-que with node_list
h = Min_priority_que(graph_node_list)
q = h.return_build_min_heap()


def relax(min_node):  ## u == src, v == dest in adjacent nodes, w == edge weight of u~v
    adj_node_names = list(min_node.edge_dict)
    
    ## for each vertext in G.Adj[u] implementation
    adj_node_list = []
    for adj_node_name in adj_node_names:
        for i in range(1, len(q.arr)):
            if adj_node_name == q.arr[i].vertex_name:
                adj_node_list.append(q.arr[i])
        
    for adj_node in adj_node_list:
    ## actual relaxation process
        if adj_node.min_dist > min_node.min_dist + min_node.edge_dict[adj_node.vertex_name]:
            adj_node.min_dist = min_node.min_dist + min_node.edge_dict[adj_node.vertex_name]
            adj_node.pred = min_node
    

for n in range(1, len(q.arr)):
    min_node = q.return_min_heap_extract()
    s = s | {min_node}
    relax(min_node)


l = sorted(list(s), key = lambda x: x.vertex_name)

for x in l:
    print(
        # x.vertex_name,
        x.min_dist,
        # x.pred,
        # x.edge_dict
    )
