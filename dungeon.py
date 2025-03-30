def text_indent(tabs):
    print(" " * tabs, end="")

def GetRoomOptions(self):
    if self.Up:
        print("\tGo Up")
    if self.Down:
        print("\tGo Down")
    if self.Left:
        print("\tGo Left")
    if self.Right:
        print("\tGo Right")
    if self.Entrance:
        print("\tGo Entrance")


class Room:
    def __init__(self, number, params=None):
        self.number = number
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

    def get_number(self):
        return self.number

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates
    
    def print_data(self):
        nsew_list = [str(self.Up.get_number()) if self.Up else "X",
                    str(self.Down.get_number()) if self.Down else "X",
                    str(self.Left.get_number()) if self.Left else "X",
                    str(self.Right.get_number()) if self.Right else "X"]
        params = []
        if self.Entrance: params.append("Entrance")
        if self.Exit: params.append("Exit")
        print(f"Room {self.number}: {self.coordinates}\t{nsew_list} {params if params else ''}")


class Floor:
    def __init__(self,entrance=None):
        self.grid = {}
        self.room_list = []
        self.entrance = Room(len(self.room_list), {"Entrance": True, "Exit": True})
        self.entrance.set_coordinates((0, 0))
        self.min = (0,0)
        self.max = (0,0)
        self.grid[self.entrance.coordinates] = self.entrance
        self.room_list.append(self.entrance)
        self.current_room = self.entrance
        self.exit = self.entrance

    def GetEntrance(self):
        return self.entrance
    
    def GetCurrentRoom(self):
        return self.current_room

    def GetExit(self):
        return self.exit
    
    def SetExit(self, room):
        self.exit.Exit = False
        room.Exit = True
        self.exit = room

    def append(self, room, direction, new_room=None):
        """Adds a new node with the given data at the end of the list."""
        """Returns the current room"""

        if new_room is None:
            new_room_params= {}
            # TODO: Should exit automatically change to second room?
            #if self.entrance == self.exit:
            #    self.entrance
            #    new_room_params["Exit"] = True
            new_room = Room(len(self.room_list), new_room_params)

        if direction == "Up":
            room.Up = new_room
            new_room.set_coordinates((room.coordinates[0], room.coordinates[1] - 1))
            new_room.Down = room
        elif direction == "Down":
            room.Down = new_room
            new_room.set_coordinates((room.coordinates[0], room.coordinates[1] + 1))
            new_room.Up = room
        elif direction == "Left":
            room.Left = new_room
            new_room.set_coordinates((room.coordinates[0] - 1, room.coordinates[1]))
            new_room.Right = room
        elif direction == "Right":
            room.Right = new_room
            new_room.set_coordinates((room.coordinates[0] + 1, room.coordinates[1]))
            new_room.Left = room
        else:
            raise ValueError("Invalid direction")
        
        if new_room.coordinates[0] < self.min[0]:
            self.min = (new_room.coordinates[0], self.min[1])
        if new_room.coordinates[0] > self.max[0]:
            self.max = (new_room.coordinates[0], self.max[1])
        if new_room.coordinates[1] < self.min[1]:
            self.min = (self.min[0], new_room.coordinates[1])
        if new_room.coordinates[1] > self.max[1]:
            self.max = (self.max[0], new_room.coordinates[1])
        
        self.grid[new_room.coordinates] = new_room
        self.room_list.append(new_room)

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
    
    def print_by_room(self, pretty=False):
        if pretty: print("Printing Floor by rooms generated:")
        if pretty: print("Room N: " + "(X, Y)\t[ N    S    E    W ] [Parameters]")
        for room in self.room_list:
            room.print_data()
        if pretty: print("")

    def print_simple_map(self, indent=2):
        print("Simple Map:")
        for y in range(self.min[1], self.max[1]+1):
            for x in range(self.min[0], self.max[0]+1):
                if (x, y) in self.grid:
                    endchar=" "
                    room = self.grid[(x, y)]
                    if room.Right:
                        endchar="-"
                    if room.Entrance:
                        print("E", end=endchar)
                    elif room.Exit:
                        print("X", end=endchar)
                    else:
                        print("O", end=endchar)
            print()
            for x in range(self.min[0], self.max[0]+1):
                if (x, y) in self.grid:
                    room = self.grid[(x, y)]
                    if room.Down:
                        print("|", end=" ")
                    else:
                        print(" ", end=" ")
            print()

if __name__ == "__main__":
    labyrinth = Floor()
    labyrinth.print_by_room(pretty=True)
    
    room = labyrinth.append(labyrinth.GetCurrentRoom(), "Up")
    labyrinth.SetExit(room)
    labyrinth.print_by_room(pretty=True)
    labyrinth.print_simple_map()

    print("Current Room:")
    room.print_data()

    room = labyrinth.append(room, "Right")
    labyrinth.SetExit(room)
    labyrinth.print_by_room(pretty=True)
    labyrinth.print_simple_map()

    room = labyrinth.append(room, "Right")
    labyrinth.SetExit(room)
    labyrinth.print_by_room(pretty=True)
    labyrinth.print_simple_map()

    room = labyrinth.append(room, "Up")
    labyrinth.SetExit(room)
    labyrinth.print_by_room(pretty=True)
    print ("This one's busted.")
    labyrinth.print_simple_map()

    #ll.append(2)
    #ll.append(3)
    #print("Linked List:", ll)
    
    #ll.prepend(0)
    #print("After Prepending 0:", ll)
    
    #ll.delete(2)
    #print("After Deleting 2:", ll)
    
    #ll.reverse()
    #print("After Reversing:", ll)
