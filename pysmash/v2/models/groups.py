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
        SmashGGObject.__init__(self, **kwargs)

        # Attributes
        self.id = kwargs.get('id')
        self.phaseId = kwargs.get('phaseId')
        self.title = kwargs.get('title')
        self.hasSets = kwargs.get('hasSets')
        self.hasCustomWinnerByes = kwargs.get('hasCustomWinnerByes')
        self.percentageComplete = kwargs.get('percentageComplete')

        # Expands
        self.sets = [Set(**_set) for _set in kwargs.get('expands', {}).get('sets', [])]


    def expand_sets(self):
        return self.expand(self.EXPAND_SETS)

    def expand_entrants(self):
        return self.expand(self.EXPAND_ENTRANTS)

    def expand_seeds_and_standings(self):
        return self.expand([self.EXPAND_STANDINGS, self.EXPAND_SEEDS])

    def expand(self, params):
        params = SmashGGObject._format_expands(params)

        if self.id is None:
            raise ValueError("Cannot fetch expand attributes as the `id` attribute is not set on group instance.")
        uri = URI_GROUP + self.id
        data = api.get(uri=uri, params=params)

        print(data)

        from pysmash.v2.support.factories import SmashGGObjectFactory
        for expand in params['expand[]']:
            result = [
                SmashGGObjectFactory.factory(key, **expand) for expand in data.get('expands', {}).get(key, [])
            ]
            setattr(self, key, result)



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


