import os
import tempfile

from tree_utils_02.size_node import FileSizeNode
from tree_utils_02.size_tree import SizeTree


def test_size_tree():
    SizeTree().filter_empty_nodes(SizeTree().get('.', False))
    dir_node = SizeTree().construct_filenode('.', True)
    assert 4096 == dir_node.size
