import pytest
from QueueClass import Queue

@pytest.fixture
def non_empty_queue():
    queue = Queue(max_length=3)
    queue.Enqueue('tset_data_1')
    queue.Enqueue('tset_data_2')
    return queue

@pytest.fixture
def empty_queue():
    return Queue()
    
def test_IsEmpty(empty_queue, non_empty_queue):
    assert empty_queue.IsEmpty() is True
    assert non_empty_queue.IsEmpty() is False

def test_IsFull(empty_queue, non_empty_queue):
    assert empty_queue.IsFull() is False
    assert non_empty_queue.IsFull() is False
    non_empty_queue.Enqueue('test_data_3')
    assert non_empty_queue.IsFull() is True
    