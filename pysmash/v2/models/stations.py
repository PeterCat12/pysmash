from pysmash.v2.models.base.smashgg_objects import SmashGGObject


class Station(SmashGGObject):

    def __init__(self, **kwargs):
        SmashGGObject.__init__(self, **kwargs)
