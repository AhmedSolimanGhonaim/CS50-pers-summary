class Node:
    def __init__(self,node_data):
        self.node_data=node_data
        self.right = None
        self.left =None
    def __str__(self):
        return str(self.node_data)
root_node=Node(7)
print(root_node)

# SECOND_LEVEL
second_node = Node(6)
third_node = Node(8)
fourth_node = Node(9)
fifth_node = Node(7)
sixth_node = Node(5)

root_node.left=second_node
root_node.right=third_node
second_node.left=sixth_node
third_node.right=fourth_node
print(third_node.left)
print(third_node.right)




class NodeTra:
    def  __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def in_order_dfs(node):
    if node is None:
        return
    in_order_dfs(node.left)
    print(node.data,end=' ')
    in_order_dfs(node.right)
    print(node.right)
def pre_order_dfs(node):
    if node is None :
        return 
    print(node.data)
    pre_order_dfs(node.left)
    pre_order_dfs(node.right)

def post_order_dfs(node):
    if node is None :
        return
    pre_order_dfs(node.left)
    pre_order_dfs(node.right)
    print(node.data,end=' ')

# ^        BFS


def bfs(root):
    if root is None:
        return
    queue = [root]
    while queue :
       node =  queue.pop(0)
       print(node.data,end=' ')
       if node.left:
           queue.append(node.left)
       if node.right:
           queue.append(node.right)


if __name__ == "__main__" :
    
    # Creating the tree
    root = NodeTra(2)
    root.left = NodeTra(3)
    root.right = NodeTra(4)
    root.left.left = NodeTra(5)

    print("In-order DFS: ", end='')
    in_order_dfs(root)
    print("\nPre-order DFS: ", end='')
    pre_order_dfs(root)
    print("\nPost-order DFS: ", end='')
    post_order_dfs(root)
    print("\nLevel order: ", end='')
    bfs(root)
