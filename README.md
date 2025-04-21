# python-dungeon-generator

A data-driven approach to generating video game dungeon layouts. The aim of the script is provide a basis for a game such as an RPG to either recreate dungeon layouts from data, or create entirely random dungeons at runtime.

This Python Script generates dungeon layouts based on a `list` of `string` directions such as
```
["Up", "Right", "Right", "Up", "Left", "Left"]
```

Every "Floor" of a dungeon contains at least two rooms, an entrance and exit. Rooms can be conjoined in the four cardinal directions, North, South, East and West. Adjacent rooms do not have to converge.

Run Script:
```
$ python3 dungeon.py --layout "Up,Right,Right,Up,Left,Left"
```


Example output:

```
$ python3 dungeon.py                                       
Printing Floor by rooms generated:
Room N: (X, Y)          [ N    S    E    W ] [Parameters]
Room 0: (0, 0)          ['1', 'X', 'X', 'X'] ['Entrance']
Room 1: (0, -1)         ['X', '0', 'X', 'X'] ['Exit']

Simple Map:
X 
| 
E 
```


```
$ python3 dungeon.py --layout "Up,Right,Right,Up,Left,Left"

Printing Floor by rooms generated:
Room N: (X, Y)          [ N    S    E    W ] [Parameters]
Room 0: (0, 0)          ['1', 'X', 'X', 'X'] ['Entrance']
Room 1: (0, -1)         ['X', '0', 'X', '2'] 
Room 2: (1, -1)         ['X', 'X', '1', '3'] 
Room 3: (2, -1)         ['4', 'X', '2', 'X'] 
Room 4: (2, -2)         ['X', '3', '5', 'X'] 
Room 5: (1, -2)         ['X', 'X', '6', '4'] 
Room 6: (0, -2)         ['X', 'X', 'X', '5'] ['Exit']

Simple Map:
X-O-O 
    | 
O-O-O 
|     
E  
```