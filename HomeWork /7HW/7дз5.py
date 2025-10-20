from functools import reduce

rooms = [
{"name":"Kitchen", "length": 6, "width": 4},
{"name":"Room 1", "length": 5.5, "width": 4.5},
{"name":"Room 2", "length": 5, "width": 4},
{"name":"Room 3", "length": 7, "width": 6.3},
]

separate_rooms = list(map(lambda room: room["length"] * room["width"], rooms))
print(reduce(lambda x, y: x + y, separate_rooms))
