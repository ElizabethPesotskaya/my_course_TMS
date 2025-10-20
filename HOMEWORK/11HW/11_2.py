class MyTime:
    def __init__(self, *args):
        if not args:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        elif len(args) == 1:
            if isinstance(args[0], str):
                h, m, s = map(int, args[0].split(":"))
                self.hours = h
                self.minutes = m
                self.seconds = s
            elif isinstance(args[0], MyTime):
                self.hours = args[0].hours
                self.minutes = args[0].minutes
                self.seconds = args[0].seconds
        elif len(args) == 3:
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]

        self.normalize()

    def _normalize(self):
        total = self.hours * 3600 + self.minutes * 60 + self.seconds
        self.hours = total // 3600
        self.minutes = (total % 3600) // 60
        self.seconds = total % 60

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()

    def __ne__(self, other):
        return self.to_seconds() != other.to_seconds()

    def __ge__(self, other):
        return self.to_seconds() >= other.to_seconds()

    def __le__(self, other):
        return self.to_seconds() <= other.to_seconds()

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()


    def __add__(self, other):
        total = self.to_seconds() + other.to_seconds()
        return MyTime(0, 0, total)

    def __sub__(self, other):
        total = self.to_seconds() - other.to_seconds()
        return MyTime(0, 0, total)

    def __mul__(self, number):
        total = int(self.to_seconds() * number)
        return MyTime(0, 0, total)
