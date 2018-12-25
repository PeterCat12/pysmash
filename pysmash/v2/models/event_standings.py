from pysmash.v2.models.base.smashgg_objects import SmashGGObject
from pysmash.v2.models.losses import Loss


class EventStanding(SmashGGObject):

    def __init__(self, **kwargs):
        SmashGGObject.__init__(**kwargs)
        self.id = kwargs.get('id')
        self.groupId = kwargs.get('groupId')
        self.entityType = kwargs.get('entityType')
        self.entityId = kwargs.get('entityId')
        self.standing = kwargs.get('standing')
        self.isTied = kwargs.get('isTied')
        self.isFinal = kwargs.get('isFinal')
        self.points = kwargs.get('points')
        self.highestPoints = kwargs.get('highestPoints')
        self.pointIds = kwargs.get('pointIds')
        self.losses = []

        mutations = kwargs.get('mutations')
        if 'losses' in mutations.keys():
            self.losses = [Loss(**loss_data) for loss_data in mutations['losses'].values()]