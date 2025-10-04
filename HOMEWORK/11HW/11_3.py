class SuperStr(str):
    def is_repeatance(self, s):
        if not s or not self:
            return False
        repeat_count = len(self) // len(s)
        return s * repeat_count == self

    def is_palindrom(self):
        cleaned = self.lower()
        return cleaned == cleaned[::-1]


