# def tree(root_label, branches=[]):
#     for branch in branches:
#         assert is_tree(branch), 'branches must be trees'
#     return [root_label] + list(branches)

# def is_tree(tree):
#     if type(tree) != list or len(tree) < 1:
node_list = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]

class BinTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right

class BinTree(object):
    def __init__(self, root=None):
        self.root = root
    
    @classmethod
    def build_from(cls, node_list):
        """通过节点信息构造二叉树
        第一次遍历我们构造 node 节点
        第二次遍历我们给 root 和 孩子赋值

        :param node_list: {'data': 'A', 'left': None, 'right': None, 'is_root': False}
        """
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)
        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return cls(root)
    
    def preorder_trav(self, subtree):
        """ 根序遍历
        """
        if subtree is not None:
            # print(subtree.data)
            self.preorder_trav(subtree.left)
            self.preorder_trav(subtree.right)

    def layer_trav(self, subtree):
        """ 层序遍历
        """
        cur_nodes = [subtree] # current layer nodes
        next_nodes = []
        while cur_nodes or next_nodes:
            for node in cur_nodes:
                # print(node.data)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            cur_nodes = next_nodes
            next_nodes = []
    
from collections import deque
class Queue(object):
    def __init__(self):
        self._items = deque()
    def append(self, value):
        return self._items.append(value)

        
btree = BinTree.build_from(node_list)
# btree.preorder_trav(btree.root)
print(btree.root)
# print(btree.node)
btree.layer_trav(btree.root)


