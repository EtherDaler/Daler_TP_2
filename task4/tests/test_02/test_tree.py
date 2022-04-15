import os
import pytest
import tempfile

from tree_utils_02.node import FileNode
from tree_utils_02.tree import Tree


def test_tree_construct():
    file_temp = tempfile.NamedTemporaryFile()
    file_node = Tree().construct_filenode(file_temp.name, False)
    assert file_node == Tree().update_filenode(file_node)


def test_tree_non_path():
    with pytest.raises(AttributeError) as e:
        Tree().get('./some-shit-which-u-really-dont-have', False)
    message = e.value.args[0]
    assert message == 'Path not exist'


def test_tree_recurse_call():
    file_temp = tempfile.NamedTemporaryFile()
    assert None == Tree().get(file_temp.name, True, True)


def test_tree_recurse_call_er():
    file_temp = tempfile.NamedTemporaryFile()
    try:
        Tree().get(file_temp.name, True, False)
    except AttributeError as e:
        assert 1 == 1


def test_tree_raises_3():
    dir = tempfile.TemporaryDirectory()
    node = Tree().construct_filenode(dir.name, True)
    os.mkdir(f'{dir.name}/qwe', mode=0o777)
    Tree().filter_empty_nodes(node, dir.name)
    try:
        print(os.listdir(dir.name))
    except FileNotFoundError:
        assert 1 == 1