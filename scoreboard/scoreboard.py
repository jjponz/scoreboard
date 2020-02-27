class ScoreBoard:
    def __init__(self):
        self.local = 0

    def add_one_for_local(self):
        self.local += 1

    def add_two_for_local(self):
        self.local += 2

    def result(self):
        return f'00{self.local}-000'
