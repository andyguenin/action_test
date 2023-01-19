from andyguenin.algorithms import traverse_dfs_preorder
from andyguenin.datastructures import Node, Leaf


def test_traverse_dfs_preorder():
    a = Node(
        "a",
        Node("b",
             Leaf("c"), Leaf("d")),
        Node("e", Node("f", None, Leaf("g")), None)
    )

    assert "".join([b.name for b in traverse_dfs_preorder(a)]) == "abcdefg"