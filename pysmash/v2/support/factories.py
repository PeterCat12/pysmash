from pysmash.v2.models.tournaments import Tournament
from pysmash.v2.models.events import Event
from pysmash.v2.models.sets import Set
from pysmash.v2.models.entrants import Entrant
from pysmash.v2.models.seeds import Seed
from pysmash.v2.models.phases import Phase
from pysmash.v2.models.groups import Group
from pysmash.v2.models.stations import Station
from pysmash.v2.models.standings import Standing


class SmashGGObjectFactory(object):
    # Object Types

    TOURNAMENTS = 'tournaments'
    EVENTS = 'event'
    SETS = 'sets'
    ENTRANTS = 'entrants'
    STANDINGS = 'standings'
    SEEDS = 'seeds'
    PHASES = 'phase'
    GROUPS = 'groups'
    STATIONS = 'stations'

    OBJECT_TYPES = [
        TOURNAMENTS,
        EVENTS,
        SETS,
        ENTRANTS,
        STANDINGS,
        SEEDS,
        PHASES,
        GROUPS,
        STATIONS,
    ]

    @staticmethod
    def factory(_type, **kwargs):
        if _type not in SmashGGObjectFactory.OBJECT_TYPES:
            raise ValueError("`type` {} not supported".format(_type))

        # return eval(type + "()")
        if _type == SmashGGObjectFactory.TOURNAMENTS:
            return Tournament(**kwargs)
        if _type == SmashGGObjectFactory.EVENTS:
            return Event(**kwargs)
        if _type == SmashGGObjectFactory.SETS:
            return Set(**kwargs)
        if _type == SmashGGObjectFactory.ENTRANTS:
            return Entrant(**kwargs)
        if _type == SmashGGObjectFactory.STANDINGS:
            return Standing(**kwargs)
        if _type == SmashGGObjectFactory.SEEDS:
            return Seed(**kwargs)
        if _type == SmashGGObjectFactory.PHASES:
            return Phase(**kwargs)
        if _type == SmashGGObjectFactory.GROUPS:
            return Group(**kwargs)
        if _type == SmashGGObjectFactory.STATIONS:
            return Station(**kwargs)
