import pytest
from LinkedListClass import Node, LinkedList 

@pytest.fixture
def node():
    return Node('test_data')

@pytest.fixture
def empty_list():
    return LinkedList()

@pytest.fixture
def a_list():
    the_list = LinkedList()
    the_list.insert_at_head('test_data_1')
    the_list.insert_at_head('test_data_2')
    the_list.insert_at_head('test_data_3')
    the_list.insert_at_head('test_data_4')
    return the_list