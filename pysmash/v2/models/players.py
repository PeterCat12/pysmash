from pysmash.v2.models.base.smashgg_objects import SmashGGObject


class Player(SmashGGObject):

    def __init__(self, **kwargs):
        SmashGGObject.__init__(self, **kwargs)
        self.id = kwargs.get('id')
        self.gamerTag = kwargs.get('gamerTag')
        self.name = kwargs.get('name')
        self.state = kwargs.get('state')
        self.county = kwargs.get('state')
        self.region = kwargs.get('region')
        self.rankings = kwargs.get('rankings')
