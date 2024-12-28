class Node:
    """Helper class, is not used by itself."""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Body of the main class."""

    def __init__(self) -> None:
        """Initialises an empty list."""

        self.head = None

    def insert_at_head(self, data) -> str:
        """Adds a new element at the beginning of the list. Returns a message string."""

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        return f"Узел с данными {new_node.data} добавлен в начало списка"

    def insert_at_end(self, data) -> str | None:
        """Adds a new element at the end of the list. Returns a message string if the list is not empty, otherwise None."""

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node
        return f"Узел с данными {new_node.data} добавлен в конец списка"

    def remove_node_position(self, rm_position) -> str:
        """Deletes an element at the specified position (starting with 1). Returns a message string."""

        if rm_position == 1:
            removed_node = self.head
            self.head = self.head.next_node
            return f"Удален узел с данными {removed_node.data} позиции {rm_position}"
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < rm_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None or current_node.next_node is None:
            return "Ничего не удалено"
        removed_node = current_node.next_node
        current_node.next_node = current_node.next_node.next_node  # removed_node.next_node
        return f"Удален узел с данными {removed_node.data} позиции {rm_position}"

    def insert_at_position(self, data, node_position) -> str | None:
        """Inserts an element at the specified position (starting with 1).
            Returns a message string or None if the position is not present."""

        new_node = Node(data)
        if node_position == 1:
            self.insert_at_head(data)
            return f"Узел с данными {new_node.data} добавлен на позицию {node_position}"
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < node_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None:
            return None
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
        return f"Узел с данными {new_node.data} добавлен на позицию {node_position}"

    def print_ll(self) -> None:
        """Displays the content of the list to the console. Returns a message string."""

        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node
        return "Данные списка выведены"

    def get(self, data) -> tuple:
        """The method is used to get the pointer to a node with the given value.
            If the value is present in the list, the function returns a tuple with True and the pointer.
            If the value is not in the list, the function returns a tuple containing False and None."""

        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True, current_node
            current_node = current_node.next_node
        return False, None

    def change_data(self, node_data, change_data) -> str:
        """Finds a node containing the given node_data and replaces it with the new change_data.
            Returns a message string."""

        current_node = self.head
        current_node_position = 1
        while current_node:
            if current_node.data == node_data:
                current_node.data = change_data
                return f"Заменены данные в узле № {current_node_position}"
            current_node = current_node.next_node
            current_node_position += 1
        return "Данные не обнаружены"
