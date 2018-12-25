from pysmash.v2.models.base.smashgg_objects import SmashGGObject


class Set(SmashGGObject):

    def __init__(self, **kwargs):
        SmashGGObject.__init__(self, **kwargs)

        # Attributes
        self.id = kwargs.get('id')
        self.fullRoundText = kwargs.get('fullRoundText')
        self.winner_id = kwargs.get('entrant1Id')
        self.bestOf = kwargs.get('bestOf')
        self.crewPlayerCount = kwargs.get('crewPlayerCount')
        self.wPlacement = kwargs.get('wPlacement')
        self.lPlacement = kwargs.get('lPlacement')
