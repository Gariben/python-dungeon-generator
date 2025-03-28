class Node:
    def __init__(self, data, params=None):
        self.data = data
        self.Entrance = None
        self.Exit = None
        self.Up = None
        self.Left = None
        self.Right = None
        self.Down = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data, direction):
        """Adds a new node with the given data at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def prepend(self, data):
        """Adds a new node with the given data at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """Deletes the first node with the specified key."""
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def search(self, key):
        """Searches for a node with the given key and returns it if found."""
        temp = self.head
        while temp:
            if temp.data == key:
                return temp
            temp = temp.next
        return None

    def reverse(self):
        """Reverses the linked list."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def __str__(self):
        """Returns a string representation of the linked list."""
        values = []
        temp = self.head
        while temp:
            values.append(str(temp.data))
            temp = temp.next
        return " -> ".join(values)

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print("Linked List:", ll)
    
    ll.prepend(0)
    print("After Prepending 0:", ll)
    
    ll.delete(2)
    print("After Deleting 2:", ll)
    
    ll.reverse()
    print("After Reversing:", ll)
