import random
import timeit

class ListNode:
    def __init__(self, data):
        """Constructor for creating a list element"""
        # Node data
        self.data = data

        # Next node
        self.next = None

        return


class SingleLinkedList:
    def __init__(self):
        """Constructor to create this object"""
        self.head: ListNode = None
        self.tail: ListNode = None
        return

    def add_list_item(self, item):
        """Add an item at the end of the list"""

        """If `item` is not a `ListNode` object we should create such 
        objec with the value as the `item` were to have"""

        if not isinstance(item, ListNode):
            item = ListNode(item)  # żeby było jako łańcuch to takie pudełko żeby połączyć
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item  # najpierw skazujemy ostatni element (czyli tail) potem przyłączamy do nowego i zmieniamy tail na ten nowy obiekt
        self.tail = item

        return

    def list_lenght(self):
        """Returns the number for list items"""
        count = 0
        current_node = self.head

        while current_node is not None:
            count += 1
            current_node = current_node.next

        return count

    def __get_element_one_by_one(self):
        """Returns each element of the list as a generator"""
        current_node = self.head

        while current_node is not None:
            yield current_node
            current_node = current_node.next

        return None

    def output_list(self):
        """Output the list = valie of the nodes"""

        for element in self.__get_element_one_by_one():
            print(element.data)

    def find_node_by_data(self, data):
        """Find the first node with the given data and return the node"""
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None

    def remove_list_item(self, item):
        """Remove the first occurrence of `item` in the list"""
        current_node = self.head
        previous_node = None
        found = False

        while current_node is not None and not found:
            if current_node.data == item:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.next

        if found:
            if previous_node is None:
                self.head = current_node.next
            else:
                previous_node.next = current_node.next

            if current_node.next is None:
                self.tail = previous_node

            del current_node
        else:
            print("Item not found in the list")

        return
if __name__ == '__main__':
    single_linked_list = SingleLinkedList()
    nums = list(range(0, 10000))
    random.shuffle(nums)
    for num in nums:
        single_linked_list.add_list_item(num)
    adding_time = 0.0
    finding_time = 0.0
    deleting_time = 0.0
    for i in range(0,10000):
        adding_time+= timeit.timeit('single_linked_list.add_list_item(10010)', globals=globals(),number=1)
        finding_time +=timeit.timeit('single_linked_list.find_node_by_data(10010)', globals=globals(),number=1)
        deleting_time +=timeit.timeit('single_linked_list.remove_list_item(10010)',globals=globals(),number=1)
    print(adding_time/10000,finding_time/10000,deleting_time/10000, sep=" - ")
    adding_time = 0.0
    finding_time = 0.0
    deleting_time = 0.0
    moj_slownik={}
    for num in nums:
        moj_slownik[num]=nums
    for i in range(0,10000):
        ...
        adding_time+= timeit.timeit('moj_slownik[10010]=10010', globals=globals(),number=1)
        finding_time +=timeit.timeit('moj_slownik.get(10010)', globals=globals(),number=1)
        deleting_time +=timeit.timeit('moj_slownik.pop(10010)',globals=globals(),number=1)
    print(adding_time/10000,finding_time/10000,deleting_time/10000, sep=" - ")
