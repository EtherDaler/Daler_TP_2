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
        Tree().get('./some-folder-which-u-really-dont-have', False)
    message = e.value.args[0]
    assert message == 'Path not exist'

@pytest.fixture()
def file_data():
    """Return answer to ultimate question."""
    file_temp = tempfile.NamedTemporaryFile()
    return file_temp.name

def test_tree_recurse_call(file_data):
    assert None == Tree().get(file_data, True, True)


def test_tree_recurse_call_er(file_data):
    with pytest.raises(AttributeError) as e:
        Tree().get(file_data, True, False)
    message = e.value.args[0]
    assert message == 'Path is not directory'


def test_tree_raises_3():
    dir = tempfile.TemporaryDirectory()
    node = Tree().construct_filenode(dir.name, True)
    os.mkdir(f'{dir.name}/qwe', mode=0o777)
    Tree().filter_empty_nodes(node, dir.name)
    with pytest.raises(FileNotFoundError) as e:
        print(os.listdir(dir.name))
    message = e.value.args[1]
    assert message == "No such file or directory"