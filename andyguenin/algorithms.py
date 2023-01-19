from typing import List, Optional
from .datastructures import Node, Leaf, AbstractNode


def traverse_dfs_preorder(root: Node) -> List[AbstractNode]:
    def inner(root: Optional[Node], order: List[AbstractNode]) -> List[AbstractNode]:
        if root is None:
            return order
        elif isinstance(root, Node):
            arr = [o for o in order]
            arr.append(root)
            arr = inner(root.left, arr)
            arr = inner(root.right, arr)
            return arr
        elif isinstance(root, Leaf):
            order.append(root)
            return order
        return order

    retval = inner(root, [])

    return retval
