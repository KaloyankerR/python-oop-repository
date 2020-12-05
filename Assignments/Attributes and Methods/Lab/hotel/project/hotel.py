class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room = [r for r in self.rooms if (r.number == room_number) and (r.capacity >= people)]
        if room:
            room = room[0]
            if not room.is_taken:
                self.guests += people
                room.take_room(people)

    def free_room(self, room_number: int):
        room = [r for r in self.rooms if (r.number == room_number)]
        if room:
            room = room[0]
            if room.is_taken:
                self.guests -= room.guests
                room.free_room()

    def print_status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]

        print(f'Hotel {self.name} has {self.guests} total guests')
        if free_rooms:
            print(f'Free rooms: {", ".join(free_rooms)}')
        if taken_rooms:
            print(f'Taken rooms: {", ".join(taken_rooms)}')
