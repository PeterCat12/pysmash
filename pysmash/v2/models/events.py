from pysmash.v2.models.base.smashgg_objects import SmashGGObject
from pysmash.v2.models.phases import Phase
from pysmash.v2.models.groups import Group
from pysmash.v2.models.event_standings import EventStanding
from pysmash.v2.models.entrants import Entrant

from pysmash.api import api


class Event(SmashGGObject):

    EXPAND_PHASE = 'phase'
    EXPAND_GROUPS = 'groups'

    EXPAND_KEYS = [EXPAND_PHASE, EXPAND_GROUPS]

    def __init__(self, **kwargs):
        SmashGGObject.__init__(self, **kwargs)
        self.id = kwargs.get('id')
        self.tournamentId = kwargs.get('tournamentId')
        self.videogameId = kwargs.get('videogameId')
        self.slug = kwargs.get('slug')
        self.typeDisplayStr = kwargs.get('typeDisplayStr')

        # Expands
        self.phase = [Phase(**phase) for phase in kwargs.get('expands', {}).get(self.EXPAND_PHASE, [])]
        self.groups = [Group(**group) for group in kwargs.get('expands', {}).get(self.EXPAND_GROUPS, [])]

        # Standings and Entrants
        self.standings = []
        self.entrants = []

    def expand_phase(self):
        return self.expand(self.EXPAND_PHASE)

    def expand_groups(self):
        return self.expand(self.EXPAND_GROUPS)

    def expand(self, params):
        params = SmashGGObject._format_expands(params)

        if self.slug is None:
            raise ValueError("Cannot fetch expand attributes as the `slug` attribute is not set on event instance.")

        data = api.get(uri=self.slug, params=self._format_expands(params))
        self._set_expands(params['expand[]'], data)

    def standings(self, page=1, per_page=25):
        data = api.get(
            self.slug + '/standings',
            {
                'entityType': 'event',
                'expands[]': [
                    'entrants',
                ],
                'mutations[]': [
                    'playerData',
                    'standingLosses'
                ],
                'page': page,
                'per_page': per_page
            }
        )
        self.standings = [EventStanding(**standing_data) for standing_data in data['items']['entities'].get('standing')]
        self.entrants = [Entrant(**entrant_data) for entrant_data in data['items']['entities'].get('entrants')]
        return data
