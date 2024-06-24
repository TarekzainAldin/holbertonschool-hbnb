class Country:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def to_dict(self):
        return {
            'name': self.name,
            'code': self.code
        }
