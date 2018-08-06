from pysmash.v2.models.base.smashgg_objects import SmashGGObject
from pysmash.v2.models.phase import Phase
from pysmash.v2.models.groups import Group


class Event(SmashGGObject):

    EXPAND_PHASE = 'phase'
    EXPAND_GROUPS = 'groups'

    EXPAND_KEYS = [EXPAND_PHASE, EXPAND_GROUPS]

    def __init__(self, **kwargs):
        SmashGGObject.__init__(**kwargs)
        self.id = kwargs.get('id')
        self.tournamentId = kwargs.get('tournamentId')
        self.videogameId = kwargs.get('videogameId')
        self.slug = kwargs.get('slug')
        self.typeDisplayStr = kwargs.get('typeDisplayStr')

        # Expands
        self.phases = [Phase(**phase) for phase in kwargs['expands'].get('phase', [])]
        self.groups = [Group(**group) for group in kwargs['expands'].get('groups', [])]

    def phases(self):
        return self.phases

    def groups(self):
        return self.groups
