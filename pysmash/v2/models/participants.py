from pysmash.v2.models.base.smashgg_objects import SmashGGObject


class Participant(SmashGGObject):

    def __init__(self, **kwargs):
        SmashGGObject.__init__(**kwargs)
        self.gamerTag = kwargs.get('gamerTag')
        self.prefix = kwargs.get('prefix')
        self.playerId = kwargs.get('playerId')