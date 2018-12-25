from pysmash.v2.models.base.smashgg_objects import SmashGGObject
from pysmash.v2.models.sets import Set
from pysmash.v2.support.contants import URI_GROUP
from pysmash.api import api


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
        self.sets = [Set(**set) for set in kwargs.get('expands', {}).get('sets')]

    # To get the standings for a single bracket, use https://
    #     api.smash.gg / phase_group / 323872?expand[] = standings & expand[] = seeds
    def standings(self):
        data = api.get(
            URI_GROUP + self.id,
            {
                'expand[]': [
                    'standings',
                    'seeds'
                ]
            }
        )

        return data


