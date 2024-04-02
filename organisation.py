class Organisation:
    def __init__(self, name, country, boxers=None):
        self.name = name
        self.country = country
        self.boxers = boxers if boxers is not None else []