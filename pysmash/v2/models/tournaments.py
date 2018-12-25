from pysmash.v2.models.base.smashgg_objects import SmashGGObject

from pysmash.v2.models.events import Event
from pysmash.v2.models.phase import Phase
from pysmash.v2.models.groups import Group
from pysmash.v2.models.stations import Station


class Tournament(SmashGGObject):

    EXPAND_EVENTS = 'event'
    EXPAND_PHASES = 'phase'
    EXPAND_GROUPS = 'groups'
    EXPAND_STATIONS = 'stations'

    EXPAND_KEYS = [EXPAND_EVENTS, EXPAND_PHASES, EXPAND_GROUPS, EXPAND_STATIONS]

    def __init__(self, **kwargs):
        SmashGGObject.__init__(self, **kwargs)

        # Attributes
        self.id = kwargs.get('id')
        self.name = kwargs.get('name', '')
        self.ownerId = kwargs.get('ownerId')
        self.slug = kwargs.get('slug')
        self.short_slug = kwargs.get('shortSlug')

        # Expands
        self.events = [
            Event(**event) for event in kwargs.get('expands', {}).get(Tournament.EXPAND_EVENTS, [])
        ]
        self.phases = [
            Phase(**phase) for phase in kwargs.get('expands', {}).get(Tournament.EXPAND_PHASES, [])
        ]
        self.groups = [
            Group(**group) for group in kwargs.get('expands', {}).get(Tournament.EXPAND_GROUPS, [])
        ]
        self.stations = [
            Station(**station) for station in kwargs.get('expands', {}).get(Tournament.EXPAND_STATIONS, [])
        ]

    def events(self):
        return self.events

    def phases(self):
        return self.phases

    def groups(self):
        return self.groups

    def stations(self):
        return self.stations

    





