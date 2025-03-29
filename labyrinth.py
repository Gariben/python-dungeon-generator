class Room:
    def __init__(self, data, params=None):
        self.data = data
        self.Entrance = None
        self.Exit = None
        self.Up = None
        self.Left = None
        self.Right = None
        self.Down = None
        self.coordinates = None

        if params is not None:
            self.Entrance = params.get("Entrance")
            self.Exit = params.get("Exit")

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

class Dungeon:
    def __init__(self,entrance=None):
        self.room_list = []
        self.entrance = Room(len(self.room_list), {"Entrance": True, "Exit": True})
        self.entrance.set_coordinates((0, 0))
        self.room_list.append(self.entrance)
        self.current_room = self.entrance
        self.exit = self.entrance

    def entrance(self):
        return self.head

    def exit(self):
        return self.exit

    def append(self, room, direction, new_room=None):
        """Adds a new node with the given data at the end of the list."""
        """Returns the current room"""
        if new_room is None:
            new_room = Room()

        if direction == "Up":
            room.Up = new_room
        elif direction == "Down":
            room.Down = new_room
        elif direction == "Left":
            room.Left = new_room
        elif direction == "Right":
            room.Right = new_room
        else:
            raise ValueError("Invalid direction")

        return new_room

    def prepend(self, data):
        """Adds a new node with the given data at the beginning of the list."""
        new_room = Room(data)
        new_room.next = self.head
        self.head = new_room

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
        node = labyrinth.entrance()
        #while node:
        #    values.append(str(temp.data))
        #temp = temp.next
        #return " -> ".join(values)
    
    def print_by_room(self):
        for room in self.room_list:
            nsew_list = [1 if room.Up else 0,
                        1 if room.Down else 0,
                        1 if room.Left else 0,
                        1 if room.Right else 0]
            params = []
            if room.Entrance: params.append("Entrance")
            if room.Exit: params.append("Exit")
            print(f"Room {room.data}: {nsew_list} {params if params else ''}")

# Example usage
if __name__ == "__main__":
    labyrinth = Dungeon()
    labyrinth.print_by_room()
    
    #labyrinth.append(labyrinth.entrance(), "Up")
    #ll.append(2)
    #ll.append(3)
    #print("Linked List:", ll)
    
    #ll.prepend(0)
    #print("After Prepending 0:", ll)
    
    #ll.delete(2)
    #print("After Deleting 2:", ll)
    
    #ll.reverse()
    #print("After Reversing:", ll)
