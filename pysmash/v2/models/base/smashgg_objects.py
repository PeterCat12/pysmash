

class SmashGGObject(object):

    def __init__(self, **raw):
        self.data = raw

    def raw(self):
        return self.data