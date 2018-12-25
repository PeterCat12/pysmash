from pysmash.v2.models.base.smashgg_objects import SmashGGObject


class Loss(SmashGGObject):

    def __init__(self, **kwargs):
        SmashGGObject.__init__(**kwargs)
        self.entrantId = kwargs.get('entrantId')
        self.name = kwargs.get('name')