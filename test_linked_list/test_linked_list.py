from test_linked_list.conftest import *

def test_node(node):
    assert node.data == 'test_data'
    assert node.next_node is None

def test_insert_at_head(empty_list):
    assert empty_list.insert_at_head('test_data') == "Узел с данными test_data добавлен в начало списка"
    assert empty_list.head.data == 'test_data'
    assert empty_list.head.next_node is None

def test_insert_at_end(empty_list):
    empty_list.insert_at_end('test_data')
    assert empty_list.head.data == 'test_data'
    assert empty_list.head.next_node is None
    assert empty_list.insert_at_end('test_data') == "Узел с данными test_data добавлен в конец списка"
    empty_list.insert_at_end('test_data_1')
    assert empty_list.head.next_node.next_node.data == 'test_data_1'

def test_remove_node_position(a_list):
    assert a_list.remove_node_position(1) == "Удален узел с данными test_data_4 позиции 1"
    assert a_list.head.data == 'test_data_3'
    assert a_list.remove_node_position(2) == "Удален узел с данными test_data_2 позиции 2"
    assert a_list.remove_node_position(10) == "Ничего не удалено"

def test_insert_at_position(a_list):
    assert a_list.insert_at_position('test_data', 10) is None
    assert a_list.insert_at_position('other_test_data', 3) == "Узел с данными other_test_data добавлен на позицию 3"
    assert a_list.head.next_node.next_node.data == 'other_test_data'
    assert a_list.insert_at_position('test_data_first', 1) == "Узел с данными test_data_first добавлен на позицию 1"
    assert a_list.head.data == 'test_data_first'

def test_print_ll(a_list, empty_list):
    assert empty_list.print_ll() == "Данные списка выведены"
    assert a_list.print_ll() == "Данные списка выведены"

def test_get(a_list):
    assert a_list.get('test_data_1')[0] is True
    assert a_list.get('test_data_1')[1].data == 'test_data_1'
    assert a_list.get('test_data_9')[0] is False
    assert a_list.get('test_data_9')[1] is None

def test_change_data(a_list):
    assert a_list.change_data('test_data_3', 'new_data') == "Заменены данные в узле № 2"
    assert a_list.head.next_node.data == 'new_data'
    assert a_list.change_data(' ', ' ') == "Данные не обнаружены"
