from collections import defaultdict

class clip:
    def __init__(self):
        self.data = defaultdict(str)

    def add_data(self, key, text):
        self.data[key] = text
    
    def req_data(self, key):
        return self.data[key]