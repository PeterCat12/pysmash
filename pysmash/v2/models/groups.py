from pysmash.v2.models.base.smashgg_objects import SmashGGObject
from pysmash.v2.models.sets import Set


class Group(SmashGGObject):

    EXPAND_SETS = 'sets'
    EXPAND_ENTRANTS = 'entrants'
    EXPAND_STANDINGS = 'standings'
    EXPAND_SEEDS = 'seeds'

    EXPAND_KEYS = [EXPAND_SETS, EXPAND_ENTRANTS, EXPAND_STANDINGS, EXPAND_SEEDS]

    def __init__(self, **kwargs):
        SmashGGObject.__init__(**kwargs)

        # Attributes
        self.id = kwargs.get('id')
        self.phaseId = kwargs.get('phaseId')
        self.title = kwargs.get('title')
        self.hasSets = kwargs.get('hasSets')
        self.hasCustomWinnerByes = kwargs.get('hasCustomWinnerByes')
        self.percentageComplete = kwargs.get('percentageComplete')

        # Expands
        self.sets = [Set(**set) for set in kwargs['expands'].get('sets')]


