from pysmash.v2.models.base.smashgg_objects import SmashGGObject

from pysmash.v2.models.events import Event
from pysmash.v2.models.phases import Phase
from pysmash.v2.models.groups import Group
from pysmash.v2.models.stations import Station

from pysmash.api import api


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
            Event(**event) for event in kwargs.get('expands', {}).get(self.EXPAND_EVENTS, [])
        ]
        self.phases = [
            Phase(**phase) for phase in kwargs.get('expands', {}).get(self.EXPAND_PHASES, [])
        ]
        self.groups = [
            Group(**group) for group in kwargs.get('expands', {}).get(self.EXPAND_GROUPS, [])
        ]
        self.stations = [
            Station(**station) for station in kwargs.get('expands', {}).get(self.EXPAND_STATIONS, [])
        ]

    def expand_events(self):
        return self.expand(self.EXPAND_EVENTS)

    def expand_phases(self):
        return self.expand(self.EXPAND_PHASES)

    def expand_groups(self):
        return self.expand(self.EXPAND_GROUPS)

    def expand_stations(self):
        return self.expand(self.EXPAND_STATIONS)

    def expand(self, params):
        params = SmashGGObject._format_expands(params)

        if self.slug is None:
            raise ValueError("Cannot fetch expand attributes as the `slug` attribute is not set on event instance.")

        data = api.get(uri=self.slug, params=self._format_expands(params))
        self._set_expands(params['expand[]'], data)


    





