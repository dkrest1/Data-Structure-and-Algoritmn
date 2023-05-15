def remove_none(list):
    return [node for node in list if node is not None]


def is_bst(node):
    if not node:
        return True, None, None
    else:
        is_bst_node_l, min_l, max_l = is_bst(node.left)
        is_bst_node_r, min_r, max_r = is_bst(node.right)

        is_bst_node = (is_bst_node_l and is_bst_node_r and (
            max_l is None or node.key > max_l) and (min_r is None or node.key < min_r))

        min_key = min(remove_none([min_l, node.key, min_r]))
        max_key = max(remove_none([max_l, node.key, max_r]))
    return is_bst_node, min_key, max_key


# BST NODE
class BstNode:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
# inserting into a binary search tree
# 1. compare key of node to be inserted and check if it less than or greater the root node
# 2. if it is less than, recursivley insert node into left side of node
# 3. if it is greater than, recursively insert into right side of node


def insert(node, key, value):
    if node is None:
        node = BstNode(key, value)
    else:
        if key < node.key:
            node.left = insert(node.left, key, value)
            node.left.parent = node
        elif key > node.key:
            node.right = insert(node.right, key, value)
            node.right.parent = node
    return node

# find a node in a BST


def find(node, key):
    if node is None:
        return None
    elif node.key == key:
        return node
    elif key < node.key:
        return find(node.left, key)
    elif key > node.key:
        return find(node.right, key)


def update(node, key, value):
    node_update = find(node, key)
    if node_update is not None:
        node_update.value == value


print(None + None + 2)
