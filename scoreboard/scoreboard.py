class ScoreBoard:
    def __init__(self):
        self.local = 0

    def add_one_for_local(self):
        self.local +=1

    def result(self):
        return f'{self.local}-0'
